from enum import Enum
from ctypes import c_int


class SyncLayer(Enum):
    SLPredef_Null = c_int(1)
    SLPredef_MP4 = c_int(2)
    SLPredef_SkipSL = c_int(240)
