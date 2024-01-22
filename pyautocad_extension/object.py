#!/usr/bin/env python
# -*- coding: utf-8 -*-
class AcadObject:
	BLOCKED_ATTRIBUTES = ()
	
	def __init__(self, obj, parent=None):
		self._me = obj # can't call New AcadObject
		self._parent = parent # for parenting purpose

	# VBA-Methods
	def delete(self):
		self._me.Delete()
		del self

	def get_extension_dictionary(self):
		"""
		Gets the extension dictionary associated with an object
		:return: AcadDictionary
		"""
		return self._me.GetExtensionDictionary()

	def get_x_data(self, app_name: str, x_data_type, x_data_value):
		"""
		Gets the extended data (XData) associated with an object
		:param app_name:
		:param x_data_type:
		:param x_data_value:
		:return:
		"""
		self._me.GetXData(app_name,x_data_type,x_data_value)

	def set_x_data(self, x_data_type, x_data_value):
		self._me.SetXData(x_data_type, x_data_value)

	# VBA-Properties
	@property
	def app(self):  # As AcadApplication
		"""
		Gets the Application object
		"""
		from .application import acad_app
		return acad_app

	@property
	def application(self):
		return self.app

	@property
	def doc(self):
		from .application import acad_docs
		return acad_docs.get_by_doc(self._me.Document)

	@property
	def document(self):
		return self.doc

	@property
	def handle(self) -> str:
		"""
		Gets the handle of an object
		:return:
		"""
		return self._me.Handle

	@property
	def has_extension_dictionary(self) -> bool:
		"""
		Determines if the object has an extension dictionary associated with it
		:return:
		"""
		return self._me.HasExtensionDictionary

	@property
	def object_id(self):
		"""
		Gets the object ID of the object
		:return:
		"""
		return self._me.ObjectID

	@property
	def object_name(self) -> str:
		"""
		Gets the AutoCAD class name of the object
		:return: str
		"""
		return self._me.ObjectName

	@property
	def owner_id(self):
		"""
		Gets the object ID of the owner (parent) object
		:return: LongPtr
		"""
		return self._me.OwnerID

	# Python-Methods
	def is_valid(self):
		try:
			self._me.Handle
			return True
		except:
			return False

	def unbind(self):
		self._me = None
		del self

	def same(self, other):
		return self._me == other

	def raw(self):
		return self._me

	def parse(self):
		if self.object_name in _parse_dict.keys():
			return _parse_dict[self.object_name](self._me, self._parent)
		return None

	@staticmethod
	def _fix_dict(kw: dict):
		# Remove all items with None value
		for k, v in kw.items():
			if v is None:
				kw.pop(k)

	# MAGIC
	def __eq__(self, other):
		if isinstance(other, AcadObject):
			return other.same(self._me)
		return False

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		try:
			hndl = self.handle
		except:
			hndl = "None"
		return "Basic AutoCAD object\n\tHandle: {0}".format(hndl)
	
	# Used for blocking some attributes, like 'add', 'document', etc.
	def __getattribute__(self, attribute):
		if attribute in self.BLOCKED_ATTRIBUTES:
			raise AttributeError("Attribute '{0}' not allowed for {1}".format(attribute, type(self)))
		return super().__getattribute__(attribute)

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
	
	def copy(self):
		"""
		Copies the entity object.
		:return:
		"""
		#TODO
		return AcadObject(self._me.Copy()).parse()
		
	def GetBoundingBox(self, min_p, max_p):
		# TODO
		return self._me.GetBoundingBox(min_p, max_p)
		
	def Highlight(self, highlight_flag: bool):
		"""
		Highlights the entity object.
		:param highlight_flag:
		:return:
		"""
		self._me.Highlight(highlight_flag)
		
	def IntersectWith(self, other, option):
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


_parse_dict = {
	# "AcDbPoint": AcadPoint,
}
