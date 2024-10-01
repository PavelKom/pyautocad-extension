#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from .types import com_parse_dict
#from .block import AcadBlock
#from .object import A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
import math
import ctypes
import re
import array
import numpy as np

from pyautocad import APoint
from pyautocad.compat import IS_PY3

pattern1 = "_.*_"

from comtypes.automation import IDispatch

class _ez_ptr:
    @classmethod
    def ptr(cls):
        prnt = cls.__bases__[0]
        p = prnt()
        p.__class__ = cls
        return p
    @classmethod
    def is_my_base(cls, cls_cast):
        return cls_cast == cls.__bases__[0]
    @classmethod
    def try_cast(cls, obj):
        if cls.is_my_base(obj.__class__):
            obj.__class__ = cls
            return obj
        return None
    def uncast(self):
        obj = self
        obj.__class__ = self.__class__.__bases__[0]
        return obj
    @property
    def com_parent(self):
        return super(self.__class__.__bases__[0], self)
    
    def _my_methods(self):
        """Get COM Object methods and properties """
        res = []
        interface = self.__com_interface__
        dir1 = dir(IDispatch)
        for val in dir(interface):
            if re.match(pattern1, val):
                continue
            if val in dir1:
                continue
            res.append(val.lower())
        return res
    
    def __getattribute__(self, attribute):
        if attribute.startswith("__") and attribute.endswith("__"):
            return super().__getattribute__(attribute)
        # Get/Set/Call attribute, if it's registered in IDispatch.__dir__
        elif attribute in dir(IDispatch):
            return super().__getattribute__(attribute)
        # Add case insensitivies for VBA
        return super().__getattribute__(attribute.lower())
      

class CastManager:
    @classmethod
    def cast(cls, obj):
        from obj_parser import dict_cast2
        from comtypes.client import GetBestInterface
        obj = GetBestInterface(obj)
        if obj.__class__.__name__ in dict_cast2.keys():
            obj.__class__ = dict_cast2[obj.__class__.__name__]
        else:
            print(f"{obj} | {obj.__class__.__name__} Can't be casted from COM.Autocad")
        return obj
    @classmethod
    def recast(cls, obj):
        from obj_parser import dict_cast
        if obj.__class__.__name__ in dict_cast.keys():
            obj.__class__ = dict_cast[obj.__class__.__name__]
        else:
            print(f"{obj} | {obj.__class__.__name__} Can't be casted to COM.Autocad")
        return obj


class SetterProperty(object):
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        return self.func(obj, value)


class A3Vertex(APoint):
    def __new__(cls, x_or_seq=0, y=0.0, z=0.0): # Allow trimmed lists for X
        if isinstance(x_or_seq, (array.array, list, tuple)):
            arr = []
            for i in range(1,4):
                if i <= len(x_or_seq):
                    arr.append(x_or_seq[i-1])
                else:
                    arr.append(0)
            return super(A3Vertex, cls).__new__(cls, arr)
        return super(A3Vertex, cls).__new__(cls, (x_or_seq, y, z))
    X = APoint.x
    Y = APoint.y
    Z = APoint.z
    @property
    def as2D(self):
        return self[:2]
        
    def __str__(self):
        return 'A3Vertex(%.2f, %.2f, %.2f)' % tuple(self)
    
    def __abs__(self):
        return A3Vertex(abs(self.x), abs(self.y), abs(self.z))
    
