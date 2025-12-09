# -*- coding: utf-8 -*-
"""
文本处理增强模块
包含文档摘要、清洗、结构化、质量过滤等功能
"""
import re
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
import numpy as np


# ==================== 文本清洗 ====================

def clean_text(text: str) -> str:
    """
    基础文本清洗
    - 移除多余空白
    - 统一换行符
    - 移除特殊控制字符
    """
    if not text:
        return ""
    
    # 移除控制字符 (保留换行、制表符)
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    
    # 统一换行符
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # 移除行尾空白
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    
    # 压缩多个空行为最多2个
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    # 移除行内多余空格
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()


def remove_urls(text: str, replace_with: str = "[URL]") -> str:
    """移除或替换 URL"""
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return re.sub(url_pattern, replace_with, text)


def remove_emails(text: str, replace_with: str = "[EMAIL]") -> str:
    """移除或替换邮箱地址"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.sub(email_pattern, replace_with, text)


def normalize_whitespace(text: str) -> str:
    """标准化空白字符"""
    # 将多个空格压缩为一个
    text = re.sub(r' +', ' ', text)
    # 将多个换行压缩为最多2个
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ==================== 文档质量评估 ====================

def calculate_text_quality_score(text: str) -> Dict[str, float]:
    """
    计算文本质量分数
    返回多个维度的质量指标
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
    
    # 1. 长度评分 (200-2000 词为最佳)
    word_count = len(words)
    if word_count < 50:
        length_score = word_count / 50
    elif word_count < 200:
        length_score = 0.5 + (word_count - 50) / 300
    elif word_count <= 2000:
        length_score = 1.0
    else:
        length_score = max(0.5, 1.0 - (word_count - 2000) / 10000)
    
    # 2. 词汇多样性 (unique words / total words)
    unique_words = len(set(w.lower() for w in words))
    diversity_score = min(1.0, unique_words / max(1, word_count) * 2)
    
    # 3. 可读性 (平均句子长度，10-25词为佳)
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
    
    # 4. 代码比例 (检测代码块)
    code_indicators = len(re.findall(r'```|def |class |import |function\(|var |const ', text))
    code_ratio = min(1.0, code_indicators / max(1, len(sentences)))
    
    # 综合评分 (可根据需求调整权重)
    overall_score = (
        length_score * 0.2 +
        diversity_score * 0.3 +
        readability_score * 0.3 +
        (1 - code_ratio * 0.5) * 0.2  # 过多代码降低分数
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
    过滤低质量文档
    docs: [(text, metadata), ...]
    """
    filtered = []
    for text, meta in docs:
        quality = calculate_text_quality_score(text)
        if quality['overall_score'] >= min_score:
            meta['quality_score'] = quality['overall_score']
            filtered.append((text, meta))
    return filtered


# ==================== 文档摘要生成 ====================

def extract_first_sentences(text: str, num_sentences: int = 3) -> str:
    """
    提取文档前 N 句作为简单摘要
    """
    sentences = re.split(r'[.!?]+\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    summary_sentences = sentences[:num_sentences]
    return '. '.join(summary_sentences) + '.' if summary_sentences else text[:200]


def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    """
    简单的关键词提取 (基于词频)
    """
    # 移除停用词 (简化版)
    stopwords = set([
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
        'can', 'could', 'may', 'might', 'must', 'this', 'that', 'these', 'those'
    ])
    
    # 提取单词
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # 过滤停用词并统计频率
    word_freq = {}
    for word in words:
        if word not in stopwords and len(word) > 2:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # 排序并返回 top-k
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:top_k]]


def generate_extractive_summary(text: str, max_sentences: int = 5) -> str:
    """
    生成抽取式摘要
    基于句子重要性评分 (简化的 TextRank 思想)
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.split()) > 5]
    
    if len(sentences) <= max_sentences:
        return text[:500]
    
    # 计算句子重要性 (基于词频和位置)
    word_freq = {}
    for sent in sentences:
        words = sent.lower().split()
        for word in words:
            if len(word) > 3:
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # 计算句子分数
    sentence_scores = []
    for idx, sent in enumerate(sentences):
        words = sent.lower().split()
        score = sum(word_freq.get(w, 0) for w in words if len(w) > 3)
        # 前面的句子加权
        position_weight = 1.5 if idx < 3 else 1.0
        score *= position_weight
        sentence_scores.append((score, idx, sent))
    
    # 选择得分最高的句子
    sentence_scores.sort(reverse=True)
    top_sentences = sorted(sentence_scores[:max_sentences], key=lambda x: x[1])
    
    summary = '. '.join(sent for _, _, sent in top_sentences)
    return summary + '.'


