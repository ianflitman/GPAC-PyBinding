from ctypes import *


class GF_QoS_Default(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int)
    ]