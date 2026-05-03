import numpy as np
from scipy.integrate import solve_ivp, RK23
from equations import *
from iodata import *
from postprocessing import *

# define total time interval to integrate, in seconds
tfinal = 3600.0 * 24.0 * 3.0  # 3 days

# define time interval to obtain data, in seconds
tinterval = 60.0 * 10.0  # every 10 minutes

# create array with the times at which I get data
times = np.arange(0.0, tfinal, tinterval)
times = np.append(times, tfinal)  # include the final time

# define variable names
var_names = []
var_names.append("h")
var_names.append("s")
var_names.append("q")
num_vars = len(var_names)

# define initial condition
state = np.zeros((3))
state[0] = 300.0  # m, boundary-layer height
state[1] = s_env(state[0] * 0.5)  # J /kg, liquid-water static energy
state[2] = q_env(state[0] * 0.5)  # total-water specific humidity

# do simulation
sol = solve_ivp(tendency, [times[0], times[-1]], state, RK23, t_eval=times)
print(sol.message)

# save data
save_netcdf(sol.t, sol.y, var_names, "mlm")

# plot result
PlotEvolution(sol.t, sol.y, var_names, "evolution")
# PlotProfiles(sol.t[-1:], sol.y[:,-1:], var_names, "profiles") # just the last
PlotProfiles(
    sol.t[[int(np.size(times) / 2), -1]],
    sol.y[:, [int(np.size(times) / 2), -1]],
    var_names,
    "profiles",
)  # one in the middle, and the last
