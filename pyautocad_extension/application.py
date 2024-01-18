from pyautocad import Autocad

# Global Autocad Automation object
# Autoopen application, because it's REALLY necessary
acad = Autocad(True)

class AcadApplication(object):
    def __init__(self):
        self.me = acad.app

    def __eq__(self, other):
        return self.me == other.me

    from .document import AcadDocument
    @property
    def doc(self):
        """
        Specifies the active document (drawing file)
        """
        #from .document import AcadDocument
        return AcadDocument.from_app(self.me.ActiveDocument)

    @doc.setter
    def doc(self, value: AcadDocument):
        #from .document import AcadDocument
        self.me.ActiveDocument = value.me

    @property
    def app(self):
        """
        Gets the Application object
        Kinda sus
        """
        #return self.me.Application
        return self.me

    @property
    def cap(self) -> str:
        """
        Gets the text that the user sees displayed for the application or a menu item
        """
        return self.me.Caption

    @property
    def docs(self):
        """
        Return tuple of all opened documents
        """
        docs = []
        for doc in self.me.Documents:
            docs.append(AcadDocument.from_app(doc))
        return tuple(docs)

    @property
    def docs_coll(self):
        """
        The collection of all AutoCAD drawings open in the current session
        """
        return self.me.Documents

    def eval(self, expression: str):
        """
        Evaluates an expression in VBA
        Hope this work...
        """
        self.me.Eval(expression)

    @property
    def fullname(self) -> str:
        """
        Gets the name of the application or document, including the path
        """
        return self.me.FullName

    def get_acad_state(self):
        """ToDo: return class AcadState(...)"""
        return self.me.GetAcadState()

    def get_interface_object(self):
        """ToDo: return class Object(...)"""
        return self.me.GetInterfaceObject()

    @property
    def height(self):
        """
        Height of the attribute, shape, text, or view toolbar or the main application window
        """
        return self.me.Height

    @height.setter
    def height(self, value):
        self.me.Height = value

    @property
    def hwnd(self):  # As LongPtr
        """
        Gets the window handle of the application window frame
        """
        return self.me.HWND

    def ListArx(self):
        """
        Gets the currently loaded AutoCAD ARX applications
        """
        return self.me.ListArx()

    def LoadArx(self, name: str):
        """
        Loads the specified AutoCAD ARX application
        """
        self.me.LoadArx(name)

    def LoadDVB(self, name: str):
        """
        Loads the specified AutoCAD VBA project file
        """
        self.me.LoadDVB(name)

    @property
    def locale_id(self) -> int:
        """
        Gets the locale ID of the current AutoCAD session
        """
        return self.me.LocaleId

    @property
    def menubar(self):  # As AcadMenuBar
        """
        Gets the MenuBar object for the session
        """
        return self.me.MenuBar

    @property
    def menu_groups(self):  # As AcadMenuGroups
        """
        Gets the MenuGroups collection for the session
        """
        return self.me.MenuGroups

    @property
    def name(self) -> str:
        """
        Specifies the name of the object
        """
        return self.me.Name

    @property
    def path(self) -> str:
        """
        Gets the path of the document, application, or external reference
        """
        return self.me.Path

    @property
    def preferences(self):  # As AcadPreferences
        """
        Gets the Preferences object
        """
        return self.me.Preferences

    def quit(self):
        """
        Closes the drawing file and exits the AutoCAD application
        """
        self.me.Quit()
        del self

    def run_macro(self, path: str):
        """
        Runs a VBA macro from the Application object
        """
        self.me.RunMacro(path)

    @property
    def status_id(self):
        """
        Gets the current active status of the viewport
        """
        return self.me.StatusId

    def UnloadArx(self, name: str):
        """
        Unloads the specified AutoCAD ARX application
        """
        self.me.UnloadArx(name)

    def UnloadDVB(self, name: str):
        """
        Unloads the specified AutoCAD VBA project file
        """
        self.me.UnloadDVB(name)

    def update(self):
        """
        Updates the object to the drawing screen
        """
        self.me.Update()

    @property
    def VBE(self):  # As Object
        """
        Gets the VBAIDE extensibility object
        """
        return self.me.VBE

    @property
    def version(self) -> str:
        """
        Gets the version of the AutoCAD application you are using
        """
        return self.me.Version

    @property
    def visible(self) -> bool:
        """
        Specifies the visibility of an object or the application
        """
        return self.me.Visible

    @visible.setter
    def visible(self, value: bool):
        self.me.Visible = value

    @property
    def width(self) -> int:
        """
        Specifies the width of the text boundary, view, image, toolbar, or main application window
        """
        return self.me.Width

    @width.setter
    def width(self, value: int):
        self.me.Width = value

    @property
    def window_left(self) -> int:
        """
        Specifies the left edge of the application window
        """
        return self.me.WindowLeft

    @window_left.setter
    def window_left(self, value: int):
        self.me.WindowLeft = value

    @property
    def window_state(self):  # As AcWindowState
        """
        Specifies the state of the application or document window
        """
        return self.me.WindowState

    @window_state.setter
    def window_state(self, value):
        self.me.WindowState = value

    @property
    def window_top(self) -> int:
        """
        Specifies the top edge of the application window
        """
        return self.me.WindowTop

    @window_top.setter
    def window_top(self, value: int):
        self.me.WindowTop = value

    def zoom_all(self):
        """
        Zooms the current viewport to display the entire drawing
        """
        self.me.ZoomAll()

    def zoom_center(self, center, magnify: float):
        """
        Zooms the current viewport to a specified center point and magnification
        """
        self.me.ZoomCenter(center, magnify)

    def zoom_extents(self):
        """
        Zooms the current viewport to the drawing extents
        """
        self.me.ZoomExtents()

    def zoom_pick_window(self):
        """
        Zooms the current viewport to a window defined by points picked on the screen
        """
        self.me.ZoomPickWindow()

    def zoom_previous(self):
        """
        Zooms the current viewport to its previous extents
        """
        self.me.ZoomPrevious()

    def zoom_scaled(self, scale: float, scaletype):  # scaletype As AcZoomScaleType
        """
        Zooms the current viewport to given scale factor
        """
        self.me.ZoomScaled(scale, scaletype)

    def zoom_window(self, lowerleft, upperright):
        """
        Zooms the current viewport to the area specified by two opposite corners of a rectangle
        """
        self.me.ZoomWindow(lowerleft, upperright)

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
            doc = get_doc_by_name(name)
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


def docs_iter():
    for doc in acad_app.docs:
        yield doc


def get_doc_by_name(name):
    for doc in docs_iter():
        if doc.name == name:
            return doc
    return None
