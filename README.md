# komamripy

Pulseq-compatible, high-performance MRI simulation in Python.

`komamripy` is powered by the Julia package [KomaMRI.jl](https://github.com/JuliaHealth/KomaMRI.jl), which is designed for fast CPU/GPU MRI simulation.

## Why komamripy?

```python
import komamripy as koma

sys = koma.Scanner()
obj = koma.brain_2dphantom()
seq = koma.PulseDesigner.EPI_example() # This doesnt do anything

raw = koma.simulate(obj, seq, sys)
```
