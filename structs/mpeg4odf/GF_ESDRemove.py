from ctypes import *


class GF_ESDRemove(Structure):
	_fields_=[
		("tag", c_char),
		("ODID", c_uint16),
		("NbESDs", c_int),
		("ES_ID", c_uint16)
	]