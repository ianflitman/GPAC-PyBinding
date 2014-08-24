from ctypes import *


class GF_OCI_Data(Structure):
    _fields_=[
        ("tag", c_char),
        ("OCICreationDate", c_char)
    ]