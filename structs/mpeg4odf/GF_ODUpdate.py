from ctypes import *
from list import GF_List


class GF_ODUpdate(Structure):
    _fields_=[
        ("tag", c_char),
        ("objectDescriptors", POINTER(GF_List))
    ]