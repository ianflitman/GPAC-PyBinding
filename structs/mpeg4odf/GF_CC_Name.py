from ctypes import *
from list import GF_List


class GF_CC_Name(Structure):
    _fields_=[
        ("tag", c_char),
        ("ContentCreators", POINTER(GF_List))
    ]