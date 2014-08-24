from ctypes import *
from list import GF_List


class GF_HEVCConfig(Structure):
	_fields_=[
		("configurationVersion", c_char),
		("profile_space", c_char),
		("profile_idc", c_char),
		("constraint_indicator_flags", c_char),
		("level_idc", c_char),
		("profile_compatibility_indications", c_int),
		("chromaFormat", c_char),
		("luma_bit_depth", c_char),
		("chroma_bit_depth", c_char),
		("avgFrameRate", c_uint16),
		("constantFrameRate", c_char),
		("numTemporalLayers", c_char),
		("nal_unit_size", c_char),
		("param_array", POINTER(GF_List))
	]