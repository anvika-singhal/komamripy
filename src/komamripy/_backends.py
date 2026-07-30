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
    if jl.Base.find_package("CUDA") is None:
        jl.seval('import Pkg; Pkg.add("CUDA")')
    jl.seval("using CUDA")


def load_metal() -> None:
    """Load Metal backend: using Metal"""
    jl = get_julia()
    if jl.Base.find_package("Metal") is None:
        jl.seval('import Pkg; Pkg.add("Metal")')
    jl.seval("using Metal")


def load_amdgpu() -> None:
    """Load AMDGPU backend: using AMDGPU"""
    jl = get_julia()
    if jl.Base.find_package("AMDGPU") is None:
        jl.seval('import Pkg; Pkg.add("AMDGPU")')
    jl.seval("using AMDGPU")


def load_oneapi() -> None:
    """Load oneAPI backend: using oneAPI (experimental)"""
    jl = get_julia()
    if jl.Base.find_package("oneAPI") is None:
        jl.seval('import Pkg; Pkg.add("oneAPI")')
    jl.seval("using oneAPI")
