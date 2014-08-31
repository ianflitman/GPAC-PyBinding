from ctypes import *


class __sha1_context(Structure):
    _fields_=[
        ("startCharOffset", c_uint16),
        ("endCharOffset", c_uint16),
        ("fontID", c_uint16),
        ("style_flags", c_char),
        ("font_size", c_char),
        ("text_color", c_int)
    ]