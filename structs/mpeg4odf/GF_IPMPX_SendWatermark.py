from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_SendWatermark(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("wm_status", c_char),
		("compression_status", c_char),
		("payload", POINTER(GF_IPMPX_ByteArray)),
		("opaqueData", POINTER(GF_IPMPX_ByteArray))
	]