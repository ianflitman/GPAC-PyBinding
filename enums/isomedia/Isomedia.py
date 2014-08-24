from enum import Enum
from ctypes import c_int

class Isomedia(Enum):
	GF_ISOM_EDIT_EMPTY = c_int(0)
	GF_ISOM_EDIT_DWELL = c_int(1)
	GF_ISOM_EDIT_NORMAL = c_int(2)
	GF_ISOM_ITUNE_PROBE = c_int(0)
	GF_ISOM_ITUNE_ALBUM = c_int(-1453233054)
	GF_ISOM_ITUNE_ARTIST = c_int(-1455336876)
	GF_ISOM_ITUNE_COMMENT = c_int(-1453101708)
	GF_ISOM_ITUNE_COMPILATION = c_int(1668311404)
	GF_ISOM_ITUNE_COMPOSER = c_int(-1453101203)
	GF_ISOM_ITUNE_COVER_ART = c_int(1668249202)
	GF_ISOM_ITUNE_CREATED = c_int(-1453039239)
	GF_ISOM_ITUNE_DISK = c_int(1684632427)
	GF_ISOM_ITUNE_TOOL = c_int(-1451987089)
	GF_ISOM_ITUNE_GENRE = c_int(1735291493)
	GF_ISOM_ITUNE_GROUP = c_int(-1452838288)
	GF_ISOM_ITUNE_ITUNES_DATA = c_int(757935405)
	GF_ISOM_ITUNE_NAME = c_int(-1452383891)
	GF_ISOM_ITUNE_TEMPO = c_int(1953329263)
	GF_ISOM_ITUNE_TRACK = c_int(-1451986325)
	GF_ISOM_ITUNE_TRACKNUMBER = c_int(1953655662)
	GF_ISOM_ITUNE_WRITER = c_int(-1451789708)
	GF_ISOM_ITUNE_ENCODER = c_int(-1452970397)
	GF_ISOM_ITUNE_ALBUM_ARTIST = c_int(1631670868)
	GF_ISOM_ITUNE_GAPLESS = c_int(1885823344)
	GF_ISOM_ISMACRYP_SCHEME = c_int(1765885251)
	GF_ISOM_SEARCH_FORWARD = c_int(1)
	GF_ISOM_SEARCH_BACKWARD = c_int(2)
	GF_ISOM_SEARCH_SYNC_FORWARD = c_int(3)
	GF_ISOM_SEARCH_SYNC_BACKWARD = c_int(4)
	GF_ISOM_SEARCH_SYNC_SHADOW = c_int(5)
	GF_ISOM_TRAF_EMPTY = c_int(0)
	GF_ISOM_TRAF_RANDOM_ACCESS = c_int(1)
	GF_ISOM_TRAF_DATA_CACHE = c_int(2)
	GF_ISOM_OPEN_READ_DUMP = c_int(0)
	GF_ISOM_OPEN_READ = c_int(1)
	GF_ISOM_OPEN_WRITE = c_int(2)
	GF_ISOM_OPEN_EDIT = c_int(3)
	GF_ISOM_WRITE_EDIT = c_int(4)
	GF_ISOM_OPEN_CAT_FRAGMENTS = c_int(5)
	GF_ISOM_STORE_FLAT = c_int(1)
	GF_ISOM_STORE_STREAMABLE = c_int(2)
	GF_ISOM_STORE_INTERLEAVED = c_int(3)
	GF_ISOM_STORE_DRIFT_INTERLEAVED = c_int(4)
	GF_ISOM_STORE_TIGHT = c_int(5)
	GF_ISOM_REF_OD = c_int(1836085092)
	GF_ISOM_REF_DECODE = c_int(1685089892)
	GF_ISOM_REF_OCR = c_int(1937337955)
	GF_ISOM_REF_IPI = c_int(1768974706)
	GF_ISOM_REF_META = c_int(1667527523)
	GF_ISOM_REF_HINT = c_int(1751740020)
	GF_ISOM_REF_CHAP = c_int(1667785072)
	GF_ISOM_MEDIA_VISUAL = c_int(1986618469)
	GF_ISOM_MEDIA_AUDIO = c_int(1936684398)
	GF_ISOM_MEDIA_HINT = c_int(1751740020)
	GF_ISOM_MEDIA_META = c_int(1835365473)
	GF_ISOM_MEDIA_TEXT = c_int(1952807028)
	GF_ISOM_MEDIA_SUBT = c_int(1935832172)
	GF_ISOM_MEDIA_SUBPIC = c_int(1937072752)
	GF_ISOM_MEDIA_OD = c_int(1868854125)
	GF_ISOM_MEDIA_OCR = c_int(1668445037)
	GF_ISOM_MEDIA_SCENE = c_int(1935962989)
	GF_ISOM_MEDIA_MPEG7 = c_int(1832350573)
	GF_ISOM_MEDIA_OCI = c_int(1868788589)
	GF_ISOM_MEDIA_IPMP = c_int(1768977261)
	GF_ISOM_MEDIA_MPEGJ = c_int(1835692909)
	GF_ISOM_MEDIA_ESM = c_int(1734701933)
	GF_ISOM_MEDIA_DIMS = c_int(1684630899)
	GF_ISOM_MEDIA_FLASH = c_int(1718383464)
	GF_ISOM_SUBTYPE_MPEG4 = c_int(1297106247)
	GF_ISOM_SUBTYPE_MPEG4_CRYP = c_int(1162756941)
	GF_ISOM_SUBTYPE_AVC_H264 = c_int(1635148593)
	GF_ISOM_SUBTYPE_AVC2_H264 = c_int(1635148594)
	GF_ISOM_SUBTYPE_SVC_H264 = c_int(1937138481)
	GF_ISOM_SUBTYPE_3GP_H263 = c_int(1932670515)
	GF_ISOM_SUBTYPE_3GP_AMR = c_int(1935764850)
	GF_ISOM_SUBTYPE_3GP_AMR_WB = c_int(1935767394)
	GF_ISOM_SUBTYPE_3GP_EVRC = c_int(1936029283)
	GF_ISOM_SUBTYPE_3GP_QCELP = c_int(1936810864)
	GF_ISOM_SUBTYPE_3GP_SMV = c_int(1936944502)
	GF_ISOM_SUBTYPE_3GP_DIMS = c_int(1684630899)
	GF_ISOM_SUBTYPE_AC3 = c_int(1633889587)
	GF_ISOM_SUBTYPE_LSR1 = c_int(1819505201)
	GF_ISOM_BRAND_ISOM = c_int(1769172845)
	GF_ISOM_BRAND_ISO2 = c_int(1769172786)
	GF_ISOM_BRAND_MP41 = c_int(1836069937)
	GF_ISOM_BRAND_MP42 = c_int(1836069938)
	GF_ISOM_BRAND_MJP2 = c_int(1835692082)
	GF_ISOM_BRAND_MJ2S = c_int(1835676275)
	GF_ISOM_BRAND_3GP4 = c_int(862416948)
	GF_ISOM_BRAND_3GP5 = c_int(862416949)
	GF_ISOM_BRAND_3GP6 = c_int(862416950)
	GF_ISOM_BRAND_3GG6 = c_int(862414646)
	GF_ISOM_BRAND_3G2A = c_int(862401121)
	GF_ISOM_BRAND_AVC1 = c_int(1635148593)
	GF_ISOM_BRAND_MP21 = c_int(1836069425)
	GF_ISOM_PL_AUDIO = c_int(0)
	GF_ISOM_PL_VISUAL = c_int(1)
	GF_ISOM_PL_GRAPHICS = c_int(2)
	GF_ISOM_PL_SCENE = c_int(3)
	GF_ISOM_PL_OD = c_int(4)
	GF_ISOM_PL_MPEGJ = c_int(5)
	GF_ISOM_PL_INLINE = c_int(6)
	GF_ISOM_HINT_RTP = c_int(1920233504)
	GF_ISOM_ISMA_USE_SEL_ENC = c_int(1)
	GF_ISOM_ISMA_IS_ENCRYPTED = c_int(2)