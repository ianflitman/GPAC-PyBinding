from ctypes import *


class GF_QoS_LossProb(Structure):
	_fields_=[
		("tag", c_char),
		("size", c_int),
		("LossProb", float)
	]