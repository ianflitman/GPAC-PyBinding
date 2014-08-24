from ctypes import *


class GF_IPIPtr(Structure):
    _fields_=[
        ("tag", c_char),
        ("IPI_ES_Id", c_uint16)
    ]