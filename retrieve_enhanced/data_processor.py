import json
import glob
from pathlib import Path
from typing import List, Dict, Any
from tqdm import tqdm
from llm_client import LLMClient, get_llm_client


from text_processing import (
    clean_text,
    semantic_chunking,
    chunk_by_markdown_headers,
    add_metadata_context
)


class DataProcessor:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def clean_text(self, text: str) -> str:
        """Use LLM to clean text (fix typos, formatting, OCR errors)."""
        text = clean_text(text)
            
        prompt = f"""Please clean the following text. Fix typos, broken lines, and formatting issues. 
        Do not summarize or change the meaning. Return ONLY the cleaned text.
        
        Text:
        {text}
        """
        return self.llm.generate(prompt, system_prompt="You are a helpful text cleaning assistant.")

    def extract_keywords(self, text: str, num_keywords: int = 10) -> List[str]:
        """Extract keywords using LLM."""
        prompt = f"""Extract {num_keywords} keywords from the following text.
        Return ONLY the keywords as a comma-separated list.
        
        Text:
        {text}
        """
        response = self.llm.generate(prompt, system_prompt="You are a helpful keyword extraction assistant.")
        keywords = [k.strip() for k in response.split(',') if k.strip()]
        return keywords

    def generate_summary(self, text: str) -> str:
        """Generate a concise summary."""
        prompt = f"""Summarize the following text in 3-5 sentences.
        
        Text:
        {text}
        """
        return self.llm.generate(prompt, system_prompt="You are a helpful summarization assistant.")

    def adaptive_chunking(self, text: str, meta: Dict[str, Any], max_chunk_size: int = 1000) -> List[Dict[str, Any]]:
        """
        Adaptive chunking based on document source.
        """
        source = meta.get('source', '')
        
        if source == 'github' or 'README' in meta.get('title', ''):
            return chunk_by_markdown_headers(text, max_chunk_size=max_chunk_size)
        elif source == 'arxiv':
            # For papers, semantic chunking works well, or we could implement section-based if we had structure
            return semantic_chunking(text, max_chunk_size=max_chunk_size)
        else:
            # Default semantic
            return semantic_chunking(text, max_chunk_size=max_chunk_size)


import concurrent.futures

def process_single_document(
    text: str, 
    meta: Dict[str, Any], 
    processor: DataProcessor, 
    enable_cleaning: bool, 
    enable_summary: bool, 
    chunk_size: int
) -> List[Dict[str, Any]]:
    """Helper function to process a single document."""
    try:
            
        # Cleaning
        if enable_cleaning:
            text = clean_text(text)
        
        # Extract keywords and summary (LLM-generated)
        generated = {}
        generated['keywords'] = processor.extract_keywords(text)
             
        # Augmentation - Summary
        doc_summary = ""
        if enable_summary:
            doc_summary = processor.generate_summary(text)
            generated['summary'] = doc_summary

        # Chunking
        if chunk_size <= 0: # Disable chunking
             chunks = [{'text': text, 'chunk_id': 0, 'type': 'full_doc'}]
        else:
             chunks = processor.adaptive_chunking(text, meta, max_chunk_size=chunk_size)
        
        processed_chunks = []
        for chunk in chunks:
            chunk_text = chunk['text']
            
            # Enrich content with metadata and summary for retrieval
            # Metadata is added before summary as per text_processing.py implementation
            enriched_content = add_metadata_context(chunk_text, meta, generated)
            
            chunk_doc = {
                'content': enriched_content,
                'raw_content': chunk_text,
                'generated': generated,
                'chunk_id': chunk['chunk_id'],
                'chunk_type': chunk.get('type', 'unknown'),
                'metadata': meta
            }
            
            processed_chunks.append(chunk_doc)
            
        return processed_chunks
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "404" in error_msg:
             # Critical error, re-raise to stop processing
             raise e
        print(f"[ERROR] Failed to process document {meta.get('title', 'unknown')}: {e}")
        return []

