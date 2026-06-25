# komamripy

**Pulseq-compatible, high-performance MRI simulation in Python.**

`komamripy` is a thin Python interface to
[KomaMRI.jl](https://github.com/JuliaHealth/KomaMRI.jl), a high-performance
Julia framework for MRI simulation. It exposes KomaMRI to Python through
[juliacall](https://juliapy.github.io/PythonCall.jl/stable/juliacall/), so
Python users can run fast CPU/GPU MRI simulations without writing any Julia.

## How it works

`komamripy` mirrors the KomaMRI Julia namespace: any function or type that
KomaMRI exposes is available as an attribute of `komamripy`. Julia code
therefore translates to Python almost line for line.

| Julia | Python |
| --- | --- |
| `Scanner()` | `km.Scanner()` |
| `brain_phantom2D()` | `km.brain_phantom2D()` |
| `PulseDesigner.EPI_example()` | `km.PulseDesigner.EPI_example()` |
| `simulate(obj, seq, sys; sim_params)` | `km.simulate(obj, seq, sys, sim_params=sim_params)` |

Simulation results are returned as Julia objects; convert array-like results to
NumPy with `numpy.asarray`.

## Installation

> `komamripy` is in early development and is not yet on PyPI. Install it from
> source.

You do **not** need to install Julia yourself: juliacall provisions a suitable
Julia automatically, and KomaMRI is installed on first import.

Using [uv](https://docs.astral.sh/uv/):

```bash
uv pip install git+https://github.com/JuliaHealth/komamripy
```

Or with pip:

```bash
pip install git+https://github.com/JuliaHealth/komamripy
```

The first import downloads Julia and precompiles KomaMRI, which can take a few
minutes. Subsequent runs are fast.

## Quick start

```python
import komamripy as km
import numpy as np

sys = km.Scanner()                       # scanner hardware
obj = km.brain_phantom2D()               # 2D brain phantom
seq = km.PulseDesigner.EPI_example()     # example EPI sequence

sim_params = km.KomaMRICore.default_sim_params()
sim_params["return_type"] = "mat"        # return the raw signal matrix

signal = np.asarray(km.simulate(obj, seq, sys, sim_params=sim_params))
print(signal.shape)
```

A runnable version lives in [`examples/`](examples/).

## Pulseq compatibility

KomaMRI reads [Pulseq](https://pulseq.github.io/) `.seq` files, so komamripy can
simulate sequences produced by any Pulseq tool, including
[pypulseq](https://github.com/imr-framework/pypulseq):

```python
seq = km.read_seq("sequence.seq")
raw = km.simulate(obj, seq, sys)
```

## Status

`komamripy` is under active development as a Google Summer of Code project.
Currently supported: the core simulation pipeline and reading Pulseq files.
Planned: PyPI releases, GPU backend selection, tighter pypulseq integration,
and differentiable workflows.

## License

[MIT](LICENSE)

## Acknowledgements

Powered by [KomaMRI.jl](https://github.com/JuliaHealth/KomaMRI.jl) and developed
within the [JuliaHealth](https://github.com/JuliaHealth) community.