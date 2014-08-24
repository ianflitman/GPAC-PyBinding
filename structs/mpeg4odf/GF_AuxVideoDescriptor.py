from ctypes import *


class GF_AuxVideoDescriptor(Structure):
	_fields_=[
		("tag", c_char),
		("aux_video_type", c_int),
		("position_offset_h", c_int),
		("position_offset_v", c_int),
		("knear", c_int),
		("kfar", c_int),
		("parallax_zero", c_int),
		("parallax_scale", c_int),
		("dref", c_int),
		("wref", c_int)
	]