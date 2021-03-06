from enum import Enum
from ctypes import c_int


class GfErr(Enum):
    GF_SCRIPT_INFO = c_int(3)
    GF_PACKED_FRAMES = c_int(2)
    GF_EOS = c_int(1)
    GF_OK = c_int(0)
    GF_BAD_PARAM = c_int(-1)
    GF_OUT_OF_MEM = c_int(-2)
    GF_IO_ERR = c_int(-3)
    GF_NOT_SUPPORTED = c_int(-4)
    GF_CORRUPTED_DATA = c_int(-5)
    GF_SG_UNKNOWN_NODE = c_int(-6)
    GF_SG_INVALID_PROTO = c_int(-7)
    GF_SCRIPT_ERROR = c_int(-8)
    GF_BUFFER_TOO_SMALL = c_int(-9)
    GF_NON_COMPLIANT_BITSTREAM = c_int(-10)
    GF_CODEC_NOT_FOUND = c_int(-11)
    GF_URL_ERROR = c_int(-12)
    GF_SERVICE_ERROR = c_int(-13)
    GF_REMOTE_SERVICE_ERROR = c_int(-14)
    GF_STREAM_NOT_FOUND = c_int(-15)
    GF_ISOM_INVALID_FILE = c_int(-20)
    GF_ISOM_INCOMPLETE_FILE = c_int(-21)
    GF_ISOM_INVALID_MEDIA = c_int(-22)
    GF_ISOM_INVALID_MODE = c_int(-23)
    GF_ISOM_UNKNOWN_DATA_REF = c_int(-24)
    GF_ODF_INVALID_DESCRIPTOR = c_int(-30)
    GF_ODF_FORBIDDEN_DESCRIPTOR = c_int(-31)
    GF_ODF_INVALID_COMMAND = c_int(-32)
    GF_BIFS_UNKNOWN_VERSION = c_int(-33)
    GF_IP_ADDRESS_NOT_FOUND = c_int(-40)
    GF_IP_CONNECTION_FAILURE = c_int(-41)
    GF_IP_NETWORK_FAILURE = c_int(-42)
    GF_IP_CONNECTION_CLOSED = c_int(-43)
    GF_IP_NETWORK_EMPTY = c_int(-44)
    GF_IP_SOCK_WOULD_BLOCK = c_int(-45)
    GF_IP_UDP_TIMEOUT = c_int(-46)
    GF_AUTHENTICATION_FAILURE = c_int(-50)
    GF_SCRIPT_NOT_READY = c_int(-51)
