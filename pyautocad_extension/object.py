#!/usr/bin/env python
# -*- coding: utf-8 -*-

from comtypes import POINTER
from comtypes.automation import IDispatch
from comtypes.client import GetEvents
from .api import acad_dll as _dll
from .utils import arr_check, recast as _recast
from ctypes import c_short
from pyautocad import APoint
import array
import numpy as np

pattern1 = "_.*_"

class A3Vertex(APoint):
	X = x
	Y = y
	Z = z
	
class A2Vertex(array.array):
	pass # ToDo: For 2d points, for LWPolylines

class A3Vertexes(array.array):
	pass # ToDo: For list<A3Vertex> uses
	
class A2Vertexes(array.array):
	pass # ToDo: For list<A2Vertex> uses

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
			

class _EventCaller:
	REGISTERED_EVENT_OBJ = {}
	_SINKS = []
	_EVENT_CONNECTIONS = {} # comtypes.client._events.py._AdviseConnection>
	# _AdviseConnection.disconnect() for disconnect event tracking for object
	def connect_to_sink(self, sink: AcadEventDumper=None):
		if sink is None:
			return # Ignore 
		else:
			if self._EVENT_CONNECTIONS.get(self) is not None:
				return # Already connected. Don't use more than one dumper
			self._EVENT_CONNECTIONS[self] = GetEvents(self, sink) # Use default event interface. ToDo: NEED TEST
	
	def is_valid(self):
		return False
	
	def _validate(self):
		if not self.is_valid(self):
			conn = self._EVENT_CONNECTIONS.get(self)
			if conn is not None:
				self._EVENT_CONNECTIONS.pop(self)
				sink = conn.reciever
				if sink not is None:
					is_need = False
				conn.disconnect()
				del conn
		

class AcadObject(POINTER(_dll.IAcadObject)):
	_BLOCKED_ATTRIBUTES = ()
	_EVENT_CONNECTIONS = {}
	def __new__(cls, *args, **kwargs):
		raise TypeError("You can't create {0}. It's prototype of other objects.".format(cls))

	def _my_methods(self):
		"""
		Get COM Object methods and properties 
		"""
		res = ["get_all_objs", "_my_methods", "_my_events"]
		interface = self.__com_interface__
		dir1 = dir(IDispatch)
		for val in dir(interface):
			if re.match(pattern1, val):
				continue
			if val in dir1:
				continue
			res.append(val)
		return res

	def _my_events(self):
		"""
		Get COM Object events
		"""
		res = []
        interface = self._outgoing_interfaces_
        dir1 = dir(IDispatch)
        for val in dir(interface):
            if re.match(pattern1, val) or val in dir1:
                continue
            res.append(val)
        return res

	def recast(self):
		return _recast(self)
	
	def add_event_connection(self, sink=None):
		# Add event connection to object
		conn = self._EVENT_CONNECTIONS.get(self)
		if conn is None and sink is not None:
			try:
				conn = GetEvents(self, self.sink)
			except: # ToDo: add exception
				pass
		return conn

	# MAGIC
	def __str__(self):
		try:
			hndl = self.Handle
		except:
			hndl = "None"
		try:
			obj_name = self.ObjectName
		except:
			obj_name = "None"
		return "Basic AutoCAD object\n\tHandle: {0}\n\tObject name: {1}".format(hndl, obj_name)

	#def __dir__(self):
	#	return [*self._my_methods, *self._my_events]

	def __getattribute__(self, attribute):
		if attribute.startswith("__") and attribute.endswith("__"):
			return super().__getattribute__(attribute)
		# Block some attributes
		elif attribute.lower() in self.__class__._BLOCKED_ATTRIBUTES:
			raise AttributeError("Attribute '{0}' not allowed for {1}".format(attribute, self.__class__.__name__))
		# Get/Set/Call attribute, if it's registered in IDispatch.__dir__
		elif attribute in dir(IDispatch):
			super().__getattribute__(attribute)
		# Add case insensitivies for VBA
		return super().__getattribute__(attribute.lower())

	# VBA-methods with recasting
	# Delete() - without changing
	def getextensiondictionary(self):
		obj = super().GetExtensionDictionary()
		return _recast(obj)
	get_extension_dictionary = getextensiondictionary
	def getxdata(self, AppName: str, XDataType: list = list(), XDataValue: list = list()):
		# ToDo: maybe array.array or something else?
		XDataType.clear()
		XDataValue.clear()
		super().GetXData(AppName, XDataType, XDataValue)
		return XDataType, XDataValue
	get_xdata = getxdata
	def setxdata(self, XDataType: list[c_short], XDataValue: list):
		arr_check(XDataType, c_short)
		if len(XDataType) != len(XDataValue):
			raise TypeError("Lenght of XDataType and XDataValue list must be same! {0} != {1}".format(len(XDataType), len(XDataValue)))
		super().SetXData(XDataType, XDataValue)
	set_xdata = setxdata
	
	# VBA-properties with recasting
	
	@property
	def application(self):
		from .application import AcadApplication
		app = super().Application
		app.__class__ = AcadApplication
		return app
	app = application
	@property
	def document(self):
		from .document import AcadDocument
		doc = super().Document
		doc.__class__ = AcadDocument
		return doc
	doc = document
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes
	has_extension_dictionary = HasExtensionDictionary
	# ObjectID<Long_Ptr> - without changes ???????
	object_id = ObjectID
	# ObjectName<String> - without changes
	object_name = ObjectName
	# OwnerID<Long_Ptr> - without changes ???????
	owner_id = OwnerID


