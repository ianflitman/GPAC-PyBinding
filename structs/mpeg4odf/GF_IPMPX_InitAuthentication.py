from ctypes import *


class GF_IPMPX_InitAuthentication(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("Context", c_int),
        ("AuthType", c_char)
    ]