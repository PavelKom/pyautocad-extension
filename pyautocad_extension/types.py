#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .object import AcadObject, AcadEntity
from comtypes import POINTER



# Python-wrapped object recast dictionary
py_parse_dict = {
	# "": AcadObject,
	# "": AcadEntity,
	# "AcDbPoint": AcadPoint,
}


from .application import acad_dll
# VBA wrapped object recast dictionary
# POINTER(A) >>> POINTER(B)		A, B - INTERFACES, not classes
com_parse_dict = {
	"AcDbPoint": POINTER(acad_dll.IAcadPoint),
	
}