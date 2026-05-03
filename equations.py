import numpy as np
from environment import *
from surface import *
from entrainment import *
import globals as gs


# Define of ordinary differential equations
def dh_dt(t, state):
    h = state[0]
    dh = gs.E(t, state) + w_env(h)
    return dh


def ds_dt(t, state):
    h = state[0]
    s = state[1]
    ds = (gs.E(t, state) * (s_env(h) - s) + gs.sflux_s(t, state)) / h
    return ds


def dq_dt(t, state):
    h = state[0]
    q = state[2]
    dq = (gs.E(t, state) * (q_env(h) - q) + gs.sflux_q(t, state)) / h
    return dq


# To test this module
def test():
    print("to be done")


if __name__ == "__main__":
    test()
