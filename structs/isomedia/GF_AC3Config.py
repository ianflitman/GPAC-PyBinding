from ctypes import *


class GF_AC3Config(Structure):
    _fields_=[
        ("fscod", c_char),
        ("bsid", c_char),
        ("bsmod", c_char),
        ("acmod", c_char),
        ("lfon", c_char),
        ("brcode", c_char)
    ]