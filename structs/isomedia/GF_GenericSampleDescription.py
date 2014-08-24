from ctypes import *


class GF_GenericSampleDescription(Structure):
    _fields_=[
        ("codec_tag", c_int),
        ("UUID", c_char),
        ("version", c_uint16),
        ("revision", c_uint16),
        ("vendor_code", c_int),
        ("temporal_quality", c_int),
        ("spacial_quality", c_int),
        ("width", c_uint16),
        ("height", c_uint16),
        ("h_res", c_int),
        ("v_res", c_int),
        ("depth", c_uint16),
        ("color_table_index", c_uint16),
        ("compressor_name", c_char),
        ("samplerate", c_int),
        ("nb_channels", c_uint16),
        ("bits_per_sample", c_uint16),
        ("extension_buf", c_char),
        ("extension_buf_size", c_int)
    ]