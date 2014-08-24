from ctypes import *
from mpeg4odf import GF_BoxRecord
from mpeg4odf import GF_StyleRecord
from mpeg4odf import GF_FontRecord


class GF_TextSampleDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("displayFlags", c_int),
        ("horiz_justif", c_byte),
        ("vert_justif", c_byte),
        ("back_color", c_int),
        ("default_pos", GF_BoxRecord),
        ("default_style", GF_StyleRecord),
        ("font_count", c_int),
        ("fonts", POINTER(GF_FontRecord)),
        ("sample_index", c_char)
    ]