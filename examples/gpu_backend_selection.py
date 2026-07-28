"""Simulate MRI acquisition with optional GPU acceleration.

This example demonstrates GPU backend selection:
- Uncomment km.load_cuda() (or load_metal/load_amdgpu/load_oneapi) to enable GPU
- Once a backend is loaded, gpu=true is used by default
- Without a backend, simulation runs on CPU automatically

The simulation produces identical results on CPU and GPU (within numerical precision).
"""

import numpy as np

import komamripy as km

# Optional: Load a GPU backend to enable GPU acceleration.
# Uncomment ONE of these (backend must be installed):
# km.load_cuda()      # NVIDIA GPUs
# km.load_metal()     # Apple Silicon
# km.load_amdgpu()    # AMD GPUs
# km.load_oneapi()    # Intel GPUs (experimental)

# If no backend is loaded, simulation runs on CPU automatically.

print("Creating phantom...")
coords = np.linspace(-40e-3, 40e-3, 64)
xx, yy = np.meshgrid(coords, coords)
radius = np.sqrt(xx**2 + yy**2)
mask = radius <= 32e-3

x = xx[mask]
y = yy[mask]
z = np.zeros_like(x)

phantom = km.Phantom(
    name="circle",
    x=x,
    y=y,
    z=z,
    ρ=np.ones_like(x),
    T1=np.ones_like(x),
    T2=0.1 * np.ones_like(x),
    T2s=0.1 * np.ones_like(x),
)

print("Setting up acquisition...")
sys = km.Scanner()
seq = km.PulseDesigner.EPI_example()

print("Simulating...")
sim_params = {"return_type": "mat"}  # gpu=true by default if backend loaded
signal = km.simulate(phantom, seq, sys, sim_params=sim_params)
signal = np.asarray(signal).reshape(-1)

print(f"Simulation complete!")
print(f"Signal shape: {signal.shape}")
print(f"Signal magnitude range: [{np.abs(signal).min():.2e}, {np.abs(signal).max():.2e}]")