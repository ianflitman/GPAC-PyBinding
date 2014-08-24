from ctypes import *


class GF_BaseODCom(Structure):
	_fields_=[
		("tag", c_char),
		("dataSize", c_int),
		("data", c_char)
	]