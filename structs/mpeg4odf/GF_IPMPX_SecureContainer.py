from ctypes import *
from mpeg4odf import GF_IPMPX_ByteArray
from mpeg4odf import GF_IPMPX_Data
from mpeg4odf import GF_IPMPX_ByteArray


class GF_IPMPX_SecureContainer(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("isMACEncrypted", c_int),
        ("encryptedData", POINTER(GF_IPMPX_ByteArray)),
        ("protectedMsg", POINTER(GF_IPMPX_Data)),
        ("MAC", POINTER(GF_IPMPX_ByteArray))
    ]