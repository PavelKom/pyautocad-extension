

class AcadDocument(object):
    def __init__(self, template="", create_new=True):
        self._me = None
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
    def app(self):  # As AcadViewport
        """
        Gets the Application object
        Kinda sus
        """
        return self._me.Application

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
    def elevationmodelspace(self) -> float:
        """
        Specifies the elevation setting in the model space
        """
        return self._me.ElevationModelSpace
        
    @elevationmodelspace.setter
    def elevationmodelspace(self, value: float):
        self._me.ElevationModelSpace = value
    
    @property
    def elevationpaperspace(self) -> float:
        """
        Specifies the elevation setting in the paper space
        """
        return self._me.ElevationPaperSpace
        
    @elevationpaperspace.setter
    def elevationpaperspace(self, value: float):
        self._me.ElevationPaperSpace = value
    
    def endundomark(self):
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

    def getvariable(self, name: str):
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
        from .application import acad_docs
        return acad_docs.open(file, read_only, password)
    





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
        
        
        
        
    """







