from ctypes import *


class GF_IPMPX_DisconnectTool(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("IPMP_ToolContextID", c_int)
	]