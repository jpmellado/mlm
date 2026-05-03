# Physical parameters of the model

# Atmospheric thermodynamics (from Iribarne and Godson, 2. edition, 1981)
Rd = 287.05  # J /kg /K
Rv = 461.51  # J /kg /K
cpd = 1005.0  # J /kg /K
cpv = 1850.0  # J /kg /K
cl = 4218.0  # J /kg /K
lv0 = 2501.0e3  # J /kg, enthalpy of vaporization at 0 C

eps1 = Rd / Rv
eps2 = Rv / Rd - 1.0

g = 9.81  # m /s^2, Earth's gravitational acceleration

T_00 = 288.15  # K, mean sea level temperature
p_00 = 101325.0  # Pa, mean sea level pressure
rho_00 = p_00 / (Rd * T_00)

# Environment. Some values from Mellado et al. (2017), https://doi.org/10.1002/qj.3095
divergence = -1.0e-6  # m /s, large-scale divergence
s_00 = cpd * T_00  # reference liquid-water static energy
gamma_T = 3.0e-3  # K /m, static temperature gradient
gamma_s = cpd * gamma_T  # J /kg /m
q_00 = 10.0e-3  # kg /kg, reference total-water specific humidity
gamma_q = -1.0e-6  # kg /kg /m, gradient of total-water specific humidity

# Forcing. Some values from Mellado et al. (2017), https://doi.org/10.1002/qj.3095
F_s0 = 200.0 / rho_00  # (J /kg) m /s, surface energy kinematic flux
F_q0 = 0.2e-4  # (kg /kg) m /s, surface moisture kinematic flux
Tdiurnal = 3600.0 * 24.0  # s, diurnal period
