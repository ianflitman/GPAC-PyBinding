from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_ToolAPI_Config(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("Instantiation_API_ID", c_int),
		("Messaging_API_ID", c_int),
		("opaqueData", POINTER(GF_IPMPX_ByteArray))
	]