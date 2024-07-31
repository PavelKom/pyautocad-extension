from comtypes import POINTER
from comtypes.automation import VARIANT
from indexedproperty import indexedproperty
from ctypes.wintypes import VARIANT_BOOL
from ctypes import c_int
from pyautocad import 

from .utils import _ez_ptr, CastManager, SetterProperty
from .utils import A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
from .api import acad_dll
from .enums import (
    Ac3DPolylineType,
    AcBooleanType,
    AcAlignment,
    AcHorizontalAlignment,
    AcDrawingDirection,
    AcVerticalAlignment,
    AcColor,
    AcDimTextMovement,
    AcDimToleranceMethod,
    AcDimToleranceJustify,
    AcDimPrecision,
    AcDimVerticalJustification,
    )
from .objects import AcadEntity
_dll = acad_dll.dll

def __get_source(source):
    from app import AcadApplication
    if source is None:
        source = AcadApplication()
    if isinstance(source, AcadApplication):
        source = source.ModelSpace
    return source

'''
TODO list:
    1. Add all geometry entities
    2. Convert tagVARIANT and other COM-types to python-types
    3. Add support for ByRef inputs/outputs for classes
    4. Tests
'''



class Acad3DFace(POINTER(_dll.IAcad3DFace), _ez_ptr):
    def __new__(self, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex, Point4: A3Vertex, source=None):
        return __get_source(source).add3dface(Point1, Point2, Point3, Point4)
    def getinvisibleedge(self, Index: int) -> bool:
		"Gets the visibility status for the edge."
        # ('in',) Index:int
        # ('out', 'retval') bVisible:bool
        # VBA: bVisible = object.GetInvisibleEdge (Index)
        return self.com_parent.GetInvisibleEdge(Index)
    def SetInvisibleEdge(self, Index: int, State: bool):
		"Sets the visibility of the edge."
		# ('in',) Index:int
		# ('in',) State:bool
		# VBA: object.SetInvisibleEdge Index, State
        self.com_parent.SetInvisibleEdge(Index, State)
        
    @indexedproperty
    def coordinate(self, index: int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
        return A3Vertex(self.com_parent.Coordinate[index])
    @coordinate.setter
    def _(self, index: int, value: A3Vertex):
        self.com_parent.Coordinate[index] = value
    
    @property
    def coordinates(self) -> A3Vertexes:
        return A3Vertexes(self.com_parent.Coordinates)
    @coordinates.setter
    def _(self, value: A3Vertexes):
        self.com_parent.Coordinates = value.flatted
    
    @property
    def visibilityedge1(self) -> bool:
        return self.com_parent.VisibilityEdge1
    @visibilityedge1.setter
    def _(self, value:bool):
        self.com_parent.VisibilityEdge1 = value
    
    @property
    def visibilityedge2(self) -> bool:
        return self.com_parent.VisibilityEdge2
    @visibilityedge2.setter
    def _(self, value:bool):
        self.com_parent.VisibilityEdge2 = value
    
    @property
    def visibilityedge3(self) -> bool:
        return self.com_parent.VisibilityEdge3
    @visibilityedge3.setter
    def _(self, value:bool):
        self.com_parent.VisibilityEdge3 = value
    
    @property
    def visibilityedge4(self) -> bool:
        return self.com_parent.VisibilityEdge4
    @visibilityedge4.setter
    def _(self, value:bool):
        self.com_parent.VisibilityEdge4 = value
    
    # Bonus:
    # Get/set coordinate as array-like
    def __getitem__(self, index: int):
        return A3Vertex(self.coordinate[index])
    def __setitem__(self, index: int, value:A3Vertex):
        self.coordinate[index] = value
    # Get/set edge visibility func-like
    def __call__(self, index:int, value:bool=None):
        if value > 4 or value < 1:
            raise IndexError("[Acad3DFace] Allowd indexed 1-4 for vertexes")
        if value is not None:
            setattr(self, f"visibilityedge{index}", value)
        return getattr(self, f"visibilityedge{index}")

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class Acad3DPolyline(POINTER(_dll.IAcad3DPolyline), _ez_ptr):
    def __new__(cls, PointsArray, source=None):
        return __get_source(source).add3dpoly(PointsArray)
    def appendvertex(self, vertex:A3Vertex):
        'Appends a vertex to the 3dPolyline.'
        self.com_parent.AppendVertex(vertex)
    def explode(self):
        'Explodes the 3dPolyline.'
		# ('out', 'retval') pArrayObjs:list<AcadObject>
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret
    
    @property
    def closed(self) -> bool:
        'Determines whether the 3D polyline is open or closed'
        return self.com_parent.Closed
    @closed.setter
    def _(self, value: bool):
        self.com_parent.Closed = value
    
    @indexedproperty
    def coordinate(self, index: int) -> A3Vertex:
        'Specifies the coordinate of a single vertex in the object'
        return A3Vertex(self.com_parent.Coordinate[index])
    @coordinate.setter
    def _(self, index: int, value:A3Vertex):
        self.com_parent.Coordinate[index] = value
    
    @property
    def coordinates(self) -> A3Vertexes:
        'Specifies the current vertex of the 3D Polyline'
        return A3Vertexes(self.com_parent.Coordinates)
    @coordinates.setter
    def _(self, value:A3Vertexes):
        self.com_parent.Coordinates = value.flatted
    
    @property
    def length(self) -> float:
        'Specifies the length of the 3D polyline'
        return self.com_parent.Length
    
    @property
    def type(self):
        'Specifies the type of line or surface curve fitting'
        return Ac3DPolylineType(self.com_parent.Type)
    @type.setter
    def _(self, value:Ac3DPolylineType):
        self.com_parent.Type = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid

# TODO: add overloads
class Acad3DSolid(POINTER(_dll.IAcad3DSolid), _ez_ptr):
    def __new__(cls, *args, **kwargs):
        raise TypeError("[Acad3DSolid] Can't create raw Acad3DSolid. Use Acad3DSolid.%type%, where is the type \nbox, cone, cylinder, ellipticalcone, ellipticalcylinder, extrudedsolid, extrudedsolidalongpath, revolvedsolid, sphere, torus or wedge")
    @classmethod
    def box(cls, Origin:A3Vertex, Length:float, Width:float, Height:float, source=None):
        return __get_source(source).addbox(Origin:A3Vertex, Length, Width, Height)
    @classmethod
    def cone(cls, Center:A3Vertex, BaseRadius:float, Height:float, source=None):
        return __get_source(source).addcone(Center, BaseRadius, Height)
    @classmethod
    def cylinder(cls, Center:A3Vertex, Radius:float, Height:float, source=None):
        return __get_source(source).addcylinder(Center, Radius, Height)
    @classmethod
    def ellipticalcone(cls, Center:A3Vertex, MajorRadius:float, MinorRadius:float, Height:float, source=None):
        return __get_source(source).addellipticalcone(Center, MajorRadius, MinorRadius, Height)
    @classmethod
    def ellipticalcylinder(cls, Center:A3Vertex, MajorRadius:float, MinorRadius:float, Height:float, source=None):
        return __get_source(source).addellipticalcylinder(Center, MajorRadius, MinorRadius, Height)
    @classmethod
    def extrudedsolid(cls, Profile:AcadRegion, Height:float, TaperAngle:float, source=None):
        return __get_source(source).addextrudedsolid(Profile, Height, TaperAngle)
    @classmethod
    def extrudedsolidalongpath(cls, Profile:AcadRegion, Path: (AcadArc, AcadCircle, AcadEllipse, AcadPolyline, AcadSpline), source=None):
        return __get_source(source).addextrudedsolidalongpath(Profile, Path)
    @classmethod
    def revolvedsolid(cls, Profile:AcadRegion, AxisPoint:A3Vertex, AxisDir:A3Vertex, Angle:float, source=None):
        return __get_source(source).addrevolvedsolid(Profile, AxisPoint, AxisDir, Angle)
    @classmethod
    def sphere(cls, Center:A3Vertex, Radius:float, source=None):
        return __get_source(source).addsphere(Center, Radius)
    @classmethod
    def torus(cls, Center:A3Vertex, TorusRadius:float, TubeRadius:float, source=None):
        return __get_source(source).addtorus(Center, TorusRadius, TubeRadius)
    @classmethod
    def wedge(cls, Center:A3Vertex, Length:float, Width:float, Height:float, source=None):
        return __get_source(source).addwedge(Center, Length, Width, Height)

    def boolean(self, Operation: AcBooleanType, SolidObject: Acad3DSolid):
        'Performs a boolean operation against another 3dsolid.'
        self.com_parent.Boolean(Operation.value, SolidObject)
    def checkinterference(self, Object: Acad3DSolid, CreateInterferenceSolid: bool):
        'Check interference for the 3dsolid object.'
        # ('in',) Object:Acad3DSolid
		# ('in',) CreateInterferenceSolid:bool
		# ('out',) SolidsInterfere:bool
		# ('out', 'retval') pIntSolid:Acad3DSolid
        ret1, ret2 = self.com_parent.CheckInterference(Object, CreateInterferenceSolid)
        return ret1, CastManager.cast(ret2)
    def sectionsolid(self, Point1:A3Vertex, Point2:A3Vertex, Point3:A3Vertex):
        'Create a section of the 3dsolid given three points that define the plane. Returns the Section as a Region object'
        return CastManager.cast(self.com_parent.SectionSolid(Point1, Point2, Point3))
    def slicesolid(self, Point1:A3Vertex, Point2:A3Vertex, point3:A3Vertex, Negative: bool):
        'Create a slice of the 3dsolid given three points that define the plane. Returns the resulting array of 3dSolid object. '
        return CastManager.cast(self.com_parent.SliceSolid(Point1, Point2, point3, Negative))
    
    @property
    def centroid(self) -> A3Vertex:
        'Gets the center of area or mass for a region or solid'
        return A3Vertex(self.com_parent.Centroid)
    
    @property
    def history(self) -> bool:
        'Specifies whether history is saved'
        return self.com_parent.History
    @history.setter
    def _(self, value: bool):
        self.com_parent.History = value
    
    @property
    def momentofinertia(self) -> A3Vertex:
        'Gets the moment of inertia for the solid'
        return A3Vertex(self.com_parent.MomentOfInertia)
    
    @property
    def position(self) -> A3Vertex:
        'Specifies the X, Y, Z coordinate for center of the base or center of the solid'
        return A3Vertex(self.com_parent.Position)
    @position.setter
    def _(self, value: A3Vertex):
        self.com_parent.Position = value
    
    @property
    def principaldirections(self):
        'Gets the principal directions of the solid or region'
        return A3Vertex(self.com_parent.PrincipalDirections)
    
    @property
    def principalmoments(self):
        'Gets the principal moments property of the solid or region'
        return A3Vertex(self.com_parent.PrincipalMoments)
    
    @property
    def productofinertia(self):
        'Gets the product of inertia of the solid or region'
        return A3Vertex(self.com_parent.ProductOfInertia)
    
    @property
    def radiiofgyration(self):
        'Gets the radius of gyration of the solid or region'
        return A3Vertex(self.com_parent.RadiiOfGyration)
    
    @property
    def showhistory(self) -> bool:
        'Specifies whether to show history of the solid'
        return self.com_parent.ShowHistory
    @showhistory.setter
    def _(self, Position: bool):
        self.com_parent.ShowHistory = Position
    
    @property
    def solidtype(self) -> str:
        'Indicates the type of solid'
        return self.com_parent.SolidType
    
    @property
    def volume(self) -> float:
        'Gets the volume of the solid'
        return self.com_parent.Volume

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadArc(POINTER(_dll.IAcadArc), _ez_ptr):
    def __new__(cls, Center, Radius, StartAngle, EndAngle, source=None):
        return __get_source(source).addarc(Center, Radius, StartAngle, EndAngle)
    def offset(self, Distance: float):
        'Offsets the arc to the given side'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret
    
    @property
    def arclength(self) -> float:
        'Specifies the arc length of the arc'
        return self.com_parent.ArcLength
    
    @property
    def area(self) -> float:
        'Specifies the area of the arc when implicitly closed with a line'
        return self.com_parent.Area
    
    @property
    def center(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the center point of the arc or use the Pick Point button to set X, Y, Z values simultaneously'
        return A3Vertex(self.com_parent.Center)
    @center.setter
    def _(self, value: A3Vertex):
        self.com_parent.Center = value
    
    @property
    def endangle(self) -> float:
        'Specifies the end angle of the arc'
        return self.com_parent.EndAngle
    @endangle.setter
    def _(self, value: float):
        self.com_parent.EndAngle = value
    
    @property
    def endpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the end point of the arc'
        return A3Vertex(self.com_parent.EndPoint)
    
    @property
    def normal(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the normal direction vector'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value: A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def radius(self) -> float:
        'Specifies the radius of the arc'
        return self.com_parent.Radius
    @radius.setter
    def _(self, value: float):
        self.com_parent.Radius = value
    
    @property
    def startangle(self) -> float:
        'Specifies the start angle of the arc'
        return self.com_parent.StartAngle
    @startangle.setter
    def _(self, value: float):
        self.com_parent.StartAngle = value
    
    @property
    def startpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the start point of the arc'
        return A3Vertex(self.com_parent.StartPoint)
    
    @property
    def thickness(self) -> float:
        'Specifies the thickness of the arc'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value: float):
        self.com_parent.Thickness = value
    
    @property
    def totalangle(self) -> float:
        'Specifies the total angle of the arc'
        return self.com_parent.TotalAngle
    
    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadAttribute(POINTER(_dll.IAcadAttribute), _ez_ptr):
    def __new__(cls, Height, Mode, Prompt, InsertionPoint, Tag, Value, source=None):
        return __get_source(source).addattribute(Height, Mode, Prompt, InsertionPoint, Tag, Value)
    def updatemtextattribute(self):
        'Updates multiline MText'
        self.com_parent.UpdateMTextAttribute()
    
    @property
    def alignment(self) -> AcAlignment:
        'Specifies both text height and text orientation by designating the endpoints of the baseline'
        return AcAlignment(self.com_parent.Alignment)
    @alignment.setter
    def _(self, value: AcAlignment):
        self.com_parent.Alignment = value.value
    
    @property
    def backward(self) -> bool:
        'Determines whether the text is backward or not'
        return self.com_parent.Backward
    @backward.setter
    def _(self, value: bool):
        self.com_parent.Backward = value
    
    @property
    def constant(self) -> bool:
        'Specifies the constant mode of the attribute'
        return self.com_parent.Constant
    @constant.setter
    def _(self, value: bool):
        self.com_parent.Constant = value
    
    @property
    def fieldlength(self) -> int:
        'Specifies the field length of the attribute'
        return self.com_parent.FieldLength
    @fieldlength.setter
    def _(self, value: int):
        self.com_parent.FieldLength = value
    
    @property
    def height(self) -> float:
        'Specifies the height of the attribute'
        return self.com_parent.Height
    @height.setter
    def _(self, value: float):
        self.com_parent.Height = value
    
    @property
    def horizontalalignment(self) -> AcHorizontalAlignment:
        'Specifies the horizontal alignment of the attribute'
        return AcHorizontalAlignment(self.com_parent.HorizontalAlignment)
    @horizontalalignment.setter
    def _(self, value: AcHorizontalAlignment):
        self.com_parent.HorizontalAlignment = value.value
    
    @property
    def insertionpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the insertion point of the text'
        return A3Vertex(self.com_parent.InsertionPoint)
    @insertionpoint.setter
    def _(self, value:A3Vertex):
        self.com_parent.InsertionPoint = value
    
    @property
    def invisible(self) -> bool:
        'Specifies the invisible mode of the attribute'
        return self.com_parent.Invisible
    @invisible.setter
    def _(self, value: bool):
        self.com_parent.Invisible = value
    
    @property
    def lockposition(self) -> bool:
        'Specifies whether the attribute may be moved relative to the geometry in the block'
        return self.com_parent.LockPosition
    @lockposition.setter
    def _(self, value: bool):
        self.com_parent.LockPosition = value
        
	@property
	def mode(self) -> AcAttributeMode:
		"Specifies the mode of the attribute definition"
		# ('out', 'retval') Mode:int
		return AcAttributeMode(self.com_parent.Mode)
	@mode.setter
	def _(self, Mode:AcAttributeMode):
		# ('in',) Mode:int
		self.com_parent.Mode = value.value
    
    @property
    def mtextattribute(self) -> bool:
        'Determines whether if the attribute is multiline'
        return self.com_parent.MTextAttribute
    @mtextattribute.setter
    def _(self, value: bool):
        self.com_parent.MTextAttribute = value
    
    @property
    def mtextattributecontent(self) -> str:
        'Gets the multiline attribute content'
        return self.com_parent.MTextAttributeContent
    @mtextattributecontent.setter
    def _(self, value: str):
        self.com_parent.MTextAttributeContent = value
    
    @property
    def mtextboundarywidth(self) -> float:
        'Gets the width of text boundary of the Mtext'
        return self.com_parent.MTextBoundaryWidth
    @mtextboundarywidth.setter
    def _(self, value: float):
        self.com_parent.MTextBoundaryWidth = value
    
    @property
    def mtextdrawingdirection(self) -> int:
        'Gets the drawing direction of the Mtext'
        return AcDrawingDirection(self.com_parent.MTextDrawingDirection)
    @mtextdrawingdirection.setter
    def _(self, value: AcDrawingDirection):
        self.com_parent.MTextDrawingDirection = value.value
    
    @property
    def normal(self) -> A3Vertex:
        'Specifies the three-dimensional normal unit vector for the entity'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def obliqueangle(self) -> float:
        'Specifies the oblique angle of the attribute'
        return self.com_parent.ObliqueAngle
    @obliqueangle.setter
    def _(self, value: float):
        self.com_parent.ObliqueAngle = value
    
    @property
    def preset(self) -> bool:
        'Specifies the preset mode of the attribute'
        return self.com_parent.Preset
    @preset.setter
    def _(self, value: bool):
        self.com_parent.Preset = value
    
    @property
    def promptstring(self) -> str:
        'Specifies the prompt string of the attribute'
        return self.com_parent.PromptString
    @promptstring.setter
    def _(self, value: str):
        self.com_parent.PromptString = value
    
    @property
    def rotation(self) -> float:
        'Specifies the rotation angle of the attribute'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value: float):
        self.com_parent.Rotation = value
    
    @property
    def scalefactor(self) -> float:
        'Specifies the scale factor of the attribute'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value: float):
        self.com_parent.ScaleFactor = value
    
    @property
    def stylename(self) -> str:
        'Specifies the text style of the attribute'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value: str):
        self.com_parent.StyleName = value
    
    @property
    def tagstring(self) -> str:
        'Specifies the tag string of the attribute'
        return self.com_parent.TagString
    @tagstring.setter
    def _(self, value: str):
        self.com_parent.TagString = value
    
    @property
    def textalignmentpoint(self) -> A3Vertex:
        'Specify the X, Y, Z alignment point of the attribute'
        return A3Vertex(self.com_parent.TextAlignmentPoint)
    @textalignmentpoint.setter
    def _(self, value:A3Vertex):
        self.com_parent.TextAlignmentPoint = value
    
    @property
    def textgenerationflag(self) -> AcTextGenerationFlag:
        'Specifies the attribute text generation flag'
        return AcTextGenerationFlag(self.com_parent.TextGenerationFlag)
    @textgenerationflag.setter
    def _(self, value: AcTextGenerationFlag):
        self.com_parent.TextGenerationFlag = value.value
    
    @property
    def textstring(self) -> str:
        'Specifies the text string of the attribute'
        return self.com_parent.TextString
    @textstring.setter
    def _(self, value: str):
        self.com_parent.TextString = value
    
    @property
    def thickness(self) -> float:
        'Specifies the thickness of the attribute'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value: float):
        self.com_parent.Thickness = value
    
    @property
    def upsidedown(self) -> bool:
        'Determines whether the text is upside down or not'
        return self.com_parent.UpsideDown
    @upsidedown.setter
    def _(self, value: bool):
        self.com_parent.UpsideDown = value
    
    @property
    def verify(self) -> bool:
        'Specifies the verify mode of the attribute'
        return self.com_parent.Verify
    @verify.setter
    def _(self, value: bool):
        self.com_parent.Verify = value
    
    @property
    def verticalalignment(self) -> AcVerticalAlignment:
        'Specifies the verify mode of the attribute'
        return AcVerticalAlignment(self.com_parent.VerticalAlignment)
    @verticalalignment.setter
    def _(self, value: AcVerticalAlignment):
        self.com_parent.VerticalAlignment = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadAttributeReference(POINTER(_dll.IAcadAttributeReference), _ez_ptr):
    #def __new__(cls, InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, Password=None, source=None):
    #    return __get_source(source).insertblock(InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, Password)
    def updatemtextattribute(self):
        'Updates attribute reference from the multiline mtext and vice versa'
        self.com_parent.UpdateMTextAttribute()
    
    @property
    def alignment(self):
        'Specifies the alignment of the attribute reference'
        return AcAlignment(self.com_parent.Alignment)
    @alignment.setter
    def _(self, value: AcAlignment):
        self.com_parent.Alignment = value.value
    
    @property
    def backward(self) -> bool:
        'Determines whether the text is backward and sets the text backward'
        return self.com_parent.Backward
    @backward.setter
    def _(self, value: bool):
        self.com_parent.Backward = value
    
    @property
    def constant(self) -> bool:
        'Specifies the constant mode of the attribute reference'
        return self.com_parent.Constant
    
    @property
    def fieldlength(self) -> int:
        'Specifies the field length of the attribute reference'
        return self.com_parent.FieldLength
    @fieldlength.setter
    def _(self, value: int):
        self.com_parent.FieldLength = value
    
    @property
    def height(self) -> float:
        'Specifies the height of the attribute reference'
        return self.com_parent.Height
    @height.setter
    def _(self, value: float):
        self.com_parent.Height = value
    
    @property
    def horizontalalignment(self):
        'Specifies the horizontal alignment of the attribute reference'
        return AcHorizontalAlignment(self.com_parent.HorizontalAlignment)
    @horizontalalignment.setter
    def _(self, value: AcHorizontalAlignment):
        self.com_parent.HorizontalAlignment = value.value
    
    @property
    def insertionpoint(self) -> A3Vertex:
        'Specifies the insertion point of the text'
        return A3Vertex(self.com_parent.InsertionPoint)
    @insertionpoint.setter
    def _(self, value:A3Vertex):
        self.com_parent.InsertionPoint = value
    
    @property
    def invisible(self) -> bool:
        'Specifies the invisible mode of the attribute reference'
        return self.com_parent.Invisible
    @invisible.setter
    def _(self, value: bool):
        self.com_parent.Invisible = value
    
    @property
    def lockposition(self) -> bool:
        'Specifies whether the attribute may be moved relative to the geometry in the block'
        return self.com_parent.LockPosition
    
    @property
    def mtextattribute(self) -> bool:
        'Determines whether if the attribute reference is multiline'
        return self.com_parent.MTextAttribute
    @mtextattribute.setter
    def _(self, value: bool):
        self.com_parent.MTextAttribute = value
    
    @property
    def mtextattributecontent(self) -> str:
        'Gets the multiline attribute reference content'
        return self.com_parent.MTextAttributeContent
    @mtextattributecontent.setter
    def _(self, value: str):
        self.com_parent.MTextAttributeContent = value
    
    @property
    def mtextboundarywidth(self) -> float:
        'Gets the width of text boundary of the Mtext'
        return self.com_parent.MTextBoundaryWidth
    @mtextboundarywidth.setter
    def _(self, value: float):
        self.com_parent.MTextBoundaryWidth = value
    
    @property
    def mtextdrawingdirection(self) -> AcDrawingDirection:
        'Gets the drawing direction of the Mtext'
        return AcDrawingDirection(self.com_parent.MTextDrawingDirection)
    @mtextdrawingdirection.setter
    def _(self, value: AcDrawingDirection):
        self.com_parent.MTextDrawingDirection = value.value
    
    @property
    def normal(self) -> A3Vertex:
        'Specifies the three-dimensional normal unit vector for the entity'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def obliqueangle(self) -> float:
        'Specifies the oblique angle of the attribute reference'
        return self.com_parent.ObliqueAngle
    @obliqueangle.setter
    def _(self, value: float):
        self.com_parent.ObliqueAngle = value
    
    @property
    def rotation(self) -> float:
        'Specifies the rotation angle of the attribute reference'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value: float):
        self.com_parent.Rotation = value
    
    @property
    def scalefactor(self) -> float:
        'Specifies the scale factor of the attribute reference'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value: float):
        self.com_parent.ScaleFactor = value
    
    @property
    def stylename(self) -> str:
        'Specifies the style name of the attribute reference'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value: str):
        self.com_parent.StyleName = value
    
    @property
    def tagstring(self) -> str:
        'Specifies the tag string of the attribute reference'
        return self.com_parent.TagString
    @tagstring.setter
    def _(self, value: str):
        self.com_parent.TagString = value
        
    @property
    def textalignmentpoint(self) -> A3Vertex:
        'Specifies the alignment point of the attribute reference'
        return A3Vertex(self.com_parent.TextAlignmentPoint)
    @textalignmentpoint.setter
    def _(self, value:A3Vertex):
        self.com_parent.TextAlignmentPoint = value
    
    @property
    def textgenerationflag(self) -> AcTextGenerationFlag:
        'Specifies the attribute reference text generation flag'
        return AcTextGenerationFlag(self.com_parent.TextGenerationFlag)
    @textgenerationflag.setter
    def _(self, value: AcTextGenerationFlag):
        self.com_parent.TextGenerationFlag = value.value
    
    @property
    def textstring(self) -> str:
        'Specifies the text string of the attribute reference'
        return self.com_parent.TextString
    @textstring.setter
    def _(self, value: str):
        self.com_parent.TextString = value
    
    @property
    def thickness(self) -> float:
        'Specifies the thickness of the attribute reference'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value: float):
        self.com_parent.Thickness = value
    
    @property
    def upsidedown(self) -> bool:
        'Returns whether the text is upside down and sets the text upside down'
        return self.com_parent.UpsideDown
    @upsidedown.setter
    def _(self, value: bool):
        self.com_parent.UpsideDown = value
    
    @property
    def verticalalignment(self):
        'Specifies the vertical alignment of the attribute reference'
        return AcVerticalAlignment(self.com_parent.VerticalAlignment)
    @verticalalignment.setter
    def _(self, value: AcVerticalAlignment):
        self.com_parent.VerticalAlignment = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadBlockReference(POINTER(_dll.IAcadBlockReference), _ez_ptr):
    def converttoanonymousblock(self):
        'Converts a dynamic block to a regular anonymous block'
        self.com_parent.ConvertToAnonymousBlock()
    def converttostaticblock(self, newBlockName: str):
        'Converts a dynamic block to a regular named block'
        self.com_parent.ConvertToStaticBlock(newBlockName)
    def explode(self):
        'Explodes the block and returns the sub-entities as an array of Object'
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret
    def getattributes(self):
        'Gets Attributes in the block'
        ret = []
        for obj in self.com_parent.GetAttributes():
            ret.append(CastManager.cast(obj))
        return ret
    def getconstantattributes(self):
        'Gets constant attributes in the block'
        ret = []
        for obj in self.com_parent.GetConstantAttributes():
            ret.append(CastManager.cast(obj))
        return ret
    def getdynamicblockproperties(self):
        'Gets the dynamic block properties'
        ret = []
        for obj in self.com_parent.GetDynamicBlockProperties():
            ret.append(CastManager.cast(obj))
        return ret
    def resetblock(self):
        "Resets the dynamic block to the default state"
        self.com_parent.ResetBlock()
    
    @property
    def effectivename(self) -> str:
        'Specifies the original block name'
        return self.com_parent.EffectiveName
    
    @property
    def hasattributes(self) -> bool:
        'Specifies if the block has any attributes in it'
        return self.com_parent.HasAttributes
    
    @property
    def insertionpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate for insertion point of the block or use the Pick Point button to set X, Y, Z values simultaneously'
        return A3Vertex(self.com_parent.InsertionPoint)
    @insertionpoint.setter
    def _(self, value:A3Vertex):
        self.com_parent.InsertionPoint = value
    
    @property
    def insunits(self) -> str:
        'Specifies insunits saved with the block'
        return self.com_parent.InsUnits
    
    @property
    def insunitsfactor(self) -> float:
        'Specifies the conversion factor between block units and drawing units'
        return self.com_parent.InsUnitsFactor
    
    @property
    def isdynamicblock(self) -> bool:
        'Specifies if this is a dynamic block'
        return self.com_parent.IsDynamicBlock
    
    @property
    def name(self) -> str:
        'Specifies the name of the block'
        return self.com_parent.Name
    @name.setter
    def _(self, value: str):
        self.com_parent.Name = value
    
    @property
    def normal(self) -> A3Vertex:
        'Specifies the three-dimensional normal unit vector for the entity'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def rotation(self) -> float:
        'Specifies the rotation angle of the block'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value: float):
        self.com_parent.Rotation = value
    
    @property
    def xeffectivescalefactor(self) -> float:
        'Specifies the effective XScale factor of the block'
        return self.com_parent.XEffectiveScaleFactor
    @xeffectivescalefactor.setter
    def _(self, value: float):
        self.com_parent.XEffectiveScaleFactor = value
    
    @property
    def xscalefactor(self) -> float:
        'Specifies the XScale factor of the block'
        return self.com_parent.XScaleFactor
    @xscalefactor.setter
    def _(self, value: float):
        self.com_parent.XScaleFactor = value
    
    @property
    def yeffectivescalefactor(self):
        'Specifies the effective YScale factor of the block'
        return self.com_parent.YEffectiveScaleFactor
    @yeffectivescalefactor.setter
    def _(self, value: float):
        self.com_parent.YEffectiveScaleFactor = value
    
    @property
    def yscalefactor(self) -> float:
        'Specifies the YScale factor of the block'
        return self.com_parent.YScaleFactor
    @yscalefactor.setter
    def _(self, value: float):
        self.com_parent.YScaleFactor = value
    
    @property
    def zeffectivescalefactor(self) -> float:
        'Specifies the effective ZScale factor of the block'
        return self.com_parent.ZEffectiveScaleFactor
    @zeffectivescalefactor.setter
    def _(self, value: float):
        self.com_parent.ZEffectiveScaleFactor = value
    
    @property
    def zscalefactor(self) -> float:
        'Specifies the ZScale factor of the block'
        return self.com_parent.ZScaleFactor
    @zscalefactor.setter
    def _(self, value: float):
        self.com_parent.ZScaleFactor = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadCircle(POINTER(_dll.IAcadCircle), _ez_ptr):
    def __new__(self, Center, Radius, source=None):
        return __get_source(source).addcircle(Center, Radius)
    def offset(self, Distance: float):
        'Offsets the arc to the given side'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret
    
    @property
    def area(self) -> float:
        'Specifies the area of the circle'
        return self.com_parent.Area
    @area.setter
    def _(self, value: float):
        self.com_parent.Area = value
    
    @property
    def center(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the center of the circle or use the Pick Point button to set X, Y, Z values simultaneously'
        return A3Vertex(self.com_parent.Center)
    @center.setter
    def _(self, value:A3Vertex):
        self.com_parent.Center = value
    
    @property
    def circumference(self) -> float:
        'Specifies the circumference of the circle'
        return self.com_parent.Circumference
    @circumference.setter
    def _(self, value: float):
        self.com_parent.Circumference = value
    
    @property
    def diameter(self) -> float:
        'Specifies the diameter of the circle'
        return self.com_parent.Diameter
    @diameter.setter
    def _(self, value: float):
        self.com_parent.Diameter = value
    
    @property
    def normal(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the normal direction vector'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def radius(self) -> float:
        'Specifies the radius of the circle'
        return self.com_parent.Radius
    @radius.setter
    def _(self, value: float):
        self.com_parent.Radius = value
    
    @property
    def thickness(self) -> float:
        'Specifies the thickness of the circle'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value: float):
        self.com_parent.Thickness = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadDimension(POINTER(_dll.IAcadDimension), _ez_ptr):
    @property
    def decimalseparator(self):
        'Specifies the decimal separator for metric dimensions (DIMDSEP system variable)'
        return self.com_parent.DecimalSeparator
    @decimalseparator.setter
    def _(self, value: str):
        self.com_parent.DecimalSeparator = value
        
    @property
    def dimtxtdirection(self):
        'Specifies the dimension text viewing direction.'
        return self.com_parent.DimTxtDirection
    @dimtxtdirection.setter
    def _(self, value: bool):
        self.com_parent.DimTxtDirection = value
    
    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value
    
    @property
    def rotation(self):
        'Specifies the rotation angle for the object'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value: float):
        self.com_parent.Rotation = value
    
    @property
    def scalefactor(self):
        'Specifies the overall scale factor applied to properties that specify sizes, distances, or offsets (DIMSCALE system variable)'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value: float):
        self.com_parent.ScaleFactor = value
    
    @property
    def stylename(self):
        'Specifies the current dimension style by name (for DIMSTYLE system variable use SETVAR)'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value: str):
        self.com_parent.StyleName = value
    
    @property
    def suppressleadingzeros(self):
        'Sets suppression of leading zeros for dimensions On or Off (DIMZIN system variable)'
        return self.com_parent.SuppressLeadingZeros
    @suppressleadingzeros.setter
    def _(self, value: bool):
        self.com_parent.SuppressLeadingZeros = value
    
    @property
    def suppresstrailingzeros(self):
        'Sets suppression of trailing zeros for dimensions On or Off (DIMZIN system variable)'
        return self.com_parent.SuppressTrailingZeros
    @suppresstrailingzeros.setter
    def _(self, value: bool):
        self.com_parent.SuppressTrailingZeros = value
    
    @property
    def textcolor(self):
        'Specifies the color of the dimension text (DIMCLRT system variable)'
        return AcColor(self.com_parent.TextColor)
    @textcolor.setter
    def _(self, value: AcColor):
        self.com_parent.TextColor = value.value
    
    @property
    def textfill(self):
        'Sets fill color On or Off (DIMTFILL system variable)'
        return self.com_parent.TextFill
    @textfill.setter
    def _(self, value: bool):
        self.com_parent.TextFill = value
    
    @property
    def textfillcolor(self):
        'Sets text fill color (DIMTFILLCLR system variable)'
        return AcColor(self.com_parent.TextFillColor)
    @textfillcolor.setter
    def _(self, value: AcColor):
        self.com_parent.TextFillColor = value.value
    
    @property
    def textgap(self):
        'Specifies distance around dimension text when dimension line breaks for dimension text (DIMGAP system variable)'
        return self.com_parent.TextGap
    @textgap.setter
    def _(self, value: float):
        self.com_parent.TextGap = value
    
    @property
    def textheight(self):
        'Specifies text height of the dimension (DIMTXT system variable)'
        return self.com_parent.TextHeight
    @textheight.setter
    def _(self, value: float):
        self.com_parent.TextHeight = value
    
    @property
    def textmovement(self):
        "Specifies position of text when it's moved, either manually or automatically (DIMTMOVE system variable)"
        return AcDimTextMovement(self.com_parent.TextMovement)
    @textmovement.setter
    def _(self, value: AcDimTextMovement):
        self.com_parent.TextMovement = value.value
    
    @property
    def textoverride(self):
        'Specifies the text string of the dimension (overrides Measurement string)'
        return self.com_parent.TextOverride
    @textoverride.setter
    def _(self, value: str):
        self.com_parent.TextOverride = value
    
    @property
    def textposition(self):
        'Specifies the dimension text position or pick point'
        return self.com_parent.TextPosition
    @textposition.setter
    def _(self, value):
        self.com_parent.TextPosition = value
    
    @property
    def textprefix(self):
        'Specifies the text prefix for the dimension (DIMPOST system variable)'
        return self.com_parent.TextPrefix
    @textprefix.setter
    def _(self, value: str):
        self.com_parent.TextPrefix = value
    
    @property
    def textrotation(self):
        'Specifies the rotation angle of the dimension text'
        return self.com_parent.TextRotation
    @textrotation.setter
    def _(self, value: float):
        self.com_parent.TextRotation = value
    
    @property
    def textstyle(self):
        'Specifies text style of the dimension (DIMTXSTY system variable)'
        return self.com_parent.TextStyle
    @textstyle.setter
    def _(self, value: str):
        self.com_parent.TextStyle = value
    
    @property
    def textsuffix(self):
        'Specifies the text suffix for the dimension (DIMPOST system variable)'
        return self.com_parent.TextSuffix
    @textsuffix.setter
    def _(self, value: str):
        self.com_parent.TextSuffix = value
    
    @property
    def tolerancedisplay(self):
        'Specifies display mode of dimension tolerances to dimension text (DIMTOL system variable)'
        return AcDimToleranceMethod(self.com_parent.ToleranceDisplay)
    @tolerancedisplay.setter
    def _(self, value: AcDimToleranceMethod):
        self.com_parent.ToleranceDisplay = value.value
    
    @property
    def toleranceheightscale(self):
        'Specifies scale factor for text height of tolerance values relative to dimension text height as set by DIMTXT (DIMTFAC system variable)'
        return self.com_parent.ToleranceHeightScale
    @toleranceheightscale.setter
    def _(self, value: float):
        self.com_parent.ToleranceHeightScale = value
    
    @property
    def tolerancejustification(self):
        'Specifies vertical justification for tolerance values relative to nominal dimension text (DIMTOLJ system variable)'
        return AcDimToleranceJustify(self.com_parent.ToleranceJustification)
    @tolerancejustification.setter
    def _(self, value: AcDimToleranceJustify):
        self.com_parent.ToleranceJustification = value.value
    
    @property
    def tolerancelowerlimit(self):
        'Specifies minimum (or lower) tolerance limit for dimension text when DIMTOL or DIMLIM is on (DIMTM system variable)'
        return self.com_parent.ToleranceLowerLimit
    @tolerancelowerlimit.setter
    def _(self, value: float):
        self.com_parent.ToleranceLowerLimit = value
    
    @property
    def toleranceprecision(self):
        'Specifies number of decimal places for tolerance values of a dimension (DIMTDEC system variable)'
        return AcDimPrecision(self.com_parent.TolerancePrecision)
    @toleranceprecision.setter
    def _(self, value: AcDimPrecision):
        self.com_parent.TolerancePrecision = value.value
    
    @property
    def tolerancesuppressleadingzeros(self):
        'Sets suppression of leading zeros for tolerance values On or Off (DIMTZIN system variable)'
        return self.com_parent.ToleranceSuppressLeadingZeros
    @tolerancesuppressleadingzeros.setter
    def _(self, value: bool):
        self.com_parent.ToleranceSuppressLeadingZeros = value
    
    @property
    def tolerancesuppresstrailingzeros(self):
        'Sets suppression of trailing zeros for tolerance values On or Off (DIMTZIN system variable)'
        return self.com_parent.ToleranceSuppressTrailingZeros
    @tolerancesuppresstrailingzeros.setter
    def _(self, value: bool):
        self.com_parent.ToleranceSuppressTrailingZeros = value
    
    @property
    def toleranceupperlimit(self):
        'Specifies the maximum (or upper) tolerance limit for dimension text when DIMTOL or DIMLIM is on (DIMTP sysem variable)'
        return self.com_parent.ToleranceUpperLimit
    @toleranceupperlimit.setter
    def _(self, value: float):
        self.com_parent.ToleranceUpperLimit = value
    
    @property
    def verticaltextposition(self):
        'Specifies number of decimal places for tolerance values of a dimension (DIMTDEC system variable)'
        return AcDimVerticalJustification(self.com_parent.VerticalTextPosition)
    @verticaltextposition.setter
    def _(self, value: AcDimVerticalJustification):
        self.com_parent.VerticalTextPosition = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadEllipse(POINTER(_dll.IAcadEllipse), _ez_ptr):
    def __new__(self, Center, MajorAxis, RadiusRatio, source=None):
        return __get_source(source).addellipse(Center, MajorAxis, RadiusRatio)
    def offset(self, Distance: float):
        'method Offset'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret
    
    @property
    def area(self) -> float:
        'Specifies the area of the ellipse'
        return self.com_parent.Area
    
    @property
    def center(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the center point of the ellipse or use the Pick Point button to set X, Y, Z values simultaneously'
        return A3Vertex(self.com_parent.Center)
    @center.setter
    def _(self, value:A3Vertex):
        self.com_parent.Center = value
    
    @property
    def endangle(self) -> float:
        'Specifies the end angle of the ellipse'
        return self.com_parent.EndAngle
    @endangle.setter
    def _(self, value: float):
        self.com_parent.EndAngle = value
    
    @property
    def endparameter(self) -> float:
        'Specifies the end parameter for an ellipse'
        return self.com_parent.EndParameter
    @endparameter.setter
    def _(self, value: float):
        self.com_parent.EndParameter = value
    
    @property
    def endpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the end point of the ellipse'
        return A3Vertex(self.com_parent.EndPoint)
    
    @property
    def majoraxis(self) -> A3Vertex:
        'Specifies the major axis of the ellipse'
        return A3Vertex(self.com_parent.MajorAxis)
    @majoraxis.setter
    def _(self, value:A3Vertex):
        self.com_parent.MajorAxis = value
    
    @property
    def majorradius(self) -> float:
        'Specifies the major radius of the ellipse'
        return self.com_parent.MajorRadius
    @majorradius.setter
    def _(self, value: float):
        self.com_parent.MajorRadius = value
    
    @property
    def minoraxis(self) -> A3Vertex:
        'Specifies the minor axis of the ellipse'
        return A3Vertex(self.com_parent.MinorAxis)
    
    @property
    def minorradius(self) -> float:
        'Specifies the minor radius of the ellipse'
        return self.com_parent.MinorRadius
    @minorradius.setter
    def _(self, value: float):
        self.com_parent.MinorRadius = value
    
    @property
    def normal(self) -> A3Vertex:
        'Specifies the three-dimensional normal unit vector for the entity'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value
    
    @property
    def radiusratio(self) -> float:
        'Specifies the radius ratio of the ellipse'
        return self.com_parent.RadiusRatio
    @radiusratio.setter
    def _(self, value: float):
        self.com_parent.RadiusRatio = value
    
    @property
    def startangle(self) -> float:
        'Specifies the start angle of the ellipse'
        return self.com_parent.StartAngle
    @startangle.setter
    def _(self, value: float):
        self.com_parent.StartAngle = value
    
    @property
    def startparameter(self) -> float:
        'Specifies the start parameter for an ellipse'
        return self.com_parent.StartParameter
    @startparameter.setter
    def _(self, value: float):
        self.com_parent.StartParameter = value
    
    @property
    def startpoint(self) -> A3Vertex:
        'Specify the X, Y, Z coordinate of the start point of the ellipse'
        return A3Vertex(self.com_parent.StartPoint)

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadGeoPositionMarker(POINTER(_dll.IAcadGeoPositionMarker), _ez_ptr):
    @property
    def altitude(self) -> float:
        'Specifies the elevation of the marker'
        return self.com_parent.Altitude
    @altitude.setter
    def _(self, value:float):
        self.com_parent.Altitude = value

    @property
    def backgroundfill(self) -> bool:
        'Specifies use Background Mask of the MText'
        return self.com_parent.BackgroundFill
    @backgroundfill.setter
    def _(self, value:bool):
        self.com_parent.BackgroundFill = value

    @property
    def drawingdirection(self) -> AcDrawingDirection:
        'Specifies the drawing direction of the MText'
        return AcDrawingDirection(self.com_parent.DrawingDirection)
    @drawingdirection.setter
    def _(self, value: AcDrawingDirection):
        self.com_parent.DrawingDirection = value.value

    @property
    def height(self) -> float:
        'Specifies the height of the Mtext'
        return self.com_parent.Height
    @height.setter
    def _(self, value:float):
        self.com_parent.Height = value

    @property
    def landinggap(self) -> float:
        'Specify the landing distance'
        return self.com_parent.LandingGap
    @landinggap.setter
    def _(self, value:float):
        self.com_parent.LandingGap = value

    @property
    def latitude(self) -> str:
        'Specifies the latitude of the marker'
        return self.com_parent.Latitude
    @latitude.setter
    def _(self, value:str):
        self.com_parent.Latitude = value

    @property
    def linespacingdistance(self) -> float:
        'Specifies the line spacing distance of the Mtext'
        return self.com_parent.LineSpacingDistance
    @linespacingdistance.setter
    def _(self, value:float):
        self.com_parent.LineSpacingDistance = value

    @property
    def linespacingfactor(self) -> float:
        'Specifies the line spacing factor of the Mtext'
        return self.com_parent.LineSpacingFactor
    @linespacingfactor.setter
    def _(self, value:float):
        self.com_parent.LineSpacingFactor = value

    @property
    def linespacingstyle(self) -> AcLineSpacingStyle:
        'Specifies the line spacing style of the Mtext'
        return AcLineSpacingStyle(self.com_parent.LineSpacingStyle)
    @linespacingstyle.setter
    def _(self, value: AcLineSpacingStyle):
        self.com_parent.LineSpacingStyle = value.value

    @property
    def longitude(self) -> str:
        'Specifies the longitude of the marker'
        return self.com_parent.Longitude
    @longitude.setter
    def _(self, value:str):
        self.com_parent.Longitude = value

    @property
    def notes(self) -> str:
        'Specifies the notes for the marker'
        return self.com_parent.Notes
    @notes.setter
    def _(self, value:str):
        self.com_parent.Notes = value

    @property
    def position(self) -> A3Vertex:
        "Specify the marker's position"
        return A3Vertex(self.com_parent.Position)
    @position.setter
    def _(self, value:A3Vertex):
        self.com_parent.Position = value

    @property
    def radius(self) -> float:
        'Radius'
        return self.com_parent.Radius
    @radius.setter
    def _(self, value:float):
        self.com_parent.Radius = value

    @property
    def rotation(self) -> float:
        'Specifies the rotation angle of the Mtext'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value:float):
        self.com_parent.Rotation = value

    @property
    def textframedisplay(self) -> bool:
        'Display/hide text frame of content'
        return self.com_parent.TextFrameDisplay
    @textframedisplay.setter
    def _(self, value:bool):
        self.com_parent.TextFrameDisplay = value

    @property
    def textjustify(self) -> AcAttachmentPoint:
        'Specifies the attachment point of the MText'
        return AcAttachmentPoint(self.com_parent.TextJustify)
    @textjustify.setter
    def _(self, value: AcAttachmentPoint):
        self.com_parent.TextJustify = value.value

    @property
    def textstring(self) -> str:
        'Specifies the text string of the MText'
        return self.com_parent.TextString
    @textstring.setter
    def _(self, value:str):
        self.com_parent.TextString = value

    @property
    def textstylename(self) -> str:
        'Specifies the style name of the MText'
        return self.com_parent.TextStyleName
    @textstylename.setter
    def _(self, value:str):
        self.com_parent.TextStyleName = value

    @property
    def textwidth(self) -> float:
        'Specifies the width of the MText'
        return self.com_parent.TextWidth
    @textwidth.setter
    def _(self, value:float):
        self.com_parent.TextWidth = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadHatch(POINTER(_dll.IAcadHatch), _ez_ptr):
    def __new__(self, PatternType, PatternName, Associativity, HatchObjectType: AcHatchObjectType=None, source=None):
        return __get_source(source).addhatch(PatternType, PatternName, Associativity, HatchObjectType)
    def appendinnerloop(self, ObjectArray):
        'Append loops to the hatch'
        self.com_parent.AppendInnerLoop(ObjectArray)

    def appendouterloop(self, ObjectArray):
        'Append loops to the hatch'
        self.com_parent.AppendOuterLoop(ObjectArray)

    def evaluate(self):
        'Evaluate the hatch'
        self.com_parent.Evaluate()

    def getloopat(self, Index):
        'Get loops at given index of the hatch'
        return self.com_parent.GetLoopAt(Index)

    def insertloopat(self, Index, LoopType, ObjectArray):
        'Insert loops at given index to the hatch'
        self.com_parent.InsertLoopAt(Index, LoopType, ObjectArray)

    def setpattern(self, PatternType, PatternName):
        'Set Pattern Type and Name of the hatch'
        self.com_parent.SetPattern(PatternType, PatternName)

    @property
    def area(self) -> float:
        'Specifies the area of the hatch entity'
        return self.com_parent.Area

    @property
    def associativehatch(self) -> bool:
        'Determines whether the hatch is associative or not'
        return self.com_parent.AssociativeHatch
    @associativehatch.setter
    def _(self, value:bool):
        self.com_parent.AssociativeHatch = value

    @property
    def backgroundcolor(self) -> AcadAcCmColor:
        'Specifies the background color of the hatch.'
        return CastManager.cast(self.com_parent.BackgroundColor)
    @backgroundcolor.setter
    def _(self, value:AcadAcCmColor):
        self.com_parent.BackgroundColor = value

    @property
    def elevation(self) -> float:
        "Specifies the elevation of the hatch relative to the Z axis of the objects' coordinate system"
        return self.com_parent.Elevation
    @elevation.setter
    def _(self, value:float):
        self.com_parent.Elevation = value

    @property
    def gradientangle(self) -> float:
        'Specifies the gradient angle'
        return self.com_parent.GradientAngle
    @gradientangle.setter
    def _(self, value:float):
        self.com_parent.GradientAngle = value

    @property
    def gradientcentered(self) -> bool:
        'Determines whether the gradient is centered or not'
        return self.com_parent.GradientCentered
    @gradientcentered.setter
    def _(self, value:bool):
        self.com_parent.GradientCentered = value

    @property
    def gradientcolor1(self) -> AcadAcCmColor:
        'Specifies the gradient start color.'
        return CastManager.cast(self.com_parent.GradientColor1)
    @gradientcolor1.setter
    def _(self, value:AcadAcCmColor):
        self.com_parent.GradientColor1 = value

    @property
    def gradientcolor2(self) -> AcadAcCmColor:
        'Specifies the gradient end color.'
        return CastManager.cast(self.com_parent.GradientColor2)
    @gradientcolor2.setter
    def _(self, value:AcadAcCmColor):
        self.com_parent.GradientColor2 = value

    @property
    def gradientname(self) -> str:
        'Specifies the pattern name of the gradient.'
        return self.com_parent.GradientName
    @gradientname.setter
    def _(self, value:str):
        self.com_parent.GradientName = value

    @property
    def hatchobjecttype(self) -> AcHatchObjectType:
        'Sets the type of the hatch.'
        return AcHatchObjectType(self.com_parent.HatchObjectType)
    @hatchobjecttype.setter
    def _(self, value: AcHatchObjectType):
        self.com_parent.HatchObjectType = value.value

    @property
    def hatchstyle(self) -> AcHatchStyle:
        'Sets the island display style of the hatch'
        return AcHatchStyle(self.com_parent.HatchStyle)
    @hatchstyle.setter
    def _(self, value: AcHatchStyle):
        self.com_parent.HatchStyle = value.value

    @property
    def isopenwidth(self) -> AcISOPenWidth:
        'Specifies the ISO pen width of an ISO hatch pattern'
        return AcISOPenWidth(self.com_parent.ISOPenWidth)
    @isopenwidth.setter
    def _(self, value: AcISOPenWidth):
        self.com_parent.ISOPenWidth = value.value

    @property
    def normal(self) -> A3Vertex:
        'Specifies the three-dimensional normal unit vector for the entity'
        return A3Vertex(self.com_parent.Normal)
    @normal.setter
    def _(self, value:A3Vertex):
        self.com_parent.Normal = value

    @property
    def numberofloops(self) -> int:
        'Gets the number of loops in the hatch boundary'
        return self.com_parent.NumberOfLoops

    @property
    def origin(self) -> A3Vertex:
        'Specifies the origin coordinates for the pattern of the hatch entity'
        return self.com_parent.Origin
    @origin.setter
    def _(self, value:A3Vertex):
        self.com_parent.Origin = value

    @property
    def patternangle(self) -> float:
        'Specifies the pattern angle of the hatch'
        return self.com_parent.PatternAngle
    @patternangle.setter
    def _(self, value:float):
        self.com_parent.PatternAngle = value

    @property
    def patterndouble(self) -> bool:
        'Determines whether the hatch pattern is double or not'
        return self.com_parent.PatternDouble
    @patterndouble.setter
    def _(self, value:bool):
        self.com_parent.PatternDouble = value

    @property
    def patternname(self):
        'Specifies the pattern name of the hatch'
        return self.com_parent.PatternName

    @property
    def patternscale(self):
        'Specifies the pattern scale of the hatch'
        return self.com_parent.PatternScale
    @patternscale.setter
    def _(self, value):
        self.com_parent.PatternScale = value

    @property
    def patternspace(self):
        'Specifies the pattern space of the hatch'
        return self.com_parent.PatternSpace
    @patternspace.setter
    def _(self, value):
        self.com_parent.PatternSpace = value

    @property
    def patterntype(self):
        'Specifies the pattern type of the hatch'
        return AcPatternType(self.com_parent.PatternType)

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadHelix(POINTER(_dll.IAcadHelix), _ez_ptr):
    @property
    def baseradius(self):
        'Specifies the base radius of the helix'
        return self.com_parent.BaseRadius
    @baseradius.setter
    def _(self, value):
        self.com_parent.BaseRadius = value

    @property
    def constrain(self):
        'Controls which property is constrained when editing other property values'
        return AcHelixConstrainType(self.com_parent.Constrain)
    @constrain.setter
    def _(self, value: AcHelixConstrainType):
        self.com_parent.Constrain = value.value

    @property
    def height(self):
        'Specifies the height of the helix'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value

    @property
    def position(self):
        'Specifies the X, Y, and Z for the center of the base of the helix'
        return self.com_parent.Position
    @position.setter
    def _(self, value):
        self.com_parent.Position = value

    @property
    def topradius(self):
        'Specifies the top radius of the helix'
        return self.com_parent.TopRadius
    @topradius.setter
    def _(self, value):
        self.com_parent.TopRadius = value

    @property
    def totallength(self):
        'Specifies the total length of the helix'
        return self.com_parent.TotalLength

    @property
    def turnheight(self):
        'Specifies the height of one full turn for the helix'
        return self.com_parent.TurnHeight
    @turnheight.setter
    def _(self, value):
        self.com_parent.TurnHeight = value

    @property
    def turnslope(self):
        'Displays the constant incline angle for the helix path'
        return self.com_parent.TurnSlope

    @property
    def turns(self):
        'Specifies the number of turns for the helix'
        return self.com_parent.Turns
    @turns.setter
    def _(self, value):
        self.com_parent.Turns = value

    @property
    def twist(self):
        'Controls the twist direction of the helix'
        return AcHelixTwistType(self.com_parent.Twist)
    @twist.setter
    def _(self, value: AcHelixTwistType):
        self.com_parent.Twist = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
   

