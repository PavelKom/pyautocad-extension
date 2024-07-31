from comtypes import POINTER
from utils import _ez_ptr, CastManager
from api import acad_dll
from enums import AcExtendOption, AcColor, AcLineWeight
_dll = acad_dll.dll


class AcadObject(POINTER(_dll.IAcadObject), _ez_ptr):
    def delete(self):
        "Deletes a specified object"
        self.com_parent.Delete()
    def erase(self): # HIDDEN
        "Erases all the objects in a selection set"
        self.com_parent.Erase()
    def getextensiondictionary(self):
        "Gets the extension dictionary associated with an object"
        return CastManager.cast(self.com_parent.GetExtensionDictionary())
    def getxdata(self, AppName: str, XDataType: list=None, XDataValue: list=None):
        "Gets the extended data (XData) associated with an object"
        XDataType = [] if XDataType is None else XDataType
        XDataValue = [] if XDataValue is None else XDataValue
        self.com_parent.GetXData(AppName, XDataType, XDataValue)
        return XDataType, XDataValue
    def setxdata(self, XDataType: list, XDataValue: list):
        self.com_parent.SetXData(XDataType, XDataValue)
    
    @property
    def application(self):
        "Gets the Application object"
        return CastManager.cast(self.com_parent.Application)
    @property
    def database(self): #Hidden
        "Gets the database in which the object belongs"
        return CastManager.cast(self.com_parent.Database)
    @property
    def document(self):
        "Gets the document (drawing) in which the object belongs"
        return CastManager.cast(self.com_parent.Document)
    @property
    def handle(self):
        "Gets the handle of an object"
        return self.com_parent.Handle
    @property
    def hasextensiondictionary(self):
        "Determines if the object has an extension dictionary associated with it"
        return self.com_parent.HasExtensionDictionary
    @property
    def objectid(self):
        "Gets the object ID of the object"
        return self.com_parent.ObjectID
    @property
    def objectname(self):
        "Gets the AutoCAD class name of the object"
        return self.com_parent.ObjectName
    @property
    def ownerid(self):
        "Gets the object ID of the owner (parent) object"
        return self.com_parent.OwnerID


class AcadObjectEvents(POINTER(_dll.IAcadObjectEvents), _ez_ptr):
    def _IAcadObjectEvents__com_Modified(self, entity):
        pass


