from ctypes import *
from list import GF_List


class GF_IPMPUpdate(Structure):
    _fields_=[
        ("tag", c_char),
        ("IPMPDescList", POINTER(GF_List))
    ]