from ctypes import *


class GF_IPMPX_Authentication(Structure):
	_fields_=[
		("tag", c_char)
	]