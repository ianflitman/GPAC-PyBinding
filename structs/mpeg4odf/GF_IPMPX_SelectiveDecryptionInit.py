from ctypes import *
from list import GF_List


class GF_IPMPX_SelectiveDecryptionInit(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("mediaTypeExtension", c_char),
		("mediaTypeIndication", c_char),
		("profileLevelIndication", c_char),
		("compliance", c_char),
		("SelEncBuffer", POINTER(GF_List)),
		("SelEncFields", POINTER(GF_List)),
		("RLE_DataLength", c_uint16),
		("RLE_Data", c_uint16)
	]