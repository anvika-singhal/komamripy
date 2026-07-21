# benchmarks/benchmark.py
import subprocess
import json
from pathlib import Path

examples = [
    "basic_simulation.py",
    "custom_phantom_creation.py",
    "motion_artifact.py",
    "pypulseq_composability.py",
]

results = {}

for example in examples:
    print(f"\n{example}:")
    times = []
    
    for run in range(1, 11):
        code = f"""
import komamripy as km
import time
tic = time.perf_counter()
import runpy
runpy.run_path('../../examples/{example}', run_name='__main__')
toc = time.perf_counter()
print(toc - tic)
"""
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')
        elapsed = float(lines[-1])
        times.append(elapsed)
        print(f"  Run {run}: {elapsed:.3f}s")
    
    avg = sum(times) / len(times)
    results[example] = {"times": times, "average": avg}
    print(f"  Average: {avg:.3f}s")

Path("../results").mkdir(exist_ok=True)

version = Path.cwd().name
with open(f"../results/{version}.json", "w") as f:
    json.dump(results, f)

print(f"\nDone. Results saved to ../results/{version}.json")