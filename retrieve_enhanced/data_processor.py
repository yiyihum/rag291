import json
import glob
from pathlib import Path
from typing import List, Dict, Any, Optional
from tqdm import tqdm
from llm_client import LLMClient, get_llm_client

# Try to import text_processing, handle if missing
try:
    from text_processing import (
        clean_text,
        calculate_text_quality_score,
        semantic_chunking,
        chunk_by_markdown_headers,
        enrich_chunk_with_summary,
        add_metadata_context
    )
    TEXT_PROCESSING_AVAILABLE = True
except ImportError:
    TEXT_PROCESSING_AVAILABLE = False
    print("[WARN] text_processing module not found. Advanced features disabled.")

class DataProcessor:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def clean_text(self, text: str) -> str:
        """Use LLM to clean text (fix typos, formatting, OCR errors)."""
        if TEXT_PROCESSING_AVAILABLE:
            # Use heuristic cleaning first to save tokens
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

    def generate_qa_pairs(self, text: str, num_pairs: int = 3) -> List[Dict[str, str]]:
        """Generate Q&A pairs for the text."""
        prompt = f"""Generate {num_pairs} question-answer pairs based on the following text.
        Format the output as a JSON list of objects with 'question' and 'answer' keys.
        
        Text:
        {text}
        """
        response = self.llm.generate(prompt, system_prompt="You are a helpful assistant that generates Q&A pairs.")
        try:
            start = response.find('[')
            end = response.rfind(']') + 1
            if start != -1 and end != -1:
                return json.loads(response[start:end])
            return []
        except:
            print(f"[WARN] Failed to parse Q&A JSON: {response[:100]}...")
            return []

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
        if not TEXT_PROCESSING_AVAILABLE:
            # Fallback to simple chunking
            return [{'text': text[i:i+max_chunk_size], 'chunk_id': i//max_chunk_size} 
                    for i in range(0, len(text), max_chunk_size)]

        source = meta.get('source', '')
        
        if source == 'github' or 'README' in meta.get('title', ''):
            return chunk_by_markdown_headers(text, max_chunk_size=max_chunk_size)
        elif source == 'arxiv':
            # For papers, semantic chunking works well, or we could implement section-based if we had structure
            return semantic_chunking(text, max_chunk_size=max_chunk_size)
        else:
            # Default semantic
            return semantic_chunking(text, max_chunk_size=max_chunk_size)

    def filter_quality(self, text: str, meta: Dict[str, Any]) -> bool:
        """
        Filter low quality documents.
        """
        if not TEXT_PROCESSING_AVAILABLE:
            return True
            
        scores = calculate_text_quality_score(text)
        
        # Specific rules
        if meta.get('source') == 'github':
            # GitHub READMEs shouldn't be just code
            if scores['code_ratio'] > 0.8:
                return False
                
        if scores['overall_score'] < 0.3:
            return False
            
        return True

import concurrent.futures

def process_single_document(
    text: str, 
    meta: Dict[str, Any], 
    processor: DataProcessor, 
    enable_cleaning: bool, 
    enable_qa: bool, 
    enable_summary: bool, 
    chunk_size: int
) -> List[Dict[str, Any]]:
    """Helper function to process a single document."""
    try:
        # Quality Filter
        if not processor.filter_quality(text, meta):
            return []
            
        # Cleaning
        if enable_cleaning:
            if TEXT_PROCESSING_AVAILABLE:
                text = clean_text(text)
            # text = processor.clean_text(text) 
        
        # Augmentation - Keywords
        if True:
             meta['keywords'] = processor.extract_keywords(text)
             
        # Augmentation - Summary
        doc_summary = ""
        if enable_summary:
            doc_summary = processor.generate_summary(text)
            meta['summary'] = doc_summary

        # Chunking
        if chunk_size <= 0: # Disable chunking
             chunks = [{'text': text, 'chunk_id': 0, 'type': 'full_doc'}]
        else:
             chunks = processor.adaptive_chunking(text, meta, max_chunk_size=chunk_size)
        
        processed_chunks = []
        for chunk in chunks:
            chunk_text = chunk['text']
            
            # Enrich chunk
            if TEXT_PROCESSING_AVAILABLE:
                if doc_summary:
                    chunk_text = enrich_chunk_with_summary(chunk_text, doc_summary)
                chunk_text = add_metadata_context(chunk_text, meta)
            
            chunk_doc = {
                'content': chunk_text,
                'metadata': meta,
                'chunk_id': chunk['chunk_id'],
                'chunk_type': chunk.get('type', 'unknown')
            }
            
            # QA Generation
            if enable_qa:
                chunk_doc['qa_pairs'] = processor.generate_qa_pairs(chunk_text)
                
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
    enable_qa: bool = False,
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
                # Arxiv jsonl doesn't have file paths per doc usually, but if it did:
                # meta['path'] = ... 
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
            meta = {'source': 'hf_model_card', 'title': p.stem, 'path': rel_path}
            all_docs.append((text, meta))
        # Datasets
        for f in glob.glob(str(hf_dir / "datasets" / "*.md")):
            p = Path(f)
            text = p.read_text(errors='ignore')
            
            try:
                rel_path = str(p.relative_to(project_root))
            except ValueError:
                rel_path = str(p)
            meta = {'source': 'hf_dataset_card', 'title': p.stem, 'path': rel_path}
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
                text, meta, processor, enable_cleaning, enable_qa, enable_summary, chunk_size
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
    parser.add_argument("--qa", action="store_true", help="Enable Q&A")
    parser.add_argument("--summary", action="store_true", help="Enable summarization")
    parser.add_argument("--chunk-size", type=int, default=1000, help="Chunk size")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--batch-size", type=int, default=50, help="Save batch size")
    parser.add_argument("--no-chunk", action="store_true", help="Disable chunking (treat full doc as one chunk)")
    
    args = parser.parse_args()
    
    final_chunk_size = 0 if args.no_chunk else args.chunk_size

    process_source_directory(
        args.data_root, 
        args.output, 
        enable_cleaning=args.clean,
        enable_qa=args.qa,
        enable_summary=args.summary,
        chunk_size=final_chunk_size,
        max_workers=args.workers,
        batch_size=args.batch_size
    )
