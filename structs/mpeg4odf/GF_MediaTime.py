from ctypes import *


class GF_MediaTime(Structure):
    _fields_=[
        ("tag", c_char),
        ("mediaTimeStamp", c_double)
    ]