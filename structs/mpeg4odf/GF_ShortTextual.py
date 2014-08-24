from ctypes import *


class GF_ShortTextual(Structure):
	_fields_=[
		("tag", c_char),
		("langCode", c_int),
		("isUTF8", c_char),
		("eventName", c_char),
		("eventText", c_char)
	]