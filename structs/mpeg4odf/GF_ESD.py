from ctypes import *
from mpeg4odf import GF_DecoderConfig
from synclayer import GF_SLConfig
from mpeg4odf import GF_IPIPtr
from mpeg4odf import GF_QoS_Descriptor
from mpeg4odf import GF_Registration
from mpeg4odf import GF_Language
from list import GF_List


class GF_ESD(Structure):
    _fields_=[
        ("tag", c_char),
        ("ESID", c_uint16),
        ("OCRESID", c_uint16),
        ("dependsOnESID", c_uint16),
        ("streamPriority", c_char),
        ("URLString", c_char),
        ("decoderConfig", POINTER(GF_DecoderConfig)),
        ("slConfig", POINTER(GF_SLConfig)),
        ("ipiPtr", POINTER(GF_IPIPtr)),
        ("qos", POINTER(GF_QoS_Descriptor)),
        ("RegDescriptor", POINTER(GF_Registration)),
        ("langDesc", POINTER(GF_Language)),
        ("IPIDataSet", POINTER(GF_List)),
        ("IPMPDescriptorPointers", POINTER(GF_List)),
        ("extensionDescriptors", POINTER(GF_List)),
        ("has_ref_base", c_int)
    ]