class AcadLWPolyline(POINTER(_dll.IAcadLWPolyline), _ez_ptr):
    def __new__(cls, VerticesList, source=None):
        return __get_source(source).addlightweightpolyline(VerticesList)
    def addvertex(self, Index, vertex):
        'Adds a vertex to the lightweight polyline'
        self.com_parent.AddVertex(Index, vertex)

    def explode(self):
        'Explodes the lightweight polyline, and returns the sub-entities as an array of Object'
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret

    def getbulge(self, Index):
        'Returns the vertex bulge of the lightweight polyline'
        return self.com_parent.GetBulge(Index)

    def getwidth(self, Index):
        'Returns segment width of the lightweight polyline'
        return self.com_parent.GetWidth(Index)

    def offset(self, Distance):
        'Creates a new entity object by offsetting the lightweight polyline by a given distance'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret

    def setbulge(self, Index, bulge):
        'Sets the vertex bulge of the lightweight polyline'
        self.com_parent.SetBulge(Index, bulge)

    def setwidth(self, Index, StartWidth, EndWidth):
        'Sets the segment width of the lightweight polyline'
        self.com_parent.SetWidth(Index, StartWidth, EndWidth)

    @property
    def area(self):
        'Specifies the area of the lightweight polyline'
        return self.com_parent.Area

    @property
    def closed(self):
        'Determines whether polyline is Open or Closed. Closed draws a line segment from current position to starting point of the polyline.'
        return self.com_parent.Closed
    @closed.setter
    def _(self, value):
        self.com_parent.Closed = value

    @property
    def constantwidth(self):
        'Specifies the constant width for the polyline'
        return self.com_parent.ConstantWidth
    @constantwidth.setter
    def _(self, value):
        self.com_parent.ConstantWidth = value

    @indexedproperty
    def coordinate(self, Index):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[Index]
    @coordinate.setter
    def _(self, Index, value):
        self.com_parent.Coordinate[Index] = value

    @property
    def coordinates(self):
        'Specifies the current vertex of the lightweight polyline'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @property
    def elevation(self):
        "Specifies the elevation of the polyline relative to the Z axis of the objects' coordinate system (Z coordinate of current vertex)"
        return self.com_parent.Elevation
    @elevation.setter
    def _(self, value):
        self.com_parent.Elevation = value

    @property
    def length(self):
        'Specifies the length of the lightweight polyline'
        return self.com_parent.Length

    @property
    def linetypegeneration(self):
        'Determines whether linetype generation is Enabled or Disabled for the polyline'
        return self.com_parent.LinetypeGeneration
    @linetypegeneration.setter
    def _(self, value):
        self.com_parent.LinetypeGeneration = value

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value

    @property
    def thickness(self):
        'Specifies the thickness of the lightweight polyline'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value):
        self.com_parent.Thickness = value 

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadLeader(POINTER(_dll.IAcadLeader), _ez_ptr):
    def __new__(cls, PointsArray, Annotation, Type, source=None):
        return __get_source(source).addleader(PointsArray, Annotation, Type)

    def evaluate(self):
        'Evaluate the leader'
        self.com_parent.Evaluate()

    @property
    def annotation(self):
        'Specifies the annotation object for a leader'
        return CastManager.cast(self.com_parent.Annotation)
    @annotation.setter
    def _(self, value):
        self.com_parent.Annotation = value

    @property
    def arrowheadblock(self):
        'Specifies the block to use as the custom arrowhead for a radial dimension or leader line'
        return self.com_parent.ArrowheadBlock
    @arrowheadblock.setter
    def _(self, value):
        self.com_parent.ArrowheadBlock = value

    @property
    def arrowheadsize(self):
        'Specifies the size of the leader arrowhead'
        return self.com_parent.ArrowheadSize
    @arrowheadsize.setter
    def _(self, value):
        self.com_parent.ArrowheadSize = value

    @property
    def arrowheadtype(self):
        'Specifies the type of the leader arrowhead'
        return AcDimArrowheadType(self.com_parent.ArrowheadType)
    @arrowheadtype.setter
    def _(self, value: AcDimArrowheadType):
        self.com_parent.ArrowheadType = value.value

    @property
    def coordinate(self, Index):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[Index]
    @coordinate.setter
    def _(self, Index, value):
        self.com_parent.Coordinate[Index] = value

    @property
    def coordinates(self):
        'Specifies the coordinates of the leader'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @property
    def dimensionlinecolor(self):
        'Specifies the color of the leader lines'
        return AcColor(self.com_parent.DimensionLineColor)
    @dimensionlinecolor.setter
    def _(self, value: AcColor):
        self.com_parent.DimensionLineColor = value.value

    @property
    def dimensionlineweight(self):
        'Specifies the lineweight of the leader line'
        return AcLineWeight(self.com_parent.DimensionLineWeight)
    @dimensionlineweight.setter
    def _(self, value: AcLineWeight):
        self.com_parent.DimensionLineWeight = value.value

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal

    @property
    def scalefactor(self):
        'Specifies the overall scale factor applied to properties that specify sizes, distances, or offsets'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value):
        self.com_parent.ScaleFactor = value

    @property
    def stylename(self):
        'Specifies the style name of the leader'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value):
        self.com_parent.StyleName = value

    @property
    def textgap(self):
        'Specifies the distance around the dimension text that the dimension line is broken'
        return self.com_parent.TextGap
    @textgap.setter
    def _(self, value):
        self.com_parent.TextGap = value

    @property
    def type(self):
        'Specifies the type of the leader'
        return AcLeaderType(self.com_parent.Type)
    @type.setter
    def _(self, value: AcLeaderType):
        self.com_parent.Type = value.value

    @property
    def verticaltextposition(self):
        'Specifies the vertical dimension text position'
        return AcDimVerticalJustification(self.com_parent.VerticalTextPosition)
    @verticaltextposition.setter
    def _(self, value: AcDimVerticalJustification):
        self.com_parent.VerticalTextPosition = value.value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadLine(POINTER(_dll.IAcadLine), _ez_ptr):
    def offset(self, Distance):
        'Creates a new line by offsetting the current line by a specified distance'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret

    @property
    def angle(self):
        'Specifies the angle of the line'
        return self.com_parent.Angle

    @property
    def delta(self):
        'Specifies the delta of the line'
        return self.com_parent.Delta

    @property
    def endpoint(self):
        'Specify the X, Y, Z coordinate of the end point of the line or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.EndPoint
    @endpoint.setter
    def _(self, value):
        self.com_parent.EndPoint = value

    @property
    def length(self):
        'Specifies the length of the line'
        return self.com_parent.Length

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value

    @property
    def startpoint(self):
        'Specify the X, Y, Z coordinate of the start point of the line or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.StartPoint
    @startpoint.setter
    def _(self, value):
        self.com_parent.StartPoint = value

    @property
    def thickness(self):
        'Specifies the thickness of the line'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value):
        self.com_parent.Thickness = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadMLeader(POINTER(_dll.IAcadMLeader), _ez_ptr):
    def addleader(self):
        'Adds a new leader cluster to this multileader object'
        return self.com_parent.AddLeader()

    def addleaderline(self, leaderIndex, pointArray):
        'Adds a leader line to the leader cluster with specified index'
        return self.com_parent.AddLeaderLine(leaderIndex, pointArray)

    def addleaderlineex(self, pointArray):
        'Adds a new leader line to this multileader object determined by input point which will be the first point of new leader line'
        return self.com_parent.AddLeaderLineEx(pointArray)

    def getblockattributevalue(self, attdefId):
        'Gets attribute value in block content determined by attribute definition id'
        return self.com_parent.GetBlockAttributeValue(attdefId)

    def getdoglegdirection(self, leaderIndex):
        'Gets the dog leg direction of the specific leader'
        return self.com_parent.GetDoglegDirection(leaderIndex)

    def getleaderindex(self, leaderLineIndex):
        'Gets the index of leader cluster which the specified leader line is in'
        return self.com_parent.GetLeaderIndex(leaderLineIndex)

    def getleaderlineindexes(self, leaderIndex):
        'Gets the indexes of leader lines of the specific leader'
        return self.com_parent.GetLeaderLineIndexes(leaderIndex)

    def getleaderlinevertices(self, leaderLineIndex):
        'Specifies the vertices of leader line with specified index'
        return self.com_parent.GetLeaderLineVertices(leaderLineIndex)

    def getvertexcount(self, leaderLineIndex):
        'Gets the number of vertices in the specified leader line'
        return self.com_parent.GetVertexCount(leaderLineIndex)

    def removeleader(self, leaderIndex):
        'Removes the leader cluster with specified index'
        self.com_parent.RemoveLeader(leaderIndex)

    def removeleaderline(self, leaderLineIndex):
        'Removes the leader line with specified index'
        self.com_parent.RemoveLeaderLine(leaderLineIndex)

    def setblockattributevalue(self, attdefId, Value):
        'Sets attribute value in block content with attribute definition id'
        self.com_parent.SetBlockAttributeValue(attdefId, Value)

    def setdoglegdirection(self, leaderIndex, dirVec):
        'Sets the dog leg direction of the specific leader'
        self.com_parent.SetDoglegDirection(leaderIndex, dirVec)

    def setleaderlinevertices(self, leaderLineIndex, pointArray):
        'Specifies the vertices of leader line with specified index'
        self.com_parent.SetLeaderLineVertices(leaderLineIndex, pointArray)

    @property
    def arrowheadblock(self):
        'Specifies the block to use as the custom arrowhead for leader lines of multileader'
        return self.com_parent.ArrowheadBlock
    @arrowheadblock.setter
    def _(self, value):
        self.com_parent.ArrowheadBlock = value

    @property
    def arrowheadsize(self):
        'Specifies the size of leader arrowhead'
        return self.com_parent.ArrowheadSize
    @arrowheadsize.setter
    def _(self, value):
        self.com_parent.ArrowheadSize = value

    @property
    def arrowheadtype(self):
        'Specifies the type of leader arrowhead'
        return AcDimArrowheadType(self.com_parent.ArrowheadType)
    @arrowheadtype.setter
    def _(self, value: AcDimArrowheadType):
        self.com_parent.ArrowheadType = value.value

    @property
    def blockconnectiontype(self):
        'Specify how leaders connect with content block'
        return AcBlockConnectionType(self.com_parent.BlockConnectionType)
    @blockconnectiontype.setter
    def _(self, value: AcBlockConnectionType):
        self.com_parent.BlockConnectionType = value.value

    @property
    def blockscale(self):
        'Specify how leaders connect with content block'
        return self.com_parent.BlockScale
    @blockscale.setter
    def _(self, value):
        self.com_parent.BlockScale = value

    @property
    def contentblockname(self):
        'Specify the name of multileader's content block'
        return self.com_parent.ContentBlockName
    @contentblockname.setter
    def _(self, value):
        self.com_parent.ContentBlockName = value

    @property
    def contentblocktype(self):
        'Specifies the content block of multileader'
        return AcPredefBlockType(self.com_parent.ContentBlockType)
    @contentblocktype.setter
    def _(self, value: AcPredefBlockType):
        self.com_parent.ContentBlockType = value.value

    @property
    def contenttype(self):
        'Specifies the content type of this multileader object'
        return AcMLeaderContentType(self.com_parent.ContentType)
    @contenttype.setter
    def _(self, value: AcMLeaderContentType):
        self.com_parent.ContentType = value.value

    @property
    def doglegged(self):
        'Enable/Disable horizontal landing of multileader'
        return self.com_parent.DogLegged
    @doglegged.setter
    def _(self, value):
        self.com_parent.DogLegged = value

    @property
    def dogleglength(self):
        'Specify the landing distance'
        return self.com_parent.DoglegLength
    @dogleglength.setter
    def _(self, value):
        self.com_parent.DoglegLength = value

    @property
    def landinggap(self):
        'Specify the text landing gap'
        return self.com_parent.LandingGap
    @landinggap.setter
    def _(self, value):
        self.com_parent.LandingGap = value

    @property
    def leadercount(self):
        'Gets the number of leader line clusters in this multileader object'
        return self.com_parent.LeaderCount

    @property
    def leaderlinecolor(self):
        'Specifies the color of the leader lines'
        return CastManager.cast(self.com_parent.LeaderLineColor)
    @leaderlinecolor.setter
    def _(self, value):
        self.com_parent.LeaderLineColor = value

    @property
    def leaderlineweight(self):
        'Specifies the line weight of leader lines'
        return AcLineWeight(self.com_parent.LeaderLineWeight)
    @leaderlineweight.setter
    def _(self, value: AcLineWeight):
        self.com_parent.LeaderLineWeight = value.value

    @property
    def leaderlinetype(self):
        'Specifies the linetype of leader lines'
        return self.com_parent.LeaderLinetype
    @leaderlinetype.setter
    def _(self, value):
        self.com_parent.LeaderLinetype = value

    @property
    def leadertype(self):
        'Specifies the leader type'
        return AcMLeaderType(self.com_parent.LeaderType)
    @leadertype.setter
    def _(self, value: AcMLeaderType):
        self.com_parent.LeaderType = value.value

    @property
    def scalefactor(self):
        'Specifies the overall scale factor of this multileader object'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value):
        self.com_parent.ScaleFactor = value

    @property
    def stylename(self):
        'Specifies the style name of this multileader object'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value):
        self.com_parent.StyleName = value

    @property
    def textattachmentdirection(self):
        'Specifies if leaders connect with the text horizontally or vertically'
        return AcTextAttachmentDirection(self.com_parent.TextAttachmentDirection)
    @textattachmentdirection.setter
    def _(self, value: AcTextAttachmentDirection):
        self.com_parent.TextAttachmentDirection = value.value

    @property
    def textbackgroundfill(self):
        'Specifies use Background Mask'
        return self.com_parent.TextBackgroundFill
    @textbackgroundfill.setter
    def _(self, value):
        self.com_parent.TextBackgroundFill = value

    @property
    def textbottomattachmenttype(self):
        'Specifies how leaders on the bottom connect with the text'
        return AcVerticalTextAttachmentType(self.com_parent.TextBottomAttachmentType)
    @textbottomattachmenttype.setter
    def _(self, value: AcVerticalTextAttachmentType):
        self.com_parent.TextBottomAttachmentType = value.value

    @property
    def textdirection(self):
        'Specifies the drawing direction of the Mtext'
        return AcDrawingDirection(self.com_parent.TextDirection)
    @textdirection.setter
    def _(self, value: AcDrawingDirection):
        self.com_parent.TextDirection = value.value

    @property
    def textframedisplay(self):
        'Display/hide text frame of multileader content'
        return self.com_parent.TextFrameDisplay
    @textframedisplay.setter
    def _(self, value):
        self.com_parent.TextFrameDisplay = value

    @property
    def textheight(self):
        'Specifies the height of the Mtext'
        return self.com_parent.TextHeight
    @textheight.setter
    def _(self, value):
        self.com_parent.TextHeight = value

    @property
    def textjustify(self):
        'Specifies the attachment point of the Mtext'
        return AcAttachmentPoint(self.com_parent.TextJustify)
    @textjustify.setter
    def _(self, value: AcAttachmentPoint):
        self.com_parent.TextJustify = value.value

    @property
    def textleftattachmenttype(self):
        'Specify how leaders on the left side connect with the text'
        return AcTextAttachmentType(self.com_parent.TextLeftAttachmentType)
    @textleftattachmenttype.setter
    def _(self, value: AcTextAttachmentType):
        self.com_parent.TextLeftAttachmentType = value.value

    @property
    def textlinespacingdistance(self):
        'Specifies the line spacing distance of the Mtext'
        return self.com_parent.TextLineSpacingDistance
    @textlinespacingdistance.setter
    def _(self, value):
        self.com_parent.TextLineSpacingDistance = value

    @property
    def textlinespacingfactor(self):
        'Specifies the line spacing factor of the Mtext'
        return self.com_parent.TextLineSpacingFactor
    @textlinespacingfactor.setter
    def _(self, value):
        self.com_parent.TextLineSpacingFactor = value

    @property
    def textlinespacingstyle(self):
        'Specifies the line spacing style of the Mtext'
        return AcLineSpacingStyle(self.com_parent.TextLineSpacingStyle)
    @textlinespacingstyle.setter
    def _(self, value: AcLineSpacingStyle):
        self.com_parent.TextLineSpacingStyle = value.value

    @property
    def textrightattachmenttype(self):
        'Gets the dog leg direction of the specific leader'
        return AcTextAttachmentType(self.com_parent.TextRightAttachmentType)
    @textrightattachmenttype.setter
    def _(self, value: AcTextAttachmentType):
        self.com_parent.TextRightAttachmentType = value.value

    @property
    def textrotation(self):
        'Specifies the rotation angle of the Mtext'
        return self.com_parent.TextRotation
    @textrotation.setter
    def _(self, value):
        self.com_parent.TextRotation = value

    @property
    def textstring(self):
        'Specifies the text string of the Mtext'
        return self.com_parent.TextString
    @textstring.setter
    def _(self, value):
        self.com_parent.TextString = value

    @property
    def textstylename(self):
        'Specifies the style name of the Mtext'
        return self.com_parent.TextStyleName
    @textstylename.setter
    def _(self, value):
        self.com_parent.TextStyleName = value

    @property
    def texttopattachmenttype(self):
        'Specifies how leaders on the top connect with the text'
        return AcVerticalTextAttachmentType(self.com_parent.TextTopAttachmentType)
    @texttopattachmenttype.setter
    def _(self, value: AcVerticalTextAttachmentType):
        self.com_parent.TextTopAttachmentType = value.value

    @property
    def textwidth(self):
        'Specifies the width of the Mtext'
        return self.com_parent.TextWidth
    @textwidth.setter
    def _(self, value):
        self.com_parent.TextWidth = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadMLine(POINTER(_dll.IAcadMLine), _ez_ptr):
    @property
    def coordinates(self):
        'Specifies the coordinates for each vertex in the object'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @property
    def justification(self):
        'Specifies the justification of the MLine'
        return AcMLineJustification(self.com_parent.Justification)
    @justification.setter
    def _(self, value: AcMLineJustification):
        self.com_parent.Justification = value.value

    @property
    def mlinescale(self):
        'Specifies the scale of the MLine'
        return self.com_parent.MLineScale
    @mlinescale.setter
    def _(self, value):
        self.com_parent.MLineScale = value

    @property
    def stylename(self):
        'Specifies the Mline style name'
        return self.com_parent.StyleName

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadMText(POINTER(_dll.IAcadMText), _ez_ptr):
    def fieldcode(self):
        'Returns the text string with field codes of the Mtext'
        return self.com_parent.FieldCode()

    @property
    def attachmentpoint(self):
        'Specifies both text height and text orientation by designating the endpoints of the baseline'
        return AcAttachmentPoint(self.com_parent.AttachmentPoint)
    @attachmentpoint.setter
    def _(self, value: AcAttachmentPoint):
        self.com_parent.AttachmentPoint = value.value

    @property
    def backgroundfill(self):
        'Specifies use Background mask'
        return self.com_parent.BackgroundFill
    @backgroundfill.setter
    def _(self, value):
        self.com_parent.BackgroundFill = value

    @property
    def drawingdirection(self):
        'Specifies the drawing direction of the Mtext'
        return AcDrawingDirection(self.com_parent.DrawingDirection)
    @drawingdirection.setter
    def _(self, value: AcDrawingDirection):
        self.com_parent.DrawingDirection = value.value

    @property
    def height(self):
        'Specifies the text height of the Mtext'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value

    @property
    def insertionpoint(self):
        'Specify the X, Y, Z coordinate for the insertion point of the Mtext or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value

    @property
    def linespacingdistance(self):
        'Specifies the line spacing distance of the Mtext'
        return self.com_parent.LineSpacingDistance
    @linespacingdistance.setter
    def _(self, value):
        self.com_parent.LineSpacingDistance = value

    @property
    def linespacingfactor(self):
        'Specifies the line spacing factor of the Mtext'
        return self.com_parent.LineSpacingFactor
    @linespacingfactor.setter
    def _(self, value):
        self.com_parent.LineSpacingFactor = value

    @property
    def linespacingstyle(self):
        'Specifies the line spacing style of the Mtext'
        return AcLineSpacingStyle(self.com_parent.LineSpacingStyle)
    @linespacingstyle.setter
    def _(self, value: AcLineSpacingStyle):
        self.com_parent.LineSpacingStyle = value.value

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value

    @property
    def rotation(self):
        'Specifies the rotation angle of the Mtext'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value):
        self.com_parent.Rotation = value

    @property
    def stylename(self):
        'Specifies the style name of the Mtext'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value):
        self.com_parent.StyleName = value

    @property
    def textstring(self):
        'Specifies the text string of the Mtext'
        return self.com_parent.TextString
    @textstring.setter
    def _(self, value):
        self.com_parent.TextString = value

    @property
    def width(self):
        'Specifies the defined width of the Mtext'
        return self.com_parent.Width
    @width.setter
    def _(self, value):
        self.com_parent.Width = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadOle(POINTER(_dll.IAcadOle), _ez_ptr):
    @property
    def height(self):
        'Specifies the height of the OLE object box'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value

    @property
    def insertionpoint(self):
        'Specifies the origin coordinates (upper left corner) of the OLE object'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value

    @property
    def lockaspectratio(self):
        'Ensures the width and height of the object stay in proportion'
        return self.com_parent.LockAspectRatio
    @lockaspectratio.setter
    def _(self, value):
        self.com_parent.LockAspectRatio = value

    @property
    def oleitemtype(self):
        'Specifies whether the OLE object is linked to the original pasted file when opening object for editing'
        return AcOleType(self.com_parent.OleItemType)
    @oleitemtype.setter
    def _(self, value: AcOleType):
        self.com_parent.OleItemType = value.value

    @property
    def oleplotquality(self):
        'Controls plot quality of OLE object based on file type selected from list'
        return AcOlePlotQuality(self.com_parent.OlePlotQuality)
    @oleplotquality.setter
    def _(self, value: AcOlePlotQuality):
        self.com_parent.OlePlotQuality = value.value

    @property
    def olesourceapp(self):
        'Application for editing OLE object'
        return self.com_parent.OleSourceApp
    @olesourceapp.setter
    def _(self, value):
        self.com_parent.OleSourceApp = value

    @property
    def rotation(self):
        'Specifies the rotation angle of the OLE object'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value):
        self.com_parent.Rotation = value

    @property
    def scaleheight(self):
        'Specifies the height of the object as a percentage of original height'
        return self.com_parent.ScaleHeight
    @scaleheight.setter
    def _(self, value):
        self.com_parent.ScaleHeight = value

    @property
    def scalewidth(self):
        'Specifies the width of the object as a percentage of original width'
        return self.com_parent.ScaleWidth
    @scalewidth.setter
    def _(self, value):
        self.com_parent.ScaleWidth = value

    @property
    def width(self):
        'Specifies the width of the OLE object box'
        return self.com_parent.Width
    @width.setter
    def _(self, value):
        self.com_parent.Width = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPViewport(POINTER(_dll.IAcadPViewport), _ez_ptr):
    def display(self, bStatus):
        'Determines whether viewport is On or Off'
        self.com_parent.Display(bStatus)

    def getgridspacing(self):
        'Specifies the grid spacing for the viewport'
        return self.com_parent.GetGridSpacing()

    def getsnapspacing(self):
        'Specifies the snap spacing for the viewport'
        return self.com_parent.GetSnapSpacing()

    def setgridspacing(self, XSpacing, YSpacing):
        'Sets the grid spacing for the viewport'
        self.com_parent.SetGridSpacing(XSpacing, YSpacing)

    def setsnapspacing(self, XSpacing, YSpacing):
        'Sets the snap spacing for the viewport'
        self.com_parent.SetSnapSpacing(XSpacing, YSpacing)

    def syncmodelview(self):
        'Updates the viewport parameters with the parameters in the associated model view.'
        self.com_parent.SyncModelView()

    @property
    def arcsmoothness(self):
        'Specifies the smoothness of circles, arcs, and ellipses'
        return self.com_parent.ArcSmoothness
    @arcsmoothness.setter
    def _(self, value):
        self.com_parent.ArcSmoothness = value

    @property
    def center(self):
        'Specify the X, Y, Z coordinate for the center of the viewport or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.Center
    @center.setter
    def _(self, value):
        self.com_parent.Center = value

    @property
    def clipped(self):
        'Specifies that standard viewport border is replaced with user defined boundary'
        return self.com_parent.Clipped

    @property
    def customscale(self):
        'Specifies the custom scale for the viewport'
        return self.com_parent.CustomScale
    @customscale.setter
    def _(self, value):
        self.com_parent.CustomScale = value

    @property
    def direction(self):
        'Specifies the viewing direction for a 3D visualization of the drawing'
        return self.com_parent.Direction
    @direction.setter
    def _(self, value):
        self.com_parent.Direction = value

    @property
    def displaylocked(self):
        'Determines whether viewport is in locked state or not'
        return self.com_parent.DisplayLocked
    @displaylocked.setter
    def _(self, value):
        self.com_parent.DisplayLocked = value

    @property
    def gridon(self):
        'Specifies the status of the viewport grid'
        return self.com_parent.GridOn
    @gridon.setter
    def _(self, value):
        self.com_parent.GridOn = value

    @property
    def hassheetview(self):
        'Specifies whether the viewport is linked to a corresponding sheet view'
        return self.com_parent.HasSheetView

    @property
    def height(self):
        'Specifies the height of the viewport'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value

    @property
    def labelblockid(self):
        'Returns and sets the label block id associated with the viewport.'
        return self.com_parent.LabelBlockId
    @labelblockid.setter
    def _(self, value):
        self.com_parent.LabelBlockId = value

    @property
    def layerpropertyoverrides(self):
        'Specifies whether the viewport has layer property overrides.'
        return self.com_parent.LayerPropertyOverrides

    @property
    def lenslength(self):
        'Specifies the lens length used in perspective viewing'
        return self.com_parent.LensLength
    @lenslength.setter
    def _(self, value):
        self.com_parent.LensLength = value

    @property
    def modelview(self):
        'Returns and sets the model view associated with the viewport.'
        return CastManager.cast(self.com_parent.ModelView)
    @modelview.setter
    def _(self, value):
        self.com_parent.ModelView = value

    @property
    def removehiddenlines(self):
        'Determines whether hidden line removal is On or Off'
        return self.com_parent.RemoveHiddenLines
    @removehiddenlines.setter
    def _(self, value):
        self.com_parent.RemoveHiddenLines = value

    @property
    def shadeplot(self):
        'Specifies the shade plot mode of the viewport'
        return self.com_parent.ShadePlot
    @shadeplot.setter
    def _(self, value):
        self.com_parent.ShadePlot = value

    @property
    def sheetview(self):
        'Returns and sets the sheet view associated with the viewport.'
        return CastManager.cast(self.com_parent.SheetView)
    @sheetview.setter
    def _(self, value):
        self.com_parent.SheetView = value

    @property
    def snapbasepoint(self):
        'Specifies the snap base point for the viewport'
        return self.com_parent.SnapBasePoint
    @snapbasepoint.setter
    def _(self, value):
        self.com_parent.SnapBasePoint = value

    @property
    def snapon(self):
        'Specifies the status of snap'
        return self.com_parent.SnapOn
    @snapon.setter
    def _(self, value):
        self.com_parent.SnapOn = value

    @property
    def snaprotationangle(self):
        'Specifies the snap rotation angle of the viewport relative to the current UCS'
        return self.com_parent.SnapRotationAngle
    @snaprotationangle.setter
    def _(self, value):
        self.com_parent.SnapRotationAngle = value

    @property
    def standardscale(self):
        'Specifies the standard scale for the viewport'
        return AcViewportScale(self.com_parent.StandardScale)
    @standardscale.setter
    def _(self, value: AcViewportScale):
        self.com_parent.StandardScale = value.value

    @property
    def standardscale2(self):
        'Specifies the standard scale for the viewport'
        return self.com_parent.StandardScale2
    @standardscale2.setter
    def _(self, value):
        self.com_parent.StandardScale2 = value

    @property
    def stylesheet(self):
        'Returns the style sheet to use'
        return self.com_parent.StyleSheet
    @stylesheet.setter
    def _(self, value):
        self.com_parent.StyleSheet = value

    @property
    def target(self):
        'Specifies the target point for the view or viewport'
        return self.com_parent.Target
    @target.setter
    def _(self, value):
        self.com_parent.Target = value

    @property
    def twistangle(self):
        'Specifies the twist angle for the viewport'
        return self.com_parent.TwistAngle
    @twistangle.setter
    def _(self, value):
        self.com_parent.TwistAngle = value

    @property
    def ucsiconatorigin(self):
        'Specifies if the UCS icon is displayed at the origin'
        return self.com_parent.UCSIconAtOrigin
    @ucsiconatorigin.setter
    def _(self, value):
        self.com_parent.UCSIconAtOrigin = value

    @property
    def ucsiconon(self):
        'Specifies if the UCS icon is on'
        return self.com_parent.UCSIconOn
    @ucsiconon.setter
    def _(self, value):
        self.com_parent.UCSIconOn = value

    @property
    def ucsperviewport(self):
        'Determines whether the UCS is saved with the viewport or not'
        return self.com_parent.UCSPerViewport
    @ucsperviewport.setter
    def _(self, value):
        self.com_parent.UCSPerViewport = value

    @property
    def viewporton(self):
        'Determines whether the viewport is On or Off'
        return self.com_parent.ViewportOn
    @viewporton.setter
    def _(self, value):
        self.com_parent.ViewportOn = value

    @property
    def visualstyle(self):
        'Specifies the visual style of the viewport'
        return self.com_parent.VisualStyle
    @visualstyle.setter
    def _(self, value):
        self.com_parent.VisualStyle = value

    @property
    def width(self):
        'Specifies the width of the viewport'
        return self.com_parent.Width
    @width.setter
    def _(self, value):
        self.com_parent.Width = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPoint(POINTER(_dll.IAcadPoint), _ez_ptr):
    @property
    def coordinates(self):
        'Specify the X, Y, Z coordinate for the position of the point or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value

    @property
    def thickness(self):
        'Specifies the thickness of the point'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value):
        self.com_parent.Thickness = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPointCloud(POINTER(_dll.IAcadPointCloud), _ez_ptr):
    @property
    def height(self):
        'Specifies the height of the point cloud.'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value

    @property
    def insertionpoint(self):
        'Specifies the insertion point of the point cloud.'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value

    @property
    def intensitycolorscheme(self):
        'Specifies the color scheme to use for displaying intensity values.'
        return AcPointCloudIntensityStyle(self.com_parent.IntensityColorScheme)
    @intensitycolorscheme.setter
    def _(self, value: AcPointCloudIntensityStyle):
        self.com_parent.IntensityColorScheme = value.value

    @property
    def length(self):
        'Specifies the length of the point cloud.'
        return self.com_parent.Length
    @length.setter
    def _(self, value):
        self.com_parent.Length = value

    @property
    def locked(self):
        'Specifies if the point cloud is locked.'
        return self.com_parent.Locked
    @locked.setter
    def _(self, value):
        self.com_parent.Locked = value

    @property
    def name(self):
        'Specifies the name of the point cloud file.'
        return self.com_parent.Name

    @property
    def path(self):
        'Specifies the path to the point cloud file.'
        return self.com_parent.Path

    @property
    def rotation(self):
        'Specifies the rotation angle of the point cloud.'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value):
        self.com_parent.Rotation = value

    @property
    def showclipped(self):
        'Enables or disables the clipping boundary of the point cloud.'
        return self.com_parent.ShowClipped
    @showclipped.setter
    def _(self, value):
        self.com_parent.ShowClipped = value

    @property
    def showintensity(self):
        """Specifies whether to display point cloud intensity using a shaded color scheme. 
        You can only see the intensity color mapping effect in 3D visual style and when hardware acceleration is on."""
        return self.com_parent.ShowIntensity
    @showintensity.setter
    def _(self, value):
        self.com_parent.ShowIntensity = value

    @property
    def stylization(self):
        'Specifies color stylization for selected point cloud.'
        return AcPointCloudStylizationType(self.com_parent.Stylization)
    @stylization.setter
    def _(self, value: AcPointCloudStylizationType):
        self.com_parent.Stylization = value.value

    @property
    def unit(self):
        'Specifies the unit of the point cloud file.'
        return self.com_parent.Unit

    @property
    def unitfactor(self):
        'Specifies insert unit factor of the point cloud file.'
        return self.com_parent.UnitFactor

    @property
    def useentitycolor(self):
        'Specifies the point cloud color source.'
        return AcPointCloudColorType(self.com_parent.UseEntityColor)
    @useentitycolor.setter
    def _(self, value: AcPointCloudColorType):
        self.com_parent.UseEntityColor = value.value

    @property
    def width(self):
        'Specifies the width of the point cloud.'
        return self.com_parent.Width
    @width.setter
    def _(self, value):
        self.com_parent.Width = value

    @property
    def scale(self):
        'Specifies the scale value of the point cloud.'
        return self.com_parent.Scale
    @scale.setter
    def _(self, value):
        self.com_parent.Scale = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPointCloudEx(POINTER(_dll.IAcadPointCloudEx), _ez_ptr):
    @property
    def colorscheme(self):
        'Specifies the color scheme to display point cloud.'
        return self.com_parent.ColorScheme
    @colorscheme.setter
    def _(self, value):
        self.com_parent.ColorScheme = value

    @property
    def geolocate(self):
        'Specifies if the point cloud is geolocated.'
        return self.com_parent.Geolocate
    @geolocate.setter
    def _(self, value):
        self.com_parent.Geolocate = value

    @property
    def insertionpoint(self):
        'Specifies the insertion point of the point cloud.'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value

    @property
    def locked(self):
        'Specifies if the point cloud is locked.'
        return self.com_parent.Locked
    @locked.setter
    def _(self, value):
        self.com_parent.Locked = value

    @property
    def name(self):
        'Specifies the name of the point cloud file.'
        return self.com_parent.Name
    @name.setter
    def _(self, value):
        self.com_parent.Name = value

    @property
    def path(self):
        'Specifies the path to the point cloud file.'
        return self.com_parent.Path

    @property
    def rotation(self):
        'Specifies the rotation angle of the point cloud.'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value):
        self.com_parent.Rotation = value

    @property
    def showcropped(self):
        'Specifies if the cropping is shown.'
        return self.com_parent.ShowCropped
    @showcropped.setter
    def _(self, value):
        self.com_parent.ShowCropped = value

    @property
    def stylization(self):
        'Specifies the point cloud color source.'
        return AcPointCloudExStylizationType(self.com_parent.Stylization)
    @stylization.setter
    def _(self, value: AcPointCloudExStylizationType):
        self.com_parent.Stylization = value.value

    @property
    def unit(self):
        'Specifies the unit of the point cloud file.'
        return self.com_parent.Unit

    @property
    def unitfactor(self):
        'Specifies insert unit factor of the point cloud file.'
        return self.com_parent.UnitFactor

    @property
    def scale(self):
        'Specifies the scale value of the point cloud.'
        return self.com_parent.Scale
    @scale.setter
    def _(self, value):
        self.com_parent.Scale = value

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPolyfaceMesh(POINTER(_dll.IAcadPolyfaceMesh), _ez_ptr):
    @indexedproperty
    def coordinate(self, Index):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[Index]
    @coordinate.setter
    def _(self, Index, value):
        self.com_parent.Coordinate[Index] = value

    @property
    def coordinates(self):
        'Specifies the vertices of the mesh'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @SetterProperty
    def faces(self, value):
        'None'
        self.com_parent.Faces = value
    
    #faces = property(None, faces)

    @property
    def numberoffaces(self):
        'Specifies the number of faces in the mesh'
        return self.com_parent.NumberOfFaces

    @property
    def numberofvertices(self):
        'Specifies the number of vertices in the mesh'
        return self.com_parent.NumberOfVertices

    # Inherits from AcadEntity
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid

