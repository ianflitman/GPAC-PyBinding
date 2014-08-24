from ctypes import *


class GF_ContentCreatorInfo(Structure):
	_fields_=[
		("langCode", c_int),
		("isUTF8", c_char),
		("contentCreatorName", c_char)
	]