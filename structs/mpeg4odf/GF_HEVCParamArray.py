from ctypes import *
from list import GF_List


class GF_HEVCParamArray(Structure):
    _fields_=[
        ("type", c_char),
        ("array_completeness", c_char),
        ("nalus", POINTER(GF_List))
    ]