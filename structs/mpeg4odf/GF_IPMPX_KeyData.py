from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_KeyData(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("keyBody", POINTER(GF_IPMPX_ByteArray)),
		("flags", c_int),
		("startDTS", c_uint64),
		("startPacketID", c_int),
		("expireDTS", c_uint64),
		("expirePacketID", c_int),
		("OpaqueData", POINTER(GF_IPMPX_ByteArray))
	]