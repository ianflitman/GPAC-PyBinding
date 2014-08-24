from ctypes import *


class GF_FontRecord(Structure):
    _fields_=[
        ("fontID", c_uint16),
        ("fontName", c_char)
    ]