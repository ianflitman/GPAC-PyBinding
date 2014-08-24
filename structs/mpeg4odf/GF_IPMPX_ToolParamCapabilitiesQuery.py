from ctypes import *


class GF_IPMPX_ToolParamCapabilitiesQuery(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("description", _tagIPMPXParamDesc)
    ]