# TODO: Add __new__ and others
class AcadPolygonMesh(POINTER(_dll.IAcadPolygonMesh), _ez_ptr):
    @indexedproperty
    def coordinate(self, Index):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[Index]
    @coordinate.setter
    def _(self, Index, value):
        self.com_parent.Coordinate[Index] = value

    @property
    def coordinates(self):
        'Specifies the vertices of the mesh'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value
    
    @property
    def mclose(self):
        'Specifies mesh style for M direction, Open or Closed'
        return self.com_parent.MClose
    @mclose.setter
    def _(self, value):
        self.com_parent.MClose = value
    
    @property
    def nclose(self):
        'Specifies mesh style for N direction, Open or Closed'
        return self.com_parent.NClose
    @nclose.setter
    def _(self, value):
        self.com_parent.NClose = value
    
    @property
    def mdensity(self):
        'Specifies M density value of the polygonmesh; valid values 3-201'
        return self.com_parent.MDensity
    @mdensity.setter
    def _(self, value):
        self.com_parent.MDensity = value
    
    @property
    def ndensity(self):
        'Specifies N density value of the polygonmesh; valid values 3-201'
        return self.com_parent.NDensity
    @ndensity.setter
    def _(self, value):
        self.com_parent.NDensity = value

    @property
    def mvertexcount(self):
        'Returns the M Vertex number of the polygonmesh'
        return self.com_parent.MVertexCount

    @property
    def nvertexcount(self):
        'Returns the N Vertex number of the polygonmesh'
        return self.com_parent.NVertexCount
    
    @property
    def type(self):
        'Specifies the type of the polygonmesh'
        return self.com_parent.Type
    @type.setter
    def _(self, value):
        self.com_parent.Type = value

    def appendvertex(self, vertex):
        'Appends a vertex to the polygonmesh'
        self.com_parent.AppendVertex(vertex)
    
    def explode(self):
        'Explodes the polygonmesh and returns the sub-entities as an array of object'
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadPolyline(POINTER(_dll.IAcadPolyline), _ez_ptr):
    @indexedproperty
    def coordinate(self, Index):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[Index]
    @coordinate.setter
    def _(self, Index, value):
        self.com_parent.Coordinate[Index] = value

    @property
    def coordinates(self):
        'Specifies the current vertex of the polyline'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value
    
    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value

    @property
    def thickness(self):
        'Specifies the thickness of the polyline'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value: float):
        self.com_parent.Thickness = value

    def AppendVertex(self, vertex):
        'Appends a vertex to the polyline'
        self.com_parent.AppendVertex(vertex)
    def explode(self):
        'Explodes the polyline and returns the sub-entities as an array of Object'
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret

    def getbulge(self, Index):
        'Returns the vertex bulge of the polyline'
        return self.com_parent.GetBulge(Index)

    def setbulge(self, Index, bulge):
        'Sets the vertex bulge of the polyline'
        self.com_parent.SetBulge(Index, bulge)
    
    def getwidth(self, Index):
        'Returns segment width of the polyline'
        return self.com_parent.GetWidth(Index)

    def setwidth(self, Index, StartWidth, EndWidth):
        'Sets the segment width of the polyline'
        self.com_parent.SetWidth(Index, StartWidth, EndWidth)

    @property
    def constantwidth(self):
        'Specifies the constant width for the polyline'
        return self.com_parent.ConstantWidth
    @constantwidth.setter
    def _(self, value):
        self.com_parent.ConstantWidth = value

    def offset(self, Distance: float):
        'Creates a new entity object by offsetting the polyline by a specified distance'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret

    @property
    def elevation(self):
        "Specifies the elevation of the polyline relative to the Z axis of the objects' coordinate system"
        return self.com_parent.Elevation
    @elevation.setter
    def _(self, value):
        self.com_parent.Elevation = value
    
    @property
    def type(self):
        'Applies a fit curve or spline type to a 2D polyline'
        return Ac3DPolylineType(self.com_parent.Type)
    @type.setter
    def _(self, value:Ac3DPolylineType):
        self.com_parent.Type = value.value
    
    @property
    def closed(self):
        'Determines whether polyline is Open or Closed. Closed draws a line segment from current position to starting point of the polyline.'
        return self.com_parent.Closed
    @closed.setter
    def _(self, value: bool):
        self.com_parent.Closed = value

    @property
    def linetypegeneration(self):
        'Generates linetype in a continuous pattern through the vertices of the polyline. When turned off, linetype is generated starting and ending with a dash at each vertex.'
        return self.com_parent.LinetypeGeneration
    @linetypegeneration.setter
    def _(self, value):
        self.com_parent.LinetypeGeneration = value
    
    @property
    def area(self):
        'Specifies the area of the polyline'
        return self.com_parent.Area
    
    @property
    def length(self):
        'Specifies the length of the polyline'
        return self.com_parent.Length

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadRasterImage(POINTER(_dll.IAcadRasterImage), _ez_ptr):
    @property
    def brightness(self):
        'Specifies the current brightness value of the raster image'
        return self.com_parent.Brightness
    @brightness.setter
    def _(self, value):
        self.com_parent.Brightness = value
        
    @property
    def contrast(self):
        'Specifies the current contrast value of the raster image'
        return self.com_parent.Contrast
    @contrast.setter
    def _(self, value):
        self.com_parent.Contrast = value
        
    @property
    def fade(self):
        'Specifies the current fade value of the raster image'
        return self.com_parent.Fade
    @fade.setter
    def _(self, value):
        self.com_parent.Fade = value

    @property
    def origin(self):
        'Specifies the origin coordinates (lower left corner) of the raster image'
        return self.com_parent.Origin
    @origin.setter
    def _(self, value):
        self.com_parent.Origin = value
    
    @property
    def rotation(self):
        'Specifies the rotation angle of the raster image'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value: float):
        self.com_parent.Rotation = value
    
    @property
    def imagewidth(self):
        'Specifies the width of the raster image'
        return self.com_parent.ImageWidth
    @imagewidth.setter
    def _(self, value: float):
        self.com_parent.ImageWidth = value
    
    @property
    def imageheight(self):
        'Specifies the height of the raster image'
        return self.com_parent.ImageHeight
    @imageheight.setter
    def _(self, value: float):
        self.com_parent.ImageHeight = value
    
    @property
    def name(self):
        'Specifies the name of the image file'
        return self.com_parent.Name
    @name.setter
    def _(self, value: str):
        self.com_parent.Name = value
    
    @property
    def imagefile(self):
        'Specifies the path to the image file'
        return self.com_parent.ImageFile
    @imagefile.setter
    def _(self, value: str):
        self.com_parent.ImageFile = value
        
    @property
    def imagevisibility(self):
        'Determines whether image is visible or not'
        return self.com_parent.ImageVisibility
    @imagevisibility.setter
    def _(self, value):
        self.com_parent.ImageVisibility = value
        
    @property
    def clippingenabled(self):
        'Enables or disables the clipping boundary of the image'
        return self.com_parent.ClippingEnabled
    @clippingenabled.setter
    def _(self, value):
        self.com_parent.ClippingEnabled = value
        
    @property
    def transparency(self):
        'Determines whether transparency for a bitonal image is On or Off'
        return self.com_parent.Transparency
    @transparency.setter
    def _(self, value):
        self.com_parent.Transparency = value
        
    def clipboundary(self, value):
        self.com_parent.ClipBoundary(value)
        
    @property
    def height(self):
        'Height of the attribute, shape, text, or view toolbar or the main application window'
        return self.com_parent.Height
        
    @property
    def width(self):
        'Specifies the width of the text boundary, view, image, toolbar, or main application window'
        return self.com_parent.Width
        
    @property
    def showrotation(self):
        'Determines if a raster image is displayed at its rotation value'
        return self.com_parent.ShowRotation
    @showrotation.setter
    def _(self, value):
        self.com_parent.ShowRotation = value
        
    @property
    def scalefactor(self):
        'Specifies the scale factor of the raster image'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value):
        self.com_parent.ScaleFactor = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadRay(POINTER(_dll.IAcadRay), _ez_ptr):
    @property
    def basepoint(self):
        'Specify the X, Y, Z coordinate of the basepoint of the ray or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.BasePoint
    @basepoint.setter
    def _(self, value):
        self.com_parent.BasePoint = value
        
    @property
    def secondpoint(self):
        'Specify the X, Y, Z coordinate of the second point of the ray or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.SecondPoint
    @secondpoint.setter
    def _(self, value):
        self.com_parent.SecondPoint = value
        
    @property
    def directionvector(self):
        'Specify the X, Y, Z direction vectors of the ray'
        return self.com_parent.DirectionVector
    @directionvector.setter
    def _(self, value):
        self.com_parent.DirectionVector = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadRegion(POINTER(_dll.IAcadRegion), _ez_ptr):
    @property
    def area(self):
        'Specifies the area of the region'
        return self.com_parent.Area
        
    @property
    def centroid(self):
        'Gets the center of area or mass for a region or solid'
        return self.com_parent.Centroid
        
    @property
    def momentofinertia(self):
        'Gets the moment of inertia for the solid'
        return self.com_parent.MomentOfInertia
        
    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
        
    @property
    def perimeter(self):
        'Specifies the perimeter of the region'
        return self.com_parent.Perimeter
        
    @property
    def principaldirections(self):
        'Gets the principal directions of the solid or region'
        return self.com_parent.PrincipalDirections
        
    @property
    def principalmoments(self):
        'Gets the principal moments property of the solid or region'
        return self.com_parent.PrincipalMoments
        
    @property
    def productofinertia(self):
        'Gets the product of inertia of the solid or region'
        return self.com_parent.ProductOfInertia
        
    @property
    def radiiofgyration(self):
        'Gets the radius of gyration of the solid or region'
        return self.com_parent.RadiiOfGyration
        
    def boolean(self, Operation, Object):
        'Perform a Boolean operation against another region.'
        self.com_parent.Boolean(Operation, Object)
    def explode(self):
        'Explodes the 3dPolyline.'
        ret = []
        for obj in self.com_parent.Explode():
            ret.append(CastManager.cast(obj))
        return ret

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadSection(POINTER(_dll.IAcadSection), _ez_ptr):
    @property
    def name(self):
        'Specifies section object name'
        return self.com_parent.Name
    @name.setter
    def _(self, value):
        self.com_parent.Name = value

    @property
    def state(self):
        'Specifies section object type'
        return self.com_parent.State
    @state.setter
    def _(self, value):
        self.com_parent.State = value

    @property
    def viewingdirection(self):
        'Specifies the viewing direction for the section plane'
        return self.com_parent.ViewingDirection
    @viewingdirection.setter
    def _(self, value):
        self.com_parent.ViewingDirection = value

    @property
    def verticaldirection(self):
        'Specifies the vertical direction for the section plane'
        return self.com_parent.VerticalDirection
    @verticaldirection.setter
    def _(self, value):
        self.com_parent.VerticalDirection = value

    @property
    def normal(self):
        'Specifies normal for the section plane'
        return self.com_parent.Normal

    @property
    def livesectionenabled(self):
        'Turns live section on or off for this section object'
        return self.com_parent.LiveSectionEnabled
    @livesectionenabled.setter
    def _(self, value):
        self.com_parent.LiveSectionEnabled = value

    @property
    def indicatortransparency(self):
        'Specifies transparency of section plane when shading is turned on'
        return self.com_parent.IndicatorTransparency
    @indicatortransparency.setter
    def _(self, value):
        self.com_parent.IndicatorTransparency = value

    @property
    def indicatorfillcolor(self):
        'Specifies color of section plane when shading is turned on'
        return self.com_parent.IndicatorFillColor
    @indicatorfillcolor.setter
    def _(self, value):
        self.com_parent.IndicatorFillColor = value

    @property
    def elevation(self):
        'Specifies elevation of section plane line'
        return self.com_parent.Elevation
    @elevation.setter
    def _(self, value):
        self.com_parent.Elevation = value

    @property
    def topheight(self):
        "Specifies elevation of section plane top extents relative to the object's elevation"
        return self.com_parent.TopHeight
    @topheight.setter
    def _(self, value):
        self.com_parent.TopHeight = value

    @property
    def bottomheight(self):
        "Specifies elevation of section plane bottom extents relative to the object's elevation"
        return self.com_parent.BottomHeight
    @bottomheight.setter
    def _(self, value):
        self.com_parent.BottomHeight = value

    @property
    def numvertices(self):
        'Gets the number of vertices in the section line'
        return self.com_parent.NumVertices

    @property
    def vertices(self):
        'Gets the vertices in the section line'
        return self.com_parent.Vertices
    @vertices.setter
    def _(self, value):
        self.com_parent.Vertices = value
        
    @indexedproperty
    def coordinate(self, index: int):
        'Specifies the co-ordinate of the specified vertex'
        return self.com_parent.Coordinate[index]
    @coordinate.setter
    def _(self, index: int, value):
        self.com_parent.Coordinate[index] = value

    def addvertex(self, nIndex, val):
        'Adds a new vertex to the section line'
        self.com_parent.AddVertex(nIndex, val)

    def removevertex(self, nIndex):
        'Removes a vertex in the section line'
        self.com_parent.RemoveVertex(nIndex)

    def hittest(self, varPtHit):
        'Does hit test on section plane'
        # TODO: fix this
        pHit = POINTER(VARIANT_BOOL)()
        pSegmentIndex = POINTER(c_int)()
        pPtOnSegment = POINTER(VARIANT)()
        pSubItem = POINTER(AcSectionSubItem)()
        self.com_parent.RemoveVertex(varPtHit, pHit, pSegmentIndex, pPtOnSegment, pSubItem)
        return pHit, pSegmentIndex, pPtOnSegment, pSubItem

    def createjog(self, varPt):
        'Creates a jog on the section plane'
        self.com_parent.CreateJog(varPt)
        
    @property
    def settings(self, index: int):
        'Gets the section settings object'
        return CastManager.cast(self.com_parent.Settings)

    def generatesectiongeometry(self, pEntity):
        'Generates 2D or 3D section geometry'
        # TODO: fix this
        pIntersectionBoundaryObjs = POINTER(VARIANT)()
        pIntersectionFillObjs = POINTER(VARIANT)()
        pBackgroudnObjs = POINTER(VARIANT)()
        pForegroudObjs = POINTER(VARIANT)()
        pCurveTangencyObjs = POINTER(VARIANT)()
        self.com_parent.GenerateSectionGeometry(
            pEntity,
            pIntersectionBoundaryObjs,
            pIntersectionFillObjs,
            pBackgroudnObjs,
            pForegroudObjs,
            pCurveTangencyObjs
        )

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadShape(POINTER(_dll.IAcadShape), _ez_ptr):
    @property
    def insertionpoint(self):
        'Specify X, Y, Z coordinate for the insertion point of the shape or use the Pick Point button to set X, Y, Z values simultaneously'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value
    
    @property
    def name(self):
        'Specifies the name of the shape'
        return self.com_parent.Name
    @name.setter
    def _(self, value):
        self.com_parent.Name = value
    
    @property
    def height(self):
        'Specifies the height of the shape'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value
    
    @property
    def rotation(self):
        'Specifies the rotation angle of the shape'
        return self.com_parent.Rotation
    @rotation.setter
    def _(self, value):
        self.com_parent.Rotation = value
    
    @property
    def scalefactor(self):
        'Specifies the width scale factor of the shape'
        return self.com_parent.ScaleFactor
    @scalefactor.setter
    def _(self, value):
        self.com_parent.ScaleFactor = value
    
    @property
    def obliqueangle(self):
        'Specifies the oblique angle of the shape'
        return self.com_parent.ObliqueAngle
    @obliqueangle.setter
    def _(self, value):
        self.com_parent.ObliqueAngle = value
    
    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value
    
    @property
    def thickness(self):
        'Specifies the thickness of the shape'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value):
        self.com_parent.Thickness = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadSolid(POINTER(_dll.IAcadSolid), _ez_ptr):
    @indexedproperty
    def coordinate(self, index: int):
        'Specifies the coordinate of a single vertex in the object'
        return self.com_parent.Coordinate[index]
    @coordinate.setter
    def _(self, index: int, value):
        self.com_parent.Coordinate[index] = value
    
    @property
    def coordinates(self):
        'Specifies the current vertex of the solid'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value

    @property
    def normal(self):
        'Specifies the three-dimensional normal unit vector for the entity'
        return self.com_parent.Normal
    @normal.setter
    def _(self, value):
        self.com_parent.Normal = value
    
    @property
    def thickness(self):
        'Specifies the thickness of the solid'
        return self.com_parent.Thickness
    @thickness.setter
    def _(self, value):
        self.com_parent.Thickness = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid


