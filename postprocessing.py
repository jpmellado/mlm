import numpy as np
import matplotlib.pyplot as plt
import globals as gs
from environment import *

plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

def PlotEvolution(times, states, var_names, filename):
    num_vars = len(var_names)

    fig, axs = plt.subplots(1, num_vars, figsize=(num_vars * 3.5, 3))

    for iv in range(num_vars):
        axs[iv].plot(times[:] / 3600.0, states[iv, :])
        axs[iv].set_ylabel(var_names[iv])

        axs[iv].set_xlabel("elapsed time (hours)")
        axs[iv].set_xlim([0, None])
        axs[iv].spines["left"].set_position(("axes", -0.01))
        axs[iv].spines["bottom"].set_position(("axes", -0.01))

    plt.tight_layout(pad=0.1)
    plt.savefig(filename + ".pdf", bbox_inches="tight")

    plt.show()

    return fig, axs


def PlotProfiles(times, states, var_names, filename):
    h = states[gs.idx_h, :]  # define pointers for readability below
    s = states[gs.idx_s, :]
    q = states[gs.idx_q, :]

    num_vars = len(var_names)

    fig, axs = plt.subplots(1, num_vars - 1, figsize=((num_vars - 1) * 3.5, 3))

    hmax = np.max(h) * 1.5  # the domain to plot is 50% larger than the maximum ABL height
    z = np.linspace(
        0.0, hmax, num=100
    )  # create grid of points in the vertical direction fro background

    for it, time in enumerate(times):
        z_bl = np.array(
            [0.0, states[0, it], states[0, it], hmax]
        )  # create grid of points for the profiles

        id = 0
        for iv in range(num_vars):
            if iv == gs.idx_h:
                continue
            if iv == gs.idx_q:
                axs[id].plot(q_env(z), z, "--", color="black")
                profile = np.array([states[iv, it], states[iv, it], q_env(h[it]), q_env(hmax)])
            if iv == gs.idx_s:
                axs[id].plot(s_env(z), z, "--", color="black")
                profile = np.array([states[iv, it], states[iv, it], s_env(h[it]), s_env(hmax)])
            axs[id].plot(profile, z_bl, label="time {} h".format(times[it] / 3600.0))
            axs[id].set_xlabel(var_names[iv])
            id = id + 1

        axs[-1].legend(loc="best")

    for id in range(num_vars - 1):
        axs[id].set_ylabel(var_names[gs.idx_h])
        axs[id].set_ylim([0, None])
        axs[id].spines["left"].set_position(("axes", -0.01))
        axs[id].spines["bottom"].set_position(("axes", -0.01))

    plt.tight_layout(pad=0.1)
    plt.savefig(filename + ".pdf", bbox_inches="tight")

    plt.show()

    return fig, axs
