from ctypes import *


class GF_Rating(Structure):
    _fields_=[
        ("tag", c_char),
        ("ratingEntity", c_int),
        ("ratingCriteria", c_uint16),
        ("infoLength", c_int),
        ("ratingInfo", c_char)
    ]