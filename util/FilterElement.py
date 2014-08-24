__author__ = 'ian'
from xml.etree.ElementTree import Element
import re

count = 0

def enumInLibraryPath(root,element, library, header):
    headerRef = element.attrib['file']
    headerPath = root.find('File/.[@id="{0}"]'.format(headerRef)).attrib['name']
    packagePath = headerPath[headerPath.rfind("/")+1:-2]
    element.set('package', re.sub('_','',packagePath))

    if(element.attrib['name'][0:2] != "._"):
        element.set('class', re.sub('_','',element.attrib['name'].title()))
    else:
        element.set('class', re.sub('_','',packagePath.title()))

    if((headerPath.find(library) == -1) & (headerPath.find(header) == -1)):
        return bool(0)
    else:
        return bool(1)

def structInLibraryPath(root,element, library):
    headerRef = element.attrib['file']
    headerPath = root.find('File/.[@id="{0}"]'.format(headerRef)).attrib['name']
    packagePath = headerPath[headerPath.rfind("/")+1:-2]
    element.set('package', re.sub('_','',packagePath))

    if not ('name' in element.attrib):
        return bool(0)

    if(element.attrib['name'][0:2] == library):
        element.set('class', element.attrib['name'])
        return bool(1)
    else:
        return bool(0)

def filter(xmlRoot, elements, type, library, header=''):
    if(type == 'Enumeration'):
        elementsFiltered = [x for x in elements if(enumInLibraryPath(xmlRoot, x, library, header))]
    elif(type == 'Structs'):
        elementsFiltered = [x for x in elements if(structInLibraryPath(xmlRoot, x, library))]

    print('lengths elementsFiltered {0}, enums {1}'.format(len(elementsFiltered), len(elements)))
    return elementsFiltered

