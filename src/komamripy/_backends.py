"""GPU backend selection for komamripy.

Maps Python functions to Julia backend loading:
- load_cuda() → using CUDA
- load_metal() → using Metal
- load_amdgpu() → using AMDGPU
- load_oneapi() → using oneAPI

Once a backend is loaded, KomaMRI.jl automatically uses it with gpu=true by default.
"""

from ._session import get_julia


def load_cuda() -> None:
    """Load CUDA backend: using CUDA"""
    jl = get_julia()
    jl.seval("using CUDA")


def load_metal() -> None:
    """Load Metal backend: using Metal"""
    jl = get_julia()
    jl.seval("using Metal")


def load_amdgpu() -> None:
    """Load AMDGPU backend: using AMDGPU"""
    jl = get_julia()
    jl.seval("using AMDGPU")


def load_oneapi() -> None:
    """Load oneAPI backend: using oneAPI (experimental)"""
    jl = get_julia()
    jl.seval("using oneAPI")
