from ctypes import *


class GF_ODCom(Structure):
	_fields_=[
		("tag", c_char)
	]