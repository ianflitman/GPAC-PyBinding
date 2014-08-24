from ctypes import *
from list import GF_List


class GF_GenericSubtitleConfig(Structure):
	_fields_=[
		("tag", c_char),
		("timescale", c_int),
		("layer", c_int16),
		("text_width", c_uint16),
		("text_height", c_uint16),
		("sample_descriptions", POINTER(GF_List)),
		("has_vid_info", c_int),
		("video_width", c_uint16),
		("video_height", c_uint16),
		("horiz_offset", c_int16),
		("vert_offset", c_int16)
	]