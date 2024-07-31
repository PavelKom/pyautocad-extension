from comtypes import POINTER, BSTR, IUnknown
from comtypes.automation import IDispatch, VARIANT
from comtypes.client import GetEvents, ShowEvents
from comtypes.client import GetModule, CreateObject, GetActiveObject
from comtypes.client.dynamic import Dispatch
from pythoncom import Nothing, Empty

import numpy as np
import ctypes
import comtypes

from enums import *
from stubs import *
#from geometry import *
from event_sink import _AcadEventDumper
from utils import dict_fix, _ez_ptr, CastManager, list_to_ptr_arr #TODO: util -> .util
from api import acad_dll #TODO: api -> .api
_dll = acad_dll.dll

class AcadDatabase(POINTER(_dll.IAcadDatabase), _ez_ptr):
    # VBA-methods TODO: add recast
    def copyobjects(self, Objects: (list, tuple), Owner=None, IDPairs=None): # Objects  as Variant (array of Objects); Owner as Variant (a single object); IDPairs as Variant (array of IDPair objects):
        """
        Duplicates multiple objects (deep cloning)
        !!!IT'S BROKEN!!! VARIANT Objects not working
        """
        # VBA
        # Dim objCollection(0 To 1) As Object <- How to make this in Python?
        # Dim retObjects As Variant
        # ...
        # retObjects = Me.CopyObjects(objCollection)
        
        #o = VARIANT()
        #for i, val in enumerate(Objects):
            
        #    o[i] = VARIANT(val)
        #print(o)
        #ctypes.cast(o, ctypes.POINTER(VARIANT))
        #arr = self.CopyObjects(o)
        return None
    def handletoobject(self, Handle: str):
        """Gets the object that corresponds to the given handle"""
        return CastManager.cast(self.com_parent.HandleToObject(Handle))
    def objectidtoobject(self, ObjectID):
        """Gets the object that corresponds to the given object ID"""
        return CastManager.cast(self.com_parent.ObjectIdToObject(ObjectID))

    # VBA-properties
    @property
    def blocks(self):
        "Gets the Blocks collection for the drawing"
        return CastManager.cast(self.com_parent.Blocks)
        
    @property
    def dictionaries(self):
        "Gets the Dictionaries collection for the document"
        return CastManager.cast(self.com_parent.Dictionaries)
        
    @property
    def dimstyles(self):
        "Gets the DimStyles collection for the document"
        return CastManager.cast(self.com_parent.DimStyles)
        
    @property
    def elevationmodelspace(self):
        "Specifies the elevation setting in the model space"
        return self.com_parent.ElevationModelSpace
    @elevationmodelspace.setter
    def _(self, value: float):
        self.com_parent.ElevationModelSpace = value
    @property
    def elevationpaperspace(self):
        "Specifies the elevation setting in the paper space"
        return self.com_parent.ElevationPaperSpace
    @elevationpaperspace.setter
    def _(self, value: float):
        self.com_parent.ElevationPaperSpace = value
    
    @property
    def groups(self):
        "Gets the Groups collection for the document"
        return CastManager.cast(self.com_parent.Groups)
    
    @property
    def layers(self):
        "Gets the Layers collection for the document"
        return CastManager.cast(self.com_parent.Layers)
    
    @property
    def layouts(self):
        "Gets the Layouts collection for the document"
        return CastManager.cast(self.com_parent.Layouts)
    
    @property
    def limits(self): # -> F4Vector:
        "Specifies the drawing limits"
        return self.com_parent.Limits
    @limits.setter
    def _(self, value): # value is F4Vector
        self.com_parent.Limits = value
    
    @property
    def linetypes(self):
        "Gets the Linetypes collection for the document"
        return CastManager.cast(self.com_parent.Linetypes)
    
    @property
    def materials(self):
        "Gets the Materials collection for the document"
        return CastManager.cast(self.com_parent.Materials)
    
    @property
    def modelspace(self):
        "Gets the ModelSpace collection for the document"
        return CastManager.cast(self.com_parent.ModelSpace)
    
    @property
    def paperspace(self):
        "Gets the PaperSpace collection for the document"
        return CastManager.cast(self.com_parent.PaperSpace)
    
    @property
    def plotconfigurations(self):
        "Gets the PlotConfigurations collection for the document"
        return CastManager.cast(self.com_parent.PlotConfigurations)
    
    @property
    def preferences(self):
        "Gets the Preferences object"
        return CastManager.cast(self.com_parent.Preferences)
    
    @property
    def registeredapplications(self):
        "The collection of all registered applications in the drawing"
        return CastManager.cast(self.com_parent.RegisteredApplications)
    
    @property
    def sectionmanager(self):
        "Returns the section manager object."
        return CastManager.cast(self.com_parent.SectionManager)
    
    @property
    def summaryinfo(self):
        "Returns the summary info object."
        return CastManager.cast(self.com_parent.SummaryInfo)
    
    @property
    def textstyles(self):
        "Gets the TextStyles collection for the document"
        return CastManager.cast(self.com_parent.TextStyles)
    
    @property
    def usercoordinatesystems(self):
        "Gets the UCSs collection for the document"
        return CastManager.cast(self.com_parent.UserCoordinateSystems)
    
    @property
    def viewports(self):
        "Gets the Viewports collection for the document"
        return CastManager.cast(self.com_parent.Viewports)
    
    @property
    def views(self):
        "Gets the Views collection for the document"
        return CastManager.cast(self.com_parent.Views)

 
