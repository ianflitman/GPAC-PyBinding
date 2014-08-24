from ctypes import *


class GF_SmpteParam(Structure):
    _fields_=[
        ("paramID", c_char),
        ("param", c_int)
    ]