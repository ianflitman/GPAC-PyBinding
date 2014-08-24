__author__ = 'ian'
import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element
import os
import sys
from util import FilterElement
from os import listdir

enums = []
codeRoot = '/enums'
filesPreGenerated = set([])
packagePath=''
package = ''
dirs = set([])
packageDict = {}
root = Element('root')

def parseHeader(filename):
    codeXML = etree.parse(filename)
    root = codeXML.getroot()
    global enums
    enums = root.findall('Enumeration')
    enums = FilterElement.filter(xmlRoot = root, elements = enums, type = 'Enumeration', library='gpac', header='isomedia')
    createEnumClasses()

def createEnumClasses():
    this_module_dir_path = os.path.abspath ( os.path.dirname( sys.modules[__name__].__file__) )
    srcPath = this_module_dir_path + codeRoot

    global enums
    for enum in enums:
        if(enum.attrib['class'] + '.py' in filesPreGenerated):
            continue

        print(enum.attrib)
        print(enum.attrib['class'])
        packagePath = srcPath + '/' + enum.attrib['package']

        if not(os.path.exists(packagePath)):
            os.makedirs(packagePath)
            init = open(packagePath + '/__init__.py','w')
            init.write("__author__ = 'ian flitman'")
            init.close()

        file = packagePath + '/' + enum.attrib['class'] + '.py'
        if((os.path.exists(file))):
            src = open(file, 'a')
        else:
            src = open(file, 'w')
            src.write('from enum import Enum\nfrom ctypes import c_int\n\n\nclass ' + enum.attrib['class'] + '(Enum):\n')

        enumValues = enum.findall('EnumValue')
        for x in enumValues:
            name = x.attrib['name']
            init = x.attrib['init']
            print(name, init)
            src.write((' '*4) + name + ' = c_int(' + init + ')\n')

        src.close()

    for x in listdir(srcPath):
        if x!='__init__.py':
            filesPreGenerated.update(set(listdir(srcPath + '/' + x)))

this_module_dir_path = os.path.abspath(os.path.dirname(sys.modules[__name__].__file__))
parseHeader(this_module_dir_path + '/xml/isomedia.xml')
parseHeader(this_module_dir_path + '/xml/isomedia_dev.xml')
print(filesPreGenerated)




