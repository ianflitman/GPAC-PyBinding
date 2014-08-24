from ctypes import *


class GF_CC_Date(Structure):
	_fields_=[
		("tag", c_char),
		("contentCreationDate", c_char)
	]