from ctypes import *
from list import GF_List


class tagODCoDec(Structure):
    _fields_=[
        ("bs", __tag_bitstream),
        ("CommandList", POINTER(GF_List))
    ]