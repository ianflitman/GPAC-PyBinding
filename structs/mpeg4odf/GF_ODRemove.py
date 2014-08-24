from ctypes import *


class GF_ODRemove(Structure):
    _fields_=[
        ("tag", c_char),
        ("NbODs", c_int),
        ("OD_ID", c_uint16)
    ]