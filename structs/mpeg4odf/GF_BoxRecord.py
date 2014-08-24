from ctypes import *


class GF_BoxRecord(Structure):
    _fields_=[
        ("top", c_int16),
        ("left", c_int16),
        ("bottom", c_int16),
        ("right", c_int16)
    ]