class A2Vertex(array.array):
    # Same as A3Vertex but for 2D
    def __new__(cls, x_or_seq=0, y=0.0): # Allow trimmed lists for X
        if isinstance(x_or_seq, (array.array, list, tuple)):
            arr = []
            for i in range(1,3):
                if i <= len(x_or_seq):
                    arr.append(x_or_seq[i-1])
                else:
                    arr.append(0)
            return super(A2Vertex, cls).__new__(cls, 'd', arr)
        return super(A2Vertex, cls).__new__(cls, 'd', (x_or_seq, y))
        
    @property
    def x(self):
        """ x coordinate of 2D point"""
        return self[0]
    @x.setter
    def x(self, value):
        self[0] = value
    X = x

    @property
    def y(self):
        """ y coordinate of 2D point"""
        return self[1]
    @y.setter
    def y(self, value):
        self[1] = value
    Y = y
    
    def distance_to(self, other):
        """ Returns distance to `other` point

        :param other: :class:`A2Vertex` instance or any sequence of 3 coordinates
        """
        return distance_2d(self, other)
    
    #Copy from APoint
    def __add__(self, other):
        return self.__left_op(self, other, operator.add)

    def __sub__(self, other):
        return self.__left_op(self, other, operator.sub)

    def __mul__(self, other):
        return self.__left_op(self, other, operator.mul)

    if IS_PY3:
        def __div__(self, other):
            return self.__left_op(self, other, operator.truediv)
    else:
        def __div__(self, other):
            return self.__left_op(self, other, operator.div)

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rdiv__ = __div__
    __floordiv__ = __div__
    __rfloordiv__ = __div__
    __truediv__ = __div__
    _r_truediv__ = __div__

    def __neg__(self):
        return self.__left_op(self, -1, operator.mul)

    def __left_op(self, p1, p2, op):
        if isinstance(p2, (float, int)):
            return A2Vertex(op(p1[0], p2), op(p1[1], p2))
        return A2Vertex(op(p1[0], p2[0]), op(p1[1], p2[1]))

    def __iadd__(self, p2):
        return self.__iop(p2, operator.add)

    def __isub__(self, p2):
        return self.__iop(p2, operator.sub)

    def __imul__(self, p2):
        return self.__iop(p2, operator.mul)

    def __idiv__(self, p2):
        return self.__iop(p2, operator.div)

    def __iop(self, p2, op):
        if isinstance(p2, (float, int)):
            self[0] = op(self[0], p2)
            self[1] = op(self[1], p2)
        else:
            self[0] = op(self[0], p2[0])
            self[1] = op(self[1], p2[1])
        return self

    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return 'A2Vertex(%.2f, %.2f)' % tuple(self)

    def __eq__(self, other):
        if not isinstance(other, (array.array, list, tuple)):
            return False
        return tuple(self) == tuple(other)
    

class A3Vertexes:
    pass
class A2Vertexes:
    pass
class A3Vertexes(list):
    def __init__(self, arr=None):
        if arr is not None:
            self.add_points(arr)
            
    def add_point(self, p: (A3Vertex, A2Vertex, array.array, list, tuple)):
        self.append(A3Vertex(p))
    def add_points(self, pp: (A3Vertexes, A2Vertexes, A3Vertex, A2Vertex, array.array, list, tuple)):
        if isinstance(pp, (A3Vertexes, A2Vertexes)):
            for p in pp:
                self.append(A3Vertex(p))
        elif isinstance(pp, (A3Vertex, A2Vertex)):
            self.append(A3Vertex(pp))
        else:
            i = 0
            simple = True
            buf = []
            for v in pp:
                if isinstance(v, (A3Vertexes, A2Vertexes)):
                    simple = False
                    self.add_points(v)
                elif isinstance(v, (A3Vertex, A2Vertex)):
                    simple = False
                    self.add_point(v)
                elif isinstance(v, (array.array, list, tuple)):
                    simple = False
                    self.add_points(v)
                elif not isinstance(v, (float, int)):
                    simple = False
                    Exception("[A3Vertexes] Can't parse '%s' to A3Vertex" % (v))
                elif simple:
                    if i % 3 == 0:
                        buf.append(A3Vertex())
                    buf[-1][i] = v 
                    i = (i+1)%3
            if simple:
                self.extend(buf)

    def flatten(self):
        ret = []
        for p in self:
            ret.extend(tuple(p))
        return ret
        #return array.array('d', ret)
    
