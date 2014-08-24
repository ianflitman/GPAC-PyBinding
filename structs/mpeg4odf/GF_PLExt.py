from ctypes import *


class GF_PLExt(Structure):
	_fields_=[
		("tag", c_char),
		("profileLevelIndicationIndex", c_char),
		("ODProfileLevelIndication", c_char),
		("SceneProfileLevelIndication", c_char),
		("AudioProfileLevelIndication", c_char),
		("VisualProfileLevelIndication", c_char),
		("GraphicsProfileLevelIndication", c_char),
		("MPEGJProfileLevelIndication", c_char)
	]