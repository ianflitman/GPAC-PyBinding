__author__ = 'ian'

exceptions = set([])


def getImportPatch(underscored):

    exceptions.update(set([underscored]))
    return{
        '_tag_array': 'from list import GF_List',
        '_tagIPMPXParamDesc': 'from mpeg4odf import GF_TagIPMPXParamDesc',
        '_ipmpx_TrustSecurityMetadata': 'from mpeg4odf import GF_IPMPX_TrustSecurityMetadata',
    }.get(underscored, underscored)


def getCTypeValue(underscored):
    return {
        '_tag_array': 'POINTER(GF_List)',
        '_tagIPMPXParamDesc': 'POINTER(GF_TagIPMPXParamDesc)',
        '_ipmpx_TrustSecurityMetadata': 'POINTER(GF_IPMPX_TrustSecurityMetadata)'
    }.get(underscored, underscored)

def getClassTreatment(underscored):
    return{
        '_tag_array': {'alias':'GF_List', 'action': 'patched'},
        '_tagIPMPXParamDesc': {'alias':'GF_TagIPMPXParamDesc', 'action': 'create'},
        '_ipmpx_TrustSecurityMetadata': {'alias': 'GF_IPMPX_TrustSecurityMetadata', 'action':'create'}
    }.get(underscored, {'alias': 'UnknownType', 'action': 'unknown'})

def processExceptions(root):
    for x in exceptions:
        root.find()
    return