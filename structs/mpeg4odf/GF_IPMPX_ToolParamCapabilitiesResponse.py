from ctypes import *


class GF_IPMPX_ToolParamCapabilitiesResponse(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("capabilitiesSupported", c_int)
	]