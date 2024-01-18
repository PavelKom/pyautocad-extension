from pyautocad import Autocad

# Global Autocad Automation object
# Autoopen application, because it's REALLY necessary
acad = Autocad(True)


class AcadApplication(object):
    def __init__(self):
        self._me = acad.app

    @property
    def app(self):
        """
        Gets the Application object
        Kinda sus
        """
        #return self._me.Application
        return self._me

    @property
    def cap(self) -> str:
        """
        Gets the text that the user sees displayed for the application or a menu item
        """
        return self._me.Caption

    
    @property
    def doc(self):
        """
        Specifies the active document (drawing file)
        """
        from .document import AcadDocument
        return AcadDocument.from_app(self._me.ActiveDocument)

    from .document import AcadDocument
    @doc.setter
    def doc(self, value: AcadDocument):
        self._me.ActiveDocument = value._me

    @property
    def docs(self):
        """
        Return global AcadDocuments object
        """
        return acad_docs

    @property
    def docs_coll(self):
        """
        The collection of all AutoCAD drawings open in the current session
        """
        return self._me.Documents

    def eval(self, expression: str):
        """
        Evaluates an expression in VBA
        Hope this work...
        """
        self._me.Eval(expression)

    @property
    def fullname(self) -> str:
        """
        Gets the name of the application or document, including the path
        """
        return self._me.FullName

    def get_acad_state(self):
        """ToDo: return class AcadState(...)"""
        return self._me.GetAcadState()

    def get_interface_object(self):
        """ToDo: return class Object(...)"""
        return self._me.GetInterfaceObject()

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

    def ListArx(self):
        """
        Gets the currently loaded AutoCAD ARX applications
        """
        return self._me.ListArx()

    def LoadArx(self, name: str):
        """
        Loads the specified AutoCAD ARX application
        """
        self._me.LoadArx(name)

    def LoadDVB(self, name: str):
        """
        Loads the specified AutoCAD VBA project file
        """
        self._me.LoadDVB(name)

    @property
    def locale_id(self) -> int:
        """
        Gets the locale ID of the current AutoCAD session
        """
        return self._me.LocaleId

    @property
    def menubar(self):  # As AcadMenuBar
        """
        Gets the MenuBar object for the session
        """
        return self._me.MenuBar

    @property
    def menu_groups(self):  # As AcadMenuGroups
        """
        Gets the MenuGroups collection for the session
        """
        return self._me.MenuGroups

    @property
    def name(self) -> str:
        """
        Specifies the name of the object
        """
        return self._me.Name

    @property
    def path(self) -> str:
        """
        Gets the path of the document, application, or external reference
        """
        return self._me.Path

    @property
    def preferences(self):  # As AcadPreferences
        """
        Gets the Preferences object
        """
        return self._me.Preferences

    def quit(self):
        """
        Closes the drawing file and exits the AutoCAD application
        """
        self._me.Quit()
        del self

    def run_macro(self, path: str):
        """
        Runs a VBA macro from the Application object
        """
        self._me.RunMacro(path)

    @property
    def status_id(self):
        """
        Gets the current active status of the viewport
        """
        return self._me.StatusId

    def UnloadArx(self, name: str):
        """
        Unloads the specified AutoCAD ARX application
        """
        self._me.UnloadArx(name)

    def UnloadDVB(self, name: str):
        """
        Unloads the specified AutoCAD VBA project file
        """
        self._me.UnloadDVB(name)

    def update(self):
        """
        Updates the object to the drawing screen
        """
        self._me.Update()

    @property
    def VBE(self):  # As Object
        """
        Gets the VBAIDE extensibility object
        """
        return self._me.VBE

    @property
    def version(self) -> str:
        """
        Gets the version of the AutoCAD application you are using
        """
        return self._me.Version

    @property
    def visible(self) -> bool:
        """
        Specifies the visibility of an object or the application
        """
        return self._me.Visible

    @visible.setter
    def visible(self, value: bool):
        self._me.Visible = value

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
    def window_left(self) -> int:
        """
        Specifies the left edge of the application window
        """
        return self._me.WindowLeft

    @window_left.setter
    def window_left(self, value: int):
        self._me.WindowLeft = value

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
    def window_top(self) -> int:
        """
        Specifies the top edge of the application window
        """
        return self._me.WindowTop

    @window_top.setter
    def window_top(self, value: int):
        self._me.WindowTop = value

    def zoom_all(self):
        """
        Zooms the current viewport to display the entire drawing
        """
        self._me.ZoomAll()

    def zoom_center(self, center, magnify: float):
        """
        Zooms the current viewport to a specified center point and magnification
        """
        self._me.ZoomCenter(center, magnify)

    def zoom_extents(self):
        """
        Zooms the current viewport to the drawing extents
        """
        self._me.ZoomExtents()

    def zoom_pick_window(self):
        """
        Zooms the current viewport to a window defined by points picked on the screen
        """
        self._me.ZoomPickWindow()

    def zoom_previous(self):
        """
        Zooms the current viewport to its previous extents
        """
        self._me.ZoomPrevious()

    def zoom_scaled(self, scale: float, scaletype):  # scaletype As AcZoomScaleType
        """
        Zooms the current viewport to given scale factor
        """
        self._me.ZoomScaled(scale, scaletype)

    def zoom_window(self, lowerleft, upperright):
        """
        Zooms the current viewport to the area specified by two opposite corners of a rectangle
        """
        self._me.ZoomWindow(lowerleft, upperright)

    def create_doc(self, template="", switch_to=True):
        """
        Create new AcadDocument
        :param template: Template filename
        :param switch_to: Switch to created document
        :return: Created document
        """
        doc = None
        old = self.doc
        if len(template) > 0:
            doc = self.docs_coll.Add()
        else:
            doc = self.docs_coll.Add(template)
        if not switch_to:
            self.doc = old
        return doc

    def close_doc(self, name=""):
        if len(name) > 0:
            doc = acad_docs.get_by_name(name)
        else:
            doc = self.doc
        if doc is not None:
            doc.close()

    """
    events:
        AppActivate
        AppDeactivate
        ARXLoaded
        ARXUnloaded
        BeginCommand
        BeginFileDrop
        BeginLisp
        BeginModal
        BeginOpen
        BeginPlot
        BeginQuit
        BeginSave
        EndCommand
        EndLisp
        EndModal
        EndOpen
        EndPlot
        EndSave
        LispCancelled
        NewDrawing
        SysVarChanged
        WindowChanged
        WindowMovedOrResized
    """


