from ctypes import *


class GF_QoS_PrefMaxDelay(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int),
        ("PrefMaxDelay", c_int)
    ]