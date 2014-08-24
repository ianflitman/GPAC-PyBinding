from ctypes import *


class GF_OCICreator_item(Structure):
    _fields_=[
        ("langCode", c_int),
        ("isUTF8", c_char),
        ("OCICreatorName", c_char)
    ]