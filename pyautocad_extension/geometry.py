#!/usr/bin/env python
# -*- coding: utf-8 -*-



class _GeoALL(AcadObject):
	"""
	Intermediate class for all geometry-type objects.
	"""
	def array_polar(self, num_of_objs: int, angle_to_fill: float, center_point):
		"""
		Creates an array of selected objects in a polar pattern.
		:param num_of_objs:
		:param angle_to_fill:
		:param center_point:
		:return:
		"""
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
		return self._me.ArrayRectangular(
				rows, columns, levels,
				dist_rows, dist_columns, dist_levels
			)

	def copy(self):
		"""
		Copies the entity object.
		:return:
		"""
		return AcadObject(self._me.Copy()).parse()

	def GetBoundingBox(self, min_p, max_p):
		return self._me.GetBoundingBox(min_p, max_p)

	def Highlight(self, highlight_flag: bool):
		"""
		Highlights the entity object.
		:param highlight_flag:
		:return:
		"""
		self._me.Highlight(highlight_flag)

	@property
	def Hyperlinks(self):
		"""
		Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)
		:return:
		"""
		return self._me.Hyperlinks

	def IntersectWith(self, other, option):
		"""
		Intersects with the input entity object.
		:param other: AcadObject
		:param option: AcExtendOption
		:return:
		"""

	@property
	def layer(self) -> str:
		"""
		Specifies the current layer of the object
		:return:
		"""
		return self._me.Layer

	@layer.setter
	def layer(self, value: str):
		self._me.Layer = value

	@property
	def linetype(self) -> str:
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
		return self._me.Lineweight

	@lineweight.setter
	def lineweight(self, value):
		self._me.Lineweight = value

	@property
	def material(self) -> str:
		return self._me.Material

	@material.setter
	def material(self, value: str):
		self._me.Material = value

	def mirror(self, p1, p2):
		return AcadObject(self._me.Mirror(p1, p2)).parse()

	def mirror3D(self, p1, p2, p3):
		return AcadObject(self._me.Mirror3D(p1, p2, p3)).parse()

	def move(self, p1, p2):
		self._me.Move(p1, p2)

	@property
	def normal(self):
		"""
		Specifies the three-dimensional normal unit vector for the entity
		:return:
		"""
		return self._me.Normal

	@normal.setter
	def normal(self, vec):
		self._me.Normal = vec

	@property
	def plot_stylename(self) -> str:
		return self._me.PlotStyleName

	@plot_stylename.setter
	def plot_stylename(self, value: str):
		self._me.PlotStyleName = value

	def rotate(self, base_p, angle: float):
		"""
		Rotates the entity object about a point.
		:param base_p:
		:param angle:
		:return:
		"""
		self._me.Rotate(base_p, angle)

	def rotate3D(self, p1, p2, angle: float):
		self._me.Rotate3D(p1, p2, angle)

	def scale_entity(self, p, scale_factor: float):
		self._me.ScaleEntity(p, scale_factor)

	@property
	def thickness(self) -> float:
		return self._me.Thickness

	@thickness.setter
	def Thickness(self, value: float):
		self._me.Thickness = value

	def transform_by(self, transform_matrix):
		self._me.TransformBy(transform_matrix)

	@property
	def truecolor(self):
		"""

		:return: AcadAcCmColor
		"""
		return self._me.TrueColor

	@truecolor.setter
	def truecolor(self, value):
		self._me.truecolor = value

	def update(self):
		self._me.Update()

	@property
	def visible(self) -> bool:
		return self._me.Visible

	@visible.setter
	def visible(self, value: bool):
		self._me.Visible = value


class AcadPoint(_GeoALL):
	"""
	Point object
	"""
	@property
	def coordinates(self):
		"""
		Specify the X, Y, Z coordinate for the position of the point or use the Pick Point button to set X, Y, Z values simultaneously
		"""
		return self._me.Coordinates

	@coordinates.setter
	def coordinates(self, value):
		self._me.Coordinates = value

	def __str__(self):
		return "AutoCAD Geometric Point\n\tHandle: {0}".format(self.handle)




