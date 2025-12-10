# -*- coding: utf-8 -*-
"""
Text Processing Enhancement Module
Contains functions for document summarization, cleaning, structuring, and quality filtering.
"""
import re
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
import numpy as np


# ==================== Text Cleaning ====================

def clean_text(text: str) -> str:
    """
    Basic text cleaning
    - Remove excess whitespace
    - Unify newlines
    - Remove special control characters
    """
    if not text:
        return ""
    
    # Remove control characters (keep newlines, tabs)
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    
    # Unify newlines
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove trailing whitespace
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    
    # Compress multiple empty lines to max 2
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    # Remove excess inline whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()


# ==================== Document Quality Assessment ====================

def calculate_text_quality_score(text: str) -> Dict[str, float]:
    """
    Calculate text quality score
    Returns quality metrics across multiple dimensions
    """
    if not text or len(text) < 50:
        return {
            'length_score': 0.0,
            'diversity_score': 0.0,
            'readability_score': 0.0,
            'code_ratio': 0.0,
            'overall_score': 0.0
        }
    
    words = text.split()
    
    # 1. Length score (200-2000 words is optimal)
    word_count = len(words)
    if word_count < 50:
        length_score = word_count / 50
    elif word_count < 200:
        length_score = 0.5 + (word_count - 50) / 300
    elif word_count <= 2000:
        length_score = 1.0
    else:
        length_score = max(0.5, 1.0 - (word_count - 2000) / 10000)
    
    # 2. Vocabulary diversity (unique words / total words)
    unique_words = len(set(w.lower() for w in words))
    diversity_score = min(1.0, unique_words / max(1, word_count) * 2)
    
    # 3. Readability (average sentence length, 10-25 words is optimal)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if sentences:
        avg_sentence_len = word_count / len(sentences)
        if 10 <= avg_sentence_len <= 25:
            readability_score = 1.0
        elif avg_sentence_len < 10:
            readability_score = avg_sentence_len / 10
        else:
            readability_score = max(0.3, 1.0 - (avg_sentence_len - 25) / 50)
    else:
        readability_score = 0.0
    
    # 4. Code ratio (detect code blocks)
    code_indicators = len(re.findall(r'```|def |class |import |function\(|var |const ', text))
    code_ratio = min(1.0, code_indicators / max(1, len(sentences)))
    
    # Overall score (weights can be adjusted as needed)
    overall_score = (
        length_score * 0.2 +
        diversity_score * 0.3 +
        readability_score * 0.3 +
        (1 - code_ratio * 0.5) * 0.2  # Excessive code lowers score
    )
    
    return {
        'length_score': round(length_score, 3),
        'diversity_score': round(diversity_score, 3),
        'readability_score': round(readability_score, 3),
        'code_ratio': round(code_ratio, 3),
        'overall_score': round(overall_score, 3)
    }


def filter_low_quality_docs(docs: List[Tuple[str, Dict]], 
                           min_score: float = 0.3) -> List[Tuple[str, Dict]]:
    """
    Filter low quality documents
    docs: [(text, metadata), ...]
    """
    filtered = []
    for text, meta in docs:
        quality = calculate_text_quality_score(text)
        if quality['overall_score'] >= min_score:
            meta['quality_score'] = quality['overall_score']
            filtered.append((text, meta))
    return filtered


# ==================== Document Summary Generation ====================

def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    """
    Simple keyword extraction (frequency-based)
    """
    # Remove stopwords (simplified)
    stopwords = set([
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
        'can', 'could', 'may', 'might', 'must', 'this', 'that', 'these', 'those'
    ])
    
    # Extract words
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # Filter stopwords and count frequency
    word_freq = {}
    for word in words:
        if word not in stopwords and len(word) > 2:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort and return top-k
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:top_k]]


