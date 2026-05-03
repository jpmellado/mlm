# List of possible surface parametrizations
import numpy as np
from parameters import *


# Constant fluxes
def Fs_constant(t, state):
    return F_s0


def Fq_constant(t, state):
    return F_q0


# A simple model for a diurnal cycle
def Fs_diurnal(t, state):
    return max(0.0, F_s0 * np.sin(t * 2.0 * np.pi / Tdiurnal))


def Fq_diurnal(t, state):
    return max(0.0, F_q0 * np.sin(t * 2.0 * np.pi / Tdiurnal))


# To test this module
def test():
    print("to be done")


if __name__ == "__main__":
    test()
