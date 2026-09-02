import numpy as np
from scipy.integrate import solve_ivp, RK23
from equations import *
import globals as gs
from iodata import *
from postprocessing import *

#####################################
# define the problem

# define total time interval to integrate, in seconds
# time is measured as elapsed time since sunrise (see surface energy flux)
tinitial = 0.0
tfinal = 3600.0 * 24.0 * 3.0  # 3 days

# define time interval to obtain data, in seconds
tinterval = 60.0 * 10.0  # every 10 minutes

# define system of equations as dictionary of dictionaries
system = {}
system["h"] = {"ode": dh_dt, "name": "h", "name_long": "height (m)"}
system["s"] = {"ode": ds_dt, "name": "s", "name_long": "liquid-water static energy (J/kg)"}
system["q"] = {"ode": dq_dt, "name": "q", "name_long": "total-water specific humidity (kg/kg)"}
num_vars = len(system)

# define the surface parametrization you want to use
gs.sflux_s = Fs_diurnal
gs.sflux_q = Fq_diurnal

# define the entrainment parametrization you want to use
gs.E = E_free_convection

#####################################
# define initial condition
h_initial = 300.0  # m, boundary-layer height
system["h"]["ics"] = h_initial  # m, boundary-layer height

# as an example, we simply define the initial bulk values as the mean of the environment over h
system["s"]["ics"] = s_env(h_initial * 0.5)  # J /kg, liquid-water static energy
system["q"]["ics"] = q_env(h_initial * 0.5)  # total-water specific humidity


##################################### No need to change beyond this point
# create array with the checkpointing times (times at which I get data)
times = np.arange(tinitial, tfinal, tinterval)
times = np.append(times, tfinal)  # include the final time


# construct initial condition
state = []
for item in system.values():
    state.append(item["ics"])
state = np.array(state)


# construct tendency accordingly to the choice of variables
def tendency(t, state):
    tendency = []
    for item in system.values():
        tendency.append(item["ode"](t, state))
    return np.array(tendency)


# construct indexes for clarity in equations
for idx, item in enumerate(system.values()):
    if item["name"] == "h":
        gs.idx_h = idx
    if item["name"] == "s":
        gs.idx_s = idx
    if item["name"] == "q":
        gs.idx_q = idx

# do simulation
sol = solve_ivp(tendency, [times[0], times[-1]], state, RK23, t_eval=times)
print(sol.message)

# save data
var_names = []
for item in system.values():
    var_names.append(item["name"])

save_netcdf(sol.t, sol.y, var_names, "mlm")

#####################################
# postprocessing

# plot result
var_names = []
for item in system.values():
    var_names.append(item["name_long"])

PlotEvolution(sol.t, sol.y, var_names, "evolution")

# PlotProfiles(sol.t[-1:], sol.y[:,-1:], var_names, "profiles") # just the last
time_indices = [int(np.size(times) / 2), -1]  # one in the middle, and the last
PlotProfiles(
    sol.t[time_indices],
    sol.y[:, time_indices],
    var_names,
    "profiles",
)
