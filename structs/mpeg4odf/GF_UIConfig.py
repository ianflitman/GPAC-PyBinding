from ctypes import *


class GF_UIConfig(Structure):
	_fields_=[
		("tag", c_char),
		("deviceName", c_char),
		("termChar", c_char),
		("delChar", c_char),
		("ui_data", c_char),
		("ui_data_length", c_int)
	]