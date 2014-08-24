from ctypes import *


class GF_DefaultDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("dataLength", c_int),
        ("data", c_char)
    ]