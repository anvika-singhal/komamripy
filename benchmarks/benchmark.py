# benchmarks/benchmark.py
import subprocess
import sys

examples = [
    "basic_simulation.py",
    "custom_phantom_creation.py",
    "motion_artifact.py",
    "pypulseq_composability.py",
]

versions = ["0.0.6", "0.0.7"]

results = {}

for version in versions:
    print(f"\n{'='*70}")
    print(f"Benchmarking komamripy v{version}")
    print('='*70)
    
    # Install version
    subprocess.run(
        [sys.executable, "-m", "pip", "install", f"komamripy=={version}"],
        capture_output=True,
        check=True,
    )
    
    results[version] = {}
    
    for example in examples:
        print(f"\n{example}:")
        times = []
        
        for run in range(1, 11):
            print(f"  Run {run}...")
            
            wrapper_code = f"""
import time
import runpy

tic = time.perf_counter()
runpy.run_path('examples/{example}', run_name='__main__')
toc = time.perf_counter()
print(f"{{toc - tic:.3f}}")
"""
            
            result = subprocess.run(
                [sys.executable, "-c", wrapper_code],
                capture_output=True,
                text=True,
            )
            
            if result.returncode == 0:
                elapsed = float(result.stdout.strip())
                times.append(elapsed)
                print(f"    Time: {elapsed:.3f}s")
            else:
                print(f"    Error: {result.stderr}")
        
        if times:
            avg_time = sum(times) / len(times)
            results[version][example] = {
                "times": times,
                "average": avg_time,
            }
            print(f"  Average: {avg_time:.3f}s")
        else:
            print(f"  No successful runs")

print(f"\n{'='*70}")
print("Summary")
print('='*70)

for example in examples:
    if example in results["0.0.6"] and example in results["0.0.7"]:
        v066 = results["0.0.6"][example]["average"]
        v067 = results["0.0.7"][example]["average"]
        speedup = v066 / v067
        
        print(f"\n{example}:")
        print(f"  v0.0.6: {v066:.3f}s")
        print(f"  v0.0.7: {v067:.3f}s")
        print(f"  Speedup: {speedup:.2f}x")