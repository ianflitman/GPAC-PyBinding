from ctypes import *


class GF_IPMPX_Data(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char)
	]