class AcadSpline(POINTER(_dll.IAcadSpline), _ez_ptr):
    @property
    def numberofcontrolpoints(self):
        'Specifies the number of control points of the spline'
        return self.com_parent.NumberOfControlPoints
    
    @property
    def controlpoints(self):
        'Specifies the current control point of the spline'
        return self.com_parent.ControlPoints
    @controlpoints.setter
    def _(self, value):
        self.com_parent.ControlPoints = value

    @property
    def numberoffitpoints(self):
        'Specifies the number of fit points of the spline'
        return self.com_parent.NumberOfFitPoints
    
    @property
    def fitpoints(self):
        'Specifies the current fit point of the spline'
        return self.com_parent.FitPoints
    @fitpoints.setter
    def _(self, value):
        self.com_parent.FitPoints = value

    @property
    def degree(self):
        'Specifies the degree of the spline'
        return self.com_parent.Degree

    @property
    def closed(self):
        'Specifies whether the spline is open or closed'
        return self.com_parent.Closed

    @property
    def isplanar(self):
        'Determines the whether the spline is planar'
        return self.com_parent.IsPlanar

    @property
    def isrational(self):
        'Determines if the given spline is planar'
        return self.com_parent.IsRational

    @property
    def isperiodic(self):
        'Determines if the given spline is periodic'
        return self.com_parent.IsPeriodic
    
    @property
    def starttangent(self):
        'Specify the X, Y, Z coordinate for start tangent of the spline'
        return self.com_parent.StartTangent
    @starttangent.setter
    def _(self, value):
        self.com_parent.StartTangent = value
    
    @property
    def endtangent(self):
        'Specify the X, Y, Z coordinate for end tangent of the spline'
        return self.com_parent.EndTangent
    @endtangent.setter
    def _(self, value):
        self.com_parent.EndTangent = value
    
    @property
    def fittolerance(self):
        'Specifies the fit tolerance of the spline'
        return self.com_parent.FitTolerance
    @fittolerance.setter
    def _(self, value):
        self.com_parent.FitTolerance = value

    @property
    def area(self):
        'Specifies the area of the spline'
        return self.com_parent.Area
    
    def setcontrolpoint(self, Index, controlPoint):
        'Sets the indexed control point of the spline at a specified point'
        self.com_parent.SetControlPoint(Index, controlPoint)
    def getcontrolpoint(self, Index):
        'Returns the control point of the spline at a given index'
        return self.com_parent.GetControlPoint(Index)
    
    def setfitpoint(self, Index, fitPoint):
        'Sets the indexed fit point of the spline at a specified point'
        self.com_parent.SetFitPoint(Index, fitPoint)
    def getfitpoint(self, Index):
        'Returns the fit point of the spline at a given index'
        return self.com_parent.GetFitPoint(Index)
    
    def setweight(self, Index, weight):
        'Sets the weight of the spline at a given control point index'
        self.com_parent.SetWeight(Index, weight)
    def getweight(self, Index):
        'Returns the weight of the spline at a given control point index'
        return self.com_parent.GetWeight(Index)
    
    def addfitpoint(self, Index, fitPoint):
        'Adds the fit point to the spline at a given index'
        self.com_parent.AddFitPoint(Index, fitPoint)
    def deletefitpoint(self, Index):
        'Deletes the fit point of the spline at a given index'
        return self.com_parent.DeleteFitPoint(Index)
    
    def elevateorder(self, Order):
        'Elevates the order of the spline'
        return self.com_parent.ElevateOrder(Order)
        
    def offset(self, Distance: float):
        'Creates a new entity object by offsetting the spline by a given value'
        ret = []
        for obj in self.com_parent.Offset(Distance):
            ret.append(CastManager.cast(obj))
        return ret
    
    def purgefitdata(self):
        'Purges the fit data of the spline'
        self.com_parent.PurgeFitData()
    def reverse(self):
        'Reverses the direction of the spline'
        self.com_parent.Reverse()
    
    @property
    def knots(self):
        'Gets the knot vector for a spline'
        return self.com_parent.Knots
    @knots.setter
    def _(self, value):
        self.com_parent.Knots = value
    
    @property
    def weights(self):
        'Gets the weight vector for spline'
        return self.com_parent.Weights
    @weights.setter
    def _(self, value):
        self.com_parent.Weights = value
    
    @property
    def knotparameterization(self):
        'Specifies knot spacing when spline was created'
        return self.com_parent.KnotParameterization
    @knotparameterization.setter
    def _(self, value):
        self.com_parent.KnotParameterization = value
    
    @property
    def splineframe(self):
        'Specifies whether displaying the CV Hull for spline'
        return self.com_parent.SplineFrame
    @splineframe.setter
    def _(self, value):
        self.com_parent.SplineFrame = value
    
    @property
    def degree2(self):
        'Specifies the degree of the spline'
        return self.com_parent.Degree2
    @degree2.setter
    def _(self, value):
        self.com_parent.Degree2 = value
    
    @property
    def closed2(self):
        'Specifies whether the spline is open or closed'
        return self.com_parent.Closed2
    @closed2.setter
    def _(self, value):
        self.com_parent.Closed2 = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadSubDMesh(POINTER(_dll.IAcadSubDMesh), _ez_ptr):
    @property
    def smoothness(self):
        'Specifies the smoothing level for the mesh'
        return self.com_parent.Smoothness
    @smoothness.setter
    def _(self, value):
        self.com_parent.Smoothness = value

    @indexedproperty
    def coordinate(self, index: int):
        'Returns the coordinate of the vertex at a given index'
        return self.com_parent.Coordinate[index]
    @coordinate.setter
    def _(self, index: int, value):
        self.com_parent.Coordinate[index] = value
    
    @property
    def coordinates(self):
        'Specifies the current vertex on the mesh'
        return self.com_parent.Coordinates
    @coordinates.setter
    def _(self, value):
        self.com_parent.Coordinates = value
    
    @property
    def vertexcount(self):
        'Specifies the number of vertices for the unsmooth mesh'
        return self.com_parent.VertexCount
    
    @property
    def facecount(self):
        'Specifies the number of faces for the unsmooth mesh'
        return self.com_parent.FaceCount

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
    

