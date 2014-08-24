from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_ParametricDescriptionItem(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("main_class", POINTER(GF_IPMPX_ByteArray)),
        ("subClass", POINTER(GF_IPMPX_ByteArray)),
        ("typeData", POINTER(GF_IPMPX_ByteArray)),
        ("type", POINTER(GF_IPMPX_ByteArray)),
        ("addedData", POINTER(GF_IPMPX_ByteArray))
    ]