# Space for global objects
import numpy as np
from parameters import *


# buoyancy variables; linearized forms in terms of T and q
def flux_b(flux_s, flux_q):
    return g * flux_s / (cpd * T_00) + g * eps2 * flux_q


def buoyancy(T, qv):
    b = g * (T - T_00) / T_00 + g * eps2 * (qv - q_00)
    return b
