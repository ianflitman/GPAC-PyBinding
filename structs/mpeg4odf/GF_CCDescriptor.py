from ctypes import *


class GF_CCDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("classificationEntity", c_int),
        ("classificationTable", c_uint16),
        ("dataLength", c_int),
        ("contentClassificationData", c_char)
    ]