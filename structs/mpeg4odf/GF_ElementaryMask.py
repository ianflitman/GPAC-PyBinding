from ctypes import *


class GF_ElementaryMask(Structure):
    _fields_=[
        ("tag", c_char),
        ("node_id", c_int),
        ("node_name", c_char)
    ]