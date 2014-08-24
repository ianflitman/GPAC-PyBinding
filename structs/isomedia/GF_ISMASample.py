from ctypes import *


class GF_ISMASample(Structure):
    _fields_=[
        ("IV", c_uint64),
        ("IV_length", c_char),
        ("key_indicator", c_char),
        ("KI_length", c_char),
        ("dataLength", c_int),
        ("data", c_char),
        ("flags", c_int)
    ]