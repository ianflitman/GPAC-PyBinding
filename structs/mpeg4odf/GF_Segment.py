from ctypes import *


class GF_Segment(Structure):
    _fields_=[
        ("tag", c_char),
        ("startTime", c_double),
        ("Duration", c_double),
        ("SegmentName", c_char)
    ]