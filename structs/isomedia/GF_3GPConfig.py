from ctypes import *


class GF_3GPConfig(Structure):
    _fields_=[
        ("type", c_int),
        ("vendor", c_int),
        ("decoder_version", c_char),
        ("frames_per_sample", c_char),
        ("H263_level", c_char),
        ("H263_profile", c_char),
        ("AMR_mode_set", c_uint16),
        ("AMR_mode_change_period", c_char)
    ]