from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_SelEncBuffer(Structure):
	_fields_=[
		("tag", c_char),
		("Version", c_char),
		("dataID", c_char),
		("cipher_Id", c_char),
		("syncBoundary", c_char),
		("mode", c_char),
		("blockSize", c_uint16),
		("keySize", c_uint16),
		("Stream_Cipher_Specific_Init_Info", POINTER(GF_IPMPX_ByteArray))
	]