from ctypes import *
from list import GF_List


class __tag_oci_codec(Structure):
    _fields_=[
        ("tag", c_char),
        ("IPMPDescList", POINTER(GF_List))
    ]