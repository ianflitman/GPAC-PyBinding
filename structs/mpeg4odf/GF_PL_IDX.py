from ctypes import *


class GF_PL_IDX(Structure):
    _fields_=[
        ("tag", c_char),
        ("profileLevelIndicationIndex", c_char)
    ]