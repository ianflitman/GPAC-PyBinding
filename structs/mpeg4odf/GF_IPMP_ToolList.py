from ctypes import *
from list import GF_List


class GF_IPMP_ToolList(Structure):
	_fields_=[
		("tag", c_char),
		("ipmp_tools", POINTER(GF_List))
	]