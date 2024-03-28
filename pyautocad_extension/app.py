from comtypes import POINTER
from comtypes.automation import IDispatch
from comtypes.client import GetEvents, ShowEvents
from comtypes.client import GetModule, CreateObject, GetActiveObject

import ctypes

from event_sink import _AcadEventDumper
from api import acad_dll #TODO: api -> .api
_dll = acad_dll.dll


class AcadApplication(POINTER(_dll.IAcadApplication)):
    def __new__(cls, create_if_not_exists=True, always_new=False, visible=True, sink=None):
        if always_new:
            # NOT DYNAMIC. Because dynamic cast used IDispatch, and Events not working
            app = CreateObject(_dll.AcadApplication)
        else:
            try:
                app = GetActiveObject(_dll.AcadApplication)
            except WindowsError:
                if not create_if_not_exists:
                    raise
                else:
                    app = CreateObject(_dll.AcadApplication)
        app.Visible = visible
        app.__class__ = AcadApplication
        app.sink = sink
        if app.sink is not None:
            app.events = GetEvents(app, sink, _dll._DAcadApplicationEvents)
        return app

    #VBA-parsed method
    def eval(self, Expression: str):
        """Evaluates an expression in VBA"""
        self._IAcadApplication__com_Eval(Expression)
    def getacadstate(self):
        """Retrieves an AcadState object."""
        self._IAcadApplication__com_GetAcadState()
    def getinterfaceobject(self, ProgID: str):
        """Accepts a program ID and attempts to load it into AutoCAD as an in-process server"""
        self._IAcadApplication__com_GetInterfaceObject(ProgID)
    def listarx(self):
        """Gets the currently loaded AutoCAD ARX applications"""
        return self._IAcadApplication__com_ListArx()
    def loadarx(self, Name: str):
        """Loads the specified AutoCAD ARX applicationUnloadArx"""
        self._IAcadApplication__com_LoadArx(Name)
    def loaddvb(self, Name: str):
        """Loads the specified AutoCAD VBA project file"""
        self._IAcadApplication__com_LoadDVB(Name)
    def quit(self):
        """Closes the drawing file and exits the AutoCAD application"""
        self._IAcadApplication__com_Quit()
    def runmacro(self, MacroPath: str):
        """Runs a VBA macro from the Application object"""
        self._IAcadApplication__com_RunMacro(MacroPath)
    def unloadarx(self, Name: str):
        """Unloads the specified AutoCAD ARX application"""
        self._IAcadApplication__com_UnloadArx(Name)
    def unloaddvb(self, Name: str):
        """Unloads the specified AutoCAD VBA project file"""
        self._IAcadApplication__com_UnloadDVB(Name)
    def Update(self):
        """Updates the object to the drawing screen"""
        self._IAcadApplication__com_Update()
    #def _IAcadApplication__com_Zoom
    def ZoomAll(self):
        """Zooms the current viewport to display the entire drawing"""
        self._IAcadApplication__com_ZoomAll()
    def ZoomCenter(self, Center, Magnify: float): #Center as A3Point
        """Zooms the current viewport to a specified center point and magnification"""
        self._IAcadApplication__com_ZoomCenter(Center, Magnify)
    def ZoomExtents(self):
        """Zooms the current viewport to the drawing extents"""
        self._IAcadApplication__com_ZoomExtents()
    def ZoomPickWindow(self):
        """Zooms the current viewport to a window defined by points picked on the screen"""
        self._IAcadApplication__com_ZoomPickWindow()
    def ZoomPrevious(self):
        """Zooms the current viewport to its previous extents"""
        self._IAcadApplication__com_ZoomPrevious()
    def ZoomScaled(self, scale: float, ScaleType: int): #ScaleType As AcZoomScaleType
        """Zooms the current viewport to given scale factor"""
        self._IAcadApplication__com_ZoomScaled(scale, ScaleType)
    def ZoomWindow(self, LowerLeft, UpperRight):#LowerLeft, UpperRight as A3Point
        """Zooms the current viewport to the area specified by two opposite corners of a rectangle"""
        self._IAcadApplication__com_ZoomWindow(LowerLeft, UpperRight)

    # VBA-properties TODO: rewrite this?
    activedocument = property(
        fget=self._IAcadApplication__com__get_ActiveDocument,
        fset=self._IAcadApplication__com__set_ActiveDocument,
        doc="Specifies the active document (drawing file)")
    application = property(
        fget=self._IAcadApplication__com__get_Application,
        doc="Gets the Application object")
    caption = property(
        fget=self._IAcadApplication__com__get_Caption,
        doc="Gets the text that the user sees displayed for the application or a menu item")
    documents = property(
        fget=self._IAcadApplication__com__get_Documents,
        doc="Returns the documents collection.")
    fullname = property(
        fget=self._IAcadApplication__com__get_FullName,
        doc="Gets the name of the application or document, including the path")
    height = property(
        fget=self._IAcadApplication__com__get_Height,
        fset=self._IAcadApplication__com__set_Height,
        doc="Height of the attribute, shape, text, or view toolbar or the main application window")
    HWND = property(
        fget=self._IAcadApplication__com__get_HWND,
        doc="Gets the window handle of the application window frame")
    localeid = property(
        fget=self._IAcadApplication__com__get_LocaleId,
        doc="Gets the locale ID of the current AutoCAD session")
    menubar = property(
        fget=self._IAcadApplication__com__get_MenuBar,
        doc="Gets the MenuBar object for the session")
    menugroups = property(
        fget=self._IAcadApplication__com__get_MenuGroups,
        doc="Gets the MenuGroups collection for the session")
    name = property(
        fget=self._IAcadApplication__com__get_Name,
        doc="Specifies the name of the object")
    path = property(
        fget=self._IAcadApplication__com__get_Path,
        doc="Gets the path of the document, application, or external reference")
    preferences = property(
        fget=self._IAcadApplication__com__get_Preferences,
        doc="Gets the Preferences object")
    statusid = property(
        fget=self._IAcadApplication__com__get_StatusId,
        doc="Gets the current active status of the viewport")
    vbe = property(
        fget=self._IAcadApplication__com__get_VBE,
        doc="Gets the VBAIDE extensibility object")
    version = property(
        fget=self._IAcadApplication__com__get_Version,
        doc="Gets the version of the AutoCAD application you are using")
    visible = property(
        fget=self._IAcadApplication__com__get_Visible,
        fset=self._IAcadApplication__com__set_Visible,
        doc="Specifies the visibility of an object or the application")
    width = property(
        fget=self._IAcadApplication__com__get_Width,
        fset=self._IAcadApplication__com__set_Width,
        doc="Specifies the width of the text boundary, view, image, toolbar, or main application window")
    windowleft = property(
        fget=self._IAcadApplication__com__get_WindowLeft,
        fset=self._IAcadApplication__com__set_WindowLeft,
        doc="Specifies the left edge of the application window")
    windowstate = property(
        fget=self._IAcadApplication__com__get_WindowState,
        fset=self._IAcadApplication__com__set_WindowState,
        doc="Specifies the state of the application or document window")
    windowtop = property(
        fget=self._IAcadApplication__com__get_WindowTop,
        fset=self._IAcadApplication__com__set_WindowTop,
        doc="Specifies the top edge of the application window")


