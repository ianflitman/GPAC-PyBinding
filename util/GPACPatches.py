__author__ = 'ian'

def getImportPatch(underscoredType):
    return{
        '_tag_array': 'from list import GF_List',
        '_tagIPMPXParamDesc' : 'from mpeg4odf import GF_TagIPMPXParamDesc',
        '_ipmpx_TrustSecurityMetadata': 'from mpeg4odf import GF_IPMPX_TrustSecurityMetadata',
    }.get(underscoredType, underscoredType)

def getCTypeValue(underscored):
    return {
        '_tag_array': {'name':' GF_List', 'process': 'handcode'},
        '_tagIPMPXParamDesc': 'GF_TagIPMPXParamDesc',
        '_ipmpx_TrustSecurityMetadata': 'GF_IPMPX_TrustSecurityMetadata'
    }.get(underscored, underscored)

#def process():