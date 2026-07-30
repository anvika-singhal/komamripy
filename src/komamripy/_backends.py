"""GPU backend selection for komamripy.

Maps Python functions to Julia backend loading:
- load_cuda() → using CUDA
- load_metal() → using Metal
- load_amdgpu() → using AMDGPU
- load_oneapi() → using oneAPI

Once a backend is loaded, KomaMRI.jl automatically uses it with gpu=true by default.

If a backend package is not installed, it will be automatically added to the
Julia environment before loading.
"""

from ._session import get_julia

_BACKENDS = {
    "CUDA": "052768ef-5323-5732-b1bb-66c8b64840ba",
    "Metal": "dde4c033-4e86-420c-a63e-0dd931031962",
    "AMDGPU": "21141c5a-9bdb-4563-92ae-f87d6854732e",
    "oneAPI": "8f75cd03-7ff8-4ecb-9b8f-daf728133b1b",
}


def _load_backend(name: str) -> None:
    """Load a GPU backend, installing it first if necessary."""
    jl = get_julia()
    jl.seval("using Pkg: Pkg")

    # Check if backend is installed
    if jl.seval(f'Base.find_package("{name}") === nothing'):
        # Not installed, add it
        jl.Pkg.add(name=name, uuid=_BACKENDS[name])

    # Load backend
    jl.seval(f"using {name}")


def load_cuda() -> None:
    """Load CUDA backend: using CUDA"""
    _load_backend("CUDA")


def load_metal() -> None:
    """Load Metal backend: using Metal"""
    _load_backend("Metal")


def load_amdgpu() -> None:
    """Load AMDGPU backend: using AMDGPU"""
    _load_backend("AMDGPU")


def load_oneapi() -> None:
    """Load oneAPI backend: using oneAPI (experimental)"""
    _load_backend("oneAPI")
    