from ctypes import *


class GF_IPMPPtr(Structure):
	_fields_=[
		("tag", c_char),
		("IPMP_DescriptorID", c_char),
		("IPMP_DescriptorIDEx", c_uint16),
		("IPMP_ES_ID", c_uint16)
	]