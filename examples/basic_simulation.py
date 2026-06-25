"""Minimal end-to-end example: simulate an EPI acquisition and read the signal.

Run from the repository root after installing the package (see the README)::

    python examples/basic_simulation.py
"""
import numpy as np

import komamripy as km


def main():
    # Build the simulation inputs. These mirror KomaMRI's Julia API directly.
    sys = km.Scanner()
    obj = km.brain_phantom2D()
    seq = km.PulseDesigner.EPI_example()

    # Request the plain signal matrix so the result converts cleanly to NumPy.
    sim_params = km.KomaMRICore.default_sim_params()
    sim_params["return_type"] = "mat"

    # The first call compiles Julia code and may take a little while.
    signal = np.asarray(km.simulate(obj, seq, sys, sim_params=sim_params))

    print("signal shape:", signal.shape)
    print("signal dtype:", signal.dtype)
    print("first sample magnitudes:", np.abs(signal[:5]).ravel())


if __name__ == "__main__":
    main()