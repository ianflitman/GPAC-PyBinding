from ctypes import *


class GF_CIDesc(Structure):
	_fields_=[
		("tag", c_char),
		("compatibility", c_char),
		("protectedContent", c_char),
		("contentTypeFlag", c_char),
		("contentIdentifierFlag", c_char),
		("contentType", c_char),
		("contentIdentifierType", c_char),
		("contentIdentifier", c_char)
	]