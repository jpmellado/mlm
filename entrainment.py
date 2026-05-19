# List of available entrainment parametrizations
import numpy as np
from parameters import *
from environment import *
from globals import buoyancy, flux_b
import globals as gs
from sys import exit


# A model for free convection conditions where the surface buoyancy flux is given
def E_free_convection(t, state):
    A = 0.2  # entrainment coefficient
    h = state[gs.idx_h]  # define pointers for readability below
    s = state[gs.idx_s]
    q = state[gs.idx_q]
    # g*z will cancel out in b_plus-b so I do not need to remove it from s
    b_plus = buoyancy(s_env(h) / cpd, q_env(h))
    b = buoyancy(s / cpd, q)

    # free convection; source of turbulence is surface buoyancy flux
    F_tur = flux_b(gs.sflux_s(t, state), gs.sflux_q(t, state))

    E = A * F_tur / (b_plus - b)
    if E < 0:
        print("Negative entrainment rate; check conditions.")
        exit()
    return E


# To test this module
def test():
    print(E_free_convection([500.0, s_env(500.0 * 0.5), q_env(500.0 * 0.5)]))


if __name__ == "__main__":
    test()
