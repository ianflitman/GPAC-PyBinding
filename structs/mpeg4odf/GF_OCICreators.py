from ctypes import *
from list import GF_List


class GF_OCICreators(Structure):
	_fields_=[
		("tag", c_char),
		("OCICreators", POINTER(GF_List))
	]