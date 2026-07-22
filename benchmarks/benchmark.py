# benchmarks/benchmark.py
import subprocess
import json
from pathlib import Path

benchmarks = {
    "Scanner": """
import komamripy as km
from time import perf_counter
tic = perf_counter()
sys = km.Scanner()
toc = perf_counter()
print(toc - tic)
""",
    "brain_phantom2D": """
import komamripy as km
from time import perf_counter
tic = perf_counter()
obj = km.brain_phantom2D()
toc = perf_counter()
print(toc - tic)
""",
    "EPI_example": """
import komamripy as km
from time import perf_counter
tic = perf_counter()
seq = km.PulseDesigner.EPI_example()
toc = perf_counter()
print(toc - tic)
""",
    "discretize": """
import komamripy as km
from time import perf_counter
seq = km.PulseDesigner.EPI_example()
tic = perf_counter()
seq_disc = km.discretize(seq)
toc = perf_counter()
print(toc - tic)
""",
    "simulate": """
import komamripy as km
from time import perf_counter
sys = km.Scanner()
obj = km.brain_phantom2D()
seq = km.PulseDesigner.EPI_example()
tic = perf_counter()
signal = km.simulate(obj, seq, sys, sim_params={"return_type": "mat"})
toc = perf_counter()
print(toc - tic)
""",
    "Phantom": """
import komamripy as km
import numpy as np
from time import perf_counter
coords = np.linspace(-40e-3, 40e-3, 64)
xx, yy = np.meshgrid(coords, coords)
radius = np.sqrt(xx**2 + yy**2)
disk_mask = radius <= 32e-3
ring_mask = radius[disk_mask] >= 22e-3
x = xx[disk_mask]
y = yy[disk_mask]
z = np.zeros_like(x)
rho = np.where(ring_mask, 0.65, 0.95)
t1 = np.where(ring_mask, 0.7, 1.2)
t2 = np.where(ring_mask, 70e-3, 110e-3)
tic = perf_counter()
phantom = km.Phantom(name="ring_phantom", x=x, y=y, z=z, ρ=rho, T1=t1, T2=t2, T2s=t2, Δw=np.zeros_like(x))
toc = perf_counter()
print(toc - tic)
""",
    "write_phantom": """
import komamripy as km
import numpy as np
from time import perf_counter
import tempfile, os
coords = np.linspace(-40e-3, 40e-3, 64)
xx, yy = np.meshgrid(coords, coords)
radius = np.sqrt(xx**2 + yy**2)
disk_mask = radius <= 32e-3
ring_mask = radius[disk_mask] >= 22e-3
x = xx[disk_mask]
y = yy[disk_mask]
z = np.zeros_like(x)
rho = np.where(ring_mask, 0.65, 0.95)
t1 = np.where(ring_mask, 0.7, 1.2)
t2 = np.where(ring_mask, 70e-3, 110e-3)
phantom = km.Phantom(name="ring_phantom", x=x, y=y, z=z, ρ=rho, T1=t1, T2=t2, T2s=t2, Δw=np.zeros_like(x))
with tempfile.TemporaryDirectory() as tmpdir:
    phantom_path = os.path.join(tmpdir, "ring_phantom.phantom")
    tic = perf_counter()
    km.files.write_phantom(phantom, phantom_path)
    toc = perf_counter()
    print(toc - tic)
""",
    "read_phantom": """
import komamripy as km
import numpy as np
from time import perf_counter
import tempfile, os
coords = np.linspace(-40e-3, 40e-3, 64)
xx, yy = np.meshgrid(coords, coords)
radius = np.sqrt(xx**2 + yy**2)
disk_mask = radius <= 32e-3
ring_mask = radius[disk_mask] >= 22e-3
x = xx[disk_mask]
y = yy[disk_mask]
z = np.zeros_like(x)
rho = np.where(ring_mask, 0.65, 0.95)
t1 = np.where(ring_mask, 0.7, 1.2)
t2 = np.where(ring_mask, 70e-3, 110e-3)
phantom = km.Phantom(name="ring_phantom", x=x, y=y, z=z, ρ=rho, T1=t1, T2=t2, T2s=t2, Δw=np.zeros_like(x))
with tempfile.TemporaryDirectory() as tmpdir:
    phantom_path = os.path.join(tmpdir, "ring_phantom.phantom")
    km.files.write_phantom(phantom, phantom_path)
    tic = perf_counter()
    loaded = km.files.read_phantom(phantom_path)
    toc = perf_counter()
    print(toc - tic)
""",
}

results = {}

for name, code in benchmarks.items():
    print(f"\n{name}:")
    times = []
    
    for run in range(1, 11):
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  Error: {result.stderr}")
            break
        lines = result.stdout.strip().split('\n')
        elapsed = float(lines[-1])
        times.append(elapsed)
        print(f"  Run {run}: {elapsed:.3f}s")
    
    if times:
        avg = sum(times) / len(times)
        results[name] = {"times": times, "average": avg}
        print(f"  Average: {avg:.3f}s")

Path("../results").mkdir(exist_ok=True)

version = Path.cwd().name
with open(f"../results/{version}.json", "w") as f:
    json.dump(results, f)

print(f"\nDone. Results saved to ../results/{version}.json")