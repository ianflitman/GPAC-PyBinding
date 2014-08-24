from ctypes import *
from list import GF_List
from mpeg4odf import GF_IPMP_ToolList


class GF_InitialObjectDescriptor(Structure):
	_fields_=[
		("tag", c_char),
		("objectDescriptorID", c_uint16),
		("URLString", c_char),
		("ESDescriptors", POINTER(GF_List)),
		("OCIDescriptors", POINTER(GF_List)),
		("IPMP_Descriptors", POINTER(GF_List)),
		("extensionDescriptors", POINTER(GF_List)),
		("ServiceID", c_uint16),
		("service_ifce", c_void_p),
		("inlineProfileFlag", c_char),
		("OD_profileAndLevel", c_char),
		("scene_profileAndLevel", c_char),
		("audio_profileAndLevel", c_char),
		("visual_profileAndLevel", c_char),
		("graphics_profileAndLevel", c_char),
		("IPMPToolList", POINTER(GF_IPMP_ToolList))
	]