class A2Vertexes(list):
    def __init__(self, arr=None):
        if arr is not None:
            self.add_points(arr)
            
    def add_point(self, p: (A3Vertex, A2Vertex, array.array, list, tuple)):
        self.append(A2Vertex(p))
    def add_points(self, pp: (A3Vertexes, A2Vertexes, A3Vertex, A2Vertex, array.array, list, tuple)):
        if isinstance(pp, (A3Vertexes, A2Vertexes)):
            for p in pp:
                self.append(A3Vertex(p))
        elif isinstance(pp, (A3Vertex, A2Vertex)):
            self.append(A3Vertex(pp))
        else:
            i = 0
            simple = True
            buf = []
            for v in pp:
                if isinstance(v, (A3Vertexes, A2Vertexes)):
                    simple = False
                    self.add_points(v)
                elif isinstance(v, (A3Vertex, A2Vertex)):
                    simple = False
                    self.add_point(v)
                elif isinstance(v, (array.array, list, tuple)):
                    simple = False
                    self.add_points(v)
                elif not isinstance(v, (float, int)):
                    simple = False
                    Exception("[A2Vertexes] Can't parse '%s' to A2Vertex" % (v))
                elif simple:
                    if i % 2 == 0:
                        buf.append(A2Vertex())
                    buf[-1][i] = v 
                    i = (i+1)%2
            if simple:
                self.extend(buf)

    def flatten(self):
        ret = []
        for p in self:
            ret.extend(tuple(p))
        return ret
        #return array.array('d', ret)

class ATrMatrix(np.matrix):
    def __new__(subtype, data=None, copy=True):
        if data is not None:
            try:
                iter(data) # Check data to iterable
                ret = N.ndarray.__new__(subtype, data=data, dtype='float', copy=copy)
                ret = ret.reshape(4,4)
                if ret.size != 16:
                    raise TypeError("Transform matrix size must be 4x4")
                return ret
            except:
                if not isinstance(data, float):
                    raise TypeError("Transform matrix scalar definition must be float")
                data = np.ones((4, 4), dtype='float') * data
        else:
            data = np.zeros((4, 4), dtype='float')
            
        return N.ndarray.__new__(subtype, data=data, dtype='float', copy=copy)






def distance_2d(p1, p2):
    """ Returns distance between two 2D points `p1` and `p2`
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 +
                     (p1[1] - p2[1]) ** 2)


def list_to_ptr_arr(data, ptype=ctypes.c_ulong):
    #l = len(data)
    arr = (ptype * l)()
    #arr = ctypes.cast((ptype * l)(), ctypes.POINTER(ptype))
    #arr = VARIANT()
    #for i, val in enumerate(data):
    #    val.__class__ = ptype
    #    arr[i] = val
    return arr

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





'''

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
        application = COM_PropertyRecast("Application", AcadApplication, read_only=True)
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
        
'''
'''
def recast(com_obj_ptr, prefer_type=None):
    if not isinstance(com_obj_ptr, POINTER):
        raise TypeError("Can't recast {0}".format(com_obj_ptr))
    elif prefer_type is not None:
        com_obj_ptr.__class__ = prefer_type
    #elif com_obj_ptr.ObjectName in com_parse_dict.keys():
    #    com_obj_ptr.__class__ = com_parse_dict[com_obj_ptr.ObjectName]
    return com_obj_ptr

def uncast(py_obj, prefer_type=None):
    if prefer_type is not None:
        com_obj_ptr.__class__ = prefer_type
    #if py_obj.ObjectName in com_parse_dict.keys():
    #    py_obj.__class__ = py_parse_dict[key]
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
    if not isinstance(source, AcadBlock):
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

'''


'''
def vertexes_flatten(vtx: (A3Vertexes, A2Vertexes)):
    return vtx.flatten()
'''

if __name__ == "__main__":
    a = A3Vertexes([1,2,3,4,5,6,7,8,9])
    print(a)
    print(a.flatten())


        

