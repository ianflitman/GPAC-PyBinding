from ctypes import *


class GF_QoS_MaxGapLoss(Structure):
    _fields_=[
        ("tag", c_char),
        ("size", c_int),
        ("MaxGapLoss", c_int)
    ]