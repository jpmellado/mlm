import numpy as np
import matplotlib.pyplot as plt
from environment import *


def PlotEvolution(times, states, var_names, filename):
    num_vars = len(var_names)

    fig, axs = plt.subplots(1, num_vars, figsize=(num_vars * 3.5, 3))

    iv = 0
    axs[iv].plot(times[:] / 3600.0, states[iv, :] / 1000.0, label=var_names[iv])
    axs[iv].set_ylabel("height (km)")

    iv = 1
    axs[iv].plot(times[:] / 3600.0, states[iv, :] / 1000.0, label=var_names[iv])
    axs[iv].set_ylabel("liquid-water static energy (kJ/kg)")

    iv = 2
    axs[iv].plot(times[:] / 3600.0, states[iv, :] / 1000.0, label=var_names[iv])
    axs[iv].set_ylabel("total-water specific humidity (g/kg)")

    for iv in range(num_vars):
        axs[iv].set_xlabel("elapsed time (hours)")
        axs[iv].set_xlim([0, None])
        axs[iv].spines["right"].set_visible(False)
        axs[iv].spines["left"].set_position(("axes", -0.01))
        axs[iv].get_yaxis().tick_left()
        axs[iv].spines["top"].set_visible(False)
        axs[iv].spines["bottom"].set_position(("axes", -0.01))
        axs[iv].get_xaxis().tick_bottom()

    plt.tight_layout(pad=0.1)
    plt.savefig(filename + ".pdf", bbox_inches="tight")

    plt.show()

    return fig, axs


def PlotProfiles(times, states, var_names, filename):
    h = states[0, :]  # define pointers for readability below
    s = states[1, :]
    q = states[2, :]

    num_vars = len(var_names)

    fig, axs = plt.subplots(1, num_vars - 1, figsize=((num_vars - 1) * 3.5, 3))

    hmax = (
        np.max(h) * 1.5
    )  # the domain to plot is 50% larger than the maximum ABL height
    z = np.linspace(
        0.0, hmax, num=100
    )  # create grid of points in the vertical direction fro background

    for it, time in enumerate(times):
        z_bl = np.array(
            [0.0, states[0, it], states[0, it], hmax]
        )  # create grid of points for the profiles

        id = 0
        iv = id + 1
        axs[id].plot(s_env(z) / 1000.0, z / 1000.0, "--", color="black")
        profile = np.array([states[iv, it], states[iv, it], s_env(h[it]), s_env(hmax)])
        axs[id].plot(profile / 1000.0, z_bl / 1000.0, label='time {}'.format(times[it]))
        axs[id].set_xlabel("liquid-water static energy (kJ/kg)")

        id = 1
        iv = id + 1
        profile = np.array([states[iv, it], states[iv, it], q_env(h[it]), q_env(hmax)])
        axs[id].plot(profile / 1000.0, z_bl / 1000.0, label='time {} h'.format(times[it]/3600.))
        axs[id].plot(q_env(z) / 1000.0, z / 1000.0, "--", color="black")
        axs[id].set_xlabel("total-water specific humidity (g/kg)")
        axs[id].legend(loc='best')

    for id in range(num_vars - 1):
        axs[id].set_ylabel("height (km)")
        axs[id].set_ylim([0, None])
        axs[id].spines["right"].set_visible(False)
        axs[id].spines["left"].set_position(("axes", -0.01))
        axs[id].get_yaxis().tick_left()
        axs[id].spines["top"].set_visible(False)
        axs[id].spines["bottom"].set_position(("axes", -0.01))
        axs[id].get_xaxis().tick_bottom()

    plt.tight_layout(pad=0.1)
    plt.savefig(filename + ".pdf", bbox_inches="tight")

    plt.show()

    return fig, axs
