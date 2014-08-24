from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_TrustSpecification(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("startDate", c_char),
        ("attackerProfile", c_char),
        ("trustedDuration", c_int),
        ("CCTrustMetadata", POINTER(GF_IPMPX_ByteArray))
    ]