#TODO: add __new__
class AcadDocument(POINTER(_dll.IAcadDocument), _ez_ptr): #AcadDocument(AcadDatabase)
    def __new__(cls, TemplateFileName: str=None, source=None):
        from app import AcadApplication
        if source is None:
            source = AcadApplication()
        if isinstance(source, AcadApplication):
            source = source.Documents
        return source.add(TemplateFileName)
            
    # AcadDatabase inherits methods
    copyobjects = AcadDatabase.copyobjects
    handletoobject = AcadDatabase.handletoobject
    objectidtoobject = AcadDatabase.objectidtoobject
    # AcadDatabase inherits props
    blocks = AcadDatabase.blocks
    dictionaries = AcadDatabase.dictionaries
    dimstyles = AcadDatabase.dimstyles
    elevationmodelspace = AcadDatabase.elevationmodelspace
    elevationpaperspace = AcadDatabase.elevationpaperspace
    groups = AcadDatabase.groups
    layers = AcadDatabase.layers
    layouts = AcadDatabase.layouts
    limits = AcadDatabase.limits
    linetypes = AcadDatabase.linetypes
    materials = AcadDatabase.materials
    modelspace = AcadDatabase.modelspace
    paperspace = AcadDatabase.paperspace
    plotconfigurations = AcadDatabase.plotconfigurations
    preferences = AcadDatabase.preferences
    registeredapplications = AcadDatabase.registeredapplications
    sectionmanager = AcadDatabase.sectionmanager
    summaryinfo = AcadDatabase.summaryinfo
    textstyles = AcadDatabase.textstyles
    usercoordinatesystems = AcadDatabase.usercoordinatesystems
    viewports = AcadDatabase.viewports
    views = AcadDatabase.views
    

    # VBA-methods
    def activate(self):
        """Makes the specified drawing active"""
        self.com_parent.Activate()
    def auditinfo(self, FixErr: bool):
        """Evaluates the integrity of the drawing"""
        self.com_parent.AuditInfo(FixErr)
    def close(self, SaveChanges: bool=None, FileName: str=None):
        """Closes the specified drawing, or all open drawings"""
        self.__close_me__(SaveChanges, FileName)
    def __close_me__(self, **kw):
        dict_fix(kw)
        self.com_parent.Close(kw)
    def endundomark(self):
        """Marks the end of a block of operations"""
        self.com_parent.EndUndoMark()
    def export(self, FileName: str, Extension: str, SelectionSet: int): # SelectionSet As AcadSelectionSet
        """Exports the AutoCAD drawing to a WMF, SAT, EPS, DXF, or BMP format"""
        self.com_parent.Export(FileName, Extension, SelectionSet)
    def getvariable(Name: str):
        """Gets the current setting of an AutoCAD system variable"""
        return CastManager.cast(self.com_parent.GetVariable(Name))
    def import_(self, FileName: str, InsertionPoint, ScaleFactor: float): # TODO: fix this? InsertionPoint as A3Point
        """Imports a drawing file in SAT, EPS, DXF, or WMF format"""
        self.com_parent.Import(FileName, InsertionPoint, ScaleFactor)
    def loadshapefile(self, FullName: str):
        """Loads a shape file (SHX)"""
        self.com_parent.LoadShapeFile(FullName)
    def new(self, TemplateFileName: str): # It's not a classmethod!!!
        """Creates a new document in SDI mode"""
        return CastManager.cast(self.com_parent.New(TemplateFileName))
    def open(self, FullName: str, ReadOnly: bool, Password=None):
        """Opens an existing drawing file (DWG) and makes it the active document"""
        return self.__open_doc__(FullName, ReadOnly, Password)
    def __open_doc__(self, **kw):
        dict_fix(kw)
        return CastManager.cast(self.com_parent.Open(**kw))
    def postcommand(self, Command: str):
        """Posts a command string from a VB or VBA application to the document for processing"""
        self.com_parent.PostCommand(Command)
    def purgeall(self):
        """Removes unused named references such as unused blocks or layers from the document"""
        self.com_parent.PurgeAll()
    def regen(self, WhichViewports: int): # WhichViewports As AcRegenType
        """Regenerates the entire drawing and recomputes the screen coordinates and view resolution for all objects"""
        self.com_parent.Regen()
    def save(self):
        """Saves the document or menu group"""
        self.com_parent.Save()
    def saveas(self, FullFileName: str, SaveAsType:AcSaveAsType=None, vSecurityParams=None): # SaveAsType as AcSaveAsType; vSecurityParams as Variant (a SecurityParams object)
        """Saves the document or menu group to a specified file"""
        self.__save_as__(FullFileName, SaveAsType.value, vSecurityParams)
    def __save_as__(self, **kw):
        dict_fix(kw)
        self.com_parent.SaveAs(**kw)
    def sendcommand(self, Command: str):
        """Sends a command string from a VB or VBA application to the document for processing"""
        self.com_parent.SendCommand(Command)
    def setvariable(self, Name: str, Value):
        """Sets the value of an AutoCAD system variable"""
        self.com_parent.SetVariable(Name, Value)
    def startundomark(self):
        """Marks the beginning of a block of operations"""
        self.com_parent.StartUndoMark()
    def wblock(self, FileName: str, SelectionSet: AcadSelectionSet):
        """Writes out the given selection set as a new drawing file"""
        self.com_parent.Wblock(FileName, SelectionSet)

    # VBA-properties
    @property
    def active(self):
        "Determines if the document is the active document for the session"
        return self.com_parent.Active
    
    @property
    def activedimstyle(self):
        "Specifies the active dimension style"
        return CastManager.cast(self.com_parent.ActiveDimStyle)
    @activedimstyle.setter
    def _(self, value: AcadDimStyle):
        self.com_parent.ActiveDimStyle = value
    
    @property
    def activelayer(self):
        "Specifies the active layer"
        return CastManager.cast(self.com_parent.ActiveLayer)
    @activelayer.setter
    def _(self, value: AcadLayer):
        self.com_parent.ActiveLayer = value
    
    @property
    def activelayout(self):
        "Specifies the active layout"
        return CastManager.cast(self.com_parent.ActiveLayout)
    @activelayout.setter
    def _(self, value: AcadLayout):
        self.com_parent.ActiveLayout = value
    
    @property
    def activelinetype(self):
        "Specifies the active linetype for the drawing"
        return CastManager.cast(self.com_parent.ActiveLinetype)
    @activelinetype.setter
    def _(self, value: AcadLineType):
        self.com_parent.ActiveLinetype = value
    
    @property
    def activematerial(self):
        "Specifies the active material"
        return CastManager.cast(self.com_parent.ActiveMaterial)
    @activematerial.setter
    def _(self, value: AcadMaterial):
        self.com_parent.ActiveMaterial = value
    
    @property
    def activepviewport(self):
        "Specifies the active paper space viewport for the drawing"
        return CastManager.cast(self.com_parent.ActivePViewport)
    @activepviewport.setter
    def _(self, value):
        self.com_parent.ActivePViewport = value
    
    @property
    def activeselectionset(self):
        "Gets the active selection set for the drawing"
        return CastManager.cast(self.com_parent.ActiveSelectionSet)
    
    @property
    def activespace(self):
        "Toggles the active space between paper space and model space"
        return AcActiveSpace(self.com_parent.ActiveSpace)
    @activespace.setter
    def _(self, value: AcActiveSpace):
        self.com_parent.ActiveSpace = value.value
    
    @property
    def activetextstyle(self):
        "Specifies the active text style for the drawing"
        return CastManager.cast(self.com_parent.ActiveTextStyle)
    @activetextstyle.setter
    def _(self, value: AcadTextStyle):
        self.com_parent.ActiveTextStyle = value
    
    @property
    def activeucs(self):
        "Specifies the active UCS for the drawing"
        return CastManager.cast(self.com_parent.ActiveUCS)
    @activeucs.setter
    def _(self, value: AcadUCS):
        self.com_parent.ActiveUCS = value
    
    @property
    def activeviewport(self):
        "Specifies the active viewport for the drawing"
        return CastManager.cast(self.com_parent.ActiveViewport)
    @activeviewport.setter
    def _(self, value: AcadViewport):
        self.com_parent.ActiveViewport = value
    
    #from app import AcadApplication
    @property
    def application(self):# -> app.AcadApplication:
        "Gets the Application object"
        return CastManager.cast(self.com_parent.Application)
    
    @property
    def database(self):
        "Gets the database in which the object belongs"
        return CastManager.cast(self.com_parent.Database)
    
    @property
    def fullname(self):
        "Gets the name of the application or document, including the path"
        return self.com_parent.FullName
    
    @property
    def hwnd(self):
        "Gets the window handle of the document window frame"
        return self.com_parent.HWND
    
    @property
    def height(self):
        "Height of the attribute, shape, text, or view toolbar or the main application window"
        return self.com_parent.Height
    @height.setter
    def _(self, value: int):
        self.com_parent.Height = value
    
    @property
    def mspace(self):
        "Allows editing of the model from floating paper space viewports"
        return self.com_parent.MSpace
    @mspace.setter
    def _(self, value: bool):
        self.com_parent.MSpace = value
    
    @property
    def name(self):
        "Specifies the name of the object"
        return self.com_parent.Name
    
    @property
    def objectsnapmode(self):
        "Specifies the setting of the object snap mode"
        return self.com_parent.ObjectSnapMode
    @objectsnapmode.setter
    def _(self, value: bool):
        self.com_parent.ObjectSnapMode = value
    
    @property
    def path(self):
        "Gets the path of the document, application, or external reference"
        return self.com_parent.Path
    
    @property
    def pickfirstselectionset(self):
        "Gets the pickfirst selection set"
        return CastManager.cast(self.com_parent.PickfirstSelectionSet)
    
    @property
    def plot(self):
        "Gets the Plot object for the document"
        return CastManager.cast(self.com_parent.Plot)
    
    @property
    def readonly(self):
        "Specifies if the document is read-only or read-write"
        return self.com_parent.ReadOnly
    
    @property
    def saved(self):
        "Specifies if the document has any unsaved changes"
        return self.com_parent.Saved
    
    @property
    def selectionsets(self):
        "Gets the SelectionSets collection for the document"
        return CastManager.cast(self.com_parent.SelectionSets)
    
    @property
    def utility(self):
        "Gets the Utility object for the document"
        return CastManager.cast(self.com_parent.Utility)
    
    @property
    def width(self):
        "Specifies the width of the text boundary, view, image, toolbar, or main application window"
        return self.com_parent.Width
    @width.setter
    def _(self, value: int):
        self.com_parent.Width= value
    
    @property
    def windowstate(self):
        "Specifies the state of the application or document window"
        return AcWindowState(self.com_parent.WindowState)
    @windowstate.setter
    def _(self, value: AcWindowState):
        self.com_parent.WindowState= value.value
    
    @property
    def windowtitle(self):
        "Gets the title of the document window"
        return self.com_parent.WindowTitle


