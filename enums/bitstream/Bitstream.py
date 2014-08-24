from enum import Enum
from ctypes import c_int

class Bitstream(Enum):
	GF_BITSTREAM_READ = c_int(0)
	GF_BITSTREAM_WRITE = c_int(1)
