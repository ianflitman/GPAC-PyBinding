from ctypes import *
from list import GF_List


class __tag_bifs_config(Structure):
    _fields_=[
        ("tag", c_char),
        ("version", c_int),
        ("nodeIDbits", c_uint16),
        ("routeIDbits", c_uint16),
        ("protoIDbits", c_uint16),
        ("pixelMetrics", c_int),
        ("pixelWidth", c_uint16),
        ("pixelHeight", c_uint16),
        ("randomAccess", c_int),
        ("elementaryMasks", POINTER(GF_List)),
        ("useNames", c_int)
    ]