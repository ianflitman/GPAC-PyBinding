from ctypes import *


class GF_MuxInfo(Structure):
	_fields_=[
		("tag", c_char),
		("file_name", c_char),
		("GroupID", c_int),
		("streamFormat", c_char),
		("startTime", int),
		("duration", c_int),
		("textNode", c_char),
		("fontNode", c_char),
		("frame_rate", c_double),
		("import_flags", c_int),
		("delete_file", c_int),
		("carousel_period_plus_one", c_int),
		("aggregate_on_esid", c_uint16)
	]