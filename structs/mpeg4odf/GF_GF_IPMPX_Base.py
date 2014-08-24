from ctypes import *


class GF_GF_IPMPX_Base(Structure):
    _fields_=[
        ("tag", c_char),
        ("version", c_char),
        ("dataID", c_int)
    ]