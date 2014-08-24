from ctypes import *


class GF_IPMP_Tool(Structure):
    _fields_=[
        ("tag", c_char),
        ("IPMP_ToolID", c_char),
        ("num_alternate", c_int),
        ("specificToolID", c_char),
        ("toolParamDesc", _tagIPMPXParamDesc),
        ("tool_url", c_char)
    ]