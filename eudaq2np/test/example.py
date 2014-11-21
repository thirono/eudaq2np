import numpy as np
from eudaq2np import data_np

if __name__ == "__main__":

    data = data_np("run000022.raw", "GENERIC")
    print data, data['x'].astype(int)

    H, xedges, yedges = np.histogram2d(data['y'].astype(int), data['x'].astype(int))
    print H
