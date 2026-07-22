# benchmarks/compare.py
import json
from pathlib import Path

with open("results/bench-0.0.6.json") as f:
    v066 = json.load(f)

with open("results/bench-0.0.7.json") as f:
    v067 = json.load(f)

# Create markdown report
report = []
report.append("# KomaMRI Precompilation Benchmark Results\n")
report.append("## v0.0.6 vs v0.0.7 Performance Comparison\n")
report.append("| Function | v0.0.6 (s) | v0.0.7 (s) | Speedup |\n")
report.append("|----------|-----------|-----------|----------|\n")

total_066 = 0
total_067 = 0

for func in sorted(v066.keys()):
    time_066 = v066[func]["average"]
    time_067 = v067[func]["average"]
    speedup = time_066 / time_067
    
    total_066 += time_066
    total_067 += time_067
    
    speedup_str = f"{speedup:.2f}x" if speedup >= 1.0 else f"{1/speedup:.2f}x (slower)"
    report.append(f"| {func} | {time_066:.3f} | {time_067:.3f} | {speedup_str} |\n")

overall_speedup = total_066 / total_067
report.append(f"\n**Overall Speedup: {overall_speedup:.2f}x**\n")
report.append(f"Total v0.0.6: {total_066:.3f}s\n")
report.append(f"Total v0.0.7: {total_067:.3f}s\n")

# Save to file
report_text = "".join(report)
Path("results/BENCHMARK_REPORT.md").write_text(report_text)

print(report_text)
print("\nReport saved to results/BENCHMARK_REPORT.md")