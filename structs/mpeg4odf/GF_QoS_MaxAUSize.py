from ctypes import *


class GF_QoS_MaxAUSize(Structure):
	_fields_=[
		("tag", c_char),
		("size", c_int),
		("MaxAUSize", c_int)
	]