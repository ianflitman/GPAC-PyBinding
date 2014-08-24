from ctypes import *
from list import GF_List


class GF_KeyWord(Structure):
	_fields_=[
		("tag", c_char),
		("languageCode", c_int),
		("isUTF8", c_char),
		("keyWordsList", POINTER(GF_List))
	]