class AcadApplicationEvents(_AcadEventDumper):
    _main = None

    # AcadApplication events (_DAcadApplicationEvents)
    def _DAcadApplicationEvents_AppActivate(self):
        pass
    def _DAcadApplicationEvents_AppDeactivate(self):
        pass
    def _DAcadApplicationEvents_ARXLoaded(self, AppName: str):
        pass
    def _DAcadApplicationEvents_ARXUnloaded(self, AppName: str):
        pass
    def _DAcadApplicationEvents_BeginCommand(self, CommandName: str):
        pass
    def _DAcadApplicationEvents_BeginFileDrop(self, FileName: str, Cancel: bool):
        pass
    def _DAcadApplicationEvents_BeginLisp(self, FirstLine: str):
        pass
    def _DAcadApplicationEvents_BeginModal(self):
        pass
    def _DAcadApplicationEvents_BeginOpen(self, FileName: str):
        pass
    def _DAcadApplicationEvents_BeginPlot(self, DrawingName: str):
        pass
    def _DAcadApplicationEvents_BeginQuit(self, Cancel: bool):
        pass
    def _DAcadApplicationEvents_BeginSave(self, FileName: str):
        pass
    def _DAcadApplicationEvents_EndCommand(self, CommandName: str):
        pass
    def _DAcadApplicationEvents_EndLisp(self):
        pass
    def _DAcadApplicationEvents_EndModal(self):
        pass
    def _DAcadApplicationEvents_EndOpen(self, FileName: str):
        pass
    def _DAcadApplicationEvents_EndPlot(self, DrawingName: str):
        pass
    def _DAcadApplicationEvents_EndSave(self, FileName: str):
        pass
    def _DAcadApplicationEvents_LispCancelled(self):
        pass
    def _DAcadApplicationEvents_NewDrawing(self):
        pass
    def _DAcadApplicationEvents_SysVarChanged(self, SysvarName: str, newVal):
        pass
    def _DAcadApplicationEvents_WindowChanged(self, WindowState: int): # WindowState As AcWindowState
        pass
    def _DAcadApplicationEvents_WindowMovedOrResized(self, HWNDFrame, bMoved: bool):
        pass



__all__ = ("AcadApplication", "AcadApplicationEvents", )