# ==================== 结构化信息提取 ====================

def extract_markdown_structure(text: str) -> Dict[str, Any]:
    """
    提取 Markdown 文档结构
    返回标题层级、章节内容等
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
        # 检测代码块
        if line.strip().startswith('```'):
            if in_code_block:
                structure['code_blocks'].append('\n'.join(code_content))
                code_content = []
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            code_content.append(line)
            continue
        
        # 检测标题
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
        
        # 收集内容
        if current_section is not None:
            current_section['content'].append(line)
        
        # 提取链接
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', line)
        structure['links'].extend(links)
        
        # 提取图片
        images = re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', line)
        structure['images'].extend(images)
    
    # 将内容列表转为字符串
    for section in structure['sections']:
        section['content'] = '\n'.join(section['content']).strip()
    
    return structure


def extract_arxiv_abstract(text: str) -> Optional[str]:
    """
    从 arXiv 论文文本中提取摘要
    """
    # 尝试多种模式
    patterns = [
        r'(?i)abstract[:\s]+(.*?)(?=\n\n(?:introduction|keywords|1\.|$))',
        r'(?i)abstract[:\s]+(.*?)(?=\nintroduction)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            abstract = match.group(1).strip()
            # 清理摘要
            abstract = re.sub(r'\s+', ' ', abstract)
            if 50 < len(abstract) < 2000:
                return abstract
    
    return None


# ==================== 智能分块增强 ====================

def semantic_chunking(text: str, 
                     max_chunk_size: int = 800,
                     min_chunk_size: int = 100,
                     overlap: int = 50) -> List[Dict[str, Any]]:
    """
    基于语义边界的智能分块
    优先在段落、句子边界切分
    """
    chunks = []
    
    # 1. 首先按段落分割
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    current_chunk = []
    current_size = 0
    chunk_id = 0
    
    for para_idx, para in enumerate(paragraphs):
        para_size = len(para)
        
        # 如果单个段落就超过最大尺寸，需要按句子切分
        if para_size > max_chunk_size:
            # 保存当前块
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
            
            # 切分大段落
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
                    # 保留重叠
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
        
        # 检查是否需要创建新块
        if current_size + para_size > max_chunk_size and current_chunk:
            chunk_text = '\n\n'.join(current_chunk)
            chunks.append({
                'text': chunk_text,
                'chunk_id': chunk_id,
                'size': len(chunk_text),
                'type': 'paragraph_based'
            })
            chunk_id += 1
            
            # 添加重叠
            if overlap > 0 and len(current_chunk) > 1:
                current_chunk = [current_chunk[-1]]
                current_size = len(current_chunk[0])
            else:
                current_chunk = []
                current_size = 0
        
        current_chunk.append(para)
        current_size += para_size + 2  # +2 for '\n\n'
    
    # 保存最后一个块
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
    按 Markdown 标题层级切分文档
    每个 section 作为独立块
    """
    structure = extract_markdown_structure(text)
    chunks = []
    
    for idx, section in enumerate(structure['sections']):
        section_text = f"# {section['title']}\n\n{section['content']}"
        
        # 如果 section 太大，进一步切分
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


# ==================== 文档增强 ====================

def enrich_chunk_with_summary(chunk_text: str, doc_summary: str = "") -> str:
    """
    为 chunk 添加文档级摘要作为上下文
    """
    if doc_summary:
        return f"[Document Summary: {doc_summary}]\n\n{chunk_text}"
    return chunk_text


def add_metadata_context(chunk_text: str, metadata: Dict[str, Any]) -> str:
    """
    将元数据信息添加到 chunk 文本中，帮助检索
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
    
    if context_parts:
        context = ' | '.join(context_parts)
        return f"[{context}]\n\n{chunk_text}"
    
    return chunk_text


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
