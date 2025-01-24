from comtypes import POINTER, BSTR
from comtypes.automation import IDispatch
from comtypes.client import GetEvents, ShowEvents
from comtypes.client import GetModule, CreateObject, GetActiveObject
from pythoncom import Nothing, Empty

import ctypes

from enums import *
from stubs import *
from event_sink import _AcadEventDumper
from api import acad_dll #TODO: api -> .api
from doc import AcadDocument, AcadDocuments #TODO: doc -> .doc
from utils import _ez_ptr, CastManager, A3Vertex
_dll = acad_dll.dll

class AcadApplication(POINTER(_dll.IAcadApplication), _ez_ptr):
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
        #app.sink = sink
        #if app.sink is not None:
        #    app.events = GetEvents(app, sink, _dll._DAcadApplicationEvents)
        return app

    #VBA-parsed method TODO: add recast
    def eval(self, Expression: str):
        """Evaluates an expression in VBA"""
        self.com_parent.Eval(Expression)
    def getacadstate(self):
        """Retrieves an AcadState object."""
        return CastManager.cast(self.com_parent.GetAcadState())
    def getinterfaceobject(self, ProgID: str):
        """Accepts a program ID and attempts to load it into AutoCAD as an in-process server"""
        return CastManager.cast(self.com_parent.GetInterfaceObject(ProgID))
    def listarx(self):
        """Gets the currently loaded AutoCAD ARX applications"""
        return CastManager.cast(self.com_parent.ListArx())
    def loadarx(self, Name: str):
        """Loads the specified AutoCAD ARX applicationUnloadArx"""
        self.com_parent.LoadArx(Name)
    def loaddvb(self, Name: str):
        """Loads the specified AutoCAD VBA project file"""
        self.com_parent.LoadDVB(Name)
    def quit(self):
        """Closes the drawing file and exits the AutoCAD application"""
        self.com_parent.Quit()
    def runmacro(self, MacroPath: str):
        """Runs a VBA macro from the Application object"""
        self.com_parent.RunMacro(MacroPath)
    def unloadarx(self, Name: str):
        """Unloads the specified AutoCAD ARX application"""
        self.com_parent.UnloadArx(Name)
    def unloaddvb(self, Name: str):
        """Unloads the specified AutoCAD VBA project file"""
        self.com_parent.UnloadDVB(Name)
    def Update(self):
        """Updates the object to the drawing screen"""
        self.com_parent.Update()
    #def _IAcadApplication__com_Zoom
    def ZoomAll(self):
        """Zooms the current viewport to display the entire drawing"""
        self.com_parent.ZoomAll()
    def ZoomCenter(self, Center: A3Vertex, Magnify: float):
        """Zooms the current viewport to a specified center point and magnification"""
        self.com_parent.ZoomCenter(Center, Magnify)
    def ZoomExtents(self):
        """Zooms the current viewport to the drawing extents"""
        self.com_parent.ZoomExtents()
    def ZoomPickWindow(self):
        """Zooms the current viewport to a window defined by points picked on the screen"""
        self.com_parent.ZoomPickWindow()
    def ZoomPrevious(self):
        """Zooms the current viewport to its previous extents"""
        self.com_parent.ZoomPrevious()
    def ZoomScaled(self, scale: float, ScaleType: AcZoomScaleType):
        """Zooms the current viewport to given scale factor"""
        self.com_parent.ZoomScaled(scale, ScaleType.value)
    def ZoomWindow(self, LowerLeft: A3Vertex, UpperRight: A3Vertex):#LowerLeft, UpperRight as A3Vertex
        """Zooms the current viewport to the area specified by two opposite corners of a rectangle"""
        self.com_parent.ZoomWindow(LowerLeft, UpperRight)

    # VBA-properties TODO: add recast
    @property
    def activedocument(self):
        "Specifies the active document (drawing file)"
        return CastManager.cast(self.com_parent.ActiveDocument)
    @activedocument.setter
    def _(self, value: AcadDocument):
        self.com_parent.ActiveDocument = value
    @property
    def application(self):
        "Gets the Application object"
        return CastManager.cast(self.com_parent.Application)
    
    @property
    def caption(self):
        "Gets the text that the user sees displayed for the application or a menu item"
        return self.com_parent.Caption

    @property
    def documents(self):
        "Returns the documents collection."
        return CastManager.cast(self.com_parent.Documents)

    @property
    def fullname(self):
        "Gets the name of the application or document, including the path"
        return self.com_parent.FullName
    
    @property
    def height(self):
        "Height of the attribute, shape, text, or view toolbar or the main application window"
        return self.com_parent.Height
    @height.setter
    def _(self, value: int):
        self.com_parent.Height = value

    @property
    def hwnd(self):
        "Gets the window handle of the application window frame"
        return self.com_parent.HWND

    @property
    def localeid(self):
        "Gets the locale ID of the current AutoCAD session"
        return self.com_parent.LocaleId
    
    @property
    def menubar(self):
        "Gets the MenuBar object for the session"
        return CastManager.cast(self.com_parent.MenuBar)
    
    @property
    def menugroups(self):
        "Gets the MenuGroups collection for the session"
        return CastManager.cast(self.com_parent.MenuGroups)
    
    @property
    def name(self):
        "Specifies the name of the object"
        return self.com_parent.Name
    
    @property
    def path(self):
        "Gets the path of the document, application, or external reference"
        return self.com_parent.Path
    
    @property
    def preferences(self):
        "Gets the Preferences object"
        return CastManager.cast(self.com_parent.Preferences)
    
    @property
    def statusid(self, VportObj):
        "Gets the current active status of the viewport"
        return self.com_parent.StatusId[VportObj]
    
    @property
    def vbe(self):
        "Gets the VBAIDE extensibility object"
        return CastManager.cast(self.com_parent.VBE)
    
    @property
    def version(self):
        "Gets the version of the AutoCAD application you are using"
        return self.com_parent.Version
    
    @property
    def visible(self):
        "Specifies the visibility of an object or the application"
        return self.com_parent.Visible
    @visible.setter
    def _(self, value: bool):
        self.com_parent.Visible = value
    
    @property
    def width(self):
        "Specifies the width of the text boundary, view, image, toolbar, or main application window"
        return self.com_parent.Width
    @width.setter
    def _(self, value: int):
        self.com_parent.Width = value
    
    @property
    def windowleft(self):
        "Specifies the left edge of the application window"
        return self.com_parent.WindowLeft
    @windowleft.setter
    def _(self, value: int):
        self.com_parent.WindowLeft = value
    
    @property
    def windowstate(self):
        "Specifies the state of the application or document window"
        return self.com_parent.WindowState
    @windowstate.setter
    def _(self, value: AcWindowState):
        self.com_parent.WindowState = value.value
    
    @property
    def windowtop(self):
        "Specifies the top edge of the application window"
        return self.com_parent.WindowTop
    @windowtop.setter
    def _(self, value: int):
        self.com_parent.WindowTop = value


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

