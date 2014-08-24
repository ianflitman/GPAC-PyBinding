from ctypes import *
from list import GF_List
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_AUTH_KeyDescriptor
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_MutualAuthentication(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("failedNegotiation", c_int),
        ("candidateAlgorithms", POINTER(GF_List)),
        ("agreedAlgorithms", POINTER(GF_List)),
        ("AuthenticationData", POINTER(GF_IPMPX_ByteArray)),
        ("certType", c_int),
        ("certificates", POINTER(GF_List)),
        ("publicKey", POINTER(GF_IPMPX_AUTH_KeyDescriptor)),
        ("opaque", POINTER(GF_IPMPX_ByteArray)),
        ("trustData", _ipmpx_TrustSecurityMetadata),
        ("authCodes", POINTER(GF_IPMPX_ByteArray))
    ]