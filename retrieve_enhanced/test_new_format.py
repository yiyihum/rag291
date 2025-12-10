#!/usr/bin/env python3
"""
测试新的数据格式:
- content: 原始文本内容
- metadata: 原始元数据
- generated: LLM生成的内容 (keywords, summary)
"""

import json
from pathlib import Path

def test_data_format():
    """测试新格式的数据结构"""
    
    # 模拟一个新格式的文档
    sample_doc = {
        'content': '[Title: Test Document | Source: github]\n\n[Document Summary: This is a test summary.]\n\n[Keywords: test, sample, document]\n\nThis is the actual content of the document.',
        'metadata': {
            'source': 'github',
            'repo': 'test/repo',
            'path': 'data/github_readmes/test/repo/README.md',
            'title': 'Test Document'
        },
        'generated': {
            'keywords': ['test', 'sample', 'document'],
            'summary': 'This is a test summary.'
        },
        'chunk_id': 0,
        'chunk_type': 'full_doc'
    }
    
    print("测试文档结构:")
    print(json.dumps(sample_doc, indent=2, ensure_ascii=False))
    print("\n" + "="*80 + "\n")
    
    # 验证字段
    assert 'content' in sample_doc, "缺少 content 字段"
    assert 'metadata' in sample_doc, "缺少 metadata 字段"
    assert 'generated' in sample_doc, "缺少 generated 字段"
    
    # 验证 metadata 不包含生成的内容
    assert 'keywords' not in sample_doc['metadata'], "metadata 不应包含 keywords"
    assert 'summary' not in sample_doc['metadata'], "metadata 不应包含 summary"
    
    # 验证 generated 包含必要字段
    assert 'keywords' in sample_doc['generated'], "generated 应包含 keywords"
    assert 'summary' in sample_doc['generated'], "generated 应包含 summary"
    
    print("✓ 所有字段验证通过!")
    
    # 检查现有文件的格式
    processed_file = Path(__file__).parent.parent / 'processed_data.jsonl'
    if processed_file.exists():
        print(f"\n检查现有文件: {processed_file}")
        print("注意:现有文件使用旧格式,需要重新处理数据")
        
        # 读取第一行检查格式
        with open(processed_file, 'r') as f:
            first_line = f.readline()
            if first_line.strip():
                doc = json.loads(first_line)
                print("\n当前文件格式:")
                print(f"- 是否有 'generated' 字段: {'generated' in doc}")
                print(f"- 'metadata' 中是否有 'keywords': {'keywords' in doc.get('metadata', {})}")
                print(f"- 'metadata' 中是否有 'summary': {'summary' in doc.get('metadata', {})}")
                
                if 'generated' not in doc:
                    print("\n⚠️  文件使用旧格式,建议重新运行数据处理!")
                else:
                    print("\n✓ 文件已使用新格式!")

if __name__ == "__main__":
    test_data_format()