def process_source_directory(
    root_dir: str,
    output_file: str,
    enable_cleaning: bool = False,
    enable_summary: bool = False,
    chunk_size: int = 1000,
    max_workers: int = 5,
    batch_size: int = 50
):
    """
    Process all data sources in the root directory in parallel.
    """
    root = Path(root_dir)
    output_path = Path(output_file)
    llm = get_llm_client() # Default to OpenRouter
    processor = DataProcessor(llm)
    
    all_docs = []
    
    # Determine project root
    project_root = root.parent
    for parent in root.parents:
        if parent.name == 'rag291':
            project_root = parent
            break
            
    print(f"[INFO] Project root determined as: {project_root}")

    # 1. Process Arxiv
    arxiv_file = root / "arxiv_llm_2025" / "arxiv_llm_2025.jsonl"
    if arxiv_file.exists():
        print(f"[INFO] Processing Arxiv data from {arxiv_file}")
        with open(arxiv_file, 'r') as f:
            for line in f:
                if not line.strip(): continue
                doc = json.loads(line)
                text = doc.get('abstract', '') + "\n" + doc.get('title', '') # Combine for context
                meta = doc
                meta['source'] = 'arxiv'
                # Ensure path exists for retrieval verification
                if 'id' in doc:
                    meta['path'] = f"arxiv/{doc['id']}"
                    meta['arxiv_id'] = doc['id']
                else:
                    meta['path'] = "arxiv/unknown"
                all_docs.append((text, meta))
    
    # 2. Process GitHub
    github_dir = root / "github_readmes"
    if github_dir.exists():
        print(f"[INFO] Processing GitHub data from {github_dir}")
        files = glob.glob(str(github_dir / "**" / "README*"), recursive=True)
        for f in files:
            p = Path(f)
            try:
                text = p.read_text(errors='ignore')
                parts = p.parts
                repo = "/".join(parts[-3:-1]) if len(parts) >= 3 else p.name
                
                # Calculate relative path to project root
                try:
                    rel_path = str(p.relative_to(project_root))
                except ValueError:
                    rel_path = str(p)

                meta = {
                    'source': 'github',
                    'repo': repo,
                    'path': rel_path,
                    'title': p.name
                }
                all_docs.append((text, meta))
            except Exception as e:
                print(f"[WARN] Failed to read {f}: {e}")

    # 3. Process Hugging Face
    hf_dir = root / "hf_cards_2025"
    if hf_dir.exists():
        print(f"[INFO] Processing HF data from {hf_dir}")
        # Models
        for f in glob.glob(str(hf_dir / "models" / "*.md")):
            p = Path(f)
            text = p.read_text(errors='ignore')
            
            try:
                rel_path = str(p.relative_to(project_root))
            except ValueError:
                rel_path = str(p)
            
            # Parse model_id from filename (owner__repo -> owner/repo)
            model_id = p.stem.replace('__', '/')
            meta = {
                'source': 'hf_models', 
                'title': p.stem, 
                'path': rel_path,
                'model_id': model_id
            }
            all_docs.append((text, meta))
        # Datasets
        for f in glob.glob(str(hf_dir / "datasets" / "*.md")):
            p = Path(f)
            text = p.read_text(errors='ignore')
            
            try:
                rel_path = str(p.relative_to(project_root))
            except ValueError:
                rel_path = str(p)
            
            # Parse dataset_id from filename (owner__repo -> owner/repo)
            dataset_id = p.stem.replace('__', '/')
            meta = {
                'source': 'hf_datasets', 
                'title': p.stem, 
                'path': rel_path,
                'dataset_id': dataset_id
            }
            all_docs.append((text, meta))

    print(f"[INFO] Total documents found: {len(all_docs)}")
    
    # Check for existing progress to resume
    processed_keys = set()
    if output_path.exists():
        print(f"[INFO] Found existing output file {output_file}. Resuming...")
        with open(output_path, 'r') as f:
            for line in f:
                if not line.strip(): continue
                try:
                    d = json.loads(line)
                    meta = d.get('metadata', {})
                    # Create a robust unique key: source + (path or title)
                    source = meta.get('source', 'unknown')
                    identifier = meta.get('path') or meta.get('title') or 'unknown'
                    key = f"{source}:{identifier}"
                    processed_keys.add(key)
                except:
                    pass
        print(f"[INFO] Already processed {len(processed_keys)} unique documents.")

    # Filter out already processed docs
    docs_to_process = []
    for text, meta in all_docs:
        source = meta.get('source', 'unknown')
        identifier = meta.get('path') or meta.get('title') or 'unknown'
        key = f"{source}:{identifier}"
        
        if key not in processed_keys:
            docs_to_process.append((text, meta))
            
    print(f"[INFO] Documents remaining to process: {len(docs_to_process)}")
    
    processed_count = 0
    buffer = []
    
    print(f"[INFO] Starting parallel processing with {max_workers} workers...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks for remaining docs
        future_to_doc = {
            executor.submit(
                process_single_document, 
                text, meta, processor, enable_cleaning, enable_summary, chunk_size
            ): (text, meta) for text, meta in docs_to_process
        }
        
        try:
            for future in tqdm(concurrent.futures.as_completed(future_to_doc), total=len(docs_to_process)):
                try:
                    chunks = future.result()
                    if chunks:
                        buffer.extend(chunks)
                        
                    # Batch Save
                    if len(buffer) >= batch_size:
                        with open(output_path, 'a') as f:
                            for doc in buffer:
                                f.write(json.dumps(doc) + '\n')
                        processed_count += len(buffer)
                        buffer = [] # Clear buffer
                except Exception as e:
                    # If a critical error (like 429) bubbled up from process_single_document (if we modified it to raise)
                    # Currently process_single_document catches all exceptions and returns [].
                    # We need to modify process_single_document to re-raise critical errors.
                    pass
                    
        except KeyboardInterrupt:
            print("\n[INFO] Processing interrupted by user. Saving progress...")
            executor.shutdown(wait=False, cancel_futures=True)
            
    # Save remaining
    if buffer:
        with open(output_path, 'a') as f:
            for doc in buffer:
                f.write(json.dumps(doc) + '\n')
        processed_count += len(buffer)
            
    print(f"[INFO] Saved {processed_count} new processed chunks to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", required=True, help="Root directory containing data folders")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--clean", action="store_true", help="Enable text cleaning")
    parser.add_argument("--summary", action="store_true", help="Enable summarization")
    parser.add_argument("--chunk-size", type=int, default=10000, help="Chunk size")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--batch-size", type=int, default=50, help="Save batch size")
    parser.add_argument("--no-chunk", action="store_true", help="Disable chunking (treat full doc as one chunk)")
    
    args = parser.parse_args()
    
    final_chunk_size = 0 if args.no_chunk else args.chunk_size

    process_source_directory(
        args.data_root, 
        args.output, 
        enable_cleaning=args.clean,
        enable_summary=args.summary,
        chunk_size=final_chunk_size,
        max_workers=args.workers,
        batch_size=args.batch_size
    )
