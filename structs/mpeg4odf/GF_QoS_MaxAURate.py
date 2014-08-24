from ctypes import *


class GF_QoS_MaxAURate(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int),
        ("MaxAURate", c_int)
    ]