cimport cython
import numpy as np
cimport numpy as np

from libcpp.string cimport string as std_string
from libcpp.vector cimport vector as std_vector
from libcpp.map cimport map as std_map

np.import_array()  # if array is used it has to be imported, otherwise possible runtime error

from libc.stdlib cimport malloc
ctypedef np.int8_t DTYPE_t

cdef extern from "lib/cfunc.h":

    void eudaq_data_map(const std_string & filename, unsigned int begin, unsigned int end, std_map[std_string, std_vector[data_row]] & data)

    struct data_row:
        np.uint32_t eventnumber
        np.uint32_t tluevent
        np.uint16_t plane
        np.uint16_t frame
        np.uint16_t x
        np.uint16_t y
        np.uint16_t val

cdef eudaq_dt = np.dtype([('eventnumber', '<u4'), ('tluevent', '<u4'), ('plane', '<u2'), ('frame', '<u2'), ('x', '<u2'), ('y', '<u2'), ('val', '<u2')]) 

def data_np(filename,begin=0,end=4294967295):
    
    cdef std_map[std_string, std_vector[data_row]] data
    eudaq_data_map(<const std_string &> filename, <unsigned int> begin, <unsigned int> end, <std_map[std_string, std_vector[data_row]] &> data)

    ret = dict() 
    cdef std_map[std_string, std_vector[data_row]].iterator iter = data.begin()    
    while iter != data.end():
        arr = data_to_numpy_array_with_spec(&cython.operator.dereference(iter).second[0], cython.operator.dereference(iter).second.size() * sizeof(data_row), np.NPY_INT8)        
        ret[cython.operator.dereference(iter).first] = arr.copy().view(eudaq_dt)
        cython.operator.preincrement(iter)

    return ret


#cdef extern from "numpy/arrayobject.h":
#    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)

cdef data_to_numpy_array_with_spec(void * ptr, np.npy_intp N, int t):
    cdef np.ndarray[DTYPE_t, ndim=1] arr = np.PyArray_SimpleNewFromData(1, &N, t, ptr)
    #PyArray_ENABLEFLAGS(arr, np.NPY_OWNDATA)
    return arr
