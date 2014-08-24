from ctypes import *


class GF_IPMPX_NotifyToolEvent(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("OD_ID", c_uint16),
		("ESD_ID", c_uint16),
		("eventType", c_char),
		("IPMP_ToolContextID", c_int)
	]