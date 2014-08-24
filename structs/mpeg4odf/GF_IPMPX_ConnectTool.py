from ctypes import *
from mpeg4odf import GF_IPMP_Descriptor


class GF_IPMPX_ConnectTool(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("toolDescriptor", POINTER(GF_IPMP_Descriptor))
	]