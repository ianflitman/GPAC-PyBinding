from ctypes import *
from list import GF_List


class GF_ESDUpdate(Structure):
    _fields_=[
        ("tag", c_char),
        ("ODID", c_uint16),
        ("ESDescriptors", POINTER(GF_List))
    ]