def generate_extractive_summary(text: str, max_sentences: int = 5) -> str:
    """
    Generate extractive summary
    Based on sentence importance score (simplified TextRank idea)
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.split()) > 5]
    
    if len(sentences) <= max_sentences:
        return text[:500]
    
    # Calculate sentence importance (based on word frequency and position)
    word_freq = {}
    for sent in sentences:
        words = sent.lower().split()
        for word in words:
            if len(word) > 3:
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # Calculate sentence scores
    sentence_scores = []
    for idx, sent in enumerate(sentences):
        words = sent.lower().split()
        score = sum(word_freq.get(w, 0) for w in words if len(w) > 3)
        # Weight earlier sentences higher
        position_weight = 1.5 if idx < 3 else 1.0
        score *= position_weight
        sentence_scores.append((score, idx, sent))
    
    # Select top scoring sentences
    sentence_scores.sort(reverse=True)
    top_sentences = sorted(sentence_scores[:max_sentences], key=lambda x: x[1])
    
    summary = '. '.join(sent for _, _, sent in top_sentences)
    return summary + '.'


# ==================== Structured Information Extraction ====================

def extract_markdown_structure(text: str) -> Dict[str, Any]:
    """
    Extract Markdown document structure
    Returns heading levels, section content, etc.
    """
    lines = text.split('\n')
    structure = {
        'title': '',
        'sections': [],
        'code_blocks': [],
        'links': [],
        'images': []
    }
    
    current_section = None
    in_code_block = False
    code_content = []
    
    for line in lines:
        # Detect code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                structure['code_blocks'].append('\n'.join(code_content))
                code_content = []
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            code_content.append(line)
            continue
        
        # Detect headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            
            if level == 1 and not structure['title']:
                structure['title'] = title
            
            current_section = {
                'level': level,
                'title': title,
                'content': []
            }
            structure['sections'].append(current_section)
            continue
        
        # Collect content
        if current_section is not None:
            current_section['content'].append(line)
        
        # Extract links
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', line)
        structure['links'].extend(links)
        
        # Extract images
        images = re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', line)
        structure['images'].extend(images)
    
    # Convert content list to string
    for section in structure['sections']:
        section['content'] = '\n'.join(section['content']).strip()
    
    return structure


# ==================== Intelligent Chunking Enhancement ====================

def semantic_chunking(text: str, 
                     max_chunk_size: int = 800,
                     min_chunk_size: int = 100,
                     overlap: int = 50) -> List[Dict[str, Any]]:
    """
    Intelligent chunking based on semantic boundaries
    Prioritizes splitting at paragraph and sentence boundaries
    """
    chunks = []
    
    # 1. First split by paragraphs
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    current_chunk = []
    current_size = 0
    chunk_id = 0
    
    for para_idx, para in enumerate(paragraphs):
        para_size = len(para)
        
        # If a single paragraph exceeds max size, split by sentences
        if para_size > max_chunk_size:
            # Save current chunk
            if current_chunk:
                chunk_text = '\n\n'.join(current_chunk)
                chunks.append({
                    'text': chunk_text,
                    'chunk_id': chunk_id,
                    'size': len(chunk_text),
                    'type': 'paragraph_based'
                })
                chunk_id += 1
                current_chunk = []
                current_size = 0
            
            # Split large paragraph
            sentences = re.split(r'([.!?]+\s+)', para)
            sub_chunk = []
            sub_size = 0
            
            for sent in sentences:
                if not sent.strip():
                    continue
                sent_size = len(sent)
                
                if sub_size + sent_size > max_chunk_size and sub_chunk:
                    chunks.append({
                        'text': ''.join(sub_chunk),
                        'chunk_id': chunk_id,
                        'size': sub_size,
                        'type': 'sentence_based'
                    })
                    chunk_id += 1
                    # Keep overlap
                    if overlap > 0 and len(sub_chunk) > 1:
                        sub_chunk = sub_chunk[-1:]
                        sub_size = len(sub_chunk[0])
                    else:
                        sub_chunk = []
                        sub_size = 0
                
                sub_chunk.append(sent)
                sub_size += sent_size
            
            if sub_chunk:
                chunks.append({
                    'text': ''.join(sub_chunk),
                    'chunk_id': chunk_id,
                    'size': sub_size,
                    'type': 'sentence_based'
                })
                chunk_id += 1
            
            continue
        
        # Check if new chunk is needed
        if current_size + para_size > max_chunk_size and current_chunk:
            chunk_text = '\n\n'.join(current_chunk)
            chunks.append({
                'text': chunk_text,
                'chunk_id': chunk_id,
                'size': len(chunk_text),
                'type': 'paragraph_based'
            })
            chunk_id += 1
            
            # Add overlap
            if overlap > 0 and len(current_chunk) > 1:
                current_chunk = [current_chunk[-1]]
                current_size = len(current_chunk[0])
            else:
                current_chunk = []
                current_size = 0
        
        current_chunk.append(para)
        current_size += para_size + 2  # +2 for '\n\n'
    
    # Save last chunk
    if current_chunk:
        chunk_text = '\n\n'.join(current_chunk)
        if len(chunk_text) >= min_chunk_size:
            chunks.append({
                'text': chunk_text,
                'chunk_id': chunk_id,
                'size': len(chunk_text),
                'type': 'paragraph_based'
            })
    
    return chunks


def chunk_by_markdown_headers(text: str, max_chunk_size: int = 1000) -> List[Dict[str, Any]]:
    """
    Split document by Markdown heading levels
    Each section as an independent chunk
    """
    structure = extract_markdown_structure(text)
    chunks = []
    
    for idx, section in enumerate(structure['sections']):
        section_text = f"# {section['title']}\n\n{section['content']}"
        
        # If section is too large, split further
        if len(section_text) > max_chunk_size:
            sub_chunks = semantic_chunking(section['content'], max_chunk_size)
            for sub_idx, sub_chunk in enumerate(sub_chunks):
                chunks.append({
                    'text': f"# {section['title']}\n\n{sub_chunk['text']}",
                    'chunk_id': f"{idx}_{sub_idx}",
                    'section_title': section['title'],
                    'section_level': section['level'],
                    'size': len(sub_chunk['text']),
                    'type': 'section_based'
                })
        else:
            chunks.append({
                'text': section_text,
                'chunk_id': idx,
                'section_title': section['title'],
                'section_level': section['level'],
                'size': len(section_text),
                'type': 'section_based'
            })
    
    return chunks


# ==================== Document Enhancement ====================

def enrich_chunk_with_summary(chunk_text: str, doc_summary: str = "") -> str:
    """
    Add document-level summary to chunk as context
    """
    if doc_summary:
        return f"[Document Summary: {doc_summary}]\n\n{chunk_text}"
    return chunk_text


def add_metadata_context(chunk_text: str, metadata: Dict[str, Any], generated: Optional[Dict[str, Any]] = None) -> str:
    """
    Add metadata information to chunk text to help retrieval
    If generated dictionary is provided, also add LLM generated summary and keywords
    """
    context_parts = []
    
    if metadata.get('title'):
        context_parts.append(f"Title: {metadata['title']}")
    
    if metadata.get('source'):
        context_parts.append(f"Source: {metadata['source']}")
    
    if metadata.get('authors'):
        authors = metadata['authors']
        if isinstance(authors, list):
            authors = ', '.join(authors[:3])
        context_parts.append(f"Authors: {authors}")
    
    if metadata.get('primary_category'):
        context_parts.append(f"Category: {metadata['primary_category']}")
    
    # Add specific IDs if available
    if metadata.get('arxiv_id'):
        context_parts.append(f"Arxiv ID: {metadata['arxiv_id']}")
    if metadata.get('model_id'):
        context_parts.append(f"Model ID: {metadata['model_id']}")
    if metadata.get('dataset_id'):
        context_parts.append(f"Dataset ID: {metadata['dataset_id']}")
    if metadata.get('repo'):
        context_parts.append(f"Repo: {metadata['repo']}")
    
    # Build base context
    full_text = chunk_text
    if context_parts:
        context = ' | '.join(context_parts)
        full_text = f"[{context}]\n\n{full_text}"
    
    # If generated summary and keywords exist, add to document header
    if generated:
        generated_parts = []
        
        if generated.get('summary'):
            generated_parts.append(f"[Document Summary: {generated['summary']}]")
        
        if generated.get('keywords'):
            keywords = generated['keywords']
            if isinstance(keywords, list):
                keywords = ', '.join(keywords)
            generated_parts.append(f"[Keywords: {keywords}]")
        
        if generated_parts:
            generated_context = '\n\n'.join(generated_parts)
            # Add generated content after base context
            if context_parts:
                full_text = f"[{context}]\n\n{generated_context}\n\n{chunk_text}"
            else:
                full_text = f"{generated_context}\n\n{chunk_text}"
    
    return full_text


# ==================== 工具函数 ====================

def estimate_token_count(text: str, avg_chars_per_token: float = 4.0) -> int:
    """
    估算文本的 token 数量
    """
    return int(len(text) / avg_chars_per_token)


def truncate_to_token_limit(text: str, max_tokens: int = 512, avg_chars_per_token: float = 4.0) -> str:
    """
    截断文本到指定 token 限制
    """
    max_chars = int(max_tokens * avg_chars_per_token)
    if len(text) <= max_chars:
        return text
    
    # 尝试在句子边界截断
    truncated = text[:max_chars]
    last_period = truncated.rfind('.')
    if last_period > max_chars * 0.8:
        return truncated[:last_period + 1]
    
    return truncated + "..."


if __name__ == "__main__":
    # 测试示例
    sample_text = """
    # Introduction to RAG
    
    Retrieval-Augmented Generation (RAG) is a powerful technique that combines 
    information retrieval with text generation. It helps reduce hallucinations 
    and provides up-to-date information.
    
    ## Key Components
    
    The main components include:
    1. Document retrieval system
    2. Text embedding models
    3. Language generation models
    
    RAG has been widely adopted in various applications including question 
    answering, summarization, and conversational AI systems.
    """
    
    # 测试清洗
    cleaned = clean_text(sample_text)
    print("Cleaned text length:", len(cleaned))
    
    # 测试质量评分
    quality = calculate_text_quality_score(cleaned)
    print("Quality scores:", quality)
    
    # 测试摘要
    summary = generate_extractive_summary(cleaned, max_sentences=2)
    print("Summary:", summary)
    
    # 测试关键词
    keywords = extract_keywords(cleaned, top_k=5)
    print("Keywords:", keywords)
    
    # 测试智能分块
    chunks = semantic_chunking(cleaned, max_chunk_size=200)
    print(f"Generated {len(chunks)} chunks")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {chunk['size']} chars, type: {chunk['type']}")
