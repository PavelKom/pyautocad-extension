#!/usr/bin/env python
# -*- coding: utf-8 -*-
import comtypes
from .types import parsedict

pattern1 = "_.*_"


class AcadObject:
	BLOCKED_ATTRIBUTES = ()
	_ALREADY_DEFINED = {}
	
	# Avoid multiply creating Python.AcadObject for same Autocad.AcadObject
	def __new__(cls, *args, **kwargs):
		com_obj = kwargs.get("obj", args[0])
		obj = cls._ALREADY_DEFINED.get(com_obj)
		if obj is None:
            return super().__new__(cls)
		if not obj.is_valid():
			obj.unbind()
			cls._ALREADY_DEFINED.pop(com_obj)
            return super().__new__(cls)
		return obj
	
	def __init__(self, obj, sink=None):
		its_me = self._ALREADY_DEFINED.get(obj)
        if its_me is None or its_me != self:
			self._me = obj # can't call New AcadObject
			self._sink = sink # for events
			self._ALREADY_DEFINED[obj] = self
			if sink is not None:
				self._event_connect = comtypes.client.GetEvents(self._me, sink, acad_dll.IAcadObjectEvents)
		
	# MAGIC
	def __eq__(self, other):
		if isinstance(other, AcadObject):
			return other.me == self.me
		return False

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		try:
			hndl = self.handle
		except:
			hndl = "None"
		return "Basic AutoCAD object\n\tHandle: {0}".format(hndl)
	
	def __dir__(self):
		return [*self._my_methods, *self._my_events]
	
	# Used for blocking some attributes, like 'add', 'document', etc.
	def __getattribute__(self, attribute):
		if attribute in self.BLOCKED_ATTRIBUTES:
			raise AttributeError("Attribute '{0}' not allowed for {1}".format(attribute, type(self)))
		return super().__getattribute__(attribute)
		
	# Python-Methods
	def is_valid(self):
		try:
			# Try update object
			self._me.Update()
			return True
		except:
			return False

	def unbind(self):
		self._me = None
		del self

	def same(self, other):
		return self._me == other

	@property
	def me(self):
		return self._me

	def parse(self):
		if self.object_name in parse_dict.keys():
			del self._ALREADY_DEFINED[self.obj]
			name = self.object_name
			obj = self._me
			sink = self._sink
			self.unbind()
			return parse_dict[name](obj, sink)
		return self
	
	def _my_methods(self):
		"""
		Get COM Object methods and properties 
		"""
        res = []
        interface = self.obj.__com_interface__
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
        interface = self.obj._outgoing_interfaces_
        dir1 = dir(IDispatch)
        for val in dir(interface):
            if re.match(pattern1, val) or val in dir1:
                continue
            res.append(val)
        return res
		
	# VBA-Methods
	def delete(self):
		self._me.Delete()
		del self
	
	Delete = delete

	def get_extension_dictionary(self):
		"""
		Gets the extension dictionary associated with an object
		:return: AcadDictionary
		"""
		return self._me.GetExtensionDictionary()
	
	GetExtensionDictionary = get_extension_dictionary

	def get_x_data(self, app_name: str, x_data_type, x_data_value):
		"""
		Gets the extended data (XData) associated with an object
		:param app_name:
		:param x_data_type:
		:param x_data_value:
		:return:
		"""
		self._me.GetXData(app_name,x_data_type,x_data_value)
	
	GetXData = get_x_data

	def set_x_data(self, x_data_type, x_data_value):
		self._me.SetXData(x_data_type, x_data_value)
	
	SetXData = set_x_data

	# VBA-Properties
	@property
	def app(self):  # As AcadApplication
		"""
		Gets the Application object
		"""
		from .application import AcadApplication
		return AcadApplication.from_obj(self._me.Application)

	Application = app
	application = app
	App = app

	@property
	def doc(self):
		from .application import acad_docs
		return AcadApplication.from_obj(self._me.Document)
	
	Document = doc
	document = doc
	Doc = doc

	@property
	def handle(self) -> str:
		"""
		Gets the handle of an object
		:return:
		"""
		return self._me.Handle
	
	Handle = handle

	@property
	def has_extension_dictionary(self) -> bool:
		"""
		Determines if the object has an extension dictionary associated with it
		:return:
		"""
		return self._me.HasExtensionDictionary
	
	HasExtensionDictionary = has_extension_dictionary

	@property
	def object_id(self):
		"""
		Gets the object ID of the object
		:return:
		"""
		return self._me.ObjectID
	
	ObjectID = object_id

	@property
	def object_name(self) -> str:
		"""
		Gets the AutoCAD class name of the object
		:return: str
		"""
		return self._me.ObjectName
	
	ObjectName = object_name

	@property
	def owner_id(self):
		"""
		Gets the object ID of the owner (parent) object
		:return: LongPtr
		"""
		return self._me.OwnerID

	OwnerID = owner_id
	
	"""
	events:
		Modified
	"""
	

