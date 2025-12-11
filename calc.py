import json
import argparse
import sys
from pathlib import Path

def calculate_throughput(input_file: str):
    file_path = Path(input_file)
    
    if not file_path.exists():
        print(f"[ERROR] File not found: {input_file}")
        return

    print(f"[INFO] Reading from: {input_file}\n")
    
    # 表头格式化
    header = f"{'QID':<6} | {'Resp Tokens':<12} | {'Time (s)':<10} | {'Throughput (T/s)':<18}"
    print(header)
    print("-" * len(header))

    throughputs = []
    valid_entries = 0
    total_response_tokens = 0
    total_time = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                data = json.loads(line)
                qid = data.get('qid', 'N/A')
                
                # 获取 metrics 数据
                metrics = data.get('metrics', {})
                if not metrics:
                    print(f"[WARN] QID {qid} missing 'metrics' field. Skipping.")
                    continue

                # 提取关键指标
                # 注意：这里使用 response_tokens，而不是 total_tokens
                resp_tokens = metrics.get('response_tokens', 0)
                latency = metrics.get('latency_seconds', 0.0)

                if latency > 0:
                    # 计算单个 Query 的 Throughput
                    tp = resp_tokens / latency
                    throughputs.append(tp)
                    
                    # 累加用于计算整体统计 (Micro-average)
                    total_response_tokens += resp_tokens
                    total_time += latency
                    valid_entries += 1
                    
                    print(f"{qid:<6} | {resp_tokens:<12} | {latency:<10.4f} | {tp:<18.2f}")
                else:
                    print(f"{qid:<6} | {resp_tokens:<12} | {latency:<10.4f} | {'INF (Time=0)':<18}")

    except json.JSONDecodeError:
        print("[ERROR] Failed to decode JSON line.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

    # 打印最终结果
    if throughputs:
        avg_throughput = sum(throughputs) / len(throughputs)
        
        print("-" * len(header))
        print(f"\n[SUMMARY]")
        print(f"Total Queries Processed: {valid_entries}")
        print(f"Average Throughput (Arithmetic Mean): {avg_throughput:.2f} Tokens/s")
        
        # 额外提供总Token/总时间的计算方式供参考 (通常这两个值会很接近)
        if total_time > 0:
            global_throughput = total_response_tokens / total_time
            print(f"Global Throughput (Total Tokens / Total Time): {global_throughput:.2f} Tokens/s")
    else:
        print("\n[WARN] No valid data found to calculate throughput.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate LLM Throughput from JSONL results.")
    parser.add_argument("--input", required=True, help="Path to the results .jsonl file")
    
    args = parser.parse_args()
    
    calculate_throughput(args.input)