from ctypes import *
from list import GF_List


class GF_IsomObjectDescriptor(Structure):
	_fields_=[
		("tag", c_char),
		("objectDescriptorID", c_uint16),
		("URLString", c_char),
		("ES_ID_RefDescriptors", POINTER(GF_List)),
		("OCIDescriptors", POINTER(GF_List)),
		("IPMP_Descriptors", POINTER(GF_List)),
		("extensionDescriptors", POINTER(GF_List)),
		("ES_ID_IncDescriptors", POINTER(GF_List))
	]