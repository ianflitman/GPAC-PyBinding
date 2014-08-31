__author__ = 'ian'
from xml.etree.ElementTree import Element
import re

count = 0


def enumInLibraryPath(root,element, library, header):
    headerRef = element.attrib['file']
    headerPath = root.find('File/.[@id="{0}"]'.format(headerRef)).attrib['name']
    packagePath = headerPath[headerPath.rfind("/")+1:-2]
    element.set('package', re.sub('_','',packagePath))

    if element.attrib['name'][0:2] != "._":
        element.set('class', re.sub('_','',element.attrib['name'].title()))
    else:
        element.set('class', re.sub('_','',packagePath.title()))

    if (headerPath.find(library) == -1) & (headerPath.find(header) == -1):
        return bool(0)
    else:
        return bool(1)


def structInLibraryPath(root, element, library):
    headerRef = element.attrib['file']
    headerPath = root.find('File/.[@id="{0}"]'.format(headerRef)).attrib['name']
    packagePath = headerPath[headerPath.rfind("/")+1:-2]

    if headerPath.find(library) == -1:
        return bool(0)
    else:
        element.set('package', re.sub('_', '', packagePath))
        element.set('class', element.attrib['name'])
        return bool(1)

    # if not ('name' in element.attrib):
    #     return bool(0)
    #
    # if element.attrib['name'][0:2] == 'GF':
    #     element.set('class', element.attrib['name'])
    #     return bool(1)
    # elif element.attrib['name'][0:1] == '_':
    #     pass
    #
    # else:
    #     return bool(0)


def filter(xmlRoot, elements, type, library, header='', libraryPath='gpac'):
    if type == 'Enumeration':
        elementsFiltered = [x for x in elements if(enumInLibraryPath(xmlRoot, x, library, header))]
    elif type == 'Structs':
        elementsFiltered = [x for x in elements if(structInLibraryPath(xmlRoot, x, library))]

    print('lengths elementsFiltered {0}, enums {1}'.format(len(elementsFiltered), len(elements)))
    return elementsFiltered