class AcadSurface(POINTER(_dll.IAcadSurface), _ez_ptr):
    @property
    def surfacetype(self):
        'Indicates the type of surface'
        return self.com_parent.SurfaceType
    
    @property
    def uisolinedensity(self):
        'Specifies the number of U isolines that are displayed'
        return self.com_parent.UIsolineDensity
    @uisolinedensity.setter
    def _(self, value):
        self.com_parent.UIsolineDensity = value
    
    @property
    def visolinedensity(self):
        'Specifies the number of V isolines that are displayed'
        return self.com_parent.VIsolineDensity
    @visolinedensity.setter
    def _(self, value):
        self.com_parent.VIsolineDensity = value
    
    @property
    def wireframetype(self):
        'Specifies the wireframe type of the selected surface'
        return self.com_parent.WireframeType
    @wireframetype.setter
    def _(self, value):
        self.com_parent.WireframeType = value
    
    @property
    def maintainassociativity(self):
        'Indicates if the surface is associated with another surface and also allows you to turn off associativity'
        return self.com_parent.MaintainAssociativity
    @maintainassociativity.setter
    def _(self, value):
        self.com_parent.MaintainAssociativity = value
    
    @property
    def showassociativity(self):
        'Higlights dependent surfaces'
        return self.com_parent.ShowAssociativity
    @showassociativity.setter
    def _(self, value):
        self.com_parent.ShowAssociativity = value
    
    @property
    def edgeextensiondistances(self):
        'Indicates the extension distances of the edges'
        return self.com_parent.EdgeExtensionDistances
    @edgeextensiondistances.setter
    def _(self, value):
        self.com_parent.EdgeExtensionDistances = value
    
    @property
    def surftrimassociativity(self):
        'Specifies whether or not the Mtext is annotative'
        return self.com_parent.SurfTrimAssociativity
    @surftrimassociativity.setter
    def _(self, value):
        self.com_parent.SurfTrimAssociativity = value

    # Inherits from AcadEntity TODO: ---
    arraypolar = AcadEntity.arraypolar
    arrayrectangular = AcadEntity.arrayrectangular
    copy = AcadEntity.copy
    getboundingbox = AcadEntity.getboundingbox
    highlight = AcadEntity.highlight
    intersectwith = AcadEntity.intersectwith
    mirror = AcadEntity.mirror
    mirror3d = AcadEntity.mirror3d
    move = AcadEntity.move
    rotate = AcadEntity.rotate
    rotate3d = AcadEntity.rotate3d
    scaleentity = AcadEntity.scaleentity
    transformby = AcadEntity.transformby
    update = AcadEntity.update
    entityname = AcadEntity.entityname
    entitytransparency = AcadEntity.entitytransparency
    entitytype = AcadEntity.entitytype
    hyperlinks = AcadEntity.hyperlinks
    layer = AcadEntity.layer
    linetype = AcadEntity.linetype
    linetypescale = AcadEntity.linetypescale
    lineweight = AcadEntity.lineweight
    material = AcadEntity.material
    plotstylename = AcadEntity.plotstylename
    truecolor = AcadEntity.truecolor
    visible = AcadEntity.visible
    color = AcadEntity.color
    delete = AcadEntity.delete
    erase = AcadEntity.erase
    getextensiondictionary = AcadEntity.getextensiondictionary
    getxdata = AcadEntity.getxdata
    setxdata = AcadEntity.setxdata
    application = AcadEntity.application
    database = AcadEntity.database
    document = AcadEntity.document
    handle = AcadEntity.handle
    hasextensiondictionary = AcadEntity.hasextensiondictionary
    objectid = AcadEntity.objectid
    objectname = AcadEntity.objectname
    ownerid = AcadEntity.ownerid
        
        
