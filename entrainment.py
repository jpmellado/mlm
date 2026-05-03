# List of possible entrainment parametrizations
import numpy as np
from parameters import *
from environment import *
import globals as gs
from sys import exit


def sflux_b(t, state):
    return g * gs.sflux_s(t, state) / (cpd * T_00) + g * eps2 * gs.sflux_q(t, state)


def buoyancy(T, qv):  # linearized form
    b = g * (T - T_00) / T_00 + g * eps2 * (qv - q_00)
    return b


# A model for free convection conditions where the surface buoyancy flux is given
def E_free_convection(t, state):
    A = 0.2  # entrainment coefficient
    h = state[0]
    s = state[1]
    q = state[2]
    # g*z will cancel out in b_plus-b so I do not need to remove it from s
    b_plus = buoyancy(s_env(h) / cpd, q_env(h))
    b = buoyancy(s / cpd, q)
    E = A * sflux_b(t, state) / (b_plus - b)
    if E < 0:
        print("Negative entrainment rate; check conditions.")
        exit()
    return E


# To test this module
def test():
    print(E_free_convection([500.0, s_env(500.0 * 0.5), q_env(500.0 * 0.5)]))


if __name__ == "__main__":
    test()