# Global AutoCAD application
acad_app = AcadApplication()

class AcadDocuments:
    def __init__(self):
        self._me = acad_app.docs
        self._docs = []
        for doc in self._me:
            from .document import AcadDocument
            self._docs.append(AcadDocument.from_app(doc))
    
    def add(self, template: str):
        """
        Creates a member object and adds it to the appropriate collection
        """
        from .document import AcadDocument
        self._docs.append(
            AcadDocument.from_app(
                self._add(template)))
        return self._docs[-1]
    
    def _add(self, template):
        return self._me.Add(template)
    
    def close(self):
        """
        Close ALL opened documents
        """
        for doc in self._docs:
            doc.unbind()
        self._me.Close()
    
    def item(self, index:int):
        self._update()
        if index < len(self) and index >= 0:
            return self._docs[index]
        return None
    
    def get(self, index:int):
        return self.item(index)
    
    def get_by_name(self, name: str):
        self._update()
        for doc in self:
            if doc.name == name:
                return doc

    def open(self, path:str, read_only=False, password=None):
        if password is None:
            doc = self._me.Open(path,read_only)
        else:
            doc = self._me.Open(path,read_only,password)
        from .document import AcadDocument
        self._docs.append(AcadDocument.from_app(doc))
    
    def _update(self):
        # Update document list
        from .document import AcadDocument
        for doc in self._me:
            if self._already_exist(doc) == -1:
                self._docs.append(AcadDocument.from_app(doc))
        # Remove invalid AcadDocument objects
        for i in range(len(self._docs)-1,-1,-1):
            if not self._docs[i].is_valid():
                self._docs[i].unbind()
                self._doc.pop(i)
    
    def __iter__(self):
        self._update()
        for doc in self._docs:
            yield doc
    
    def _already_exist(self, doc):
        for i, adoc in enumerate(self._docs):
            if adoc.same(doc):
                return i
        return 0
        
    def __len__(self):
        return self._me.Count

# Global AutoCAD AcadDocuments object
acad_docs = AcadDocuments()

