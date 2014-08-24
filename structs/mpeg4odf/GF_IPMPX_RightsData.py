from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_RightsData(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("rightsInfo", POINTER(GF_IPMPX_ByteArray))
    ]