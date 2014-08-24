from ctypes import *


class GF_IPMPX_AddToolNotificationListener(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("scope", c_char),
        ("eventTypeCount", c_char),
        ("eventType", c_char)
    ]