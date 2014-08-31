from ctypes import *
from mpeg4odf import GF_DefaultDescriptor
from mpeg4odf import GF_DefaultDescriptor
from list import GF_List


class GF_DecoderConfig(Structure):
    _fields_=[
        ("tag", c_char),
        ("objectTypeIndication", c_int),
        ("streamType", c_char),
        ("upstream", c_char),
        ("bufferSizeDB", c_int),
        ("maxBitrate", c_int),
        ("avgBitrate", c_int),
        ("decoderSpecificInfo", POINTER(GF_DefaultDescriptor)),
        ("predefined_rvc_config", c_uint16),
        ("rvc_config", POINTER(GF_DefaultDescriptor)),
        ("profileLevelIndicationIndexDescriptor", POINTER(GF_List)),
        ("udta", c_void_p)
    ]