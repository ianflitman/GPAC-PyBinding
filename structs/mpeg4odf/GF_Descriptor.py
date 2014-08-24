from ctypes import *


class GF_Descriptor(Structure):
    _fields_=[
        ("tag", c_char)
    ]