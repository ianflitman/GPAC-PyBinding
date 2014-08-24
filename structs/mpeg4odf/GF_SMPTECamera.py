from ctypes import *
from list import GF_List


class GF_SMPTECamera(Structure):
	_fields_=[
		("tag", c_char),
		("cameraID", c_char),
		("ParamList", POINTER(GF_List))
	]