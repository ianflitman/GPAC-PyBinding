GPAC-PyBinding
==============
This Python project creates enumerations and structs for ctypes compliant Python3.4 classes for GPAC based on 
the gccxml generation of the gpac headers I am personally interested in, i.e. the MP4Box functionality, 

It thus parses the isomedia.h and isomediadev.h files. This code could be used as a basis for further conversion of GPAC 
file headers into ctype structs and enumerations.

The code currently has its rough edges, as some types still need hand-crafting.
