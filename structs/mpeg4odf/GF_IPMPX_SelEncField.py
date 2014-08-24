from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_SelEncField(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("field_Id", c_char),
		("field_Scope", c_char),
		("buf", c_char),
		("mappingTableSize", c_uint16),
		("mappingTable", c_uint16),
		("shuffleSpecificInfo", POINTER(GF_IPMPX_ByteArray))
	]