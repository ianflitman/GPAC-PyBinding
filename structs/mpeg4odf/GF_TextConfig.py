from ctypes import *
from list import GF_List


class GF_TextConfig(Structure):
    _fields_=[
        ("tag", c_char),
        ("Base3GPPFormat", c_char),
        ("MPEGExtendedFormat", c_char),
        ("profileLevel", c_char),
        ("timescale", c_int),
        ("sampleDescriptionFlags", c_char),
        ("layer", c_int16),
        ("text_width", c_uint16),
        ("text_height", c_uint16),
        ("nb_compatible_formats", c_char),
        ("compatible_formats", c_char),
        ("sample_descriptions", POINTER(GF_List)),
        ("has_vid_info", c_int),
        ("video_width", c_uint16),
        ("video_height", c_uint16),
        ("horiz_offset", c_int16),
        ("vert_offset", c_int16)
    ]