#!/usr/bin/env python
# -*- coding: utf-8 -*-



class _GeoALL(AcadObject):
	"""
	Intermediate class for all geometry-type objects.
	"""
	













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
	def thickness(self) -> float:
		return self._me.Thickness

	@thickness.setter
	def Thickness(self, value: float):
		self._me.Thickness = value






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




