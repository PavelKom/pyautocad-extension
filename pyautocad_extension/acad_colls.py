#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .application import acad_app
# Some Acad collections
from .object import AcadObject


class _AcadCollPre(AcadObject):
	"""
	Intermediate class for all collection-type Acad objects.
	"""
	def __init__(self, obj, parent=None):
		"""
		Intermediate class for all collection-type Acad objects.
		:param obj: VBA Autocad collection object
		:param parent: VBA Autocad object, used for parenting (like AcadDocument, etc.)
		"""
		super().__init__(obj, parent)
		self._items = []
		self._update()

	# VBA-Methods
	def add(self, **kwargs):
		self._fix_dict(kwargs)
		self._items.append(AcadObject(self._me.Add(**kwargs)).parse())
		return self._items[-1]

	def delete(self, index=None):
		for item in self:
			item.delete()
		self._me.Delete()
		del self

	# get_extension_dictionary
	# get_x_data

	def item(self, index):
		return self[index]

	# set_x_data

	# VBA-Properties
	# application
	@property
	def count(self):
		return len(self)

	# document
	# handle
	# has_extension_dictionary
	# object_id
	# object_name
	# owner_id

	# Python-Methods
	def list(self):
		return self._items

	def get_by_raw(self, raw):
		"""
		Return parsed AcadObject, and it's index by VBA-object
		:param raw: VBA-object
		:return: parsed AcadObject, index
		"""
		for i, item in enumerate(self._items):
			if item.raw == raw:
				return item, i
		return None, None

	def _update(self):
		_max = max(len(self), len(self._items))
		for i in range(_max):
			# Checked: Python-class object is wrapper for VBA-Acad-object
			if i < len(self._items) and self[i].raw == self._me.Item(i+1):
				continue
			# AcadObject already wrapped in this collection, but have wrong index
			if self._me.Item(i+1) in self:
				item, id = self.get_by_raw(self._me.Item(i+1))
				# Move wrapper to proper position
				if id != i:
					self._items.insert(self._items.pop(id), i)
			# Add wrapper for VBA-Acad-object
			else:
				self._items.insert(AcadObject(self._me.Item(i + 1), self).parse(), i)
			# Delete redundant wrappers
			if i >= len(self):
				self[i].unbind()

	# MAGIC
	def __getitem__(self, index):
		return self._items[index]

	def __delitem__(self, index):
		if index is None:
			for item in self:
				try:
					item.delete()
				except:
					pass
			self._me.Delete()
		else:
			try:
				self[index].delete()
			except:
				pass

	def __len__(self):
		return self._me.Count

	def __iter__(self):
		self._update()
		i = 0
		# range(VERY_BIG_NUMBER) used a more RAM than 'while a < b'
		_l = len(self)
		while i < _l:
			yield self[i]
			i += 1

	def __reversed__(self):
		self._update()
		i = len(self) - 1
		while i > 0:
			yield self[i]
			i -= 1

	def __contains__(self, item):
		if isinstance(item, AcadObject):
			for _item in self._items:
				if _item.raw == item.raw:
					return True
			return False
		for _item in self._items:
			if _item.raw == item:
				return True
		return False


class AcadBlocks(_AcadCollPre):
	"""
	The collection of all blocks in the drawing
	"""
	# VBA-Methods
	def add(self, insertion_point, name: str):
		kwargs = {
			"InsertionPoint": insertion_point,
			"Name": name
		}
		return super().add(**kwargs)


class AcadDictionaries(_AcadCollPre):
	"""
	The collection of all dictionaries in the drawing
	"""
	# VBA-Methods
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadDimStyles(_AcadCollPre):
	"""
	The collection of all dimension styles in the drawing
	"""
	# VBA-Methods
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadDocuments(_AcadCollPre):
	"""
	The collection of all AutoCAD drawings open in the current session
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"document",
		"doc",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)
	# VBA-Methods
	def add(self, template_name=None):
		kwargs = {
			"TemplateName": template_name
		}
		return super().add(**kwargs)

	def close(self):
		self._me.Close()

	def __delitem__(self, index):
		del self[index]


class AcadGroups(_AcadCollPre):
	"""
	The collection of all groups in the drawing
	"""
	# VBA-Methods
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadHyperlinks(_AcadCollPre):
	"""
	The collection of all hyperlinks for a given entity
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"document",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)
	# VBA-Methods
	def add(self, name: str, description=None, named_location=None):
		kwargs = {
			"Name": name,
			"Description": description,
			"NamedLocation": named_location
		}
		return super().add(**kwargs)


