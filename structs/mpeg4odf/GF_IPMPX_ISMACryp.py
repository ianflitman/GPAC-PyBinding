from ctypes import *


class GF_IPMPX_ISMACryp(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("cryptoSuite", c_char),
		("IV_length", c_char),
		("use_selective_encryption", c_int),
		("key_indicator_length", c_char)
	]