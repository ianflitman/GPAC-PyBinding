from ctypes import *
from list import GF_List


class GF_ExpandedTextual(Structure):
	_fields_=[
		("tag", c_char),
		("langCode", c_int),
		("isUTF8", c_char),
		("itemDescriptionList", POINTER(GF_List)),
		("itemTextList", POINTER(GF_List)),
		("NonItemText", c_char)
	]