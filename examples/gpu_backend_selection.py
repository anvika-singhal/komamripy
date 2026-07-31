"""Simulate MRI acquisition with optional GPU backend acceleration.

This example demonstrates GPU backend selection. Uncomment one of the backend
load functions to enable GPU acceleration (CUDA, Metal, AMDGPU, or oneAPI).
Without a backend, simulation runs on CPU automatically.
"""

import numpy as np

import komamripy as km

# Optional: Load a GPU backend to enable GPU acceleration
# Uncomment ONE of these (backend must be installed):
# km.load_cuda()      # NVIDIA GPUs
# km.load_metal()     # Apple Silicon
# km.load_amdgpu()    # AMD GPUs
# km.load_oneapi()    # Intel GPUs (experimental)

# Define acquisition inputs
sys = km.Scanner()
obj = km.brain_phantom2D()
seq = km.PulseDesigner.EPI_example()

# Simulate with KomaMRI (gpu=true by default if backend loaded)
sim_params = {"return_type": "mat"}
signal = km.simulate(obj, seq, sys, sim_params=sim_params)
signal = np.asarray(signal).reshape(-1)
