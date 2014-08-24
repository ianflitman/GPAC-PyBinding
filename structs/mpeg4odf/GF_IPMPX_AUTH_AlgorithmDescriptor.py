from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_AUTH_AlgorithmDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("regAlgoID", c_uint16),
        ("specAlgoID", POINTER(GF_IPMPX_ByteArray)),
        ("OpaqueData", POINTER(GF_IPMPX_ByteArray))
    ]