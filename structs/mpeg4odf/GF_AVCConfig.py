from ctypes import *
from list import GF_List


class GF_AVCConfig(Structure):
	_fields_=[
		("configurationVersion", c_char),
		("AVCProfileIndication", c_char),
		("profile_compatibility", c_char),
		("AVCLevelIndication", c_char),
		("nal_unit_size", c_char),
		("sequenceParameterSets", POINTER(GF_List)),
		("pictureParameterSets", POINTER(GF_List)),
		("complete_representation", c_char),
		("chroma_format", c_char),
		("luma_bit_depth", c_char),
		("chroma_bit_depth", c_char),
		("sequenceParameterSetExtensions", POINTER(GF_List))
	]