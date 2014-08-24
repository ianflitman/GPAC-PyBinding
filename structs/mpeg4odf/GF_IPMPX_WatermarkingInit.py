from ctypes import *


class GF_IPMPX_WatermarkingInit(Structure):
    _fields_=[
        ("tag", c_char),
        ("Version", c_char),
        ("dataID", c_char),
        ("inputFormat", c_char),
        ("requiredOp", c_char),
        ("nChannels", c_char),
        ("bitPerSample", c_char),
        ("frequency", c_int),
        ("frame_horizontal_size", c_uint16),
        ("frame_vertical_size", c_uint16),
        ("chroma_format", c_char),
        ("wmPayloadLen", c_int),
        ("wmPayload", c_char),
        ("wmRecipientId", c_uint16),
        ("opaqueDataSize", c_int),
        ("opaqueData", c_char)
    ]