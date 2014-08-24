from ctypes import *
from list import GF_List


class GF_ObjectDescriptor(Structure):
    _fields_=[
        ("tag", c_char),
        ("objectDescriptorID", c_uint16),
        ("URLString", c_char),
        ("ESDescriptors", POINTER(GF_List)),
        ("OCIDescriptors", POINTER(GF_List)),
        ("IPMP_Descriptors", POINTER(GF_List)),
        ("extensionDescriptors", POINTER(GF_List)),
        ("ServiceID", c_uint16),
        ("service_ifce", c_void_p)
    ]