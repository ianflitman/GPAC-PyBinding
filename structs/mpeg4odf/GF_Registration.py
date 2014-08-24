from ctypes import *


class GF_Registration(Structure):
    _fields_=[
        ("tag", c_char),
        ("formatIdentifier", c_int),
        ("dataLength", c_int),
        ("additionalIdentificationInfo", c_char)
    ]