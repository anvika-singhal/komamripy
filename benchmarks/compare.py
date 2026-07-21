# benchmarks/compare.py
import json

with open("results/bench-0.0.6.json") as f:
    v066 = json.load(f)

with open("results/bench-0.0.7.json") as f:
    v067 = json.load(f)

print(f"\n{'='*70}")
print("Benchmark Results: v0.0.6 vs v0.0.7")
print('='*70)

for example in v066:
    time_066 = v066[example]["average"]
    time_067 = v067[example]["average"]
    speedup = time_066 / time_067
    
    print(f"\n{example}:")
    print(f"  v0.0.6: {time_066:.3f}s")
    print(f"  v0.0.7: {time_067:.3f}s")
    print(f"  Speedup: {speedup:.2f}x")
