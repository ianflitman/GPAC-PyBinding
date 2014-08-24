from ctypes import *


class GF_AVCConfigSlot(Structure):
    _fields_=[
        ("size", c_uint16),
        ("data", c_char),
        ("id", int)
    ]