from ctypes import *


class GF_QoS_AvgAUSize(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int),
        ("AvgAUSize", c_int)
    ]