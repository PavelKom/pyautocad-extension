#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AcadDocument(object):
	def __init__(self, template="", create_new=True):
		self._me = None
		self._model = None
		if create_new:
			from .application import acad_app
			self._me = acad_app.create_doc(template)

	def __eq__(self, other):
		return other.same(self._me)

	@staticmethod
	def from_app(doc):
		_doc = AcadDocument(create_new=False)
		_doc._me = doc
		return _doc

	def unbind(self):
		self._me = None
		del self

	def same(self, other):
		return self._me == other

	def is_valid(self):
		try:
			self._me.Name
			return True
		except:
			False

	def activate(self):
		"""
		Makes the specified drawing active
		"""
		self._me.Activate()

	@property
	def active(self) -> bool:
		"""
		Determines if the document is the active document for the session
		"""
		return self._me.Active

	@property
	def active_dim_style(self):  # As AcadDimStyle
		"""
		Specifies the active dimension style
		"""
		return self._me.ActiveDimStyle

	@active_dim_style.setter
	def active_dim_style(self, value):
		self._me.ActiveDimStyle = value

	@property
	def active_layer(self):  # As AcadLayer
		"""
		Specifies the active layer
		"""
		return self._me.ActiveLayer

	@active_layer.setter
	def active_layer(self, value):
		self._me.ActiveLayer = value

	@property
	def active_layout(self):  # As AcadLayout
		"""
		Specifies the active layout
		"""
		return self._me.ActiveLayout

	@active_layout.setter
	def active_layout(self, value):
		self._me.ActiveLayout = value

	@property
	def active_linetype(self):  # As AcadLineType
		"""
		Specifies the active linetype for the drawing
		"""
		return self._me.ActiveLinetype

	@active_linetype.setter
	def active_linetype(self, value):
		self._me.ActiveLinetype = value

	@property
	def active_material(self):  # As AcadMaterial
		"""
		"""
		return self._me.ActiveMaterial

	@active_material.setter
	def active_material(self, value):
		self._me.ActiveMaterial = value

	@property
	def active_pviewport(self):  # As AcadPViewport
		"""
		Specifies the active paper space viewport for the drawing
		"""
		return self._me.ActivePViewport

	@active_pviewport.setter
	def active_pviewport(self, value):
		self._me.ActivePViewport = value

	@property
	def active_selection_set(self):  # As AcadSelectionSet
		"""
		Gets the active selection set for the drawing
		"""
		return self._me.ActiveSelectionSet

	@property
	def active_space(self):  # As AcActiveSpace
		"""
		Toggles the active space between paper space and model space
		"""
		return self._me.ActiveSpace

	@active_space.setter
	def active_space(self, value):
		self._me.ActiveSpace = value

	@property
	def active_text_style(self):  # As AcadTextStyle
		"""
		Specifies the active text style for the drawing
		"""
		return self._me.ActiveTextStyle

	@active_text_style.setter
	def active_text_style(self, value):
		self._me.ActiveTextStyle = value

	@property
	def active_ucs(self):  # As AcadUCS
		"""
		Specifies the active UCS for the drawing
		"""
		return self._me.ActiveUCS

	@active_ucs.setter
	def active_ucs(self, value):
		self._me.ActiveUCS = value

	@property
	def active_viewport(self):  # As AcadViewport
		"""
		Specifies the active viewport for the drawing
		"""
		return self._me.ActiveViewport

	@active_viewport.setter
	def active_viewport(self, value):
		self._me.ActiveViewport = value

	@property
	def app(self):  # As AcadApplication
		"""
		Gets the Application object
		Kinda sus
		"""
		from .application import acad_app
		return acad_app

	def audit_info(self, fix_err: bool):
		"""
		Evaluates the integrity of the drawing
		"""
		self._me.AuditInfo(fix_err)

	@property
	def blocks_coll(self):  # As AcadBlocks
		"""
		Gets the Blocks collection for the drawing
		"""
		return self._me.Blocks

	def close(self, save=False, file=None):
		"""
		Closes the specified drawing, or all open drawings
		"""
		if not save:
			self._me.Close()
		elif file is None:
			self._me.Close(save)
		else:
			self._me.Close(save, file)
		del self

	def copy_objects(self, obj, owner=None, id_pairs=None):
		"""
		Duplicates multiple objects (deep cloning)
		"""
		if owner is None and id_pairs is None:
			self._me.CopyObjects(obj)
		elif id_pairs is None:
			self._me.CopyObjects(obj, owner)
		else:
			self._me.CopyObjects(obj, owner, id_pairs)

	@property
	def database(self):  # As AcadDatabase
		"""
		Gets the database in which the object belongs
		"""
		return self._me.Database

	@property
	def dictionaries(self):  # As AcadDictionaries
		"""
		Gets the Dictionaries collection for the document
		"""
		return self._me.Dictionaries

	@property
	def dimstyles(self):  # As AcadDimStyles
		"""
		Gets the DimStyles collection for the document
		"""
		return self._me.DimStyles

	@property
	def elevation_modelspace(self) -> float:
		"""
		Specifies the elevation setting in the model space
		"""
		return self._me.ElevationModelSpace

	@elevation_modelspace.setter
	def elevation_modelspace(self, value: float):
		self._me.ElevationModelSpace = value

	@property
	def elevation_paperspace(self) -> float:
		"""
		Specifies the elevation setting in the paper space
		"""
		return self._me.ElevationPaperSpace

	@elevation_paperspace.setter
	def elevation_paperspace(self, value: float):
		self._me.ElevationPaperSpace = value

	def end_undo_mark(self):
		self._me.EndUndoMark()

	def export(self, file, ext, select):  # select As AcadSelectionSet
		"""
		Exports the AutoCAD drawing to a WMF, SAT, EPS, DXF, or BMP format
		"""
		self._me.Export(file, ext, select)

	@property
	def fullname(self) -> str:
		"""
		Gets the name of the application or document, including the path
		"""
		return self._me.FullName

	def get_variable(self, name: str):
		"""
		Gets the current setting of an AutoCAD system variable
		"""
		return self._me.GetVariable(name)

	@property
	def groups(self):
		"""
		Gets the Groups collection for the document
		"""
		return self._me.Groups

	def handle_to_object(self, handle: str):
		"""
		Gets the object that corresponds to the given handle
		"""
		return self._me.HandleToObject(handle)

	@property
	def height(self) -> int:
		"""
		Height of the attribute, shape, text, or view toolbar or the main application window
		"""
		return self._me.Height

	@height.setter
	def height(self, value):
		self._me.Height = value

	@property
	def hwnd(self):  # As LongPtr
		"""
		Gets the window handle of the application window frame
		"""
		return self._me.HWND

	def imports(self, file: str, point, scale: float):
		"""
		Imports a drawing file in SAT, EPS, DXF, or WMF format
		"""
		return self._me.Import(file, point, scale)

	@property
	def layers(self):  # As AcadLayers
		"""
		Gets the Layers collection for the document
		"""
		return self._me.Layers

	@property
	def layouts(self):  # As AcadLayouts
		"""
		Gets the Layouts collection for the document
		"""
		return self._me.Layouts

	@property
	def limits(self):  # As Variant
		"""
		Specifies the drawing limits
		"""
		return self._me.Limits 

	@limits.setter
	def limits(self, value):
		self._me.Limits = value

	@property
	def linetypes(self):  # As AcadLineTypes
		"""
		Gets the Linetypes collection for the document
		"""
		return self._me.Linetypes 

	def load_shape_file(self, file: str):
		"""
		Loads a shape file (SHX)
		"""
		self._me.load_shape_file(file)

	@property
	def materials(self):  # As AcadMaterials
		"""
		Gets the Materials collection for the document
		"""
		return self._me.Materials 

	@property
	def model_space(self):  # As AcadModelSpace
		"""
		Gets the ModelSpace collection for the document
		"""
		return self.model

	@property
	def model(self):  # As AcadModelSpace
		"""
		Gets the ModelSpace collection for the document
		"""
		from .acad_colls import AcadModelSpace
		if self._model is None:
			self._model = AcadModelSpace(self)
		return self._model

	@property
	def model_raw(self):
		return self._me.ModelSpace

	@property
	def mspace(self) -> bool:
		"""
		Allows editing of the model from floating paper space viewports
		"""
		return self._me.MSpace 

	@mspace.setter
	def mspace(self, value: bool):
		self._me.MSpace = value

	@property
	def name(self) -> str:
		"""
		Specifies the name of the document
		"""
		return self._me.Name 

	@staticmethod
	def new(template: str):
		"""
		Creates a new document in SDI mode
		"""
		return AcadDocument(template)

	def obj_id_to_object(self, object_id):
		"""
		Gets the object that corresponds to the given object ID
		"""
		return self._me.ObjectIdToObject(object_id)

	@property
	def object_snap_mode(self) -> bool:
		"""
		Specifies the setting of the object snap mode
		"""
		return self._me.ObjectSnapMode 

	@object_snap_mode.setter
	def object_snap_mode(self, value: bool):
		self._me.ObjectSnapMode = value

	@staticmethod
	def open(file: str, read_only=False, password=None):
		"""
		Open AutoCAD document
		"""
		from .application import acad_docs
		return acad_docs.open(file, read_only, password)

	@property
	def paperspace(self):  # As AcadPaperSpace
		"""
		Gets the PaperSpace collection for the document
		"""
		return self._me.PaperSpace 

	@property
	def path(self) -> str:
		"""
		Gets the path of the document, application, or external reference
		"""
		return self._me.Path 

	@property
	def pick_first_selection_set(self):  # As AcadSelectionSet
		"""
		Gets the pickfirst selection set
		"""
		return self._me.PickfirstSelectionSet 

	@property
	def plot(self):  # As AcadPlot
		"""
		Gets the Plot object for the document
		"""
		return self._me.Plot 

	@property
	def plot_configurations(self):  # As AcadPlotConfigurations
		"""
		Gets the PlotConfigurations collection for the document
		"""
		return self._me.PlotConfigurations 

	def post_command(self, command: str):
		"""
		Posts a command string from a VB or VBA application to the document for processing.
		Posts a command string to the document for execution when the document enters an idle state.
		"""
		self._me.PostCommand(command)

	@property
	def preferences(self):  # As AcadDatabasePreferences
		"""
		Gets the Preferences object
		"""
		return self._me.Preferences 

	def purge_all(self):
		"""
		Removes unused named references such as unused blocks or layers from the document
		"""
		self._me.PurgeAll()

	@property
	def readonly(self) -> bool:
		"""
		Specifies if the document is read-only or read-write
		"""
		return self._me.ReadOnly 

	def regen(self, all_viewports=False):
		"""
		Regenerates the entire drawing and recomputes the screen coordinates and view resolution for all objects
		"""
		# originaly used AcRegenType enum
		# acActiveViewport = 0
		# acAllViewports = 1
		self._me.Regen(int(all_viewports))

	@property
	def registered_applications(self):  # As AcadRegisteredApplications
		"""
		The collection of all registered applications in the drawing
		"""
		return self._me.RegisteredApplications 
	from .enum import AcSaveAsType
	def save(self, file="", type=AcSaveAsType.acUnknown,security=None):
		"""
		Saves the document or menu group to a specified file
		"""
		if len(file) == 0:
			self._me.Save()
		else:
			from .enum import AcSaveAsType
			if type== AcSaveAsType.acUnknown and security is None:
				self._me.SaveAs(file)
			elif security is None:
				self._me.SaveAs(file, type)
			else:
				self._me.SaveAs(file, type, security)

	@property
	def saved(self) -> bool:
		"""
		Specifies if the document has any unsaved changes
		"""
		return self._me.Saved 

	@property
	def section_manager(self):  # As AcadSectionManager
		"""
		Returns the section manager object
		"""
		return self._me.SectionManager 

	@property
	def selection_sets(self):  # As AcadSelectionSets
		"""
		Gets the SelectionSets collection for the document
		"""
		return self._me.SelectionSets 

	def send_command(self, command):
		"""
		Sends a command string from a VB or VBA application to the document for processing.
		"""
		self._me.SendCommand(command)

	def SetVariable(self, name: str, value):
		"""
		Sets the value of an AutoCAD system variable
		"""
		self._me.SetVariable(name, value)

	@property
	def summary_info(self):  # As AcadSummaryInfo
		"""
		Returns the summary info object.
		"""
		return self._me.SummaryInfo 

	@property
	def text_styles(self):  # As AcadTextStyles
		"""
		Gets the TextStyles collection for the document
		"""
		return self._me.TextStyles 

	@property
	def user_coordinate_systems(self):  # As AcadUCSs
		"""
		Gets the UCSs collection for the document
		"""
		return self._me.UserCoordinateSystems 

	@property
	def utility(self):  # As AcadUtility
		"""
		Gets the Utility object for the document
		"""
		return self._me.Utility 

	@property
	def viewports(self):  # As AcadViewports
		"""
		Gets the Viewports collection for the document
		"""
		return self._me.Viewports 

	@property
	def views(self):  # As AcadViews
		"""
		Gets the Views collection for the document
		"""
		return self._me.Views 

	def wblock(self, file: str, selects):  # selects as AcadSelectionSet
		"""
		Writes out the given selection set as a new drawing file
		"""
		self._me.Wblock(file, selects)

	@property
	def width(self) -> int:
		"""
		Specifies the width of the text boundary, view, image, toolbar, or main application window
		"""
		return self._me.Width 

	@width.setter
	def width(self, value: int):
		self._me.Width = value

	@property
	def window_state(self):  # As AcWindowState
		"""
		Specifies the state of the application or document window
		"""
		return self._me.WindowState 

	@window_state.setter
	def window_state(self, value):
		self._me.WindowState = value

	@property
	def window_title(self) -> str:
		"""
		Gets the title of the document window
		"""
		return self._me.WindowTitle 

	@property
	def get_raw(self):
		return self._me

	"""
	events:
		Activate
		BeginClose
		BeginCommand
		BeginDocClose
		BeginDoubleClick
		BeginLisp
		BeginPlot
		BeginRightClick
		BeginSave
		BeginShortcutMenuCommand
		BeginShortcutMenuDefault
		BeginShortcutMenuEdit
		BeginShortcutMenuGrip
		BeginShortcutMenuOsnap
		Deactivate
		EndCommand
		EndLisp
		EndPlot
		EndSave
		EndShortcutMenu
		LayoutSwitched
		LispCancelled
		ObjectAdded
		ObjectErased
		ObjectModified
		SelectionChanged
		WindowChanged
		WindowMovedOrResized
	"""







