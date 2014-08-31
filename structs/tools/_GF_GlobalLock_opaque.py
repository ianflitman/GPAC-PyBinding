from ctypes import *


class _GF_GlobalLock_opaque(Structure):
    _fields_=[
        ("tag", c_char),
        ("classificationEntity", c_int),
        ("classificationTable", c_uint16),
        ("dataLength", c_int),
        ("contentClassificationData", c_char)
    ]