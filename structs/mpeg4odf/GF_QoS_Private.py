from ctypes import *


class GF_QoS_Private(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int),
        ("DataLength", c_int),
        ("Data", c_char)
    ]