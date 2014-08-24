from ctypes import *


class GF_IPMPX_AUTH_KeyDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("keyBody", c_char),
        ("keyBodyLength", c_int)
    ]