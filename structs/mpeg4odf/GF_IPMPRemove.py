from ctypes import *


class GF_IPMPRemove(Structure):
    _fields_=[
        ("tag", c_char),
        ("NbIPMPDs", c_int),
        ("IPMPDescID", c_char)
    ]