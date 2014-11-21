cimport cython
import numpy as np
cimport numpy as np

from libcpp.string cimport string as std_string
from libcpp.vector cimport vector as std_vector

np.import_array()  # if array is used it has to be imported, otherwise possible runtime error

from libc.stdlib cimport malloc
ctypedef np.int8_t DTYPE_t

cdef extern from "lib/cfunc.h":

    void eudaq_data_vector(const std_string & filename, const std_string & type, std_vector[data_row] & data)

    struct data_row:
        np.uint32_t tluevent
        np.uint32_t plane
        np.uint32_t frame
        np.uint32_t id
        np.float64_t x
        np.float64_t y
        np.float64_t val

cdef dt = np.dtype([('tluevent', '<u4'), ('plane', '<u4'), ('frame', '<u4'), ('id', '<u4'), ('x', '<f8'), ('y', '<f8'), ('val', '<f8')]) 

def data_np(filename, type):

    cdef std_vector[data_row] vect

    eudaq_data_vector(<const std_string &> filename ,<const std_string &> type, <std_vector[data_row] &> vect)

    arr = data_to_numpy_array_with_spec(&vect[0], vect.size() * sizeof(data_row), np.NPY_INT8)

    return arr.copy().view(dt) # should be way to do it without copy

#cdef extern from "numpy/arrayobject.h":
#    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)

cdef data_to_numpy_array_with_spec(void * ptr, np.npy_intp N, int t):
    cdef np.ndarray[DTYPE_t, ndim=1] arr = np.PyArray_SimpleNewFromData(1, &N, t, ptr)
    #PyArray_ENABLEFLAGS(arr, np.NPY_OWNDATA)
    return arr