class AcadEntity(POINTER(_dll.IAcadEntity), _ez_ptr):
    def arraypolar(self, NumberOfObjects, AngleToFill, CenterPoint):
        'Creates an array of selected objects in a polar pattern.'
        res = []
        for obj in self.com_parent.ArrayPolar(NumberOfObjects, AngleToFill, CenterPoint):
            res.append(CastManager.cast(obj))
        return res
    def arrayrectangular(self, NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenCols, DistBetweenLevels):
        'Creates an array of selected objects in a rectangular pattern.'
        res = []
        for obj in self.com_parent.ArrayRectangular(NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenCols, DistBetweenLevels):
            res.append(CastManager.cast(obj))
        return res
    def copy(self):
        'Copies the entity object.'
        return CastManager.cast(self.com_parent.Copy())
    def getboundingbox(self):
        return self.com_parent.GetBoundingBox()
    def highlight(self, HighlightFlag):
        'Highlights the entity object.'
        self.com_parent.Highlight(HighlightFlag)
    def intersectwith(self, IntersectObject, option: AcExtendOption):
        'Intersects with the input entity object.'
        return self.com_parent.IntersectWith(IntersectObject, option.value)
    def mirror(self, Point1, Point2):
        'Mirrors selected objects about a line.'
        return CastManager.cast(self.com_parent.Mirror(Point1, Point2))
    def mirror3d(self, Point1, Point2, point3):
        'Mirrors selected objects about a plane defined by three points.'
        return CastManager.cast(self.com_parent.Mirror3D(Point1, Point2, point3))
    def move(self, FromPoint, ToPoint):
        'Moves the entity object from source to destination.'
        self.com_parent.Move(FromPoint, ToPoint)
    def rotate(self, BasePoint, RotationAngle):
        'Rotates the entity object about a point.'
        self.com_parent.Rotate(BasePoint, RotationAngle)
    def rotate3d(self, Point1, Point2, RotationAngle):
        'Rotates the entity object about a 3D line.'
        self.com_parent.Rotate3D(Point1, Point2, RotationAngle)
    def scaleentity(self, BasePoint, ScaleFactor):
        'Scale the entity object with respect to the base point and the scale factor.'
        self.com_parent.ScaleEntity(BasePoint, ScaleFactor)
    def transformby(self, TransformationMatrix):
        'Performs the specified transformation on the entity object.'
        self.com_parent.TransformBy(TransformationMatrix)
    def update(self):
        self.com_parent.Update()
    
    # VBA properties
    @property
    def entityname(self):
        'Returns the class name of the object.'
        return self.com_parent.EntityName
        
    @property
    def entitytransparency(self):
        'Specifies the transparency of the object'
        return self.com_parent.EntityTransparency
    @entitytransparency.setter
    def _(self, value: str):
        self.com_parent.EntityTransparency = value
        
    @property
    def entitytype(self):
        'Returns the entity type of the object as an integer.'
        return self.com_parent.EntityType
        
    @property
    def hyperlinks(self):
        'Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)'
        return self.com_parent.Hyperlinks
        
    @property
    def layer(self):
        'Specifies the current layer of the object'
        return self.com_parent.Layer
    @layer.setter
    def _(self, value: str):
        self.com_parent.Layer = value
        
    @property
    def linetype(self):
        'Specifies the current linetype of the object'
        return self.com_parent.Linetype
    @linetype.setter
    def _(self, value: str):
        self.com_parent.Linetype = value
        
    @property
    def linetypescale(self):
        'Specifies the linetype scale factor of the object'
        return self.com_parent.LinetypeScale
    @linetypescale.setter
    def _(self, value: float):
        self.com_parent.LinetypeScale = value
        
    @property
    def lineweight(self):
        'Specifies the lineweight for the object'
        return AcLineWeight(self.com_parent.Lineweight)
    @lineweight.setter
    def _(self, value: AcLineWeight):
        self.com_parent.Lineweight = value.value
        
    @property
    def material(self):
        'Specifies the material'
        return self.com_parent.Material
    @material.setter
    def _(self, value: str):
        self.com_parent.Material = value
        
    @property
    def plotstylename(self):
        'Specifies the plotstyle name for the object'
        return self.com_parent.PlotStyleName
    @plotstylename.setter
    def _(self, value: str):
        self.com_parent.PlotStyleName = value
        
    @property
    def truecolor(self):
        'Returns the true color of the object.'
        return CastManager.cast(self.com_parent.TrueColor)
    @truecolor.setter
    def _(self, value):
        self.com_parent.TrueColor = value
        
    @property
    def visible(self):
        'Specifies the visibility of an object or the application'
        return self.com_parent.Visible
    @visible.setter
    def _(self, value: bool):
        self.com_parent.Visible = value
        
    @property
    def color(self):
        'Specifies the color for objects'
        return AcColor(self.com_parent.color)
    @color.setter
    def _(self, value: AcColor):
        self.com_parent.color = value.value

    delete = AcadObject.delete
    erase = AcadObject.erase
    getextensiondictionary = AcadObject.getextensiondictionary
    getxdata = AcadObject.getxdata
    setxdata = AcadObject.setxdata
    application = AcadObject.application
    database = AcadObject.database
    document = AcadObject.document
    handle = AcadObject.handle
    hasextensiondictionary = AcadObject.hasextensiondictionary
    objectid = AcadObject.objectid
    objectname = AcadObject.objectname
    ownerid = AcadObject.ownerid