class AcadEntity(AcadObject):
	# VBA-Methods
	def array_polar(self, num_of_objs: int, angle_to_fill: float, center_point):
		"""
		Creates an array of selected objects in a polar pattern.
		:param num_of_objs:
		:param angle_to_fill:
		:param center_point:
		:return:
		"""
		# TODO
		return self._me.ArrayPolar(num_of_objs, angle_to_fill, center_point)
	
	ArrayPolar = array_polar

	def array_rectangular(
			self,
			rows: int,
			columns: int,
			levels: int,
			dist_rows: float,
			dist_columns: float,
			dist_levels: float):
		"""
		Creates an array of selected objects in a rectangular pattern.
		:param rows:
		:param columns:
		:param levels:
		:param dist_rows:
		:param dist_columns:
		:param dist_levels:
		:return:
		"""
		# TODO
		return self._me.ArrayRectangular(
				rows, columns, levels,
				dist_rows, dist_columns, dist_levels
			)
	
	ArrayRectangular = array_rectangular
	
	def copy(self):
		"""
		Copies the entity object.
		:return:
		"""
		#TODO
		return AcadObject(self._me.Copy()).parse()
	
	Copy = copy
		
	def get_bounding_box(self, min_p, max_p):
		# TODO
		return self._me.GetBoundingBox(min_p, max_p)
	
	GetBoundingBox = get_bounding_box
		
	def highlight(self, highlight_flag: bool):
		"""
		Highlights the entity object.
		:param highlight_flag:
		:return:
		"""
		self._me.Highlight(highlight_flag)
	
	Highlight = highlight
		
	def Intersect_With(self, other, option):
		"""
		Intersects with the input entity object.
		:param other: AcadObject
		:param option: AcExtendOption
		:return:
		"""
		# TODO
		pass
		
	def mirror(self, p1, p2):
		#TODO
		return AcadObject(self._me.Mirror(p1, p2)).parse()

	def mirror3D(self, p1, p2, p3):
		#TODO
		return AcadObject(self._me.Mirror3D(p1, p2, p3)).parse()
		
	def move(self, p1, p2):
		#TODO
		self._me.Move(p1, p2)
		
	def rotate(self, base_p, angle: float):
		"""
		Rotates the entity object about a point.
		:param base_p:
		:param angle:
		:return:
		"""
		#TODO
		self._me.Rotate(base_p, angle)

	def rotate3D(self, p1, p2, angle: float):
		#TODO
		self._me.Rotate3D(p1, p2, angle)

	def scale_entity(self, p, scale_factor: float):
		#TODO
		self._me.ScaleEntity(p, scale_factor)
		
	def transform_by(self, transform_matrix):
		#TODO
		self._me.TransformBy(transform_matrix)
		
	def update(self):
		#TODO
		self._me.Update()
		
	# VBA-Properties
	@property
	def entity_transparency(self) -> str:
		#TODO
		return self._me.EntityTransparency
		
	@entity_transparency.setter
	def entity_transparency(self, value: str):
		self._me.EntityTransparency = value
		
	@property
	def Hyperlinks(self):
		"""
		Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)
		:return:
		"""
		#TODO
		return self._me.Hyperlinks
		
	@property
	def layer(self) -> str:
		"""
		Specifies the current layer of the object
		:return:
		"""
		#TODO
		return self._me.Layer

	@layer.setter
	def layer(self, value: str):
		self._me.Layer = value

	@property
	def linetype(self) -> str:
		#TODO
		return self._me.Linetype
		
	@linetype.setter
	def linetype(self, value: str):
		self._me.Linetype = value
		
	@property
	def linetype_scale(self):
		"""
		Specifies the linetype scale factor of the object
		:return: ACAD_NOUNITS enum
		"""
		#TODO
		return self._me.LinetypeScale

	@linetype_scale.setter
	def linetype_scale(self, value):
		self._me.LinetypeScale = value
		
	@property
	def lineweight(self):
		"""
		Specifies the lineweight for the object
		:return: ACAD_LWEIGHT
		"""
		#TODO
		return self._me.Lineweight

	@lineweight.setter
	def lineweight(self, value):
		self._me.Lineweight = value
		
	@property
	def material(self) -> str:
		#TODO
		return self._me.Material

	@material.setter
	def material(self, value: str):
		self._me.Material = value
		
	@property
	def plot_stylename(self) -> str:
		#TODO
		return self._me.PlotStyleName

	@plot_stylename.setter
	def plot_stylename(self, value: str):
		self._me.PlotStyleName = value
		
	@property
	def truecolor(self):
		"""
		Returns the true color of the object
		:return: AcadAcCmColor
		"""
		#TODO
		return self._me.TrueColor

	@truecolor.setter
	def truecolor(self, value):
		self._me.truecolor = value
		
	@property
	def visible(self) -> bool:
		#TODO
		return self._me.Visible

	@visible.setter
	def visible(self, value: bool):
		self._me.Visible = value


