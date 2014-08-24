from ctypes import *


class GF_IPMPX_ByteArray(Structure):
	_fields_=[
		("length", c_int),
		("data", c_char)
	]