from ctypes import *


class GF_DIMSDescription(Structure):
    _fields_=[
        ("profile", c_char),
        ("level", c_char),
        ("pathComponents", c_char),
        ("fullRequestHost", c_int),
        ("streamType", c_int),
        ("containsRedundant", c_char),
        ("textEncoding", c_char),
        ("contentEncoding", c_char),
        ("content_script_types", c_char)
    ]