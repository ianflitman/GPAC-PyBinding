from ctypes import *


class GF_IPMPX_GetToolContext(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("scope", c_char),
		("IPMP_DescriptorIDEx", c_uint16)
	]