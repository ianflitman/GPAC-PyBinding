__author__ = 'ian'
import xml.etree.ElementTree as etree
from util import FilterElement
from util import CTypeMapper
from util import GPACPatches
from xml.etree.ElementTree import Element
import logging
import os
import sys
from os import listdir

fieldTypeName = ''
codeRoot = '/structs'
structs = []
filesPreGenerated = set([])
root = Element('root')


def parseHeader(filename):
    logging.basicConfig(filename='log/example.log', level=logging.DEBUG)
    codeXML = etree.parse(filename)
    global root
    root = codeXML.getroot()
    global structs
    structs = root.findall('Struct')
    structs = FilterElement.filter(xmlRoot=root, elements=structs, type='Structs', library='gpac', header='isomedia')
    for struct in structs:
        if struct.attrib['class'] + '.py' in filesPreGenerated:
            continue

        types = []
        print("structs/{0}/{1} with name:{2}".format(struct.attrib['package'], struct.attrib['class'],
                                                     struct.attrib['name']))
        print(struct.attrib)
        if 'members' in struct.attrib:
            members = str(struct.attrib['members']).strip().split(' ')

            for x in members:
                findStr = 'Field/.[@id="{0}"]'.format(x)
                field = root.find(findStr)
                if field is not None:
                    typeInfo = processField(field)
                    typeInfo['name'] = field.attrib['name']
                    if typeInfo['type'][0:2] == 'GF':
                        pointedTo = root.find('*[@name="{0}"]'.format(typeInfo['type']))
                        typeInfo['path'] = pointedTo.attrib['package'] + '/' + pointedTo.attrib['class']
                    types.append(typeInfo)
                    print(typeInfo)
        else:
            print(struct.attrib['id'])
            print(struct.attrib['package'])
            referredTo = root.find('Typedef/.[@type="{0}"]'.format(struct.attrib['id']))

            if referredTo is not None:
                typedefID = referredTo.attrib['id']
                typeName = referredTo.attrib['name']
                logging.info('underscored type found: {0} referring to type: {1} in package: {2}'.format(struct.attrib['name'], typeName, struct.attrib['package']))

            continue

                # print(typedefID, typeName)
                #
                # pointerTypeID = root.find('PointerType/.[@type="{0}"]'.format(typedefID)).attrib['id']
                # print(pointerTypeID)
                # findStr = 'Field/.[@id="{0}"]'.format(pointerTypeID)
                # membersElement= []
                # membersElement.append(root.find('Field/.[@type="{0}"]'.format(pointerTypeID)).attrib['id'])
                # count=0
                # #memberslist = membersElement.find('[@id]')
                # for f in membersElement:
                # count +=1
                #     print(x)
                # print(count)
                # members = [x.attrib['id'] for x in membersElement]
                #
                # for x in members:
                #     typeInfo = processField(x)
                #     typeInfo['name'] = field.attrib['name']
                #     print(typeInfo)
                #     print('')
                #str(referredTo.attrib['members']).strip().split(' ')
            # else:
            #     print('')

        writeStruct(struct, types)

    global this_module_dir_path
    this_module_dir_path = os.path.abspath(os.path.dirname(sys.modules[__name__].__file__))
    srcPath = this_module_dir_path + '/structs'
    global filesPreGenerated
    for x in listdir(srcPath):
        if x != '__init__.py':
            filesPreGenerated.update(set(listdir(srcPath + '/' + x)))
    print(filesPreGenerated)


def processField(field):
    isPointer = bool(0)
    while 'type' in field.attrib:
        typeRef = field.attrib['type']
        global root
        field = root.find('*[@id="{0}"]'.format(typeRef))
        if field.tag == 'PointerType':
            isPointer = bool(1)
        processField(field)

    return {'type': field.attrib['name'], 'pointer': isPointer}


def writeStruct(struct, types):
    global this_module_dir_path
    this_module_dir_path = os.path.abspath(os.path.dirname(sys.modules[__name__].__file__))
    srcPath = this_module_dir_path + '/structs'
    packagePath = srcPath + '/' + struct.attrib['package']

    if not (os.path.exists(srcPath + '/' + struct.attrib['package'])):
        os.makedirs(srcPath + '/' + struct.attrib['package'])
        init = open(packagePath + '/__init__.py', 'w')
        init.write("__author__ = 'ian flitman'")
        init.close()

    init = open(srcPath + '/' + struct.attrib['package'] + '/__init__.py', 'w')
    init.write("__author__ = 'ian flitman'")
    init.close()

    file = srcPath + '/' + struct.attrib['package'] + '/' + struct.attrib['class'] + '.py'
    if os.path.exists(file):
        src = open(file, 'a')
    else:
        src = open(file, 'w')
        src.writelines('from ctypes import *\n')
        GF_ListFound = bool(0)
        for member in types:
            if 'path' in member:
                src.write("from {0} import {1}\n".format(member['path'][0:member['path'].find('/')],
                                                         member['path'][member['path'].find('/') + 1:]))

            # if member['type'][0:1] == '_':
            #    src.write(GPACPatches.getImportPatch(member['type']))

            if (member['type'] == '_tag_array') & (not GF_ListFound):
                src.write("from list import GF_List\n")
                GF_ListFound = bool(1)

                # if struct.attrib['class'][0:1] == '_':
                #     underscoredHandle = GPACPatches.getClassTreatment(struct.attrib['class'])
                #     if underscoredHandle['action'] == 'patched':
                #         continue
                #     elif underscoredHandle['action'] == 'unknown':
                #         print('UNKNOWN type: {0}'.format(struct.attrib['class']))
                #         continue
                #     else:
                #         struct.attrib['class'] = underscoredHandle.alias;

        src.write("\n\nclass " + struct.attrib['class'] + "(Structure):\n")
        src.write('    _fields_=[\n')
        for member in types:
            if ('path' in member) & (member['pointer']):
                src.write('        ("' + member['name'] + '", ' + 'POINTER(' + member['type'] + ')),\n')
            elif ('path' in member) & (not (member['pointer'])):
                src.write('        ("' + member['name'] + '", ' + member['type'] + '),\n')
            else:
                src.write('        ("' + member['name'] + '", ' + CTypeMapper.getCTypeValue(member['type']) + '),\n')

        print(src.tell())
        # back up two characters to remove last comma and return character
        src.seek(src.tell() - 2, 0)
        src.write('\n    ]')

    src.close()


this_module_dir_path = os.path.abspath(os.path.dirname(sys.modules[__name__].__file__))
parseHeader(this_module_dir_path + '/xml/isomedia.xml')