class AcadEntity(POINTER(_dll.IAcadEntity), AcadObject):
	def __str__(self):
		try:
			hndl = self.handle
		except:
			hndl = "None"
		return "Basic AutoCAD geometry entity\n\tHandle: {0}".format(hndl)

	# VBA-methods with recasting
	def arraypolar(NumberOfObjects: int, AngleToFill: float, CenterPoint: A3Vertex):
		objs = super().ArrayPolar()
		res = []
		for obj in objs:
			res.append(_recast(obj))
		return res
	array_polar = arraypolar
	def arrayrectangular(NumberOfRows: int = 1, NumberOfColumns: int = 1, NumberOfLevels: int = 1, DistBetweenRows: float = 0.0, DistBetweenColumns: float = 0.0, DistBetweenLevels: float = 0.0):
		objs = super().ArrayRectangular()
		res = []
		for obj in objs:
			res.append(_recast(obj))
		return res
	array_rectangular = arrayrectangular
	def copy(self):
		return _recast(super().Copy())
	# Delete - without changes
	def getboundingbox(self, MinPoint: A3Vertex = A3Vertex(), MaxPoint: A3Vertex = A3Vertex()):
		super().GetBoundingBox(MinPoint, MaxPoint)
		return MinPoint, MaxPoint
	get_bounding_box = getboundingbox
	# GetExtensionDictionary - from parent
	# GetXData - from parent
	# Highlight<bool> - without changes
	def intersectwith(self, IntersectObject:AcadEntity, ExtendOption:int):
		# ExtendOption is AcExtendOption enum
		return A3Vertexes(super().GetBoundingBox(IntersectObject, ExtendOption))
	intersect_with = intersectwith
	def mirror(self, Point1: A3Vertex, Point2: A3Vertex):
		return _recast(super().Mirror(Point1, Point2))
	
	def mirror3d(self, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex):
		return _recast(super().Mirror3D(Point1, Point2, Point3))
	# Move - without changes
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	scale_entity = ScaleEntity
	# SetXData - from parent
	def transformby(self, TransformationMatrix: ATrMatrix):
		super().TransformBy(TransformationMatrix) # ToDo: need test!!!
	transform_by = transformby
	# Update - without changes
	
	# VBA-properties with recasting
	
	# Application<AcadApplication> - from parent
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - from parent
	entity_transparency = EntityTransparency
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	@property
	def hyperlinks(self):
		return _recast(super().Hyperlinks)
	# Layer<String> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	linetype_scale = LinetypeScale
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	@property
	def truecolor(self):
		return _recast(super().TrueColor)
	true_color = truecolor # TOO UGLY
	# Visible<bool> - without changes
	
	
class AcadDictionary(POINTER(_dll.IAcadDictionary), AcadObject):
	def __new__(cls, source=None):
		if source is None:
		
	def __str__(self):
		try:
			hndl = self.handle
		except:
			hndl = "None"
		return "AutoCAD Dictionary object\n\tHandle: {0}".format(hndl)
	# VBA-methods with recasting
	# AddObject(<String>, <String>)<Object> - idk. need test
	def addxrecord(self, Keyword: str):
		# return <XRecord>
		return _recast(super().AddXRecord(Keyword))
	add_xrecord = addxrecord
	# GetName(<Object>)<String> - without changes
	def getobject(self, Name: str):
		return _recast(super().GetObject(Name))
	get_object = getobject
	def remove(self, Name:str):
		return _recast(super().Remove(Name))
	# Rename(<String>, <String>) - without changes
	# Replace(<String>, <Object>) - without changes
	
	# VBA-properties with recasting
	
	# Application<AcadApplication> - from parent
	# Count<int> - without changes
	# Document<AcadDocument> - from parent
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Name<String> - without changes
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent



