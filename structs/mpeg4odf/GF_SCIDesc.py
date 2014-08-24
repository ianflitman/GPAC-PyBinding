from ctypes import *


class GF_SCIDesc(Structure):
    _fields_=[
        ("tag", c_char),
        ("languageCode", c_int),
        ("supplContentIdentifierTitle", c_char),
        ("supplContentIdentifierValue", c_char)
    ]