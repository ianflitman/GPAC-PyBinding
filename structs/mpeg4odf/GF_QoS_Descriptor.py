from ctypes import *
from list import GF_List


class GF_QoS_Descriptor(Structure):
	_fields_=[
		("tag", c_char),
		("predefined", c_char),
		("QoS_Qualifiers", POINTER(GF_List))
	]