from enum import Enum
from ctypes import c_int

class GfIsomavctype(Enum):
	GF_ISOM_AVCTYPE_NONE = c_int(0)
	GF_ISOM_AVCTYPE_AVC_ONLY = c_int(1)
	GF_ISOM_AVCTYPE_AVC_SVC = c_int(2)
	GF_ISOM_AVCTYPE_SVC_ONLY = c_int(3)
