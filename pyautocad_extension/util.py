#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .types import com_parse_dict
from .block import AcadBlock
from .object import A3Vertex
import math


class COM_Property(object):
	"""
	Property-like decorator for easy get/set build-in-types (Integer, Double, etc.) or non-recasting classes (A3Vertex, ...) attributes from COM objects
	Don't use:
		@COM_Property
		def prop(self):
			...
	Use:
		prop = COM_Property(%COM Interface property name%, %type for getter%, %type(s) for setter%, %read_only%, %function for preprocess setted value, like abs or ceil% )
	Example:
	AcadCircle(POINTER(_dll.IAcadCircle), AcadEntity):
		...
		center = COM_Property("Center", A3Vertex)
		radius = COM_Property("Radius", A3Vertex, value_wrapper=non_neg)
		...
	"""
    def __init__(self, ffunc: str, type_get=float, type_set=None, read_only: bool=False, value_wrapper=None):
        #self.fget = fget
        #self.fset = fset
        self.__ffunc = ffunc
        self.__tget = type_get
		self.__wrapper = value_wrapper
		if not read_only:
			self.__tset = type_set or type_get
		else:
			self.__tset = None
        self.__read = read_only

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.__tget(super(klass, obj).__getattribute__(self.__ffunc))

    def __set__(self, obj, value):
        if self.__read:
            raise AttributeError("Attribute '{0}' read-only".format(self.__ffunc))
        if not isinstance(value, self.__tset):
            raise TypeError("Attribute '{0}' must be (on of types) {1}".format(self.__tset))
        klass = type(obj)
		if self.__wrapper is None:
			super(klass, obj).__setattr__(self.__ffunc, value)
		else:
			super(klass, obj).__setattr__(self.__ffunc, self.__wrapper(value))
	
	def __doc__(self):
		return "Property '{0}' from COM-object. Return type for property: {1}. Setter type for property: {2}. Read only: {3}".format(self.__ffunc, self.__tget, self.__tset, self.__read)


class COM_PropertyRecast(object):
	"""
	Property-like decorator for easy get/set RECASTED attributes from COM objects
	Don't use:
		@COM_Property
		def prop(self):
			...
	Use:
		prop = COM_Property(%COM Interface property name%, %type for getter%, %type(s) for setter%, %read_only%)
	Example:
	class AcadObject(POINTER(_dll.IAcadObject)):
		...
		application = COM_Property("Application", read_only=True)
		...
	"""
	def __init__(self, ffunc: str, type_get=None, type_set=None, read_only: bool=False):
        #self.fget = fget
        #self.fset = fset
        self.__ffunc = ffunc
        self.__tget = type_get
		if not read_only:
			self.__tset = type_set
		else:
			self.__tset = None
        self.__read = read_only

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return recast(super(klass, obj).__getattribute__(self.__ffunc), self.__tget)

    def __set__(self, obj, value):
        if self.__read:
            raise AttributeError("Attribute '{0}' read-only".format(self.__ffunc))
        if not isinstance(value, self.__tset):
            raise TypeError("Attribute '{0}' must be {1}".format(self.__tset))
        klass = type(obj)
        super(klass, obj).__setattr__(self.__ffunc, uncast(value, self.__tset))
	
	def __doc__(self):
		return "Property '{0}' from COM-object. Return dynamic-cast object (POINTER(IInterface) >> AcadOBJ(POINTER(IInterface))). Setter type for property: {1}. Read only: {2}".format(self.__ffunc, self.__tset, self.__read)
		

def dict_fix(kw: dict):
	# Remove all items with None value
	kk = []
	for k, v in kw.items():
		if v is None:
			kk.append(k)
	for k in kk:
		kw.pop(k)

def arr_cont(var):
	try:
		res = []
		for v in var:
			res.extend(_cont(v))
		return res
	except:
		return [var]


def arr_check(var, t):
	try:
		for item in var:
			if not isinstance(item, t):
				raise TypeError("Variable '{0}' from '{1}' must be '{2}'".format(item, var, t))
	except:
		if not isinstance(var, t):
			raise TypeError("Variable '{0}' must be '{1}'".format(var, t))


def recast(com_obj_ptr, prefer_type=None):
	if not isinstance(com_obj_ptr,	POINTER):
		raise TypeError("Can't recast {0}".format(com_obj_ptr))
	if prefer_type is not None:
		com_obj_ptr.__class__ = prefer_type
	if com_obj_ptr.ObjectName in com_parse_dict.keys():
		com_obj_ptr.__class__ = com_parse_dict[key]
	return com_obj_ptr

def uncast(py_obj, prefer_type=None):
	if prefer_type is not None:
		com_obj_ptr.__class__ = prefer_type
	if py_obj.ObjectName in com_parse_dict.keys():
		py_obj.__class__ = py_parse_dict[key]
	returnpy_obj

def get_obj_block_source(source=None, new_doc_if_need: bool=True):
	if source is None:
		source = AcadApplication()
	if isinstance(source, AcadApplication):
		if source.Documents.Count == 0 and not new_doc_if_need:
			raise ValueError("[get_obj_block_source] Can't create new AcadDocument")
		source = source.ActiveDocument if source.Documents.Count > 0 else source.Documents.Add()
	if isinstance(source, AcadDocument):
		source = source.ModelSpace
	if isinstance(source, AcadBlock):
		raise ValueError("[get_obj_block_source] 'source' argument must be AcadApplication, AcadDocument oe any type of AcadBlock (AcadBlock, AcadModelSpace, AcadPaperSpace)")
	return source

def bounding_box(*args:A3Vertex):
	if len(args) < 1:
		raise ValueError("[bounding_box] Can't calculate bounding box without vertexes")
	v_min = A3Vertex(args[0])
	v_max = A3Vertex(args[0])
	for i, vtx in enumerate(args):
		if i == 0:
			continue
		v_min.x = min(v_min.x, vtx.x)
		v_min.y = min(v_min.y, vtx.y)
		v_min.z = min(v_min.z, vtx.z)
		v_max.x = max(v_max.x, vtx.x)
		v_max.y = max(v_max.y, vtx.y)
		v_max.z = max(v_max.z, vtx.z)
	return v_min, v_max


def try_me(func, value):
	try:
		func(value)
		return True
	except:
		return False

# FUNCTION PREPROCESSORS
def non_neg(value: (int, float)):
	# Return absolute value. if 0 return 0.000001
	if value == 0: # Fix for 0
		if isinstance(value, float):
			return 0.000001
		return 1
	return abs(value)


def angle_radian_scope(value: float):
	return value % (2 * math.pi)


def angle_degree_scope(value: float):
	return value % 360.0


def str_cut256(value: str):
	if len(value) > 256: return value[:256]
	return value



