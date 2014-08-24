from ctypes import *


class GF_SLHeader(Structure):
	_fields_=[
		("accessUnitStartFlag", c_char),
		("accessUnitEndFlag", c_char),
		("paddingFlag", c_char),
		("randomAccessPointFlag", c_char),
		("OCRflag", c_char),
		("idleFlag", c_char),
		("decodingTimeStampFlag", c_char),
		("compositionTimeStampFlag", c_char),
		("instantBitrateFlag", c_char),
		("degradationPriorityFlag", c_char),
		("paddingBits", c_char),
		("packetSequenceNumber", c_uint16),
		("objectClockReference", c_uint64),
		("AU_sequenceNumber", c_uint16),
		("decodingTimeStamp", c_uint64),
		("compositionTimeStamp", c_uint64),
		("accessUnitLength", c_uint16),
		("instantBitrate", c_int),
		("degradationPriority", c_uint16),
		("au_duration", c_int),
		("isma_encrypted", c_char),
		("isma_BSO", c_uint64),
		("m2ts_version_number_plus_one", c_char),
		("m2ts_pcr", c_char)
	]