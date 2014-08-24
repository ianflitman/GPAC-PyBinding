from ctypes import *
from list import GF_List


class GF_IPMPX_GetToolsResponse(Structure):
	_fields_=[
		("ipmp_tools", POINTER(GF_List))
	]