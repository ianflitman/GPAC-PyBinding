__author__ = 'ian'
from util import GPACPatches


def getCTypeValue(xmlName):
    print(xmlName)
    print(xmlName[0:1])
    if xmlName[0:1] == '_':
        return GPACPatches.getCTypeValue(xmlName)
    else:
        return{
            'short unsigned int': 'c_uint16',
            'short int': 'c_int16',
            'unsigned char': 'c_char',
            'char': 'c_char',
            'unsigned int': 'c_int',
            'void': 'c_void_p',
            'long unsigned int': 'c_uint64',
            'long long unsigned int': 'c_unit64',
            'signed char': 'c_byte',
            'double':'c_double'
        }.get(xmlName, xmlName)
