from ctypes import *


class __tag_oci_event(Structure):
    _fields_=[
        ("paramID", c_char),
        ("param", c_int)
    ]