from ctypes import *


class GF_KeyWordItem(Structure):
	_fields_=[
		("keyWord", c_char)
	]