class AcadDocuments(POINTER(_dll.IAcadDocuments), _ez_ptr):
    def add(self, TemplateName: str=None):
        """Creates a member object and adds it to the appropriate collection"""
        return self.__add_doc__(TemplateName=TemplateName)
    def __add_doc__(self, **kw):
        dict_fix(kw)
        return CastManager.cast(self.com_parent.Add(**kw))
    def close(self):
        """Closes the specified drawing, or all open drawings"""
        self.com_parent.Close()
    def item(self, Index: int):
        """Gets the member object at a given index in a collection, group, or selection set"""
        return CastManager.cast(self.com_parent.Item(Index))
    def open(self, Name:str, ReadOnly=None, Password=None):
        """Opens an existing drawing file (DWG) and makes it the active document"""
        return self.__open_doc__(Name, ReadOnly, Password)
    def __open_doc__(self, **kw):
        dict_fix(kw)
        return self.com_parent.Open(**kw)
    @property
    def application(self):# -> app.AcadApplication:
        "Gets the Application object"
        return CastManager.cast(self.com_parent.Application)
        
    @property
    def count(self):
        "Gets the number of items in the collection, dictionary, group, or selection set"
        return self.com_parent.Count
        
    # _IAcadDocuments__com__get__NewEnum - iterator


__all__ = ('AcadDatabase',
           'AcadDocument',
           'AcadDocuments',
           )

# for debugging
if __name__ == "__main__":
    from app import AcadApplication
    a = AcadApplication()
    doc = a.activedocument
    objs = GetBestInterface(doc.ModelSpace[0])
    print(objs)
    



    
