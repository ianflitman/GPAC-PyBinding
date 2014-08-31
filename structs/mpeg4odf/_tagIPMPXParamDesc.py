from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from list import GF_List


class _tagIPMPXParamDesc(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("descriptionComment", POINTER(GF_IPMPX_ByteArray)),
        ("majorVersion", c_char),
        ("minorVersion", c_char),
        ("descriptions", POINTER(GF_List))
    ]