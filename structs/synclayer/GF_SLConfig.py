from ctypes import *


class GF_SLConfig(Structure):
	_fields_=[
		("tag", c_char),
		("predefined", c_char),
		("useAccessUnitStartFlag", c_char),
		("useAccessUnitEndFlag", c_char),
		("useRandomAccessPointFlag", c_char),
		("hasRandomAccessUnitsOnlyFlag", c_char),
		("usePaddingFlag", c_char),
		("useTimestampsFlag", c_char),
		("useIdleFlag", c_char),
		("durationFlag", c_char),
		("timestampResolution", c_int),
		("OCRResolution", c_int),
		("timestampLength", c_char),
		("OCRLength", c_char),
		("AULength", c_char),
		("instantBitrateLength", c_char),
		("degradationPriorityLength", c_char),
		("AUSeqNumLength", c_char),
		("packetSeqNumLength", c_char),
		("timeScale", c_int),
		("AUDuration", c_uint16),
		("CUDuration", c_uint16),
		("startDTS", c_uint64),
		("startCTS", c_uint64)
	]