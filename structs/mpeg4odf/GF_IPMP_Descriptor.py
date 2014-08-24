from ctypes import *
from list import GF_List


class GF_IPMP_Descriptor(Structure):
	_fields_=[
		("tag", c_char),
		("IPMP_DescriptorID", c_char),
		("IPMPS_Type", c_uint16),
		("opaque_data", c_char),
		("opaque_data_size", c_int),
		("IPMP_DescriptorIDEx", c_uint16),
		("IPMP_ToolID", c_char),
		("control_point", c_char),
		("cp_sequence_code", c_char),
		("ipmpx_data", POINTER(GF_List))
	]