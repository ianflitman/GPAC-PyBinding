from ctypes import *
from list import GF_List


class _ipmpx_TrustSecurityMetadata(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("TrustedTools", POINTER(GF_List))
    ]