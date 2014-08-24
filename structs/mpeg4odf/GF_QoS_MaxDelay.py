from ctypes import *


class GF_QoS_MaxDelay(Structure):
	_fields_=[
		("tag", c_char),
		("size", c_int),
		("MaxDelay", c_int)
	]