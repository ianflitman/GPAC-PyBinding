from ctypes import *


class __tag_laser_config(Structure):
    _fields_=[
        ("tag", c_char),
        ("profile", c_char),
        ("level", c_char),
        ("pointsCodec", c_char),
        ("pathComponents", c_char),
        ("fullRequestHost", c_char),
        ("time_resolution", c_uint16),
        ("colorComponentBits", c_char),
        ("resolution", c_byte),
        ("coord_bits", c_char),
        ("scale_bits_minus_coord_bits", c_char),
        ("newSceneIndicator", c_char),
        ("extensionIDBits", c_char),
        ("force_string_ids", c_int)
    ]