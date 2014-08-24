from ctypes import *


class GF_IPMPX_CanProcess(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("canProcess", c_int)
    ]