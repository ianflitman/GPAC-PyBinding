__author__ = 'ian'
from ctypes import *

class GF_List(Structure):
    _fields_ = [
        ("slots", POINTER(c_void_p)),
        ("entryCount", c_int32),
        ("allocSize", c_int32)
    ]