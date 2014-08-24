from ctypes import *


class GF_ES_ID_Inc(Structure):
    _fields_=[
        ("tag", c_char),
        ("trackID", c_int)
    ]