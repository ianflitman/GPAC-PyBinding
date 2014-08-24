from ctypes import *


class GF_Language(Structure):
	_fields_=[
		("tag", c_char),
		("langCode", c_int)
	]