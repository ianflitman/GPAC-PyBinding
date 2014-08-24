from ctypes import *


class GF_GenericSubtitleSampleDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("sample_index", c_char)
    ]