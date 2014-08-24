from ctypes import *


class GF_ES_ID_Ref(Structure):
    _fields_=[
        ("tag", c_char),
        ("trackRef", c_uint16)
    ]