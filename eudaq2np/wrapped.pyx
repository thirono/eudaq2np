cimport cython
import numpy as np
cimport numpy as cnp

from libcpp.string cimport string as std_string
from libcpp.vector cimport vector as std_vector

cimport numpy as cnp
cnp.import_array()  # if array is used it has to be imported, otherwise possible runtime error

cdef extern from "lib/cfunc.h":

    void eudaq_data_vector(const std_string & filename, const std_string & type, std_vector[data_row] & data)

    struct data_row:
        cnp.uint32_t tluevent
        cnp.uint32_t plane
        cnp.uint32_t frame
        cnp.uint32_t id
        cnp.float64_t x
        cnp.float64_t y
        cnp.float64_t val

def data_np(filename, type):

    cdef std_vector[data_row] vect

    eudaq_data_vector(<const std_string &> filename ,<const std_string &> type, <std_vector[data_row] &> vect)

    dt = np.dtype([('tluevent', '<u4'), ('plane', '<u4'), ('frame', '<u4'), ('id', '<u4'), ('x', '<f8'), ('y', '<f8'), ('val', '<f8')]) 

    out = np.empty([vect.size()], dtype=dt)
    
    # this is not smart and slow
    for i in range(vect.size()):
        out['x'][i] = vect[i].x
        out['y'][i] = vect[i].y
        out['val'][i] = vect[i].val

        out['tluevent'][i] = vect[i].tluevent
        out['plane'][i] = vect[i].plane
        out['frame'][i] = vect[i].frame
        out['id'][i] = vect[i].id

    return out