class AcadTable(POINTER(_dll.IAcadTable), _ez_ptr):
    @property
    def stylename(self):
        'Specifies the style name of the Table'
        return self.com_parent.StyleName
    @stylename.setter
    def _(self, value):
        self.com_parent.StyleName = value
        
    @property
    def rows(self):
        'Specifies the rows in the Table'
        return self.com_parent.Rows
    @rows.setter
    def _(self, value):
        self.com_parent.Rows = value
        
    @property
    def columns(self):
        'Specifies the columns in the Table'
        return self.com_parent.Columns
    @columns.setter
    def _(self, value):
        self.com_parent.Columns = value
        
    @property
    def flowdirection(self):
        'Specifies the Table flow direction'
        return self.com_parent.FlowDirection
    @flowdirection.setter
    def _(self, value):
        self.com_parent.FlowDirection = value
        
    @property
    def width(self):
        'Specifies the Table width'
        return self.com_parent.Width
    @width.setter
    def _(self, value):
        self.com_parent.Width = value
        
    @property
    def height(self):
        'Specifies the Table height'
        return self.com_parent.Height
    @height.setter
    def _(self, value):
        self.com_parent.Height = value
        
    @property
    def vertcellmargin(self):
        'Specifies the vertical distance between text and edge of cell'
        return self.com_parent.VertCellMargin
    @vertcellmargin.setter
    def _(self, value):
        self.com_parent.VertCellMargin = value
        
    @property
    def horzcellmargin(self):
        'Specifies the horizontal distance between text and edge of cell'
        return self.com_parent.HorzCellMargin
    @horzcellmargin.setter
    def _(self, value):
        self.com_parent.HorzCellMargin = value
        
    @property
    def insertionpoint(self):
        'Specifies the insertion point of the table'
        return self.com_parent.InsertionPoint
    @insertionpoint.setter
    def _(self, value):
        self.com_parent.InsertionPoint = value
    
    def getcolumnwidth(self, col):
        'Returns the column width for the specified column.'
        return self.com_parent.GetColumnWidth(col)
    def setcolumnwidth(self, col, Width):
        'Sets the column width for the specified column.'
        self.com_parent.SetColumnWidth(col, Width)
    @property
    def columnwidth(self):
        'Sets the uniform column width for all the columns in the table.'
        return Exception("ColumnWidth only setter!")
    @columnwidth.setter
    def _(self, value)
        'Specifies the insertion point of the table'
        self.com_parent.ColumnWidth = value
    
    def getrowheight(self, col):
        'Returns the row height for the specified row.'
        return self.com_parent.GetRowHeight(col)
    def setrowheight(self, col, Height):
        'Sets the row height for the specified row.'
        self.com_parent.SetRowHeight(col, Height)
    @property
    def rowheight(self):
        'Sets the uniform row height for all the rows in the table.'
        return Exception("RowHeight only setter!")
    @rowheight.setter
    def _(self, value)
        'Specifies the insertion point of the table'
        self.com_parent.RowHeight = value
    
    def getminimumcolumnwidth(self, col):
        'Gets the minimum column width for the specified column.'
        return self.com_parent.GetMinimumColumnWidth(col)
    def getminimumrowheight(self, col):
        'Gets the minimum row height for the specified row.'
        return self.com_parent.GetMinimumRowHeight(col)
    
    @property
    def minimumtablewidth(self):
        'Gets the minimum width for the table.'
        return self.com_parent.MinimumTableWidth
    
    @property
    def minimumtableheight(self):
        'Gets the minimum height for the table.'
        return self.com_parent.MinimumTableHeight
        
    @property
    def direction(self):
        'Specifies the direction vector of the table'
        return self.com_parent.Direction
    @direction.setter
    def _(self, value):
        self.com_parent.Direction = value
        
    @property
    def titlesuppressed(self):
        'Returns and sets the title suppressed flag value.'
        return self.com_parent.TitleSuppressed
    @titlesuppressed.setter
    def _(self, value):
        self.com_parent.TitleSuppressed = value
        
    @property
    def headersuppressed(self):
        'Returns and sets the header suppressed flag value.'
        return self.com_parent.HeaderSuppressed
    @headersuppressed.setter
    def _(self, value):
        self.com_parent.HeaderSuppressed = value
    
    def getalignment(self, rowType):
        'Returns the cell alignment for the specified row type.'
        return self.com_parent.GetAlignment(rowType)
    def setalignment(self, rowType, cellAlignment):
        'Sets the cell alignment for the specified row types.'
        self.com_parent.SetAlignment(rowType, cellAlignment)
    
    def getbackgroundcolornone(self, rowType):
        'Returns the backgroundColorNone flag value for the specified row type.'
        return self.com_parent.GetBackgroundColorNone(rowType)
    def setbackgroundcolornone(self, rowType, bValue):
        'Sets the backgroundColorNone flag value for the specified row types.'
        self.com_parent.SetBackgroundColorNone(rowType, bValue)
    
    def getbackgroundcolor(self, rowType):
        'Returns the background true color value for the specified row type.'
        return self.com_parent.GetBackgroundColor(rowType)
    def setbackgroundcolor(self, rowType, pColor):
        'Sets the background true color value for the specified row types.'
        self.com_parent.SetBackgroundColor(rowType, pColor)
    
    def getcontentcolor(self, rowType):
        'Returns the true color value for the specified row type.'
        return self.com_parent.GetContentColor(rowType)
    def setcontentcolor(self, rowType, pColor):
        'Sets the true color value for the specified row types.'
        self.com_parent.SetContentColor(rowType, pColor)
    
    def gettextstyle(self, rowType):
        'Returns the text style name for the specified row type.'
        return self.com_parent.GetTextStyle(rowType)
    def settextstyle(self, rowType, bstrName):
        'Sets the text style name for the specified row types.'
        self.com_parent.SetTextStyle(rowType, bstrName)
    
    def gettextheight(self, rowType):
        'Returns the text height for the specified row type.'
        return self.com_parent.GetTextHeight(rowType)
    def settextheight(self, rowTypes, TextHeight):
        'Sets the text height for the specified row types.'
        self.com_parent.SetTextHeight(rowTypes, TextHeight)
    
    def getgridlineweight(self, gridLineType, rowType):
        'Returns the gridLineWeight value for the specified gridLineType and row type.'
        return self.com_parent.GetGridLineWeight(gridLineType, rowType)
    def setgridlineweight(self, gridLineTypes, rowTypes, Lineweight):
        'Sets the gridLineWeight value for the specified gridLineType(s) and row type(s).'
        self.com_parent.SetGridLineWeight(gridLineTypes, rowTypes, Lineweight)
    
    def getgridcolor(self, gridLineType, rowType):
        'Returns the gridColor value for the specified gridLineType and row type.'
        return self.com_parent.GetGridColor(gridLineType, rowType)
    def setgridcolor(self, gridLineTypes, rowTypes, pColor):
        'Sets the gridColor value for the specified gridLineType(s) and row type(s).'
        self.com_parent.SetGridColor(gridLineTypes, rowTypes, pColor)
    
    def getgridvisibility(self, gridLineType, rowType):
        'Returns the gridVisibility value for the specified gridLineType and row type.'
        return self.com_parent.GetGridVisibility(gridLineType, rowType)
    def setgridvisibility(self, gridLineTypes, rowTypes, bValue):
        'Sets the gridVisibility value for the specified gridLineType(s) and row type(s).'
        self.com_parent.SetGridVisibility(gridLineTypes, rowTypes, bValue)
        
    @property
    def tablestyleoverrides(self):
        'Returns the tableStyleOverrides.'
        return self.com_parent.TableStyleOverrides
    
    def cleartablestyleoverrides(self, flag):
        'Clears the tableStyleOverrides.'
        self.com_parent.ClearTableStyleOverrides(flag)
    
    def getcelltype(self, row, col):
        'Gets the cell type for the specified row and column.'
        return self.com_parent.GetCellType(row, col)
    def setcelltype(self, row, col, CellType):
        'Sets the cell type for the specified row and column.'
        self.com_parent.SetCellType(row, col, CellType)
    
    def getcellextents(self, row, col, bOuterCell):
        'Gets the cell extents for the specified row and column.'
        return self.com_parent.GetCellExtents(row, col, bOuterCell)
    
    def getattachmentpoint(self, row, col):
        'Gets the attachment point for the specified row and column.'
        return self.com_parent.GetAttachmentPoint(row, col)
    
    def getcellalignment(self, row, col):
        'Returns the alignment for the specified row and column.'
        return self.com_parent.GetCellAlignment(row, col)
    def setcellalignment(self, row, col, cellAlignment):
        'Sets the cell alignment for the specified row and column.'
        self.com_parent.SetCellAlignment(row, col, cellAlignment)
    
    def getcellbackgroundcolornone(self, row, col):
        'Returns the backgroundColorNone flag value for the specified row and column.'
        return self.com_parent.GetCellBackgroundColorNone(row, col)
    def setcellbackgroundcolornone(self, row, col, bValue):
        'Sets the backgroundColorNone flag value for the specified row and column.'
        self.com_parent.SetCellBackgroundColorNone(row, col, bValue)
    
    def getcellcontentcolor(self, row, col):
        'Returns the true color value for the specified row and column.'
        return self.com_parent.GetCellContentColor(row, col)
    def setcellcontentcolor(self, row, col, pColor):
        'Sets the true color value for the specified row and column.'
        self.com_parent.SetCellContentColor(row, col, pColor)
    
    def getcellstyleoverrides(self, row, col):
        'Returns the cellStyleOverrides.'
        return self.com_parent.GetCellStyleOverrides(row, col)
        
    def deletecellcontent(self, row, col):
        'Deletes the cell content for the specified row and column.'
        self.com_parent.DeleteCellContent(row, col)
        
    def getrowtype(self, row):
        'Gets the row type for the specified row.'
        return self.com_parent.GetRowType(row)
        
    def gettext(self, row, col):
        'Returns the text value value for the specified row and column.'
        return self.com_parent.GetText(row, col)
    def settext(self, row, col, pStr):
        'Sets the text value value for the specified row and column.'
        self.com_parent.SetText(row, col, pStr)
        
    def getcelltextstyle(self, row, col):
        'Returns the text style name for the specified row and column.'
        return self.com_parent.GetCellTextStyle(row, col)
    def setcelltextstyle(self, row, col, bstrName):
        'Sets the text style name for the specified row and column.'
        self.com_parent.SetCellTextStyle(row, col, bstrName)
        
    def getcelltextheight(self, row, col):
        'Returns the text height for the specified row and column.'
        return self.com_parent.GetCellTextHeight(row, col)
    def setcelltextheight(self, row, col, TextHeight):
        'Sets the text height for the specified row and column.'
        self.com_parent.SetCellTextHeight(row, col, TextHeight)
        
    def gettextrotation(self, row, col):
        'Returns the text rotation for the specified row and column.'
        return self.com_parent.GetTextRotation(row, col)
    def settextrotation(self, row, col, TextRotation):
        'Sets the text rotation for the specified row and column.'
        self.com_parent.SetTextRotation(row, col, TextRotation)
        
    def getautoscale(self, row, col):
        'Returns the auto scale flag value for the specified row and column.'
        return self.com_parent.GetAutoScale(row, col)
    def setautoscale(self, row, col, bValue):
        'Sets the auto scale flag value for the specified row and column.'
        self.com_parent.SetAutoScale(row, col, bValue)
        
    def getblocktablerecordid(self, row, col):
        'Returns the block table record id associated to the block-type cell.'
        return self.com_parent.GetBlockTableRecordId(row, col)
    def setblocktablerecordid(self, row, col, blkId, bAutoFit):
        'Sets the block table record id associated to the block-type cell.'
        self.com_parent.SetBlockTableRecordId(row, col, blkId, bAutoFit)
        
    def getblockscale(self, row, col):
        'Returns the block scale value for the specified row and column.'
        return self.com_parent.GetBlockScale(row, col)
    def setblockscale(self, row, col, blkScale):
        'Sets the block scale value for the specified row and column.'
        self.com_parent.SetBlockScale(row, col, blkScale)
        
    def getblockrotation(self, row, col):
        'Returns the block rotation for the specified row and column.'
        return self.com_parent.GetBlockRotation(row, col)
    def setblockrotation(self, row, col, blkRotation):
        'Sets the block rotation for the specified row and column.'
        self.com_parent.SetBlockRotation(row, col, blkRotation)
        
    def getblockattributevalue(self, row, col, attdefId):
        'Returns the attribute value from the Specified block cell for the attribute definition object contained in the block.'
        return self.com_parent.GetBlockAttributeValue(row, col, attdefId)
    def setblockattributevalue(self, row, col, attdefId, bstrValue):
        'Sets the attribute value to the Specified block cell for the attribute definition object contained in the block.'
        self.com_parent.SetBlockAttributeValue(row, col, attdefId, bstrValue)
        
    def getcellgridlineweight(self, row, col, edge):
        'Returns the gridLineWeight value for the given edge of specified row and column.'
        return self.com_parent.GetCellGridLineWeight(row, col, edge)
    def setcellgridlineweight(self, row, col, edge, Lineweight):
        'Sets the gridLineWeight value for the given edges of specified row and column.'
        self.com_parent.SetCellGridLineWeight(row, col, edge, Lineweight)
        
    def getcellgridcolor(self, row, col, edge):
        'Returns the gridColor value for the given edge of specified row and column.'
        return self.com_parent.GetCellGridColor(row, col, edge)
    def setcellgridcolor(self, row, col, edges, pColor):
        'Sets the gridColor value for the given edges of specified row and column.'
        self.com_parent.SetCellGridColor(row, col, edges, pColor)
        
    def getcellgridvisibility(self, row, col, edge):
        'Returns the gridVisibility value for the given edge of specified row and column.'
        return self.com_parent.GetCellGridVisibility(row, col, edge)
    def setcellgridvisibility(self, row, col, edges, bValue):
        'Sets the gridVisibility value for the given edges of specified row and column.'
        self.com_parent.SetCellGridVisibility(row, col, edges, bValue)
        
    def insertcolumns(self, col, Width, cols):
        'Inserts the column(s) of specified width.'
        self.com_parent.InsertColumns(col, Width, cols)
    def deletecolumns(self, col, cols):
        'deletes the column(s) from the specified column index.'
        self.com_parent.DeleteColumns(col, cols)
        
    def insertrows(self, row, Height, Rows):
        'Inserts the row(s) of specified height.'
        self.com_parent.InsertRows(row, Height, Rows)
    def deleterows(self, row, Rows):
        'deletes the row(s) from the specified row index.'
        self.com_parent.DeleteRows(row, Rows)
        
    def mergecells(self, minRow, maxRow, minCol, maxCol):
        'merge cells.'
        self.com_parent.MergeCells(minRow, maxRow, minCol, maxCol)
    def unmergecells(self, minRow, maxRow, minCol, maxCol):
        'UnmergeCells'
        self.com_parent.UnmergeCells(minRow, maxRow, minCol, maxCol)
        
    def ismergedcell(self, row, col):
        'is Merged Cell.'
        # TODO: ---
        minRow = c_int()
        maxRow = c_int()
        minCol = c_int()
        maxCol = c_int()
        ret = self.com_parent.IsMergedCell(row, col, minRow, maxRow, minCol, maxCol)
        return ret, minRow.value, maxRow.value, minCol.value, maxCol.value
    
    def getfieldid(self, row, col):
        'Returns the field object id associated to the specifed cell.'
        return self.com_parent.GetFieldId(row, col)
    def setfieldid(self, row, col, fieldId):
        'Sets the field object id in the specifed cell.'
        return self.com_parent.SetFieldId(row, col, fieldId)
        
    def generatelayout(self):
        'Generate layout.'
        self.com_parent.GenerateLayout()
    
    def recomputetableblock(self, bForceUpdate):
        'Recompute TableBlock.'
        self.com_parent.RecomputeTableBlock(bForceUpdate)
        
    def hittest(self, wpt, wviewVec):
        'Hit test.'
        # TODO: ---
        resultRowIndex = c_int()
        resultColumnIndex = c_int()
        ret = self.com_parent.HitTest(wpt, wviewVec, resultRowIndex, resultColumnIndex)
        return ret, resultRowIndex.value, resultColumnIndex.value
    
    def select(self, wpt, wvwVec, wvwxVec, wxaper, wyaper, allowOutside):
        'Select.'
        return self.com_parent.Select(wpt, wvwVec, wvwxVec, wxaper, wyaper, allowOutside)
        
    def selectsubregion(self, wpt1, wpt2, wvwVec, wvwxVec, seltype, bIncludeCurrentSelection):
        return self.com_parent.SelectSubRegion(wpt1, wpt2, wvwVec, wvwxVec, seltype, bIncludeCurrentSelection)
        "Select SubRegion."
    
    def reselectsubregion(self):
        "Re select SubRegion."
        self.com_parent.ReselectSubRegion()
    
    def getsubselection(self):
        "GetSubSelection."
        return self.com_parent.GetSubSelection()
    
    def setsubselection(self, rowMin, rowMax, colMin, colMax):
        "SetSubSelection."
        self.com_parent.SetSubSelection(rowMin, rowMax, colMin, colMax)
    
    def clearsubselection(self):
        "ClearSubSelection."
        self.com_parent.ClearSubSelection()
    
    @property
    def hassubselection(self):
        'HasSubSelection.'
        return self.com_parent.HasSubSelection
    
    @property
    def regeneratetablesuppressed(self):
        'Enables or disables the regeneration of table block'
        return self.com_parent.RegenerateTableSuppressed
    @regeneratetablesuppressed.setter
    def _(self, value):
        'Enables or disables the regeneration of table block'
        self.com_parent.RegenerateTableSuppressed = value
    
    def getdatatype(self, rowType):
        "Gets the row data type and unit type for the specified row type."
        return self.com_parent.GetDataType(rowType)
    
    def setdatatype(self, rowTypes, dataType, unitType):
        "Sets the row data type and unit type for the specified row type."
        self.com_parent.SetDataType(rowTypes, dataType, unitType)
    
    def getformat(self, rowType):
        "Gets the format for the specified row type."
        return self.com_parent.GetFormat(rowType)
    
    def setformat(self, rowTypes, pFormat):
        "Sets the format for the specified row type."
        self.com_parent.SetFormat(rowTypes, pFormat)
    
    def formatvalue(self, row, col, nOption):
        "Gets the formatted text string for the specified row and column."
        return self.com_parent.FormatValue(row, col, nOption)
    
    def getcelldatatype(self, row, col):
        "Gets the cell data type and unit type for the specified row and column."
        return self.com_parent.GetCellDataType(row, col)
    
    def setcelldatatype(self, row, col, dataType, unitType):
        "Sets the cell data type and unit type for the specified row and column."
        self.com_parent.SetCellDataType(row, col, dataType, unitType)
    
    def getcellformat(self, row, col):
        "Gets the cell format for the specified row and column."
        return self.com_parent.GetCellFormat(row, col)
    
    def setcellformat(self, row, col, pFormat):
        "Sets the cell format for the specified row and column."
        self.com_parent.SetCellFormat(row, col, pFormat)
    
    def getcellvalue(self, row, col):
        "Gets the cell value for the specified row and column."
        return self.com_parent.GetCellValue(row, col)
    
    def setcellvalue(self, row, col, val):
        "Sets the cell value for the specified row and column."
        self.com_parent.SetCellValue(row, col, val)
    
    def setcellvaluefromtext(self, row, col, val, nOption):
        "Sets the cell value by parsing the text for the specified row and column."
        self.com_parent.SetCellValueFromText(row, col, val, nOption)
    
    def resetcellvalue(self, row, col):
        "Resets the cell value for the specified row and column."
        self.com_parent.ResetCellValue(row, col)
    
    def isempty(self, nRow, nCol):
        "Checks if the content of the specified cell is empty."
        return self.com_parent.IsEmpty(row, col)
    
    def createcontent(self, nRow, nCol, nIndex):
        "Creates new content in a cell"
        return self.com_parent.CreateContent(nRow, nCol, nIndex)
    
    def movecontent(self, nRow, nCol, nFromIndex, nToIndex):
        "Moves a content in a cell from one position to another position within the cell"
        self.com_parent.MoveContent(nRow, nCol, nFromIndex, nToIndex)
    
    def deletecontent(self, nRow, nCol):
        "Deletes a content from a cell"
        self.com_parent.DeleteContent(nRow, nCol)
    
    def getvalue(self, nRow, nCol, nContent):
        "Gets the cell value for the specified row and column and nContent."
        return self.com_parent.GetValue(nRow, nCol, nContent)
    
    def setvalue(self, nRow, nCol, nContent, acValue):
        "Sets the cell value by parsing the text for the specified row and column and nContent."
        self.com_parent.SetValue(nRow, nCol, nContent, acValue)
        
    def setvaluefromtext(self, nRow, nCol, nContent, szText, nOption):
        "Sets the value of the content at the specified content index."
        self.com_parent.SetValueFromText(nRow, nCol, nContent, szText, nOption)
    
    def getdataformat(self, nRow, nCol, nContent):
        "Gets the cell format for the specified row and column and nContent."
        return self.com_parent.GetDataFormat(nRow, nCol, nContent)
    
    def setdataformat(self, nRow, nCol, nContent, szFormat):
        "Sets the cell format for the specified row and column and nContent."
        self.com_parent.SetDataFormat(nRow, nCol, nContent, szFormat)
    
    def gettextstring(self, nRow, nCol, nContent):
        "Gets the text value value for the specified row and column  and nContent."
        return self.com_parent.GetTextString(nRow, nCol, nContent)
    
    def settextstring(self, nRow, nCol, nContent, Text):
        "Sets the text value value for the specified row and column."
        self.com_parent.SetTextString(nRow, nCol, nContent, Text)
    
    def getfieldid2(self, nRow, nCol, nContent):
        "Returns the field object id associated to the specifed cell  and nContent."
        return self.com_parent.GetFieldId2(nRow, nCol, nContent)
    
    def setfieldid2(self, nRow, nCol, nContent, acDbObjectId, nflag):
        "Sets  the field object id associated to the specifed cell  and nContent."
        self.com_parent.SetFieldId2(nRow, nCol, nContent, acDbObjectId, nflag)
    
    
    
    
    
    
    
    def enablemergeall(self, nRow, nCol, bEnable):
        "Enables or disables the merge all flag in row or column."
    def getautoscale2(self, nRow, nCol, nContent):
        "Returns the auto scale flag value for the specified row and column  and nContent."
    def getblockattributevalue2(self, nRow, nCol, nContent, blkId):
        "Returns the attribute value from the Specified block cell for the attribute definition object contained in the block  and nContent."
    def getblocktablerecordid2(self, nRow, nCol, nContent):
        "Gets the block table record id associated to the block-type cell  and nContent."
    def getbreakheight(self, nIndex):
        "Returns the break height of the specified table when table breaking is enabled."
    def getcellbackgroundcolor(self, row, col):
        "Returns the background true color value for the specified row and column."
    def getcellstate(self, nRow, nCol):
        "Gets the cell state."
    def getcellstyle(self, nRow, nCol):
        "Gets the cell style of cell, row, or column."
    def getcolumnname(self, nIndex):
        "Gets the columns name."
    def getcontentcolor2(self, nRow, nCol, nContent):
        "Returns the true color value for the specified row type  and nContent."
    def getcontentlayout(self, row, col):
        "Gets the content layout of the cell."
    def getcontenttype(self, nRow, nCol):
        "Gets the content type of the content at the specified content index."
    def getcustomdata(self, nRow, nCol, szKey):
        "Gets the custom data value set in cell, row, or column."
    def getdatatype2(self, nRow, nCol, nContent):
        "Gets the row data type and unit type for the specified row type  and nContent."
    def getformula(self, nRow, nCol, nContent):
        "Gets the formula if the content at the specified content index has a formula."
    def getgridcolor2(self, nRow, nCol, nGridLineType):
        "Returns the gridColor value for the specified gridLineType and row type  and nContent."
    def getgriddoublelinespacing(self, nRow, nCol, nGridLineType):
        "Gets the grid double line spacing from cell, row, or column"
    def getgridlinestyle(self, nRow, nCol, nGridLineType):
        "Gets the grid line style of cell, row, or column."
    def getgridlinetype(self, nRow, nCol, nGridLineType):
        "Gets the grid line type of cell, row, or column."
    def getgridlineweight2(self, nRow, nCol, nGridLineType):
        "Gets the gridLineWeight value for the specified gridLineType(s) and row type(s)   and nContent."
    def getgridvisibility2(self, nRow, nCol, nGridLineType):
        "Returns the gridVisibility value for the specified gridLineType and row type."
    def gethasformula(self, nRow, nCol, nContent):
        "Returns true if the content at the specified index is a formula."
    def getmargin(self, nRow, nCol, nMargin):
        "Gets the margin of cell, row, or column."
    def getoverride(self, nRow, nCol, nContent):
        "Gets the override in cell, row, column, or content."
    def getrotation(self, nRow, nCol, nContent):
        "Gets the rotation angle of the content at the specified content index."
    def getscale(self, nRow, nCol, nContent):
        "Gets the scale of the content at the specified content index."
    def gettextheight2(self, nRow, nCol, nContent):
        "Returns the text height for the specified row and column  and nContent."
    def gettextstyle2(self, nRow, nCol, nContent):
        "Gets the text style name for the specified row and column  and nContent."
    def insertcolumnsandinherit(self, col, nInheritFrom, nNumCols):
        "Inserts one or more columns at the specified index and inherits the column properties from specified column."
    def insertrowsandinherit(self, nIndex, nInheritFrom, nNumRows):
        "Inserts one or more rows at the specified index and inherits the row properties from specified row."
    def iscontenteditable(self, nRow, nCol):
        "Checks if the content of the specified cell can be modified."
    def isformateditable(self, nRow, nCol):
        "Checks if the format of the specified cell can be modified."
    def ismergeallenabled(self, nRow, nCol):
        "Returns whether merge all flag is enabled or not in row or column."
    def removealloverrides(self, nRow, nCol):
        "Removes all the overrides in cell, row, or column."
    def setautoscale2(self, nRow, nCol, nContent, bAutoFit):
        "Sets the auto scale flag value for the specified row and column  and nContent."
    def setblockattributevalue2(self, nRow, nCol, nContent, blkId, Value):
        "Sets the attribute value from the Specified block cell for the attribute definition object contained in the block  and nContent."
    def setblocktablerecordid2(self, nRow, nCol, nContent, blkId, autoFit):
        "Sets the block table record id associated to the block-type cell  and nContent."
    def setbreakheight(self, nIndex, Height):
        "Sets the break height of the specified table when table breaking is enabled."
    def setcellbackgroundcolor(self, row, col, pColor):
        "Sets the background true color value for the specified row and column."
    def setcellstate(self, nRow, nCol, nLock):
        "Sets the cell state."
    def setcellstyle(self, nRow, nCol, szCellStyle):
        "Sets the the cell style of cell, row, or column."
    def setcolumnname(self, nIndex, Name):
        "Sets the columns name."
    def setcontentcolor2(self, nRow, nCol, nContent, pColor):
        "Sets the true color value for the specified row type  and nContent."
    def setcontentlayout(self, row, col, nLayout):
        "Sets the content layout of the cell."
    def setcustomdata(self, nRow, nCol, szKey, data):
        "Sets the custom data value set in cell, row, or column."
    def setdatatype2(self, nRow, nCol, nContent, dataType, unitType):
        "Sets the row data type and unit type for the specified row type  and nContent."
    def setformula(self, nRow, nCol, nContent, pszFormula):
        "Sets the formula at the specified content index."
    def setgridcolor2(self, nRow, nCol, nGridLineType, pColor):
        "Sets the gridColor value for the specified gridLineType and row type  and nContent."
    def setgriddoublelinespacing(self, nRow, nCol, nGridLineType, fSpacing):
        "Sets the grid double line spacing in cell, row, or column."
    def setgridlinestyle(self, nRow, nCol, nGridLineTypes, nLineStyle):
        "Sets the grid line style of cell, row, or column."
    def setgridlinetype(self, nRow, nCol, nGridLineType, idLinetype):
        "Sets the grid line type of cell, row, or column."
    def setgridlineweight2(self, nRow, nCol, nGridLineType, Lineweight):
        "Sets the gridLineWeight value for the specified gridLineType(s) and row type(s)   and nContent."
    def setgridvisibility2(self, nRow, nCol, nGridLineType, bVisible):
        "Sets the gridVisibility value for the specified gridLineType and row type."
    def setmargin(self, nRow, nCol, nMargins, fMargin):
        "Sets the margin of cell, row, or column."
    def setoverride(self, nRow, nCol, nContent, nProp):
        "Sets the override in cell, row, column, or content."
    def setrotation(self, nRow, nCol, nContent, Value):
        "Sets the rotation angle of the content at the specified content index."
    def setscale(self, nRow, nCol, nContent, scale):
        "Sets the scale of the content at the specified content index."
    def settextheight2(self, nRow, nCol, nContent, Height):
        "Gets the text height for the specified row and column  and nContent."
    def settextstyle2(self, nRow, nCol, nContent, bstrStyleName):
        "Sets the text style name for the specified row and column  and nContent."
    def settooltip(self, nRow, nCol, tip):
        "Sets the tooltip string for cell, row, or column."

    
    
        

'''
class IAcadText(IAcadEntity):
class IAcadTolerance(IAcadEntity):
class IAcadTrace(IAcadEntity):
class IAcadUnderlay(IAcadEntity):
class IAcadXline(IAcadEntity):
'''

# for debugging
if __name__ == "__main__":
    pass