class AcadLayers(_AcadCollPre):
	"""
	The collection of all layers in the drawing
	"""
	# VBA-Methods
	def add(self, name):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)

	def generate_usage_data(self):
		"""
		Generates layer usage data. See also Used property of Layer.
		"""
		self._me.GenerateUsageData()

	def get_extension_dictionary(self):
		"""
		Gets the extension dictionary associated with an object
		:return: AcadDictionary
		"""
		return self._me.GetExtensionDictionary()


class AcadLayouts(_AcadCollPre):
	"""
	The collection of all layouts in the drawing
	"""
	# VBA-Methods
	def add(self, name):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadLineTypes(_AcadCollPre):
	"""
	The collection of all linetypes in the drawing
	"""
	# VBA-Methods
	def add(self, name):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)

	def load(self, name: str, filename: str):
		self._me.Load(name, filename)


class AcadMaterials(_AcadCollPre):
	"""
	The collection of all materials in the drawing
	"""
	# VBA-Methods
	def add(self, name):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadMenuGroups(_AcadCollPre):
	"""
	A collection of MenuGroup objects representing all the menu groups loaded in the current AutoCAD session
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"add",
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"doc",
		"document",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)

	def load(self, menu_filename: str, base_menu):
		kwargs = {
			"MenuFileName": menu_filename,
			"BaseMenu": base_menu
		}
		return AcadObject(self._me.Load(**kwargs)).parse()

	@property
	def parent(self):
		return self._me.Parent


class AcadPlotConfigurations(_AcadCollPre):
	"""
	A collection of named plot settings
	"""
	def add(self, name: str, model_type=None):
		kwargs = {
			"Name": name,
			"ModelType": model_type
		}
		return super().add(**kwargs)


class AcadPopupMenus(_AcadCollPre):
	"""
	A collection of PopupMenu objects representing all the popup menus loaded in the MenuGroup
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"doc",
		"document",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)

	def add(self, menu_name: str):
		kwargs = {
			"MenuName": menu_name
		}
		return super().add(**kwargs)


class AcadRegisteredApplications(_AcadCollPre):
	"""
	The collection of all registered applications in the drawing
	"""
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadSelectionSets(_AcadCollPre):
	"""
	The collection of all selection sets in the drawing
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"doc",
		"document",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)

	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadTextStyles(_AcadCollPre):
	"""
	The collection of all text styles in the drawing
	"""
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


class AcadToolbars(_AcadCollPre):
	"""
	A collection of Toolbar objects representing all the toolbars loaded in the current AutoCAD session
	"""
	BLOCKED_ATTRIBUTES = (
		# Methods
		"delete",
		"get_extension_dictionary",
		"get_x_data",
		"set_x_data",
		# Properties
		"doc",
		"document",
		"handle",
		"has_extension_dictionary",
		"object_id",
		"object_name",
		"owner_id"
	)

	def add(self, toolbar_name: str):
		kwargs = {
			"ToolbarName": toolbar_name
		}
		return super().add(**kwargs)

	@property
	def large_buttons(self) -> bool:
		return self._me.LargeButtons

	@large_buttons.setter
	def large_buttons(self, value: bool):
		self._me.LargeButtons = value

	@property
	def parent(self):
		return self._me.Parent


class AcadUCSs(_AcadCollPre):
	"""
	The collection of all user coordinate systems (UCSs) in the drawing
	"""
	def add(self, origin, x_axis_point, y_axis_point, name: str):
		kwargs = {
			"Origin": origin,
			"XAxisPoint": x_axis_point,
			"YAxisPoint": y_axis_point,
			"Name": name
		}
		return super().add(**kwargs)


class AcadViewports(_AcadCollPre):
	"""
	The collection of all viewports in the drawing
	"""
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)

	def delete_configuration(self, name: str):
		self._me.DeleteConfiguration(name)


class AcadViews(_AcadCollPre):
	"""
	The collection of all views in the drawing
	"""
	def add(self, name: str):
		kwargs = {
			"Name": name
		}
		return super().add(**kwargs)


__all__ = (
	"AcadBlocks",
	"AcadDictionaries",
	"AcadDimStyles",
	"AcadDocuments",
	"AcadGroups",
	"AcadHyperlinks",
	"AcadLayers",
	"AcadLineTypes",
	"AcadMaterials",
	"AcadMenuGroups",
	"AcadPlotConfigurations",
	"AcadPopupMenus",
	"AcadRegisteredApplications",
	"AcadSelectionSets",
	"AcadTextStyles",
	"AcadToolbars",
	"AcadUCSs",
	"AcadViewports",
	"AcadViews",
)




