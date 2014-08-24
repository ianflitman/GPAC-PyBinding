from ctypes import *


class GF_ISOSample(Structure):
	_fields_=[
		("dataLength", c_int),
		("data", c_char),
		("DTS", c_uint64),
		("CTS_Offset", c_int),
		("IsRAP", c_char)
	]