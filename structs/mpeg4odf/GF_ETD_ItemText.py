from ctypes import *


class GF_ETD_ItemText(Structure):
    _fields_=[
        ("text", c_char)
    ]