#!/usr/bin/env python
# -*- coding: utf-8 -*-
class AcadObject:
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
		return "Basic AutoCAD object\n\tHandle: {0}".format(self.handle)

	"""
	events:
		Modified
	"""


_parse_dict = {
	# "AcDbPoint": AcadPoint,
}
