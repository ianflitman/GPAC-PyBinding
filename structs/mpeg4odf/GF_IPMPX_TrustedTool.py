from ctypes import *
from list import GF_List


class GF_IPMPX_TrustedTool(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("toolID", c_char),
        ("AuditDate", c_char),
        ("trustSpecifications", POINTER(GF_List))
    ]