# for debugging
if __name__ == "__main__":
	app = AcadApplication()
	'''
    import pyperclip
    class Method(dict):
        def __str__(self):
            return f"\tdef {self['name'].lower()}(self, ___):\n\t\t'{self['desc']}'\n\t\tself.com_parent.{self['name']}(___)\n"
        __repr__ = __str__
    class Prop(dict):
        def __str__(self):
            data = ""
            if 'getter' in self.keys():
                data += f"\t@property\n\tdef {self['name'].lower()}(self):\n\t\t'{self['desc']}'\n\t\treturn self.com_parent.{self['name']}"
            if 'setter' in self.keys():
                if 'getter' in self.keys():
                    data += f"\n\t@{self['name'].lower()}.setter\n\tdef _(self, value):\n\t\tself.com_parent.{self['name']} = value"
                else:
                    data += f"\t@{self['name'].lower()}.setter\n\tdef _(self, value):\n\t\t'{self['desc']}'\n\t\tself.com_parent.{self['name']} = value"
            data += "\n"
            return data
        __repr__ = __str__
    def write(name):
        pyperclip.copy(name) #Копирует в буфер обмена информацию
        pyperclip.paste()
                
    
    def get_method_type(o):
        for i, obj2 in enumerate(obj):
            if i == 1:
                if str(obj2).startswith("_get_"):
                    return 1
                if str(obj2).startswith("_set_"):
                    return 2
                return 0
    def is_method(o):
        return get_method_type(o) == 0
    def is_get(o):
        return get_method_type(o) == 1
    def is_set(o):
        return get_method_type(o) == 2
    def get_name(o):
        for i, obj2 in enumerate(obj):
            if i == 1:
                return str(obj2).replace("_get_", "").replace("_set_", "")
    def get_desc(o):
        for i, obj2 in enumerate(obj):
            if i == 5:
                return str(obj2)
    
    
    data = ""
    objs = {}
    for obj in _dll.IAcadPolyfaceMesh._methods_:
        if get_name(obj) not in objs.keys():
            if is_method(obj):
                d = Method()
                d['name'] = get_name(obj)
                d['desc'] = get_desc(obj)
                objs[get_name(obj)] = d
            elif is_get(obj):
                d = Prop()
                d['getter'] = True
                d['name'] = get_name(obj)
                d['desc'] = get_desc(obj)
                objs[get_name(obj)] = d
            elif is_set(obj):
                d = Prop()
                d['setter'] = True
                d['name'] = get_name(obj)
                d['desc'] = get_desc(obj)
                objs[get_name(obj)] = d
        else:
            if is_get(obj):
                objs[get_name(obj)]['getter'] = True
            elif is_set(obj):
                objs[get_name(obj)]['setter'] = True

    props = []
    methods = []
    for k, v in objs.items():
        if type(v) == Method:
            methods.append(k)
        else:
            props.append(k)
    methods.sort()
    props.sort()
    #print(m_keys, p_keys)
    data = ""
    for k in methods:
        #print(objs[k])
        data += str(objs[k]) + "\n"
    for k in props:
        #print(objs[k])
        data += str(objs[k]) + "\n"
    write(data)
	'''
    
    
