import netCDF4 as nc


def save_netcdf(times, state, var_names, filename):
    # creating netcdf
    file_dst = nc.Dataset(filename + ".nc", "w")

    # create dimensions for destiny nc-file
    file_dst.createDimension("t", None)

    # create and write independent variables in destiny nc-file using single precision
    t_dst = file_dst.createVariable("t", "f4", ("t",))
    t_dst[:] = times[:]

    for iv, name in enumerate(var_names):
        var_dst = file_dst.createVariable( name, "f4", ("t",) )
        var_dst[:] = state[iv,:]

    file_dst.close()


def read_netcdf(state, filename):
    print("to be done")
