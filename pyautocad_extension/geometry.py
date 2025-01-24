from comtypes import POINTER
from comtypes.automation import VARIANT
from indexedproperty import indexedproperty
from ctypes.wintypes import VARIANT_BOOL
from ctypes import c_int
from pyautocad import *

try:
	from .stubs import (Acad3DSolid, AcadRegion, AcadAcCmColor,
	AcadView, AcadSectionSettings) # TODO: recheck this
except:
	from stubs import (Acad3DSolid, AcadRegion, AcadAcCmColor,
	AcadView, AcadSectionSettings) # TODO: recheck this
try:
	from .utils import (_ez_ptr, CastManager, SetterProperty,
	A3Vertex, A3Vertexes, A2Vertex, A2Vertexes,
	get_obj_block_source)
except:
	from utils import (_ez_ptr, CastManager, SetterProperty,
	A3Vertex, A3Vertexes, A2Vertex, A2Vertexes,
	get_obj_block_source)
try:
	from .api import acad_dll
except:
	from api import acad_dll
try:
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
except:
	from enums import (
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
try:
	from .objects import AcadEntity
except:
	from objects import AcadEntity
_dll = acad_dll.dll


def __get_source(source):
	"Get ModelSpace or PaperSpace form Application if not specified"
	from app import AcadApplication
	if source is None:
		source = AcadApplication()
	if isinstance(source, AcadApplication):
		source = source.ModelSpace
	return source


'''
TODO list:
	1. Add all geometry entities
	2. Convert tagVARIANT and other COM-types to python-types:
		A3Vertex(es)
		A2Vertex(es)
		int to Enums
	3. Add support for ByRef inputs/outputs for classes
	4. Add inherits methods and props from AcadEntity and  other
	5. Add __new__ for entities
	6. Add aliases for long_name_functions
	7. Add overloads
	9999. Tests
'''

"""
For some reason inheritance doesn't work in this case. So you have to copy methods and props directly

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
"""


class Acad3DFace(POINTER(_dll.IAcad3DFace), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcad3DFace
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcad3DFace VBA-class wrapped as Acad3DFace python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__ +
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	def __new__(cls, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex, Point4: A3Vertex, source=None):
		return get_obj_block_source(source).add3dface(Point1, Point2, Point3, Point4)
	# Methods
	def getinvisibleedge(self, Index: int) -> bool:
		"Gets the visibility status for the edge."
		# TODO: Check arguments
		# ['in'] Index:int 1-4
		# ['out', 'retval'] bVisible:bool
		# VBA: bVisible = object.GetInvisibleEdge (Index)
		return self.com_parent.GetInvisibleEdge(Index)

	def setinvisibleedge(self, Index: int, State: bool):
		"Sets the visibility of the edge."
		# ['in'] Index:int
		# ['in'] State:bool
		# VBA: object.SetInvisibleEdge Index, State
		self.com_parent.SetInvisibleEdge(Index, State)

	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object. Index from 1 to 4"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the current vertex of the 3D face"
		# TODO: Check arguments
		# ['out', 'retval'] corners:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, corners:A3Vertexes):
		# TODO: Check arguments
		# ['in'] corners:tagVARIANT | A3Vertexes
		if len(corners) >= 4:
			self.com_parent.Coordinates = corners[:4]
		else:
			pp = A3Vertexes()

	@property
	def visibilityedge1(self) -> bool:
		"Determines whether 3DFace Edge 1 is visible or hidden"
		# TODO: Check arguments
		# ['out', 'retval'] visibility:bool
		return self.com_parent.VisibilityEdge1
	@visibilityedge1.setter
	def _(self, visibility:bool):
		# ['in'] visibility:bool
		self.com_parent.VisibilityEdge1 = visibility

	@property
	def visibilityedge2(self) -> bool:
		"Determines whether 3DFace Edge 2 is visible or hidden"
		# TODO: Check arguments
		# ['out', 'retval'] visibility:bool
		return self.com_parent.VisibilityEdge2
	@visibilityedge2.setter
	def _(self, visibility:bool):
		# ['in'] visibility:bool
		self.com_parent.VisibilityEdge2 = visibility

	@property
	def visibilityedge3(self) -> bool:
		"Determines whether 3DFace Edge 3 is visible or hidden"
		# TODO: Check arguments
		# ['out', 'retval'] visibility:bool
		return self.com_parent.VisibilityEdge3
	@visibilityedge3.setter
	def _(self, visibility:bool):
		# ['in'] visibility:bool
		self.com_parent.VisibilityEdge3 = visibility

	@property
	def visibilityedge4(self) -> bool:
		"Determines whether 3DFace Edge 4 is visible or hidden"
		# TODO: Check arguments
		# ['out', 'retval'] visibility:bool
		return self.com_parent.VisibilityEdge4
	@visibilityedge4.setter
	def _(self, visibility:bool):
		# ['in'] visibility:bool
		self.com_parent.VisibilityEdge4 = visibility
	
	# Get/set coordinate array-like
	def __getitem__(self, index:int):
		return self.coordinate[index]
	def __setitem__(self, index:int, val:A3Vertex):
		self.coordinate[i] = val
	
	# Inherits
	# AcadEntity methods
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
	# AcadEntity props
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
	# AcadObject method
	delete = AcadEntity.delete
	erase = AcadEntity.erase
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	setxdata = AcadEntity.setxdata
	# AcadObject props
	application = AcadEntity.application
	database = AcadEntity.database
	document = AcadEntity.document
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	

class Acad3DPolyline(POINTER(_dll.IAcad3DPolyline), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcad3DPolyline
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcad3DPolyline VBA-class wrapped as Acad3DPolyline python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__ +
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	def __new__(cls, PointsArray: A3Vertexes, source=None):
		return get_obj_block_source(source).add3dpoly(PointsArray)
	# Methods
	def appendvertex(self, vertex: A3Vertex):
		"Appends a vertex to the 3dPolyline."
		# TODO: Check arguments
		# ['in'] vertex:tagVARIANT | A3Vertex
		# VBA: object.AppendVertex vertex
		self.com_parent.AppendVertex(vertex)

	def explode(self) -> list:
		"Explodes the 3dPolyline."
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT | A3Vertex
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret
		

	# Properties
	@property
	def closed(self) -> bool:
		"Determines whether the 3D polyline is open or closed"
		# TODO: Check arguments
		# ['out', 'retval'] fClose:bool
		return self.com_parent.Closed
	@closed.setter
	def _(self, fClose:bool):
		# ['in'] fClose:bool
		self.com_parent.Closed = fClose

	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the current vertex of the 3D Polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = Coordinates.flatten

	@property
	def length(self) -> float:
		"Specifies the length of the 3D polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Length

	@property
	def type(self) -> int:
		"Specifies the type of line or surface curve fitting"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.Type
	@type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Type = Type

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


class Acad3DSolid(POINTER(_dll.IAcad3DSolid), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcad3DSolid
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcad3DSolid VBA-class wrapped as Acad3DSolid python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Methods
	def boolean(self, Operation: int, SolidObject: Acad3DSolid):
		"Performs a boolean operation against another 3dsolid."
		# TODO: Check arguments
		# ['in'] Operation:int
		# ['in'] SolidObject:Acad3DSolid
		# VBA: object.Boolean Operation, SolidObject
		self.com_parent.Boolean(Operation, SolidObject)

	def checkinterference(self, Object: Acad3DSolid, CreateInterferenceSolid: bool):
		"Check interference for the 3dsolid object."
		# TODO: Check arguments
		# ['in'] Object:Acad3DSolid
		# ['in'] CreateInterferenceSolid:bool
		# ['out'] SolidsInterfere:bool
		# ['out', 'retval'] pIntSolid:Acad3DSolid
		# VBA: pIntSolid = object.CheckInterference (Object, CreateInterferenceSolid, SolidsInterfere)
		return self.com_parent.CheckInterference(Object, CreateInterferenceSolid)

	def sectionsolid(self, Point1: A3Vertex, Point2: A3Vertex, point3: A3Vertex) -> AcadRegion:
		"Create a section of the 3dsolid given three points that define the plane. Returns the Section as a Region object"
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT | A3Vertex
		# ['in'] Point2:tagVARIANT | A3Vertex
		# ['in'] point3:tagVARIANT | A3Vertex
		# ['out', 'retval'] pRegion:AcadRegion
		# VBA: pRegion = object.SectionSolid (Point1, Point2, point3)
		return self.com_parent.SectionSolid(Point1, Point2, point3)

	def slicesolid(self, Point1: A3Vertex, Point2: A3Vertex, point3: A3Vertex, Negative: bool) -> Acad3DSolid:
		"Create a slice of the 3dsolid given three points that define the plane. Returns the resulting array of 3dSolid object. "
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT | A3Vertex
		# ['in'] Point2:tagVARIANT | A3Vertex
		# ['in'] point3:tagVARIANT | A3Vertex
		# ['in'] Negative:bool
		# ['out', 'retval'] pNegSideSolid:Acad3DSolid
		# VBA: pNegSideSolid = object.SliceSolid (Point1, Point2, point3, Negative)
		return self.com_parent.SliceSolid(Point1, Point2, point3, Negative)

	# Properties
	@property
	def centroid(self) -> A3Vertex:
		"Gets the center of area or mass for a region or solid"
		# TODO: Check arguments
		# ['out', 'retval'] Centroid:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Centroid)

	@property
	def history(self) -> bool:
		"Specifies whether history is saved"
		# TODO: Check arguments
		# ['out', 'retval'] bHistory:bool
		return self.com_parent.History
	@history.setter
	def _(self, bHistory:bool):
		# ['in'] bHistory:bool
		self.com_parent.History = bHistory

	@property
	def momentofinertia(self) -> A3Vertex:
		"Gets the moment of inertia for the solid"
		# TODO: Check arguments
		# ['out', 'retval'] momentInertia:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.MomentOfInertia)

	@property
	def position(self) -> A3Vertex:
		"Specifies the X, Y, Z coordinate for center of the base or center of the solid"
		# TODO: Check arguments
		# ['out', 'retval'] Position:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Position)
	@position.setter
	def _(self, Position:A3Vertex):
		# TODO: Check arguments
		# ['in'] Position:tagVARIANT | A3Vertex
		self.com_parent.Position = Position

	@property
	def principaldirections(self) -> A3Vertex:
		"Gets the principal directions of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prinDir:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.PrincipalDirections)

	@property
	def principalmoments(self) -> A3Vertex:
		"Gets the principal moments property of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prinMoments:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.PrincipalMoments)

	@property
	def productofinertia(self) -> A3Vertex:
		"Gets the product of inertia of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prodInertia:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ProductOfInertia)

	@property
	def radiiofgyration(self) -> A3Vertex:
		"Gets the radius of gyration of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] radiiGyration:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.RadiiOfGyration)

	@property
	def showhistory(self) -> bool:
		"Specifies whether to show history of the solid"
		# TODO: Check arguments
		# ['out', 'retval'] Position:bool
		return self.com_parent.ShowHistory
	@showhistory.setter
	def _(self, Position:bool):
		# ['in'] Position:bool
		self.com_parent.ShowHistory = Position

	@property
	def solidtype(self) -> str:
		"Indicates the type of solid"
		# TODO: Check arguments
		# ['out', 'retval'] SolidType:str
		return self.com_parent.SolidType

	@property
	def volume(self) -> float:
		"Gets the volume of the solid"
		# TODO: Check arguments
		# ['out', 'retval'] Volume:float
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


class AcadArc(POINTER(_dll.IAcadArc), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadArc
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadArc VBA-class wrapped as AcadArc python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Methods
	def offset(self, Distance: float) -> list:
		"Offsets the arc to the given side"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT | list
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return e

	# Properties
	@property
	def arclength(self) -> float:
		"Specifies the arc length of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] ArcLength:float
		return self.com_parent.ArcLength

	@property
	def area(self) -> float:
		"Specifies the area of the arc when implicitly closed with a line"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def center(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the center point of the arc or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] CenterPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Center)
	@center.setter
	def _(self, CenterPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] CenterPoint:tagVARIANT | A3Vertex
		self.com_parent.Center = CenterPoint

	@property
	def endangle(self) -> float:
		"Specifies the end angle of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.EndAngle
	@endangle.setter
	def _(self, Angle:float):
		# ['in'] Angle:float
		self.com_parent.EndAngle = Angle

	@property
	def endpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the end point of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] EndPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.EndPoint)

	@property
	def normal(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the normal direction vector"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def radius(self) -> float:
		"Specifies the radius of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] Radius:float
		return self.com_parent.Radius
	@radius.setter
	def _(self, Radius:float):
		# ['in'] Radius:float
		self.com_parent.Radius = Radius

	@property
	def startangle(self) -> float:
		"Specifies the start angle of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.StartAngle
	@startangle.setter
	def _(self, Angle:float):
		# ['in'] Angle:float
		self.com_parent.StartAngle = Angle

	@property
	def startpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the start point of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] StartPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.StartPoint)

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

	@property
	def totalangle(self) -> float:
		"Specifies the total angle of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] TotalAngle:float
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


class AcadAttribute(POINTER(_dll.IAcadAttribute), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadAttribute
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadAttribute VBA-class wrapped as AcadAttribute python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	# Methods
	def updatemtextattribute(self):
		"Updates multiline MText"
		# VBA: object.UpdateMTextAttribute 
		self.com_parent.UpdateMTextAttribute()

	# Properties
	@property
	def alignment(self) -> int:
		"Specifies both text height and text orientation by designating the endpoints of the baseline"
		# TODO: Check arguments
		# ['out', 'retval'] align:int |ENUM?
		return self.com_parent.Alignment
	@alignment.setter
	def _(self, align:int):
		# ['in'] align:int
		self.com_parent.Alignment = align

	@property
	def backward(self) -> bool:
		"Determines whether the text is backward or not"
		# TODO: Check arguments
		# ['out', 'retval'] bBackward:bool
		return self.com_parent.Backward
	@backward.setter
	def _(self, bBackward:bool):
		# ['in'] bBackward:bool
		self.com_parent.Backward = bBackward

	@property
	def constant(self) -> bool:
		"Specifies the constant mode of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bConstant:bool
		return self.com_parent.Constant
	@constant.setter
	def _(self, bConstant:bool):
		# ['in'] bConstant:bool
		self.com_parent.Constant = bConstant

	@property
	def fieldlength(self) -> int:
		"Specifies the field length of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] fieldLen:int
		return self.com_parent.FieldLength
	@fieldlength.setter
	def _(self, fieldLen:int):
		# ['in'] fieldLen:int
		self.com_parent.FieldLength = fieldLen

	@property
	def height(self) -> float:
		"Specifies the height of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def horizontalalignment(self) -> int:
		"Specifies the horizontal alignment of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] horizAlign:int | ENUM?
		return self.com_parent.HorizontalAlignment
	@horizontalalignment.setter
	def _(self, horizAlign:int):
		# ['in'] horizAlign:int
		self.com_parent.HorizontalAlignment = horizAlign

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the insertion point of the text"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def invisible(self) -> bool:
		"Specifies the invisible mode of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bInvisible:bool
		return self.com_parent.Invisible
	@invisible.setter
	def _(self, bInvisible:bool):
		# ['in'] bInvisible:bool
		self.com_parent.Invisible = bInvisible

	@property
	def lockposition(self) -> bool:
		"Specifies whether the attribute may be moved relative to the geometry in the block"
		# TODO: Check arguments
		# ['out', 'retval'] bLockPosition:bool
		return self.com_parent.LockPosition
	@lockposition.setter
	def _(self, bLockPosition:bool):
		# ['in'] bLockPosition:bool
		self.com_parent.LockPosition = bLockPosition

	@property
	def mode(self) -> int:
		"Specifies the mode of the attribute definition"
		# TODO: Check arguments
		# ['out', 'retval'] Mode:int | ENUM?
		return self.com_parent.Mode
	@mode.setter
	def _(self, Mode:int):
		# ['in'] Mode:int
		self.com_parent.Mode = Mode

	@property
	def mtextattribute(self) -> bool:
		"Determines whether if the attribute is multiline"
		# TODO: Check arguments
		# ['out', 'retval'] bMTextAttribute:bool
		return self.com_parent.MTextAttribute
	@mtextattribute.setter
	def _(self, bMTextAttribute:bool):
		# ['in'] bMTextAttribute:bool
		self.com_parent.MTextAttribute = bMTextAttribute

	@property
	def mtextattributecontent(self) -> str:
		"Gets the multiline attribute content"
		# TODO: Check arguments
		# ['out', 'retval'] content:str
		return self.com_parent.MTextAttributeContent
	@mtextattributecontent.setter
	def _(self, content:str):
		# ['in'] content:str
		self.com_parent.MTextAttributeContent = content

	@property
	def mtextboundarywidth(self) -> float:
		"Gets the width of text boundary of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] boundaryWidth:float
		return self.com_parent.MTextBoundaryWidth
	@mtextboundarywidth.setter
	def _(self, boundaryWidth:float):
		# [] boundaryWidth:float
		self.com_parent.MTextBoundaryWidth = boundaryWidth

	@property
	def mtextdrawingdirection(self) -> int:
		"Gets the drawing direction of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] drawDir:int
		return self.com_parent.MTextDrawingDirection
	@mtextdrawingdirection.setter
	def _(self, drawDir:int):
		# ['in'] drawDir:int
		self.com_parent.MTextDrawingDirection = drawDir

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def obliqueangle(self) -> float:
		"Specifies the oblique angle of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] obliAngle:float
		return self.com_parent.ObliqueAngle
	@obliqueangle.setter
	def _(self, obliAngle:float):
		# ['in'] obliAngle:float
		self.com_parent.ObliqueAngle = obliAngle

	@property
	def preset(self) -> bool:
		"Specifies the preset mode of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bPreset:bool
		return self.com_parent.Preset
	@preset.setter
	def _(self, bPreset:bool):
		# ['in'] bPreset:bool
		self.com_parent.Preset = bPreset

	@property
	def promptstring(self) -> str:
		"Specifies the prompt string of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bstrPrompt:str
		return self.com_parent.PromptString
	@promptstring.setter
	def _(self, bstrPrompt:str):
		# ['in'] bstrPrompt:str
		self.com_parent.PromptString = bstrPrompt

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the scale factor of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] scalFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scalFactor:float):
		# ['in'] scalFactor:float
		self.com_parent.ScaleFactor = scalFactor

	@property
	def stylename(self) -> str:
		"Specifies the text style of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.StyleName = Name

	@property
	def tagstring(self) -> str:
		"Specifies the tag string of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] Tag:str
		return self.com_parent.TagString
	@tagstring.setter
	def _(self, Tag:str):
		# ['in'] Tag:str
		self.com_parent.TagString = Tag

	@property
	def textalignmentpoint(self) -> A3Vertex:
		"Specify the X, Y, Z alignment point of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] alignPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.TextAlignmentPoint)
	@textalignmentpoint.setter
	def _(self, alignPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] alignPoint:tagVARIANT | A3Vertex
		self.com_parent.TextAlignmentPoint = alignPoint

	@property
	def textgenerationflag(self) -> int:
		"Specifies the attribute text generation flag"
		# TODO: Check arguments
		# ['out', 'retval'] textGenFlag:int | ENUM?
		return self.com_parent.TextGenerationFlag
	@textgenerationflag.setter
	def _(self, textGenFlag:int):
		# ['in'] textGenFlag:int
		self.com_parent.TextGenerationFlag = textGenFlag

	@property
	def textstring(self) -> str:
		"Specifies the text string of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

	@property
	def upsidedown(self) -> bool:
		"Determines whether the text is upside down or not"
		# TODO: Check arguments
		# ['out', 'retval'] bUpsideDown:bool
		return self.com_parent.UpsideDown
	@upsidedown.setter
	def _(self, bUpsideDown:bool):
		# ['in'] bUpsideDown:bool
		self.com_parent.UpsideDown = bUpsideDown

	@property
	def verify(self) -> bool:
		"Specifies the verify mode of the attribute"
		# TODO: Check arguments
		# ['out', 'retval'] bVerify:bool
		return self.com_parent.Verify
	@verify.setter
	def _(self, bVerify:bool):
		# ['in'] bVerify:bool
		self.com_parent.Verify = bVerify

	@property
	def verticalalignment(self) -> int:
		"Specifies the vertical alignment of the attribute."
		# TODO: Check arguments
		# ['out', 'retval'] vertiAlign:int
		return self.com_parent.VerticalAlignment
	@verticalalignment.setter
	def _(self, vertiAlign:int):
		# ['in'] vertiAlign:int
		self.com_parent.VerticalAlignment = vertiAlign

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
	

class AcadAttributeReference(POINTER(_dll.IAcadAttributeReference), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadAttributeReference
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadAttributeReference VBA-class wrapped as AcadAttributeReference python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Methods
	def updatemtextattribute(self):
		"Updates attribute reference from the multiline mtext and vice versa"
		# VBA: object.UpdateMTextAttribute 
		self.com_parent.UpdateMTextAttribute()

	# Properties
	@property
	def alignment(self) -> int:
		"Specifies the alignment of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] align:int | ENUM?
		return self.com_parent.Alignment
	@alignment.setter
	def _(self, align:int):
		# ['in'] align:int
		self.com_parent.Alignment = align

	@property
	def backward(self) -> bool:
		"Determines whether the text is backward and sets the text backward"
		# TODO: Check arguments
		# ['out', 'retval'] bBackward:bool
		return self.com_parent.Backward
	@backward.setter
	def _(self, bBackward:bool):
		# ['in'] bBackward:bool
		self.com_parent.Backward = bBackward

	@property
	def constant(self) -> bool:
		"Specifies the constant mode of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] bConstant:bool
		return self.com_parent.Constant

	@property
	def fieldlength(self) -> int:
		"Specifies the field length of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] fieldLen:int
		return self.com_parent.FieldLength
	@fieldlength.setter
	def _(self, fieldLen:int):
		# ['in'] fieldLen:int
		self.com_parent.FieldLength = fieldLen

	@property
	def height(self) -> float:
		"Specifies the height of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def horizontalalignment(self) -> int:
		"Specifies the horizontal alignment of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] horizAlign:int | ENUM?
		return self.com_parent.HorizontalAlignment
	@horizontalalignment.setter
	def _(self, horizAlign:int):
		# ['in'] horizAlign:int
		self.com_parent.HorizontalAlignment = horizAlign

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specifies the insertion point of the text"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def invisible(self) -> bool:
		"Specifies the invisible mode of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] bInvisible:bool
		return self.com_parent.Invisible
	@invisible.setter
	def _(self, bInvisible:bool):
		# ['in'] bInvisible:bool
		self.com_parent.Invisible = bInvisible

	@property
	def lockposition(self) -> bool:
		"Specifies whether the attribute may be moved relative to the geometry in the block"
		# TODO: Check arguments
		# ['out', 'retval'] bLockPosition:bool
		return self.com_parent.LockPosition

	@property
	def mtextattribute(self) -> bool:
		"Determines whether if the attribute reference is multiline"
		# TODO: Check arguments
		# ['out', 'retval'] bMTextAttribute:bool
		return self.com_parent.MTextAttribute
	@mtextattribute.setter
	def _(self, bMTextAttribute:bool):
		# ['in'] bMTextAttribute:bool
		self.com_parent.MTextAttribute = bMTextAttribute

	@property
	def mtextattributecontent(self) -> str:
		"Gets the multiline attribute reference content"
		# TODO: Check arguments
		# ['out', 'retval'] content:str
		return self.com_parent.MTextAttributeContent
	@mtextattributecontent.setter
	def _(self, content:str):
		# ['in'] content:str
		self.com_parent.MTextAttributeContent = content

	@property
	def mtextboundarywidth(self) -> float:
		"Gets the width of text boundary of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] boundaryWidth:float
		return self.com_parent.MTextBoundaryWidth
	@mtextboundarywidth.setter
	def _(self, boundaryWidth:float):
		# [] boundaryWidth:float
		self.com_parent.MTextBoundaryWidth = boundaryWidth

	@property
	def mtextdrawingdirection(self) -> int:
		"Gets the drawing direction of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] drawDir:int | ENUM?
		return self.com_parent.MTextDrawingDirection
	@mtextdrawingdirection.setter
	def _(self, drawDir:int):
		# ['in'] drawDir:int
		self.com_parent.MTextDrawingDirection = drawDir

	@property
	def normal(self) -> A3Vertex:
		"Specifies the normal direction vector"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def obliqueangle(self) -> float:
		"Specifies the oblique angle of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] obliAngle:float
		return self.com_parent.ObliqueAngle
	@obliqueangle.setter
	def _(self, obliAngle:float):
		# ['in'] obliAngle:float
		self.com_parent.ObliqueAngle = obliAngle

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the scale factor of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] scalFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scalFactor:float):
		# ['in'] scalFactor:float
		self.com_parent.ScaleFactor = scalFactor

	@property
	def stylename(self) -> str:
		"Specifies the style name of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.StyleName = Name

	@property
	def tagstring(self) -> str:
		"Specifies the tag string of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] bstrTag:str
		return self.com_parent.TagString
	@tagstring.setter
	def _(self, bstrTag:str):
		# ['in'] bstrTag:str
		self.com_parent.TagString = bstrTag

	@property
	def textalignmentpoint(self) -> A3Vertex:
		"Specifies the alignment point of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] alignPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.TextAlignmentPoint)
	@textalignmentpoint.setter
	def _(self, alignPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] alignPoint:tagVARIANT | A3Vertex
		self.com_parent.TextAlignmentPoint = alignPoint

	@property
	def textgenerationflag(self) -> int:
		"Specifies the attribute reference text generation flag"
		# TODO: Check arguments
		# ['out', 'retval'] textGenFlag:int | ENUM?
		return self.com_parent.TextGenerationFlag
	@textgenerationflag.setter
	def _(self, textGenFlag:int):
		# ['in'] textGenFlag:int
		self.com_parent.TextGenerationFlag = textGenFlag

	@property
	def textstring(self) -> str:
		"Specifies the text string of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

	@property
	def upsidedown(self) -> bool:
		"Returns whether the text is upside down and sets the text upside down"
		# TODO: Check arguments
		# ['out', 'retval'] bUpsideDown:bool
		return self.com_parent.UpsideDown
	@upsidedown.setter
	def _(self, bUpsideDown:bool):
		# ['in'] bUpsideDown:bool
		self.com_parent.UpsideDown = bUpsideDown

	@property
	def verticalalignment(self) -> int:
		"Specifies the vertical alignment of the attribute reference"
		# TODO: Check arguments
		# ['out', 'retval'] vertiAlign:int | ENUM?
		return self.com_parent.VerticalAlignment
	@verticalalignment.setter
	def _(self, vertiAlign:int):
		# ['in'] vertiAlign:int
		self.com_parent.VerticalAlignment = vertiAlign
	
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


class AcadBlockReference(POINTER(_dll.IAcadBlockReference), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadBlockReference
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadBlockReference VBA-class wrapped as AcadBlockReference python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Methods
	def converttoanonymousblock(self):
		"Converts a dynamic block to a regular anonymous block"
		# VBA: object.ConvertToAnonymousBlock 
		self.com_parent.ConvertToAnonymousBlock()

	def converttostaticblock(self, newBlockName: str):
		"Converts a dynamic block to a regular named block"
		# ['in'] newBlockName:str
		# VBA: object.ConvertToStaticBlock newBlockName
		self.com_parent.ConvertToStaticBlock(newBlockName)

	def explode(self) -> list:
		"Explodes the block and returns the sub-entities as an array of Object"
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT | list
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret

	def getattributes(self) -> list:
		"Gets Attributes in the block"
		# TODO: Check arguments
		# ['out', 'retval'] pAttrObjs:tagVARIANT | list
		# VBA: pAttrObjs = object.GetAttributes ()
		ret = []
		for e in self.com_parent.GetAttributes():
			ret.append(CastManager.cast(e))
		return ret

	def getconstantattributes(self) -> list:
		"Gets constant attributes in the block"
		# TODO: Check arguments
		# ['out', 'retval'] pAttrObjs:tagVARIANT | list
		# VBA: pAttrObjs = object.GetConstantAttributes ()
		ret = []
		for e in self.com_parent.GetConstantAttributes():
			ret.append(CastManager.cast(e))
		return ret

	def getdynamicblockproperties(self) -> list:
		"Gets the dynamic block properties"
		# TODO: Check arguments
		# ['out', 'retval'] dynamicPropertyArray:tagVARIANT | list
		# VBA: dynamicPropertyArray = object.GetDynamicBlockProperties ()
		ret = []
		for e in self.com_parent.GetDynamicBlockProperties():
			ret.append(CastManager.cast(e))
		return ret

	def resetblock(self):
		"Resets the dynamic block to the default state"
		# VBA: object.ResetBlock 
		self.com_parent.ResetBlock()

	# Properties
	@property
	def effectivename(self) -> str:
		"Specifies the original block name"
		# TODO: Check arguments
		# ['out', 'retval'] EffectiveName:str
		return self.com_parent.EffectiveName

	@property
	def hasattributes(self) -> bool:
		"Specifies if the block has any attributes in it"
		# TODO: Check arguments
		# ['out', 'retval'] bHas:bool
		return self.com_parent.HasAttributes

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for insertion point of the block or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def insunits(self) -> str:
		"Specifies insunits saved with the block"
		# TODO: Check arguments
		# ['out', 'retval'] Units:str
		return self.com_parent.InsUnits

	@property
	def insunitsfactor(self) -> float:
		"Specifies the conversion factor between block units and drawing units"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.InsUnitsFactor

	@property
	def isdynamicblock(self) -> bool:
		"Specifies if this is a dynamic block"
		# TODO: Check arguments
		# ['out', 'retval'] pDynamicBlock:bool
		return self.com_parent.IsDynamicBlock

	@property
	def name(self) -> str:
		"Specifies the name of the block"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the block"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def xeffectivescalefactor(self) -> float:
		"Specifies the effective XScale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.XEffectiveScaleFactor
	@xeffectivescalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.XEffectiveScaleFactor = ScaleFactor

	@property
	def xscalefactor(self) -> float:
		"Specifies the XScale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.XScaleFactor
	@xscalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.XScaleFactor = ScaleFactor

	@property
	def yeffectivescalefactor(self) -> float:
		"Specifies the effective Yscale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.YEffectiveScaleFactor
	@yeffectivescalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.YEffectiveScaleFactor = ScaleFactor

	@property
	def yscalefactor(self) -> float:
		"Specifies the Yscale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.YScaleFactor
	@yscalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.YScaleFactor = ScaleFactor

	@property
	def zeffectivescalefactor(self) -> float:
		"Specifies the effective ZScale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.ZEffectiveScaleFactor
	@zeffectivescalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.ZEffectiveScaleFactor = ScaleFactor

	@property
	def zscalefactor(self) -> float:
		"Specifies the ZScale factor of the block"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.ZScaleFactor
	@zscalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.ZScaleFactor = ScaleFactor

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


class AcadCircle(POINTER(_dll.IAcadCircle), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadCircle
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadCircle VBA-class wrapped as AcadCircle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Methods
	def offset(self, Distance: float) -> list:
		"Creates an circle by offsetting the original circle by a specified distance"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return ret

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the circle"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area
	@area.setter
	def _(self, Area:float):
		# ['in'] Area:float
		self.com_parent.Area = Area

	@property
	def center(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the center of the circle or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] CenterPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Center)
	@center.setter
	def _(self, CenterPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] CenterPoint:tagVARIANT | A3Vertex
		self.com_parent.Center = CenterPoint

	@property
	def circumference(self) -> float:
		"Specifies the circumference of the circle"
		# TODO: Check arguments
		# ['out', 'retval'] Circumference:float
		return self.com_parent.Circumference
	@circumference.setter
	def _(self, Circumference:float):
		# ['in'] Circumference:float
		self.com_parent.Circumference = Circumference

	@property
	def diameter(self) -> float:
		"Specifies the diameter of the circle"
		# TODO: Check arguments
		# ['out', 'retval'] Diameter:float
		return self.com_parent.Diameter
	@diameter.setter
	def _(self, Diameter:float):
		# ['in'] Diameter:float
		self.com_parent.Diameter = Diameter

	@property
	def normal(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the normal direction vector"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def radius(self) -> float:
		"Specifies the radius of the circle"
		# TODO: Check arguments
		# ['out', 'retval'] Radius:float
		return self.com_parent.Radius
	@radius.setter
	def _(self, Radius:float):
		# ['in'] Radius:float
		self.com_parent.Radius = Radius

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the circle"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

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


class AcadDimension(POINTER(_dll.IAcadDimension), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimension
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadDimension VBA-class wrapped as AcadDimension python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Properties
	@property
	def decimalseparator(self) -> str:
		"Specifies the decimal separator for metric dimensions (DIMDSEP system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] character:str
		return self.com_parent.DecimalSeparator
	@decimalseparator.setter
	def _(self, character:str):
		# ['in'] character:str
		self.com_parent.DecimalSeparator = character

	@property
	def dimtxtdirection(self) -> bool:
		"Specifies the dimension text viewing direction."
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.DimTxtDirection
	@dimtxtdirection.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.DimTxtDirection = bVal

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle for the object"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the overall scale factor applied to properties that specify sizes, distances, or offsets (DIMSCALE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.ScaleFactor = factor

	@property
	def stylename(self) -> str:
		"Specifies the current dimension style by name (for DIMSTYLE system variable use SETVAR)"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def suppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressLeadingZeros
	@suppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressLeadingZeros = bVal

	@property
	def suppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressTrailingZeros
	@suppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressTrailingZeros = bVal

	@property
	def textcolor(self) -> int:
		"Specifies the color of the dimension text (DIMCLRT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.TextColor
	@textcolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.TextColor = color

	@property
	def textfill(self) -> bool:
		"Sets fill color On or Off (DIMTFILL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.TextFill
	@textfill.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.TextFill = bVal

	@property
	def textfillcolor(self) -> int:
		"Sets text fill color (DIMTFILLCLR system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] color:int | ENUM?
		return self.com_parent.TextFillColor
	@textfillcolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.TextFillColor = color

	@property
	def textgap(self) -> float:
		"Specifies distance around dimension text when dimension line breaks for dimension text (DIMGAP system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.TextGap
	@textgap.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.TextGap = Offset

	@property
	def textheight(self) -> float:
		"Specifies text height of the dimension (DIMTXT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.TextHeight
	@textheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.TextHeight = Height

	@property
	def textmovement(self) -> int:
		"Specifies position of text when it's moved, either manually or automatically (DIMTMOVE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Move:int | ENUM?
		return self.com_parent.TextMovement
	@textmovement.setter
	def _(self, Move:int):
		# ['in'] Move:int
		self.com_parent.TextMovement = Move

	@property
	def textoverride(self) -> str:
		"Specifies the text string of the dimension (overrides Measurement string)"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextOverride
	@textoverride.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextOverride = bstrText

	@property
	def textposition(self) -> A3Vertex:
		"Specifies the dimension text position or pick point"
		# TODO: Check arguments
		# ['out', 'retval'] textPos:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.TextPosition)
	@textposition.setter
	def _(self, textPos:A3Vertex):
		# TODO: Check arguments
		# ['in'] textPos:tagVARIANT | A3Vertex
		self.com_parent.TextPosition = textPos

	@property
	def textprefix(self) -> str:
		"Specifies the text prefix for the dimension (DIMPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.TextPrefix
	@textprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.TextPrefix = prefix

	@property
	def textrotation(self) -> float:
		"Specifies the rotation angle of the dimension text"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.TextRotation
	@textrotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.TextRotation = rotAngle

	@property
	def textstyle(self) -> str:
		"Specifies text style of the dimension (DIMTXSTY system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] style:str
		return self.com_parent.TextStyle
	@textstyle.setter
	def _(self, style:str):
		# ['in'] style:str
		self.com_parent.TextStyle = style

	@property
	def textsuffix(self) -> str:
		"Specifies the text suffix for the dimension (DIMPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.TextSuffix
	@textsuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.TextSuffix = suffix

	@property
	def tolerancedisplay(self) -> int:
		"Specifies display mode of dimension tolerances to dimension text (DIMTOL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] method:int | ENUM?
		return self.com_parent.ToleranceDisplay
	@tolerancedisplay.setter
	def _(self, method:int):
		# ['in'] method:int
		self.com_parent.ToleranceDisplay = method

	@property
	def toleranceheightscale(self) -> float:
		"Specifies scale factor for text height of tolerance values relative to dimension text height as set by DIMTXT (DIMTFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.ToleranceHeightScale
	@toleranceheightscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.ToleranceHeightScale = scale

	@property
	def tolerancejustification(self) -> int:
		"Specifies vertical justification for tolerance values relative to nominal dimension text (DIMTOLJ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] method:int | ENUM?
		return self.com_parent.ToleranceJustification
	@tolerancejustification.setter
	def _(self, method:int):
		# ['in'] method:int
		self.com_parent.ToleranceJustification = method

	@property
	def tolerancelowerlimit(self) -> float:
		"Specifies minimum (or lower) tolerance limit for dimension text when DIMTOL or DIMLIM is on (DIMTM system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lower:float
		return self.com_parent.ToleranceLowerLimit
	@tolerancelowerlimit.setter
	def _(self, lower:float):
		# ['in'] lower:float
		self.com_parent.ToleranceLowerLimit = lower

	@property
	def toleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of a dimension (DIMTDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.TolerancePrecision
	@toleranceprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.TolerancePrecision = precision

	@property
	def tolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressLeadingZeros
	@tolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressLeadingZeros = bVal

	@property
	def tolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressTrailingZeros
	@tolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressTrailingZeros = bVal

	@property
	def toleranceupperlimit(self) -> float:
		"Specifies the maximum (or upper) tolerance limit for dimension text when DIMTOL or DIMLIM is on (DIMTP sysem variable)"
		# TODO: Check arguments
		# ['out', 'retval'] upper:float
		return self.com_parent.ToleranceUpperLimit
	@toleranceupperlimit.setter
	def _(self, upper:float):
		# ['in'] upper:float
		self.com_parent.ToleranceUpperLimit = upper

	@property
	def verticaltextposition(self) -> int:
		"Specifies the vertical dimension text position relative to dimension line (DIMTAD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.VerticalTextPosition
	@verticaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.VerticalTextPosition = Type

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
	

class AcadDim3PointAngular(POINTER(_dll.IAcadDim3PointAngular), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDim3PointAngular
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDim3PointAngular VBA-class wrapped as AcadDim3PointAngular python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Properties
	@property
	def angleformat(self) -> int:
		"Specifies the angle format (DIMAUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.AngleFormat
	@angleformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.AngleFormat = format

	@property
	def anglevertex(self) -> A3Vertex:
		"Specifies the angle vertex for the three point angular dimension"
		# TODO: Check arguments
		# ['out', 'retval'] AngleVertex:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.AngleVertex)
	@anglevertex.setter
	def _(self, AngleVertex:A3Vertex):
		# TODO: Check arguments
		# ['in'] AngleVertex:tagVARIANT | A3Vertex
		self.com_parent.AngleVertex = AngleVertex

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def dimlineinside(self) -> bool:
		"Sets drawing of dimension lines outside extension lines On or Off (DIMSOXD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.DimLineInside
	@dimlineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.DimLineInside = bInside

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ExtensionLineColor = Type

	@property
	def extensionlineextend(self) -> float:
		"Specifies amount to extend extension line beyond the dimension line (DIMEXE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.ExtensionLineExtend
	@extensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.ExtensionLineExtend = extend

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extline1endpoint(self) -> A3Vertex:
		"Specifies the endpoint of the first extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine1Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine1EndPoint)
	@extline1endpoint.setter
	def _(self, xLine1Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine1Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine1EndPoint = xLine1Point

	@property
	def extline1linetype(self) -> str:
		"Specifies the linetype of the first extension line (DIMLTEX1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine1Linetype
	@extline1linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine1Linetype = Linetype

	@property
	def extline1suppress(self) -> bool:
		"Sets suppression of first extension line On or Off (DIMSE1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine1Suppress
	@extline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine1Suppress = bSuppress

	@property
	def extline2endpoint(self) -> A3Vertex:
		"Specifies the endpoint of the second extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine2Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine2EndPoint)
	@extline2endpoint.setter
	def _(self, xLine2Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine2Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine2EndPoint = xLine2Point

	@property
	def extline2linetype(self) -> str:
		"Specifies the linetype of the second extension line (DIMLTEX2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine2Linetype
	@extline2linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine2Linetype = Linetype

	@property
	def extline2suppress(self) -> bool:
		"Sets suppression of second extension line On or Off (DIMSE2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine2Suppress
	@extline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine2Suppress = bSuppress

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def horizontaltextposition(self) -> int:
		"Specifies horizontal dimension text position (DIMJUST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.HorizontalTextPosition
	@horizontaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.HorizontalTextPosition = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def textinside(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def textprecision(self) -> int:
		"Specifies number of precision decimal places displayed for angular dimension text (DIMADEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] AngleVertex:int | ENUM?
		return self.com_parent.TextPrecision
	@textprecision.setter
	def _(self, AngleVertex:int):
		# ['in'] AngleVertex:int
		self.com_parent.TextPrecision = AngleVertex
		
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
	
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


class AcadDimAligned(POINTER(_dll.IAcadDimAligned), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimAligned
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimAligned VBA-class wrapped as AcadDimAligned python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
	
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsubunitsfactor(self) -> float:
		"Specifies the alternate sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.AltSubUnitsFactor
	@altsubunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.AltSubUnitsFactor = factor

	@property
	def altsubunitssuffix(self) -> str:
		"Specifies the text suffix for the alternate dimension when change to alternate sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.AltSubUnitsSuffix
	@altsubunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.AltSubUnitsSuffix = suffix

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.AltTextSuffix = suffix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets alternate units dimensioning On or Off (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies the type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies the type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies the size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.DimensionLineColor = color

	@property
	def dimensionlineextend(self) -> float:
		"Specifies amount to extend dimension lines beyond the extension line (DIMDLE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.DimensionLineExtend
	@dimensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.DimensionLineExtend = extend

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies the lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of the first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of the second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def dimlineinside(self) -> bool:
		"Sets drawing of dimension lines outside extension lines On or Off (DIMSOXD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.DimLineInside
	@dimlineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.DimLineInside = bInside

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] color:int | ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.ExtensionLineColor = color

	@property
	def extensionlineextend(self) -> float:
		"Specifies amount to extend the extension line beyond the dimension line (DIMEXE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.ExtensionLineExtend
	@extensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.ExtensionLineExtend = extend

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extline1linetype(self) -> str:
		"Specifies the linetype of the first extension line (DIMLTEX1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine1Linetype
	@extline1linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine1Linetype = Linetype

	@property
	def extline1point(self) -> A3Vertex:
		"Specifies the origin of extension line 1"
		# TODO: Check arguments
		# ['out', 'retval'] xLine1Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine1Point)
	@extline1point.setter
	def _(self, xLine1Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine1Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine1Point = xLine1Point

	@property
	def extline1suppress(self) -> bool:
		"Sets suppression of the first extension line On or Off (DIMSE1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine1Suppress
	@extline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine1Suppress = bSuppress

	@property
	def extline2linetype(self) -> str:
		"Specifies the linetype of the second extension line (DIMLTEX2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine2Linetype
	@extline2linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine2Linetype = Linetype

	@property
	def extline2point(self) -> A3Vertex:
		"Specifies the origin of extension line 1"
		# TODO: Check arguments
		# ['out', 'retval'] xLine2Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine2Point)
	@extline2point.setter
	def _(self, xLine2Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine2Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine2Point = xLine2Point

	@property
	def extline2suppress(self) -> bool:
		"Sets suppression of the second extension line On or Off (DIMSE2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine2Suppress
	@extline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine2Suppress = bSuppress

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing a dimension line between extension lines even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def horizontaltextposition(self) -> int:
		"Specifies horizontal dimension text position (DIMJUST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.HorizontalTextPosition
	@horizontaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.HorizontalTextPosition = Type

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def subunitsfactor(self) -> float:
		"Specifies the sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.SubUnitsFactor
	@subunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.SubUnitsFactor = factor

	@property
	def subunitssuffix(self) -> str:
		"Specifies the text suffix for all applicable linear dimension when change to sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.SubUnitsSuffix
	@subunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.SubUnitsSuffix = suffix

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def textinside(self) -> bool:
		"Sets drawing of text between extension lines On or Off (DIMTIX system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside the extension lines On or Off (DIMTXT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimAngular(POINTER(_dll.IAcadDimAngular), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimAngular
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimAngular VBA-class wrapped as AcadDimAngular python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def angleformat(self) -> int:
		"Specifies the angle format (DIMAUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.AngleFormat
	@angleformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.AngleFormat = format

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies the color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def dimlineinside(self) -> bool:
		"Sets drawing of dimension lines outside extension lines On or Off (DIMSOXD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.DimLineInside
	@dimlineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.DimLineInside = bInside

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ExtensionLineColor = Type

	@property
	def extensionlineextend(self) -> float:
		"Specifies amount to extend extension line beyond the dimension line (DIMEXE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.ExtensionLineExtend
	@extensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.ExtensionLineExtend = extend

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extline1endpoint(self) -> A3Vertex:
		"Specifies the endpoint of the first extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine1Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine1EndPoint)
	@extline1endpoint.setter
	def _(self, xLine1Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine1Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine1EndPoint = xLine1Point

	@property
	def extline1linetype(self) -> str:
		"Specifies the linetype of the first extension line (DIMLTEX1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine1Linetype
	@extline1linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine1Linetype = Linetype

	@property
	def extline1startpoint(self) -> A3Vertex:
		"Specifies the start point of the first extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine1Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine1StartPoint)
	@extline1startpoint.setter
	def _(self, xLine1Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine1Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine1StartPoint = xLine1Point

	@property
	def extline1suppress(self) -> bool:
		"Sets suppression of first extension line On or Off (DIMSE1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine1Suppress
	@extline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine1Suppress = bSuppress

	@property
	def extline2endpoint(self) -> A3Vertex:
		"Specifies the endpoint of the second extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine2Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine2EndPoint)
	@extline2endpoint.setter
	def _(self, xLine2Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine2Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine2EndPoint = xLine2Point

	@property
	def extline2linetype(self) -> str:
		"Specifies the linetype of the second extension line (DIMLTEX2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine2Linetype
	@extline2linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine2Linetype = Linetype

	@property
	def extline2startpoint(self) -> A3Vertex:
		"Specifies the start point of the second extension line"
		# TODO: Check arguments
		# ['out', 'retval'] xLine2Point:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine2StartPoint)
	@extline2startpoint.setter
	def _(self, xLine2Point:A3Vertex):
		# TODO: Check arguments
		# ['in'] xLine2Point:tagVARIANT | A3Vertex
		self.com_parent.ExtLine2StartPoint = xLine2Point

	@property
	def extline2suppress(self) -> bool:
		"Sets suppression of second extension line On or Off (DIMSE2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine2Suppress
	@extline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine2Suppress = bSuppress

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def horizontaltextposition(self) -> int:
		"Specifies horizontal dimension text position (DIMJUST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.HorizontalTextPosition
	@horizontaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.HorizontalTextPosition = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def textinside(self) -> bool:
		"Sets drawing of text between extension lines On or Off (DIMTIX system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def textprecision(self) -> int:
		"Specifies number of precision decimal places displayed for angular dimension text (DIMADEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.TextPrecision
	@textprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.TextPrecision = precision


class AcadDimArcLength(POINTER(_dll.IAcadDimArcLength), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimArcLength
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimArcLength VBA-class wrapped as AcadDimArcLength python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsubunitsfactor(self) -> float:
		"Specifies the alternate sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.AltSubUnitsFactor
	@altsubunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.AltSubUnitsFactor = factor

	@property
	def altsubunitssuffix(self) -> str:
		"Specifies the text suffix for the alternate dimension when change to alternate sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.AltSubUnitsSuffix
	@altsubunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.AltSubUnitsSuffix = suffix

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets units format for alternate units dimensions On or Off, except angular (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arcendparam(self) -> float:
		"Specifies the end parameter of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.ArcEndParam
	@arcendparam.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.ArcEndParam = pVal

	@property
	def arcpoint(self) -> A3Vertex:
		"Specifies a point on the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ArcPoint)
	@arcpoint.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.ArcPoint = pVal

	@property
	def arcstartparam(self) -> float:
		"Specifies the start parameter of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.ArcStartParam
	@arcstartparam.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.ArcStartParam = pVal

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def centerpoint(self) -> A3Vertex:
		"Specifies the center of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.CenterPoint)
	@centerpoint.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.CenterPoint = pVal

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlineextend(self) -> float:
		"Specifies amount to extend dimension lines beyond the extension line (DIMDLE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.DimensionLineExtend
	@dimensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.DimensionLineExtend = extend

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def dimlineinside(self) -> bool:
		"Sets drawing of dimension lines outside extension lines On or Off (DIMSOXD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.DimLineInside
	@dimlineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.DimLineInside = bInside

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ExtensionLineColor = Type

	@property
	def extensionlineextend(self) -> float:
		"Specifies amount to extend extension line beyond the dimension line (DIMEXE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.ExtensionLineExtend
	@extensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.ExtensionLineExtend = extend

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extline1linetype(self) -> str:
		"Specifies the linetype of the first extension line (DIMLTEX1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine1Linetype
	@extline1linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine1Linetype = Linetype

	@property
	def extline1point(self) -> A3Vertex:
		"Specifies the origin of extension line 1"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine1Point)
	@extline1point.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.ExtLine1Point = pVal

	@property
	def extline1suppress(self) -> bool:
		"Sets suppression of first extension line On or Off (DIMSE1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine1Suppress
	@extline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine1Suppress = bSuppress

	@property
	def extline2linetype(self) -> str:
		"Specifies the linetype of the second extension line (DIMLTEX2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine2Linetype
	@extline2linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine2Linetype = Linetype

	@property
	def extline2point(self) -> A3Vertex:
		"Specifies the origin of extension line 2"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ExtLine2Point)
	@extline2point.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.ExtLine2Point = pVal

	@property
	def extline2suppress(self) -> bool:
		"Sets suppression of second extension line On or Off (DIMSE2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine2Suppress
	@extline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine2Suppress = bSuppress

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def hasleader(self) -> bool:
		"Specifies the whether the dimension has leader"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.HasLeader
	@hasleader.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.HasLeader = pVal

	@property
	def horizontaltextposition(self) -> int:
		"Specifies horizontal dimension text position (DIMJUST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.HorizontalTextPosition
	@horizontaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.HorizontalTextPosition = Type

	@property
	def ispartial(self) -> bool:
		"Specifies whether the dimension is for a partial arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IsPartial
	@ispartial.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.IsPartial = pVal

	@property
	def leader1point(self) -> A3Vertex:
		"Specifies the origin of leader 1"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Leader1Point)
	@leader1point.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Leader1Point = pVal

	@property
	def leader2point(self) -> A3Vertex:
		"Specifies the origin of leader 2"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Leader2Point)
	@leader2point.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT
		self.com_parent.Leader2Point = pVal

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def subunitsfactor(self) -> float:
		"Specifies the sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.SubUnitsFactor
	@subunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.SubUnitsFactor = factor

	@property
	def subunitssuffix(self) -> str:
		"Specifies the text suffix for all applicable linear dimension when change to sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.SubUnitsSuffix
	@subunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.SubUnitsSuffix = suffix

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def symbolposition(self) -> int:
		"Specifies placement of the arc length dimension symbol (DIMARCSYM system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Position:int | ENUM?
		return self.com_parent.SymbolPosition
	@symbolposition.setter
	def _(self, Position:int):
		# ['in'] Position:int
		self.com_parent.SymbolPosition = Position

	@property
	def textinside(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimDiametric(POINTER(_dll.IAcadDimDiametric), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimDiametric
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimDiametric VBA-class wrapped as AcadDimDiametric python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets alternate units dimensioning On or Off (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def centermarksize(self) -> float:
		"Specifies size of the center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.CenterMarkSize
	@centermarksize.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.CenterMarkSize = Type

	@property
	def centertype(self) -> int:
		"Specifies type of center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.CenterType
	@centertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CenterType = Type

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def leaderlength(self):
		"Specifies the length of the leader on the diameter or radius dimension"
		Exception("Can't GET LeaderLength value")
	@leaderlength.setter
	def _(self, rhs:float):
		# ['in'] rhs:float
		self.com_parent.LeaderLength = rhs

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def textinside(self) -> bool:
		"Sets drawing of text between extension lines On or Off (DIMTIX system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimOrdinate(POINTER(_dll.IAcadDimOrdinate), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimOrdinate
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimOrdinate VBA-class wrapped as AcadDimOrdinate python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsubunitsfactor(self) -> float:
		"Specifies the alternate sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.AltSubUnitsFactor
	@altsubunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.AltSubUnitsFactor = factor

	@property
	def altsubunitssuffix(self) -> str:
		"Specifies the text suffix for the alternate dimension when change to alternate sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.AltSubUnitsSuffix
	@altsubunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.AltSubUnitsSuffix = suffix

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets units format for alternate units dimensions On or Off, except angular (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ExtensionLineColor = Type

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def subunitsfactor(self) -> float:
		"Specifies the sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.SubUnitsFactor
	@subunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.SubUnitsFactor = factor

	@property
	def subunitssuffix(self) -> str:
		"Specifies the text suffix for all applicable linear dimension when change to sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.SubUnitsSuffix
	@subunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.SubUnitsSuffix = suffix

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimRadial(POINTER(_dll.IAcadDimRadial), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimRadial
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimRadial VBA-class wrapped as AcadDimRadial python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets units format for alternate units dimensions On or Off, except angular (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowheadblock(self) -> str:
		"Specifies the block to use as the custom arrowhead for a radial dimension or leader line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ArrowheadBlock
	@arrowheadblock.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ArrowheadBlock = BlockName

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def arrowheadtype(self) -> int:
		"Specifies type of the dimension arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ArrowheadType
	@arrowheadtype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ArrowheadType = Type

	@property
	def centermarksize(self) -> float:
		"Specifies size of the center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.CenterMarkSize
	@centermarksize.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.CenterMarkSize = Type

	@property
	def centertype(self) -> int:
		"Specifies type of center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.CenterType
	@centertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CenterType = Type

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimlinesuppress(self) -> bool:
		"Sets the suppression of the second dimension line On or Off (DIMSD2)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLineSuppress
	@dimlinesuppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLineSuppress = bSuppress

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def leaderlength(self):
		"Specifies the length of the leader on the diameter or radius dimension"
		Exception("Can't GET LeaderLength value")
	@leaderlength.setter
	def _(self, rhs:float):
		# ['in'] rhs:float
		self.com_parent.LeaderLength = rhs

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def textinside(self) -> bool:
		"Sets drawing of text between extension lines On or Off (DIMTIX system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimRadialLarge(POINTER(_dll.IAcadDimRadialLarge), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimRadialLarge
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimRadialLarge VBA-class wrapped as AcadDimRadialLarge python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets units format for alternate units dimensions On or Off, except angular (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowheadblock(self) -> str:
		"Specifies the block to use as the custom arrowhead for a radial dimension or leader line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ArrowheadBlock
	@arrowheadblock.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ArrowheadBlock = BlockName

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def arrowheadtype(self) -> int:
		"Specifies type of the dimension arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ArrowheadType
	@arrowheadtype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ArrowheadType = Type

	@property
	def center(self) -> A3Vertex:
		"Specifies the center of the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVar:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Center)
	@center.setter
	def _(self, pVar:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVar:tagVARIANT | A3Vertex
		self.com_parent.Center = pVar

	@property
	def centermarksize(self) -> float:
		"Specifies size of the center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.CenterMarkSize
	@centermarksize.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.CenterMarkSize = Type

	@property
	def centertype(self) -> int:
		"Specifies type of center mark on the dimension (DIMCEN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.CenterType
	@centertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CenterType = Type

	@property
	def chordpoint(self) -> A3Vertex:
		"Specifies the chord point for the arc"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ChordPoint)
	@chordpoint.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.ChordPoint = pVal

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimlinesuppress(self) -> bool:
		"Sets the suppression of the second dimension line On or Off (DIMSD2)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLineSuppress
	@dimlinesuppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLineSuppress = bSuppress

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def jogangle(self) -> float:
		"Specifies the jog angle (DIMJOGANG system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] JogAngle:float
		return self.com_parent.JogAngle
	@jogangle.setter
	def _(self, JogAngle:float):
		# ['in'] JogAngle:float
		self.com_parent.JogAngle = JogAngle

	@property
	def joglocation(self) -> A3Vertex:
		"Specifies the jog location or pick point"
		# TODO: Check arguments
		# ['out', 'retval'] jogPos:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.JogLocation)
	@joglocation.setter
	def _(self, jogPos:A3Vertex):
		# TODO: Check arguments
		# ['in'] jogPos:tagVARIANT | A3Vertex
		self.com_parent.JogLocation = jogPos

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def overridecenter(self) -> A3Vertex:
		"Specifies the override center location or pick point"
		# TODO: Check arguments
		# ['out', 'retval'] overrideCenterPos:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.OverrideCenter)
	@overridecenter.setter
	def _(self, overrideCenterPos:A3Vertex):
		# TODO: Check arguments
		# ['in'] overrideCenterPos:tagVARIANT | A3Vertex
		self.com_parent.OverrideCenter = overrideCenterPos

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def textinside(self) -> bool:
		"Sets drawing of text between extension lines On or Off (DIMTIX system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadDimRotated(POINTER(_dll.IAcadDimRotated), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDimRotated
	#	IAcadDimension
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDimRotated VBA-class wrapped as AcadDimRotated python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadDimension
	decimalseparator = AcadDimension.decimalseparator
	dimtxtdirection = AcadDimension.dimtxtdirection
	normal = AcadDimension.normal
	rotation = AcadDimension.rotation
	scalefactor = AcadDimension.scalefactor
	stylename = AcadDimension.stylename
	suppressleadingzeros = AcadDimension.suppressleadingzeros
	suppresstrailingzeros = AcadDimension.suppresstrailingzeros
	textcolor = AcadDimension.textcolor
	textfill = AcadDimension.textfill
	textfillcolor = AcadDimension.textfillcolor
	textgap = AcadDimension.textgap
	textheight = AcadDimension.textheight
	textmovement = AcadDimension.textmovement
	textoverride = AcadDimension.textoverride
	textposition = AcadDimension.textposition
	textprefix = AcadDimension.textprefix
	textrotation = AcadDimension.textrotation
	textstyle = AcadDimension.textstyle
	textsuffix = AcadDimension.textsuffix
	tolerancedisplay = AcadDimension.tolerancedisplay
	toleranceheightscale = AcadDimension.toleranceheightscale
	tolerancejustification = AcadDimension.tolerancejustification
	tolerancelowerlimit = AcadDimension.tolerancelowerlimit
	toleranceprecision = AcadDimension.toleranceprecision
	tolerancesuppressleadingzeros = AcadDimension.tolerancesuppressleadingzeros
	tolerancesuppresstrailingzeros = AcadDimension.tolerancesuppresstrailingzeros
	toleranceupperlimit = AcadDimension.toleranceupperlimit
	verticaltextposition = AcadDimension.verticaltextposition
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
	# Properties
	@property
	def altrounddistance(self) -> float:
		"Specifies distance rounding value for alternate units (DIMALTRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.AltRoundDistance
	@altrounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.AltRoundDistance = Distance

	@property
	def altsubunitsfactor(self) -> float:
		"Specifies the alternate sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.AltSubUnitsFactor
	@altsubunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.AltSubUnitsFactor = factor

	@property
	def altsubunitssuffix(self) -> str:
		"Specifies the text suffix for the alternate dimension when change to alternate sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.AltSubUnitsSuffix
	@altsubunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.AltSubUnitsSuffix = suffix

	@property
	def altsuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressLeadingZeros
	@altsuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressLeadingZeros = bVal

	@property
	def altsuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressTrailingZeros
	@altsuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressTrailingZeros = bVal

	@property
	def altsuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroFeet
	@altsuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroFeet = bVal

	@property
	def altsuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units dimensions On or Off (DIMALTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltSuppressZeroInches
	@altsuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltSuppressZeroInches = bVal

	@property
	def alttextprefix(self) -> str:
		"Specifies text prefix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextPrefix
	@alttextprefix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextPrefix = prefix

	@property
	def alttextsuffix(self) -> str:
		"Specifies text sufffix to alternate dimensions except angular (DIMAPOST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] prefix:str
		return self.com_parent.AltTextSuffix
	@alttextsuffix.setter
	def _(self, prefix:str):
		# ['in'] prefix:str
		self.com_parent.AltTextSuffix = prefix

	@property
	def alttoleranceprecision(self) -> int:
		"Specifies number of decimal places for tolerance values of an alternate units dimension (DIMALTTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:int | ENUM?
		return self.com_parent.AltTolerancePrecision
	@alttoleranceprecision.setter
	def _(self, Distance:int):
		# ['in'] Distance:int
		self.com_parent.AltTolerancePrecision = Distance

	@property
	def alttolerancesuppressleadingzeros(self) -> bool:
		"Sets suppression of leading zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressLeadingZeros
	@alttolerancesuppressleadingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressLeadingZeros = bVal

	@property
	def alttolerancesuppresstrailingzeros(self) -> bool:
		"Sets suppression of trailing zeros for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressTrailingZeros
	@alttolerancesuppresstrailingzeros.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressTrailingZeros = bVal

	@property
	def alttolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroFeet
	@alttolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroFeet = bVal

	@property
	def alttolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for alternate units tolerance values On or Off (DIMALTTZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.AltToleranceSuppressZeroInches
	@alttolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.AltToleranceSuppressZeroInches = bVal

	@property
	def altunits(self) -> bool:
		"Sets units format for alternate units dimensions On or Off, except angular (DIMALT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bAlternate:bool
		return self.com_parent.AltUnits
	@altunits.setter
	def _(self, bAlternate:bool):
		# ['in'] bAlternate:bool
		self.com_parent.AltUnits = bAlternate

	@property
	def altunitsformat(self) -> int:
		"Specifies units format for alternate units dimensions except angular (DIMALTU system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Units:int | ENUM?
		return self.com_parent.AltUnitsFormat
	@altunitsformat.setter
	def _(self, Units:int):
		# ['in'] Units:int
		self.com_parent.AltUnitsFormat = Units

	@property
	def altunitsprecision(self) -> int:
		"Specifies decimal place precision for alternate units (DIMALTD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] precision:int | ENUM?
		return self.com_parent.AltUnitsPrecision
	@altunitsprecision.setter
	def _(self, precision:int):
		# ['in'] precision:int
		self.com_parent.AltUnitsPrecision = precision

	@property
	def altunitsscale(self) -> float:
		"Specifies scale factor for alternate units (DIMALTF system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.AltUnitsScale
	@altunitsscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.AltUnitsScale = scale

	@property
	def arrowhead1block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the first end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead1Block
	@arrowhead1block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead1Block = BlockName

	@property
	def arrowhead1type(self) -> int:
		"Specifies type of the first dimension arrowhead (DIMBLK1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead1Type
	@arrowhead1type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead1Type = Type

	@property
	def arrowhead2block(self) -> str:
		"Specifies the block to use as the custom arrowhead for the second end of the dimension line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.Arrowhead2Block
	@arrowhead2block.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.Arrowhead2Block = BlockName

	@property
	def arrowhead2type(self) -> int:
		"Specifies type of the second dimension arrowhead (DIMBLK2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Arrowhead2Type
	@arrowhead2type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Arrowhead2Type = Type

	@property
	def arrowheadsize(self) -> float:
		"Specifies size of the dimension arrowhead (DIMASZ system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def dimconstrdesc(self) -> str:
		"Specifies description for constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDescription:str
		return self.com_parent.DimConstrDesc
	@dimconstrdesc.setter
	def _(self, bstrDescription:str):
		# ['in'] bstrDescription:str
		self.com_parent.DimConstrDesc = bstrDescription

	@property
	def dimconstrexpression(self) -> str:
		"Specifies the expression or the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] bstrExpression:str
		return self.com_parent.DimConstrExpression
	@dimconstrexpression.setter
	def _(self, bstrExpression:str):
		# ['in'] bstrExpression:str
		self.com_parent.DimConstrExpression = bstrExpression

	@property
	def dimconstrform(self) -> bool:
		"Specifies the constraint type - Dynamic or Annotational"
		# TODO: Check arguments
		# ['out', 'retval'] bIsDynamic:bool
		return self.com_parent.DimConstrForm
	@dimconstrform.setter
	def _(self, bIsDynamic:bool):
		# ['in'] bIsDynamic:bool
		self.com_parent.DimConstrForm = bIsDynamic

	@property
	def dimconstrname(self) -> str:
		"Specifies the name of the dimensional constraint. Names cannot have spaces"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.DimConstrName
	@dimconstrname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.DimConstrName = bstrName

	@property
	def dimconstrreference(self) -> bool:
		"Specifies whether the parameter is a reference constraint. Reference dimensions can be used in expressions but don't drive geometry - similar to an associative dimension"
		# TODO: Check arguments
		# ['out', 'retval'] bIsReference:bool
		return self.com_parent.DimConstrReference
	@dimconstrreference.setter
	def _(self, bIsReference:bool):
		# ['in'] bIsReference:bool
		self.com_parent.DimConstrReference = bIsReference

	@property
	def dimconstrvalue(self) -> str:
		"Specifies the value of the constraint"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		return self.com_parent.DimConstrValue
	@dimconstrvalue.setter
	def _(self, Value:str):
		# ['in'] Value:str
		self.com_parent.DimConstrValue = Value

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies color of the dimension lines (DIMCLRD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlineextend(self) -> float:
		"Specifies amount to extend dimension lines beyond the extension line (DIMDLE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.DimensionLineExtend
	@dimensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.DimensionLineExtend = extend

	@property
	def dimensionlinetype(self) -> str:
		"Specifies the linetype of the dimension line (DIMLTYPE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.DimensionLinetype
	@dimensionlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.DimensionLinetype = Linetype

	@property
	def dimensionlineweight(self) -> int:
		"Specifies lineweight for dimension lines (DIMLWD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def dimline1suppress(self) -> bool:
		"Sets suppression of first dimension line On or Off (DIMSD1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine1Suppress
	@dimline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine1Suppress = bSuppress

	@property
	def dimline2suppress(self) -> bool:
		"Sets suppression of second dimension line On or Off (DIMSD2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.DimLine2Suppress
	@dimline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.DimLine2Suppress = bSuppress

	@property
	def dimlineinside(self) -> bool:
		"Sets drawing of dimension lines outside extension lines On or Off (DIMSOXD system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.DimLineInside
	@dimlineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.DimLineInside = bInside

	@property
	def extensionlinecolor(self) -> int:
		"Specifies color of the extension line (DIMCLRE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int |ENUM?
		return self.com_parent.ExtensionLineColor
	@extensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ExtensionLineColor = Type

	@property
	def extensionlineextend(self) -> float:
		"Specifies amount to extend extension line beyond the dimension line (DIMEXE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] extend:float
		return self.com_parent.ExtensionLineExtend
	@extensionlineextend.setter
	def _(self, extend:float):
		# ['in'] extend:float
		self.com_parent.ExtensionLineExtend = extend

	@property
	def extensionlineoffset(self) -> float:
		"Specifies offset of extension lines from the origin points (DIMEXO system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.ExtensionLineOffset
	@extensionlineoffset.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.ExtensionLineOffset = Offset

	@property
	def extensionlineweight(self) -> int:
		"Specifies lineweight for extension lines (DIMLWE system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] lweight:int | ENUM?
		return self.com_parent.ExtensionLineWeight
	@extensionlineweight.setter
	def _(self, lweight:int):
		# ['in'] lweight:int
		self.com_parent.ExtensionLineWeight = lweight

	@property
	def extline1linetype(self) -> str:
		"Specifies the linetype of the first extension line (DIMLTEX1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine1Linetype
	@extline1linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine1Linetype = Linetype

	@property
	def extline1suppress(self) -> bool:
		"Sets suppression of first extension line On or Off (DIMSE1 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine1Suppress
	@extline1suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine1Suppress = bSuppress

	@property
	def extline2linetype(self) -> str:
		"Specifies the linetype of the second extension line (DIMLTEX2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ExtLine2Linetype
	@extline2linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ExtLine2Linetype = Linetype

	@property
	def extline2suppress(self) -> bool:
		"Sets suppression of second extension line On or Off (DIMSE2 system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bSuppress:bool
		return self.com_parent.ExtLine2Suppress
	@extline2suppress.setter
	def _(self, bSuppress:bool):
		# ['in'] bSuppress:bool
		self.com_parent.ExtLine2Suppress = bSuppress

	@property
	def extlinefixedlen(self) -> float:
		"Set extension line fixed length (DIMFXL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] FixedLen:float
		return self.com_parent.ExtLineFixedLen
	@extlinefixedlen.setter
	def _(self, FixedLen:float):
		# ['in'] FixedLen:float
		self.com_parent.ExtLineFixedLen = FixedLen

	@property
	def extlinefixedlensuppress(self) -> bool:
		"Sets suppression of extension line fixed length On or Off (DIMFXLON system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bFixedLen:bool
		return self.com_parent.ExtLineFixedLenSuppress
	@extlinefixedlensuppress.setter
	def _(self, bFixedLen:bool):
		# ['in'] bFixedLen:bool
		self.com_parent.ExtLineFixedLenSuppress = bFixedLen

	@property
	def fit(self) -> int:
		"Determines what elements are moved to fit text and arrowheads in space between extension lines (DIMATFIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] fittype:int | ENUM?
		return self.com_parent.Fit
	@fit.setter
	def _(self, fittype:int):
		# ['in'] fittype:int
		self.com_parent.Fit = fittype

	@property
	def forcelineinside(self) -> bool:
		"Forces drawing dimension line between extension lines On or Off, even when text is placed outside extension lines (DIMTOFL system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.ForceLineInside
	@forcelineinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.ForceLineInside = bInside

	@property
	def fractionformat(self) -> int:
		"Sets fraction type (DIMFRAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.FractionFormat
	@fractionformat.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.FractionFormat = Type

	@property
	def horizontaltextposition(self) -> int:
		"Specifies horizontal dimension text position (DIMJUST system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.HorizontalTextPosition
	@horizontaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.HorizontalTextPosition = Type

	@property
	def linearscalefactor(self) -> float:
		"Specifies global scale factor for linear dimensions (DIMLFAC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Type:float
		return self.com_parent.LinearScaleFactor
	@linearscalefactor.setter
	def _(self, Type:float):
		# ['in'] Type:float
		self.com_parent.LinearScaleFactor = Type

	@property
	def measurement(self) -> float:
		"Specifies dimension measurement value"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:float
		return self.com_parent.Measurement

	@property
	def primaryunitsprecision(self) -> int:
		"Specifies precision for primary units dimensions (DIMDEC system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Prec:int | ENUM?
		return self.com_parent.PrimaryUnitsPrecision
	@primaryunitsprecision.setter
	def _(self, Prec:int):
		# ['in'] Prec:int
		self.com_parent.PrimaryUnitsPrecision = Prec

	@property
	def rounddistance(self) -> float:
		"Specifies distance rounding value (DIMRND system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.RoundDistance
	@rounddistance.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.RoundDistance = Distance

	@property
	def subunitsfactor(self) -> float:
		"Specifies the sub-units scale factor for all applicable linear dimension"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.SubUnitsFactor
	@subunitsfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.SubUnitsFactor = factor

	@property
	def subunitssuffix(self) -> str:
		"Specifies the text suffix for all applicable linear dimension when change to sub-units"
		# TODO: Check arguments
		# ['out', 'retval'] suffix:str
		return self.com_parent.SubUnitsSuffix
	@subunitssuffix.setter
	def _(self, suffix:str):
		# ['in'] suffix:str
		self.com_parent.SubUnitsSuffix = suffix

	@property
	def suppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroFeet
	@suppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroFeet = bVal

	@property
	def suppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for dimensions On or Off (DIMZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.SuppressZeroInches
	@suppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.SuppressZeroInches = bVal

	@property
	def textinside(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInside
	@textinside.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInside = bInside

	@property
	def textinsidealign(self) -> bool:
		"Sets position of dimension text inside extension lines On or Off (DIMTIH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextInsideAlign
	@textinsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextInsideAlign = bInside

	@property
	def textoutsidealign(self) -> bool:
		"Sets positioning of dimension text outside extension lines On or Off (DIMTOH system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bInside:bool
		return self.com_parent.TextOutsideAlign
	@textoutsidealign.setter
	def _(self, bInside:bool):
		# ['in'] bInside:bool
		self.com_parent.TextOutsideAlign = bInside

	@property
	def tolerancesuppresszerofeet(self) -> bool:
		"Sets suppression of zero feet for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroFeet
	@tolerancesuppresszerofeet.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroFeet = bVal

	@property
	def tolerancesuppresszeroinches(self) -> bool:
		"Sets suppression of zero inches for tolerance values On or Off (DIMTZIN system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] bVal:bool
		return self.com_parent.ToleranceSuppressZeroInches
	@tolerancesuppresszeroinches.setter
	def _(self, bVal:bool):
		# ['in'] bVal:bool
		self.com_parent.ToleranceSuppressZeroInches = bVal

	@property
	def unitsformat(self) -> int:
		"Specifies units format for linear dimensions (DIMLUNIT system variable)"
		# TODO: Check arguments
		# ['out', 'retval'] format:int | ENUM?
		return self.com_parent.UnitsFormat
	@unitsformat.setter
	def _(self, format:int):
		# ['in'] format:int
		self.com_parent.UnitsFormat = format


class AcadUnderlay(POINTER(_dll.IAcadUnderlay), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadUnderlay
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadUnderlay VBA-class wrapped as AcadUnderlay python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def clipboundary(self, boundry: A2Vertex):
		"Get/Set clipping boundary"
		# TODO: Check arguments
		# ['in'] boundry:tagVARIANT | A2Vertex
		# VBA: object.ClipBoundary boundry
		self.com_parent.ClipBoundary(boundry)

	# Properties
	@property
	def adjustforbackground(self) -> bool:
		"Determines whether the underlay colors are adjusted for the current background color"
		# TODO: Check arguments
		# ['out', 'retval'] Value:bool
		return self.com_parent.AdjustForBackground
	@adjustforbackground.setter
	def _(self, Value:bool):
		# ['in'] Value:bool
		self.com_parent.AdjustForBackground = Value

	@property
	def clippingenabled(self) -> bool:
		"Enables or disables the clipping boundary of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] kClip:bool
		return self.com_parent.ClippingEnabled
	@clippingenabled.setter
	def _(self, kClip:bool):
		# ['in'] kClip:bool
		self.com_parent.ClippingEnabled = kClip

	@property
	def contrast(self) -> int:
		"Specifies the current contrast value of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] Contrast:int
		return self.com_parent.Contrast
	@contrast.setter
	def _(self, Contrast:int):
		# ['in'] Contrast:int
		self.com_parent.Contrast = Contrast

	@property
	def fade(self) -> int:
		"Specifies the current fade value of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] Fade:int
		return self.com_parent.Fade
	@fade.setter
	def _(self, Fade:int):
		# ['in'] Fade:int
		self.com_parent.Fade = Fade

	@property
	def file(self) -> str:
		"Specifies the path to the underlay file"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.File
	@file.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.File = Name

	@property
	def height(self) -> float:
		"Specifies the height of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def itemname(self) -> str:
		"Specifies the item of the underlay file"
		# TODO: Check arguments
		# ['out', 'retval'] sheetName:str
		return self.com_parent.ItemName
	@itemname.setter
	def _(self, sheetName:str):
		# ['in'] sheetName:str
		self.com_parent.ItemName = sheetName

	@property
	def monochrome(self) -> bool:
		"Determines whether underlay is monochrome or not"
		# TODO: Check arguments
		# ['out', 'retval'] bMono:bool
		return self.com_parent.Monochrome
	@monochrome.setter
	def _(self, bMono:bool):
		# ['in'] bMono:bool
		self.com_parent.Monochrome = bMono

	@property
	def position(self) -> A3Vertex:
		"Specifies the origin coordinates (lower left corner) of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] pos:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Position)
	@position.setter
	def _(self, pos:A3Vertex):
		# TODO: Check arguments
		# ['in'] pos:tagVARIANT | A3Vertex
		self.com_parent.Position = pos

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the scale factor of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.ScaleFactor = ScaleFactor

	@property
	def underlaylayeroverrideapplied(self) -> int:
		"Specifies layer override state for the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] bOverride:int | ENUM?
		return self.com_parent.UnderlayLayerOverrideApplied
	@underlaylayeroverrideapplied.setter
	def _(self, bOverride:int):
		# ['in'] bOverride:int
		self.com_parent.UnderlayLayerOverrideApplied = bOverride

	@property
	def underlayname(self) -> str:
		"Specifies the name of the underlay file"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.UnderlayName
	@underlayname.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.UnderlayName = Name

	@property
	def underlayvisibility(self) -> bool:
		"Determines whether underlay is visible or not"
		# TODO: Check arguments
		# ['out', 'retval'] fVisible:bool
		return self.com_parent.UnderlayVisibility
	@underlayvisibility.setter
	def _(self, fVisible:bool):
		# ['in'] fVisible:bool
		self.com_parent.UnderlayVisibility = fVisible

	@property
	def width(self) -> float:
		"Specifies the width of the underlay"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width

'''
TODO:
class AcadPdfUnderlay(AcadUnderlay):
	pass
class AcadDgnUnderlay(AcadUnderlay):
	pass
'''

class AcadDwfUnderlay(POINTER(_dll.IAcadDwfUnderlay), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadDwfUnderlay
	#	IAcadUnderlay
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadDwfUnderlay VBA-class wrapped as AcadDwfUnderlay python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	#Inherits from AcadUnderlay
	clipboundary					= AcadUnderlay.clipboundary
	adjustforbackground				= AcadUnderlay.adjustforbackground
	clippingenabled					= AcadUnderlay.clippingenabled
	contrast						= AcadUnderlay.contrast
	fade							= AcadUnderlay.fade
	file							= AcadUnderlay.file
	height							= AcadUnderlay.height
	itemname						= AcadUnderlay.itemname
	monochrome						= AcadUnderlay.monochrome
	position						= AcadUnderlay.position
	rotation						= AcadUnderlay.rotation
	scalefactor						= AcadUnderlay.scalefactor
	underlaylayeroverrideapplied	= AcadUnderlay.underlaylayeroverrideapplied
	underlayname					= AcadUnderlay.underlayname
	underlayvisibility				= AcadUnderlay.underlayvisibility
	width							= AcadUnderlay.width
	# Properties
	@property
	def dwfformat(self) -> str:
		"Specifies the format of DWF file"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.DWFFormat
	@dwfformat.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.DWFFormat = Name


class AcadEllipse(POINTER(_dll.IAcadEllipse), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadEllipse
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadEllipse VBA-class wrapped as AcadEllipse python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def offset(self, Distance: float) -> list:
		"method Offset"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT | list
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return ret

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def center(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the center point of the ellipse or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] Center:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Center)
	@center.setter
	def _(self, Center:A3Vertex):
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT | A3Vertex
		self.com_parent.Center = Center

	@property
	def endangle(self) -> float:
		"Specifies the end angle of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] EndAngle:float
		return self.com_parent.EndAngle
	@endangle.setter
	def _(self, EndAngle:float):
		# ['in'] EndAngle:float
		self.com_parent.EndAngle = EndAngle

	@property
	def endparameter(self) -> float:
		"Specifies the end parameter for an ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] EndParameter:float
		return self.com_parent.EndParameter
	@endparameter.setter
	def _(self, EndParameter:float):
		# ['in'] EndParameter:float
		self.com_parent.EndParameter = EndParameter

	@property
	def endpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the end point of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] EndPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.EndPoint)

	@property
	def majoraxis(self) -> A3Vertex:
		"Specifies the major axis of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] MajorAxis:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.MajorAxis)
	@majoraxis.setter
	def _(self, MajorAxis:A3Vertex):
		# TODO: Check arguments
		# ['in'] MajorAxis:tagVARIANT | A3Vertex
		self.com_parent.MajorAxis = MajorAxis

	@property
	def majorradius(self) -> float:
		"Specifies the major radius of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] MajorRadius:float
		return self.com_parent.MajorRadius
	@majorradius.setter
	def _(self, MajorRadius:float):
		# ['in'] MajorRadius:float
		self.com_parent.MajorRadius = MajorRadius

	@property
	def minoraxis(self) -> A3Vertex:
		"Specifies the minor axis of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] MinorAxis:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.MinorAxis)

	@property
	def minorradius(self) -> float:
		"Specifies the minor radius of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] MinorRadius:float
		return self.com_parent.MinorRadius
	@minorradius.setter
	def _(self, MinorRadius:float):
		# ['in'] MinorRadius:float
		self.com_parent.MinorRadius = MinorRadius

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def radiusratio(self) -> float:
		"Specifies the radius ratio of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] RadiusRatio:float
		return self.com_parent.RadiusRatio
	@radiusratio.setter
	def _(self, RadiusRatio:float):
		# ['in'] RadiusRatio:float
		self.com_parent.RadiusRatio = RadiusRatio

	@property
	def startangle(self) -> float:
		"Specifies the start angle of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] StartAngle:float
		return self.com_parent.StartAngle
	@startangle.setter
	def _(self, StartAngle:float):
		# ['in'] StartAngle:float
		self.com_parent.StartAngle = StartAngle

	@property
	def startparameter(self) -> float:
		"Specifies the start parameter for an ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] StartParameter:float
		return self.com_parent.StartParameter
	@startparameter.setter
	def _(self, StartParameter:float):
		# ['in'] StartParameter:float
		self.com_parent.StartParameter = StartParameter

	@property
	def startpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the start point of the ellipse"
		# TODO: Check arguments
		# ['out', 'retval'] StartPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.StartPoint)


class AcadExternalReference(POINTER(_dll.IAcadExternalReference), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadExternalReference
	#	IAcadBlockReference
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadExternalReference VBA-class wrapped as AcadExternalReference python-class
	# TODO list:
		# 1. COM-types to python-types vars and props -
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Inherits from AcadBlockReference
	converttoanonymousblock		= AcadBlockReference.converttoanonymousblock
	converttostaticblock		= AcadBlockReference.converttostaticblock
	effectivename				= AcadBlockReference.effectivename
	explode						= AcadBlockReference.explode
	getattributes				= AcadBlockReference.getattributes
	getconstantattributes		= AcadBlockReference.getconstantattributes
	getdynamicblockproperties	= AcadBlockReference.getdynamicblockproperties
	hasattributes				= AcadBlockReference.hasattributes
	insertionpoint				= AcadBlockReference.insertionpoint
	insunits					= AcadBlockReference.insunits
	insunitsfactor				= AcadBlockReference.insunitsfactor
	isdynamicblock				= AcadBlockReference.isdynamicblock
	name						= AcadBlockReference.name
	normal						= AcadBlockReference.normal
	resetblock					= AcadBlockReference.resetblock
	rotation					= AcadBlockReference.rotation
	xeffectivescalefactor		= AcadBlockReference.xeffectivescalefactor
	xscalefactor				= AcadBlockReference.xscalefactor
	yeffectivescalefactor		= AcadBlockReference.yeffectivescalefactor
	yscalefactor				= AcadBlockReference.yscalefactor
	zeffectivescalefactor		= AcadBlockReference.zeffectivescalefactor
	zscalefactor				= AcadBlockReference.zscalefactor
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
	# Properties
	@property
	def path(self) -> str:
		"Specifies the path of the external reference"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Path
	@path.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Path = bstrName


class AcadExternalReference2(POINTER(_dll.IAcadExternalReference2), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadExternalReference2
	#	IAcadExternalReference
	#		IAcadBlockReference
	#			IAcadEntity
	#				IAcadObject
	#					IDispatch
	#						IUnknown
	#							object
	# Prototype for IAcadExternalReference2 VBA-class wrapped as AcadExternalReference2 python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	converttoanonymousblock		= AcadBlockReference.converttoanonymousblock
	converttostaticblock		= AcadBlockReference.converttostaticblock
	effectivename				= AcadBlockReference.effectivename
	explode						= AcadBlockReference.explode
	getattributes				= AcadBlockReference.getattributes
	getconstantattributes		= AcadBlockReference.getconstantattributes
	getdynamicblockproperties	= AcadBlockReference.getdynamicblockproperties
	hasattributes				= AcadBlockReference.hasattributes
	insertionpoint				= AcadBlockReference.insertionpoint
	insunits					= AcadBlockReference.insunits
	insunitsfactor				= AcadBlockReference.insunitsfactor
	isdynamicblock				= AcadBlockReference.isdynamicblock
	name						= AcadBlockReference.name
	normal						= AcadBlockReference.normal
	resetblock					= AcadBlockReference.resetblock
	rotation					= AcadBlockReference.rotation
	xeffectivescalefactor		= AcadBlockReference.xeffectivescalefactor
	xscalefactor				= AcadBlockReference.xscalefactor
	yeffectivescalefactor		= AcadBlockReference.yeffectivescalefactor
	yscalefactor				= AcadBlockReference.yscalefactor
	zeffectivescalefactor		= AcadBlockReference.zeffectivescalefactor
	zscalefactor				= AcadBlockReference.zscalefactor
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
	path = AcadExternalReference.path
	# Properties
	@property
	def layerpropertyoverrides(self) -> bool:
		"Specifies whether the object has layer property overrides."
		# TODO: Check arguments
		# ['out', 'retval'] bOverrides:bool
		return self.com_parent.LayerPropertyOverrides


class AcadSurface(POINTER(_dll.IAcadSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSurface
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadSurface VBA-class wrapped as AcadSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +-
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	#	_IAcadSurface__com__get_EdgeExtensionDistances
	#	_IAcadSurface__com__set_EdgeExtensionDistances
	# Properties
	@property
	def edgeextensiondistances(self): # -> tagVARIANT:
		"Indicates the extension distances of the edges"
		# TODO: Check arguments
		# ['out', 'retval'] extDistances:tagVARIANT ???????????????????
		return self.com_parent.EdgeExtensionDistances
	@edgeextensiondistances.setter
	def _(self, extDistances):
		# TODO: Check arguments
		# ['in'] extDistances:tagVARIANT
		self.com_parent.EdgeExtensionDistances = extDistances

	@property
	def maintainassociativity(self) -> int:
		"Indicates if the surface is associated with another surface and also allows you to turn off associativity"
		# TODO: Check arguments
		# ['out', 'retval'] maintainAssoc:int
		return self.com_parent.MaintainAssociativity
	@maintainassociativity.setter
	def _(self, maintainAssoc:int):
		# ['in'] maintainAssoc:int
		self.com_parent.MaintainAssociativity = maintainAssoc

	@property
	def showassociativity(self) -> bool:
		"Higlights dependent surfaces"
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.ShowAssociativity
	@showassociativity.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.ShowAssociativity = bEnabled

	@property
	def surfacetype(self) -> str:
		"Indicates the type of surface"
		# TODO: Check arguments
		# ['out', 'retval'] SurfaceType:str
		return self.com_parent.SurfaceType

	@property
	def surftrimassociativity(self) -> bool:
		"Specifies whether or not the Mtext is annotative"
		# TODO: Check arguments
		# ['out', 'retval'] associative:tagVARIANT | bool ??????????
		return self.com_parent.SurfTrimAssociativity
	@surftrimassociativity.setter
	def _(self, associative:bool):
		# TODO: Check arguments
		# ['in'] associative:tagVARIANT | bool ??????????
		self.com_parent.SurfTrimAssociativity = associative

	@property
	def uisolinedensity(self) -> int:
		"Specifies the number of U isolines that are displayed"
		# TODO: Check arguments
		# ['out', 'retval'] density:int
		return self.com_parent.UIsolineDensity
	@uisolinedensity.setter
	def _(self, density:int):
		# ['in'] density:int
		self.com_parent.UIsolineDensity = density

	@property
	def visolinedensity(self) -> int:
		"Specifies the number of V isolines that are displayed"
		# TODO: Check arguments
		# ['out', 'retval'] density:int
		return self.com_parent.VIsolineDensity
	@visolinedensity.setter
	def _(self, density:int):
		# ['in'] density:int
		self.com_parent.VIsolineDensity = density

	@property
	def wireframetype(self) -> int:
		"Specifies the wireframe type of the selected surface"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.WireframeType
	@wireframetype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.WireframeType = Type


class AcadExtrudedSurface(POINTER(_dll.IAcadExtrudedSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadExtrudedSurface
	#	IAcadSurface
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadExtrudedSurface VBA-class wrapped as AcadExtrudedSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Inherits from AcadSurface
	edgeextensiondistances =	AcadSurface.edgeextensiondistances
	maintainassociativity =     AcadSurface.maintainassociativity
	showassociativity =         AcadSurface.showassociativity
	surfacetype =               AcadSurface.surfacetype
	surftrimassociativity =     AcadSurface.surftrimassociativity
	uisolinedensity =           AcadSurface.uisolinedensity
	visolinedensity =           AcadSurface.visolinedensity
	wireframetype =             AcadSurface.wireframetype
	# Properties
	@property
	def direction(self) -> A3Vertex:
		"Displays the extrusion direction"
		# TODO: Check arguments
		# ['out', 'retval'] Direction:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Direction)

	@property
	def height(self) -> float:
		"Specifies the height of the extrusion"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def taperangle(self) -> float:
		"Specifies the taper angle of the extrusion"
		# TODO: Check arguments
		# ['out', 'retval'] TaperAngle:float
		return self.com_parent.TaperAngle
	@taperangle.setter
	def _(self, TaperAngle:float):
		# ['in'] TaperAngle:float
		self.com_parent.TaperAngle = TaperAngle


class AcadGeoPositionMarker(POINTER(_dll.IAcadGeoPositionMarker), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadGeoPositionMarker
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadGeoPositionMarker VBA-class wrapped as AcadGeoPositionMarker python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def altitude(self) -> float:
		"Specifies the elevation of the marker"
		# TODO: Check arguments
		# ['out', 'retval'] Altitude:float
		return self.com_parent.Altitude
	@altitude.setter
	def _(self, Altitude:float):
		# ['in'] Altitude:float
		self.com_parent.Altitude = Altitude

	@property
	def backgroundfill(self) -> bool:
		"Specifies use Background Mask of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] bUseBackgroundFill:bool
		return self.com_parent.BackgroundFill
	@backgroundfill.setter
	def _(self, bUseBackgroundFill:bool):
		# ['in'] bUseBackgroundFill:bool
		self.com_parent.BackgroundFill = bUseBackgroundFill

	@property
	def drawingdirection(self) -> int:
		"Specifies the drawing direction of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] drawDir:int | ENUM?
		return self.com_parent.DrawingDirection
	@drawingdirection.setter
	def _(self, drawDir:int):
		# ['in'] drawDir:int
		self.com_parent.DrawingDirection = drawDir

	@property
	def height(self) -> float:
		"Specifies the height of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def landinggap(self) -> float:
		"Specify the landing distance"
		# TODO: Check arguments
		# ['out', 'retval'] gap:float
		return self.com_parent.LandingGap
	@landinggap.setter
	def _(self, gap:float):
		# ['in'] gap:float
		self.com_parent.LandingGap = gap

	@property
	def latitude(self) -> str:
		"Specifies the latitude of the marker"
		# TODO: Check arguments
		# ['out', 'retval'] Latitude:str
		return self.com_parent.Latitude
	@latitude.setter
	def _(self, Latitude:str):
		# ['in'] Latitude:str
		self.com_parent.Latitude = Latitude

	@property
	def linespacingdistance(self) -> float:
		"Specifies the line spacing distance of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Value:float
		return self.com_parent.LineSpacingDistance
	@linespacingdistance.setter
	def _(self, Value:float):
		# ['in'] Value:float
		self.com_parent.LineSpacingDistance = Value

	@property
	def linespacingfactor(self) -> float:
		"Specifies the line spacing factor of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.LineSpacingFactor
	@linespacingfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.LineSpacingFactor = factor

	@property
	def linespacingstyle(self) -> int:
		"Specifies the line spacing style of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] style:int | ENUM?
		return self.com_parent.LineSpacingStyle
	@linespacingstyle.setter
	def _(self, style:int):
		# ['in'] style:int
		self.com_parent.LineSpacingStyle = style

	@property
	def longitude(self) -> str:
		"Specifies the longitude of the marker"
		# TODO: Check arguments
		# ['out', 'retval'] Longitude:str
		return self.com_parent.Longitude
	@longitude.setter
	def _(self, Longitude:str):
		# ['in'] Longitude:str
		self.com_parent.Longitude = Longitude

	@property
	def notes(self) -> str:
		"Specifies the notes for the marker"
		# TODO: Check arguments
		# ['out', 'retval'] Notes:str
		return self.com_parent.Notes
	@notes.setter
	def _(self, Notes:str):
		# ['in'] Notes:str
		self.com_parent.Notes = Notes

	@property
	def position(self) -> A3Vertex:
		"Specify the marker's position"
		# TODO: Check arguments
		# ['out', 'retval'] Position:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Position)
	@position.setter
	def _(self, Position:A3Vertex):
		# TODO: Check arguments
		# ['in'] Position:tagVARIANT | A3Vertex
		self.com_parent.Position = Position

	@property
	def radius(self) -> float:
		"Radius"
		# TODO: Check arguments
		# ['out', 'retval'] gap:float
		return self.com_parent.Radius
	@radius.setter
	def _(self, gap:float):
		# ['in'] gap:float
		self.com_parent.Radius = gap

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def textframedisplay(self) -> bool:
		"Display/hide text frame of content"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.TextFrameDisplay
	@textframedisplay.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.TextFrameDisplay = pVal

	@property
	def textjustify(self) -> int:
		"Specifies the attachment point of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] attPoint:int | ENUM?
		return self.com_parent.TextJustify
	@textjustify.setter
	def _(self, attPoint:int):
		# ['in'] attPoint:int
		self.com_parent.TextJustify = attPoint

	@property
	def textstring(self) -> str:
		"Specifies the text string of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def textstylename(self) -> str:
		"Specifies the style name of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.TextStyleName
	@textstylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.TextStyleName = bstrName

	@property
	def textwidth(self) -> float:
		"Specifies the width of the MText"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.TextWidth
	@textwidth.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.TextWidth = Width


class AcadRasterImage(POINTER(_dll.IAcadRasterImage), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadRasterImage
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadRasterImage VBA-class wrapped as AcadRasterImage python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def clipboundary(self, boundry: A2Vertex):
		"Set clipping boundary"
		# TODO: Check arguments
		# ['in'] boundry:tagVARIANT | A2Vertex
		# VBA: object.ClipBoundary boundry
		self.com_parent.ClipBoundary(boundry)

	# Properties
	@property
	def brightness(self) -> int:
		"Specifies the current brightness value of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Brightness:int
		return self.com_parent.Brightness
	@brightness.setter
	def _(self, Brightness:int):
		# ['in'] Brightness:int
		self.com_parent.Brightness = Brightness

	@property
	def clippingenabled(self) -> bool:
		"Enables or disables the clipping boundary of the image"
		# TODO: Check arguments
		# ['out', 'retval'] kClip:bool
		return self.com_parent.ClippingEnabled
	@clippingenabled.setter
	def _(self, kClip:bool):
		# ['in'] kClip:bool
		self.com_parent.ClippingEnabled = kClip

	@property
	def contrast(self) -> int:
		"Specifies the current contrast value of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Contrast:int
		return self.com_parent.Contrast
	@contrast.setter
	def _(self, Contrast:int):
		# ['in'] Contrast:int
		self.com_parent.Contrast = Contrast

	@property
	def fade(self) -> int:
		"Specifies the current fade value of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Fade:int
		return self.com_parent.Fade
	@fade.setter
	def _(self, Fade:int):
		# ['in'] Fade:int
		self.com_parent.Fade = Fade

	@property
	def height(self) -> float:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] pixelHeight:float
		return self.com_parent.Height

	@property
	def imagefile(self) -> str:
		"Specifies the path to the image file"
		# TODO: Check arguments
		# ['out', 'retval'] imageFileName:str
		return self.com_parent.ImageFile
	@imagefile.setter
	def _(self, imageFileName:str):
		# ['in'] imageFileName:str
		self.com_parent.ImageFile = imageFileName

	@property
	def imageheight(self) -> float:
		"Specifies the height of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.ImageHeight
	@imageheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.ImageHeight = Height

	@property
	def imagevisibility(self) -> bool:
		"Determines whether image is visible or not"
		# TODO: Check arguments
		# ['out', 'retval'] fVisible:bool
		return self.com_parent.ImageVisibility
	@imagevisibility.setter
	def _(self, fVisible:bool):
		# ['in'] fVisible:bool
		self.com_parent.ImageVisibility = fVisible

	@property
	def imagewidth(self) -> float:
		"Specifies the width of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.ImageWidth
	@imagewidth.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.ImageWidth = Width

	@property
	def name(self) -> str:
		"Specifies the name of the image file"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.Name
	@name.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.Name = Name

	@property
	def origin(self) -> A3Vertex:
		"Specifies the origin coordinates (lower left corner) of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] Origin:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Origin)
	@origin.setter
	def _(self, Origin:A3Vertex):
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT | A3Vertex
		self.com_parent.Origin = Origin

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the scale factor of the raster image"
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.ScaleFactor = ScaleFactor

	@property
	def showrotation(self) -> bool:
		"Determines if a raster image is displayed at its rotation value"
		# TODO: Check arguments
		# ['out', 'retval'] bShow:bool
		return self.com_parent.ShowRotation
	@showrotation.setter
	def _(self, bShow:bool):
		# ['in'] bShow:bool
		self.com_parent.ShowRotation = bShow

	@property
	def transparency(self) -> bool:
		"Determines whether transparency for a bitonal image is On or Off"
		# TODO: Check arguments
		# ['out', 'retval'] bTransp:bool
		return self.com_parent.transparency
	@transparency.setter
	def _(self, bTransp:bool):
		# ['in'] bTransp:bool
		self.com_parent.transparency = bTransp

	@property
	def width(self) -> float:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] pixelWidth:float
		return self.com_parent.Width


class AcadGeomapImage(POINTER(_dll.IAcadGeomapImage), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadGeomapImage
	#	IAcadRasterImage
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadGeomapImage VBA-class wrapped as AcadGeomapImage python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	clipboundary	= AcadRasterImage.clipboundary
	brightness		= AcadRasterImage.brightness
	clippingenabled	= AcadRasterImage.clippingenabled
	contrast		= AcadRasterImage.contrast
	fade			= AcadRasterImage.fade
	height			= AcadRasterImage.height
	imagefile		= AcadRasterImage.imagefile
	imageheight		= AcadRasterImage.imageheight
	imagevisibility	= AcadRasterImage.imagevisibility
	imagewidth		= AcadRasterImage.imagewidth
	name			= AcadRasterImage.name
	origin			= AcadRasterImage.origin
	rotation		= AcadRasterImage.rotation
	scalefactor		= AcadRasterImage.scalefactor
	showrotation	= AcadRasterImage.showrotation
	transparency	= AcadRasterImage.transparency
	width			= AcadRasterImage.width
	
	# Properties
	@property
	def geoimagebrightness(self) -> int:
		"Specifies the brightness of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Brightness:int
		return self.com_parent.GeoImageBrightness
	@geoimagebrightness.setter
	def _(self, Brightness:int):
		# ['in'] Brightness:int
		self.com_parent.GeoImageBrightness = Brightness

	@property
	def geoimagecontrast(self) -> int:
		"Specifies the contrast of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Contrast:int
		return self.com_parent.GeoImageContrast
	@geoimagecontrast.setter
	def _(self, Contrast:int):
		# ['in'] Contrast:int
		self.com_parent.GeoImageContrast = Contrast

	@property
	def geoimagefade(self) -> int:
		"Specifies the fade of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Fade:int
		return self.com_parent.GeoImageFade
	@geoimagefade.setter
	def _(self, Fade:int):
		# ['in'] Fade:int
		self.com_parent.GeoImageFade = Fade

	@property
	def geoimageheight(self) -> float:
		"Specifies the height of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.GeoImageHeight

	@property
	def geoimageposition(self) -> A3Vertex:
		"Specifies the position of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Position:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.GeoImagePosition)

	@property
	def geoimagewidth(self) -> float:
		"Specifies the width of the Geomap image"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.GeoImageWidth


class AcadHatch(POINTER(_dll.IAcadHatch), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadHatch
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadHatch VBA-class wrapped as AcadHatch python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def appendinnerloop(self, ObjectArray: (array.array, list, tuple)):
		"Append loops to the hatch"
		# TODO: Check arguments
		# ['in'] ObjectArray:tagVARIANT
		# VBA: object.AppendInnerLoop ObjectArray
		self.com_parent.AppendInnerLoop(ObjectArray)

	def appendouterloop(self, ObjectArray: (array.array, list, tuple)):
		"Append loops to the hatch"
		# TODO: Check arguments
		# ['in'] ObjectArray:tagVARIANT | Iterable
		# VBA: object.AppendOuterLoop ObjectArray
		self.com_parent.AppendOuterLoop(ObjectArray)

	def evaluate(self):
		"Evaluate the hatch"
		# VBA: object.Evaluate 
		self.com_parent.Evaluate()

	def getloopat(self, Index: int) -> list:
		"Get loops at given index of the hatch"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out'] ObjectArray:tagVARIANT
		# VBA: object.GetLoopAt Index, ObjectArray
		ret = []
		for e in self.com_parent.GetLoopAt(Index):
			ret.append(CastManager.cast(e))
		return ret

	def insertloopat(self, Index: int, LoopType: int, ObjectArray: (array.array, list, tuple)):
		"Insert loops at given index to the hatch"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] LoopType:int
		# ['in'] ObjectArray:tagVARIANT | Iterable
		# VBA: object.InsertLoopAt Index, LoopType, ObjectArray
		self.com_parent.InsertLoopAt(Index, LoopType, ObjectArray)

	def setpattern(self, PatternType: int, PatternName: str):
		"Set Pattern Type and Name of the hatch"
		# ['in'] PatternType:int | ENUM?
		# ['in'] PatternName:str
		# VBA: object.SetPattern PatternType, PatternName
		self.com_parent.SetPattern(PatternType, PatternName)

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the hatch entity"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def associativehatch(self) -> bool:
		"Determines whether the hatch is associative or not"
		# TODO: Check arguments
		# ['out', 'retval'] fAssoc:bool
		return self.com_parent.AssociativeHatch
	@associativehatch.setter
	def _(self, fAssoc:bool):
		# ['in'] fAssoc:bool
		self.com_parent.AssociativeHatch = fAssoc

	@property
	def backgroundcolor(self) -> AcadAcCmColor:
		"Specifies the background color of the hatch."
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.BackgroundColor
	@backgroundcolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.BackgroundColor = pColor

	@property
	def elevation(self) -> float:
		"Specifies the elevation of the hatch relative to the Z axis of the objects' coordinate system"
		# TODO: Check arguments
		# ['out', 'retval'] Elevation:float
		return self.com_parent.Elevation
	@elevation.setter
	def _(self, Elevation:float):
		# ['in'] Elevation:float
		self.com_parent.Elevation = Elevation

	@property
	def gradientangle(self) -> float:
		"Specifies the gradient angle"
		# TODO: Check arguments
		# ['out', 'retval'] GradientAngle:float
		return self.com_parent.GradientAngle
	@gradientangle.setter
	def _(self, GradientAngle:float):
		# ['in'] GradientAngle:float
		self.com_parent.GradientAngle = GradientAngle

	@property
	def gradientcentered(self) -> bool:
		"Determines whether the gradient is centered or not"
		# TODO: Check arguments
		# ['out', 'retval'] fCentered:bool
		return self.com_parent.GradientCentered
	@gradientcentered.setter
	def _(self, fCentered:bool):
		# ['in'] fCentered:bool
		self.com_parent.GradientCentered = fCentered

	@property
	def gradientcolor1(self) -> AcadAcCmColor:
		"Specifies the gradient start color."
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.GradientColor1
	@gradientcolor1.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.GradientColor1 = pColor

	@property
	def gradientcolor2(self) -> AcadAcCmColor:
		"Specifies the gradient end color."
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.GradientColor2
	@gradientcolor2.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.GradientColor2 = pColor

	@property
	def gradientname(self) -> str:
		"Specifies the pattern name of the gradient."
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.GradientName
	@gradientname.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.GradientName = bstrName

	@property
	def hatchobjecttype(self) -> int:
		"Sets the type of the hatch."
		# TODO: Check arguments
		# ['out', 'retval'] hatchType:int | ENUM?
		return self.com_parent.HatchObjectType
	@hatchobjecttype.setter
	def _(self, hatchType:int):
		# ['in'] hatchType:int
		self.com_parent.HatchObjectType = hatchType

	@property
	def hatchstyle(self) -> int:
		"Sets the island display style of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] HatchStyle:int | ENUM?
		return self.com_parent.HatchStyle
	@hatchstyle.setter
	def _(self, HatchStyle:int):
		# ['in'] HatchStyle:int
		self.com_parent.HatchStyle = HatchStyle

	@property
	def isopenwidth(self) -> int:
		"Specifies the ISO pen width of an ISO hatch pattern"
		# TODO: Check arguments
		# ['out', 'retval'] penWidth:int | ENUM?
		return self.com_parent.ISOPenWidth
	@isopenwidth.setter
	def _(self, penWidth:int):
		# ['in'] penWidth:int
		self.com_parent.ISOPenWidth = penWidth

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def numberofloops(self) -> int:
		"Gets the number of loops in the hatch boundary"
		# TODO: Check arguments
		# ['out', 'retval'] numLoops:int
		return self.com_parent.NumberOfLoops

	@property
	def origin(self) -> A3Vertex:
		"Specifies the origin coordinates for the pattern of the hatch entity"
		# TODO: Check arguments
		# ['out', 'retval'] Origin:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Origin)
	@origin.setter
	def _(self, Origin:A3Vertex):
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT | A3Vertex
		self.com_parent.Origin = Origin

	@property
	def patternangle(self) -> float:
		"Specifies the pattern angle of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] PatternAngle:float
		return self.com_parent.PatternAngle
	@patternangle.setter
	def _(self, PatternAngle:float):
		# ['in'] PatternAngle:float
		self.com_parent.PatternAngle = PatternAngle

	@property
	def patterndouble(self) -> bool:
		"Determines whether the hatch pattern is double or not"
		# TODO: Check arguments
		# ['out', 'retval'] bDouble:bool
		return self.com_parent.PatternDouble
	@patterndouble.setter
	def _(self, bDouble:bool):
		# ['in'] bDouble:bool
		self.com_parent.PatternDouble = bDouble

	@property
	def patternname(self) -> str:
		"Specifies the pattern name of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.PatternName

	@property
	def patternscale(self) -> float:
		"Specifies the pattern scale of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] PatternScale:float
		return self.com_parent.PatternScale
	@patternscale.setter
	def _(self, PatternScale:float):
		# ['in'] PatternScale:float
		self.com_parent.PatternScale = PatternScale

	@property
	def patternspace(self) -> float:
		"Specifies the pattern space of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] PatternSpace:float
		return self.com_parent.PatternSpace
	@patternspace.setter
	def _(self, PatternSpace:float):
		# ['in'] PatternSpace:float
		self.com_parent.PatternSpace = PatternSpace

	@property
	def patterntype(self) -> int:
		"Specifies the pattern type of the hatch"
		# TODO: Check arguments
		# ['out', 'retval'] PatternType:int | ENUM?
		return self.com_parent.PatternType


class AcadHelix(POINTER(_dll.IAcadHelix), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadHelix
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadHelix VBA-class wrapped as AcadHelix python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def baseradius(self) -> float:
		"Specifies the base radius of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] Radius:float
		return self.com_parent.BaseRadius
	@baseradius.setter
	def _(self, Radius:float):
		# ['in'] Radius:float
		self.com_parent.BaseRadius = Radius

	@property
	def constrain(self) -> int:
		"Controls which property is constrained when editing other property values"
		# TODO: Check arguments
		# ['out', 'retval'] constrainType:int
		return self.com_parent.Constrain
	@constrain.setter
	def _(self, constrainType:int):
		# ['in'] constrainType:int
		self.com_parent.Constrain = constrainType

	@property
	def height(self) -> float:
		"Specifies the height of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Height
	@height.setter
	def _(self, Length:float):
		# ['in'] Length:float
		self.com_parent.Height = Length

	@property
	def position(self) -> A3Vertex:
		"Specifies the X, Y, and Z for the center of the base of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] StartPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Position)
	@position.setter
	def _(self, StartPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] StartPoint:tagVARIANT | A3Vertex
		self.com_parent.Position = StartPoint

	@property
	def topradius(self) -> float:
		"Specifies the top radius of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] Radius:float
		return self.com_parent.TopRadius
	@topradius.setter
	def _(self, Radius:float):
		# ['in'] Radius:float
		self.com_parent.TopRadius = Radius

	@property
	def totallength(self) -> float:
		"Specifies the total length of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] TotalLength:float
		return self.com_parent.TotalLength

	@property
	def turnheight(self) -> float:
		"Specifies the height of one full turn for the helix"
		# TODO: Check arguments
		# ['out', 'retval'] Distance:float
		return self.com_parent.TurnHeight
	@turnheight.setter
	def _(self, Distance:float):
		# ['in'] Distance:float
		self.com_parent.TurnHeight = Distance

	@property
	def turns(self) -> float:
		"Specifies the number of turns for the helix"
		# TODO: Check arguments
		# ['out', 'retval'] Turns:float
		return self.com_parent.Turns
	@turns.setter
	def _(self, Turns:float):
		# ['in'] Turns:float
		self.com_parent.Turns = Turns

	@property
	def turnslope(self) -> float:
		"Displays the constant incline angle for the helix path"
		# TODO: Check arguments
		# ['out', 'retval'] slopeAngle:float
		return self.com_parent.TurnSlope

	@property
	def twist(self) -> int:
		"Controls the twist direction of the helix"
		# TODO: Check arguments
		# ['out', 'retval'] twistType:int | ENUM?
		return self.com_parent.Twist
	@twist.setter
	def _(self, twistType:int):
		# ['in'] twistType:int
		self.com_parent.Twist = twistType


class AcadLWPolyline(POINTER(_dll.IAcadLWPolyline), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadLWPolyline
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadLWPolyline VBA-class wrapped as AcadLWPolyline python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def addvertex(self, Index: int, vertex: A3Vertex):
		"Adds a vertex to the lightweight polyline"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] vertex:tagVARIANT | A3Vertex
		# VBA: object.AddVertex Index, vertex
		self.com_parent.AddVertex(Index, vertex)

	def explode(self) -> list:
		"Explodes the lightweight polyline, and returns the sub-entities as an array of Object"
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret

	def getbulge(self, Index: int) -> float:
		"Returns the vertex bulge of the lightweight polyline"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] bulge:float
		# VBA: bulge = object.GetBulge (Index)
		return self.com_parent.GetBulge(Index)

	def getwidth(self, Index: int):
		"Returns segment width of the lightweight polyline"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out'] StartWidth:float
		# ['out'] EndWidth:float
		# VBA: object.GetWidth Index, StartWidth, EndWidth
		return self.com_parent.GetWidth(Index)

	def offset(self, Distance: float) -> list:
		"Creates a new entity object by offsetting the lightweight polyline by a given distance"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return ret

	def setbulge(self, Index: int, bulge: float):
		"Sets the vertex bulge of the lightweight polyline"
		# ['in'] Index:int
		# ['in'] bulge:float
		# VBA: object.SetBulge Index, bulge
		self.com_parent.SetBulge(Index, bulge)

	def setwidth(self, Index: int, StartWidth: float, EndWidth: float):
		"Sets the segment width of the lightweight polyline"
		# ['in'] Index:int
		# ['in'] StartWidth:float
		# ['in'] EndWidth:float
		# VBA: object.SetWidth Index, StartWidth, EndWidth
		self.com_parent.SetWidth(Index, StartWidth, EndWidth)

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the lightweight polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def closed(self) -> bool:
		"Determines whether polyline is Open or Closed. Closed draws a line segment from current position to starting point of the polyline."
		# TODO: Check arguments
		# ['out', 'retval'] fClose:bool
		return self.com_parent.Closed
	@closed.setter
	def _(self, fClose:bool):
		# ['in'] fClose:bool
		self.com_parent.Closed = fClose

	@property
	def constantwidth(self) -> float:
		"Specifies the constant width for the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.ConstantWidth
	@constantwidth.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.ConstantWidth = Width

	@indexedproperty
	def coordinate(self, Index:int) -> A2Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A2Vertex
		return A2Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A2Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A2Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A2Vertexes:
		"Specifies the current vertex of the lightweight polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT
		return A2Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A2Vertexes):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT
		self.com_parent.Coordinates = Coordinates.flatten

	@property
	def elevation(self) -> float:
		"Specifies the elevation of the polyline relative to the Z axis of the objects' coordinate system (Z coordinate of current vertex)"
		# TODO: Check arguments
		# ['out', 'retval'] Elevation:float
		return self.com_parent.Elevation
	@elevation.setter
	def _(self, Elevation:float):
		# ['in'] Elevation:float
		self.com_parent.Elevation = Elevation

	@property
	def length(self) -> float:
		"Specifies the length of the lightweight polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Length

	@property
	def linetypegeneration(self) -> bool:
		"Determines whether linetype generation is Enabled or Disabled for the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] bLinetypeGen:bool
		return self.com_parent.LinetypeGeneration
	@linetypegeneration.setter
	def _(self, bLinetypeGen:bool):
		# ['in'] bLinetypeGen:bool
		self.com_parent.LinetypeGeneration = bLinetypeGen

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the lightweight polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadLeader(POINTER(_dll.IAcadLeader), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadLeader
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadLeader VBA-class wrapped as AcadLeader python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def evaluate(self):
		"Evaluate the leader"
		# VBA: object.Evaluate 
		self.com_parent.Evaluate()

	# Properties
	@property
	def annotation(self):# -> AcadEntity:
		"Specifies the annotation object for a leader"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:AcadEntity ADD CAST???
		return CastManager.cast(self.com_parent.Annotation)
	@annotation.setter
	def _(self, pVal):#:AcadEntity):
		# TODO: Check arguments
		# ['in'] pVal:AcadEntity
		self.com_parent.Annotation = pVal

	@property
	def arrowheadblock(self) -> str:
		"Specifies the block to use as the custom arrowhead for a radial dimension or leader line"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ArrowheadBlock
	@arrowheadblock.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ArrowheadBlock = BlockName

	@property
	def arrowheadsize(self) -> float:
		"Specifies the size of the leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def arrowheadtype(self) -> int:
		"Specifies the type of the leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ArrowheadType
	@arrowheadtype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ArrowheadType = Type

	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the coordinates of the leader"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = Coordinates.flatten

	@property
	def dimensionlinecolor(self) -> int:
		"Specifies the color of the leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def dimensionlineweight(self) -> int:
		"Specifies the lineweight of the leader line"
		# TODO: Check arguments
		# ['out', 'retval'] weight:int | ENUM?
		return self.com_parent.DimensionLineWeight
	@dimensionlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.DimensionLineWeight = weight

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)

	@property
	def scalefactor(self) -> float:
		"Specifies the overall scale factor applied to properties that specify sizes, distances, or offsets"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.ScaleFactor = factor

	@property
	def stylename(self) -> str:
		"Specifies the style name of the leader"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def textgap(self) -> float:
		"Specifies the distance around the dimension text that the dimension line is broken"
		# TODO: Check arguments
		# ['out', 'retval'] Offset:float
		return self.com_parent.TextGap
	@textgap.setter
	def _(self, Offset:float):
		# ['in'] Offset:float
		self.com_parent.TextGap = Offset

	@property
	def type(self) -> int:
		"Specifies the type of the leader"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Type
	@type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Type = Type

	@property
	def verticaltextposition(self) -> int:
		"Specifies the vertical dimension text position"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.VerticalTextPosition
	@verticaltextposition.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.VerticalTextPosition = Type


class AcadLine(POINTER(_dll.IAcadLine), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadLine
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadLine VBA-class wrapped as AcadLine python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Methods
	def offset(self, Distance: float) -> list:
		"Creates a new line by offsetting the current line by a specified distance"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return ret

	# Properties
	@property
	def angle(self) -> float:
		"Specifies the angle of the line"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.Angle

	@property
	def delta(self) -> A3Vertex:
		"Specifies the delta of the line"
		# TODO: Check arguments
		# ['out', 'retval'] Delta:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Delta)

	@property
	def endpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the end point of the line or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] EndPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.EndPoint)
	@endpoint.setter
	def _(self, EndPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] EndPoint:tagVARIANT | A3Vertex
		self.com_parent.EndPoint = EndPoint

	@property
	def length(self) -> float:
		"Specifies the length of the line"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Length

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def startpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the start point of the line or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] StartPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.StartPoint)
	@startpoint.setter
	def _(self, StartPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] StartPoint:tagVARIANT | A3Vertex
		self.com_parent.StartPoint = StartPoint

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the line"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadLoftedSurface(POINTER(_dll.IAcadLoftedSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadLoftedSurface
	#	IAcadSurface
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadLoftedSurface VBA-class wrapped as AcadLoftedSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	edgeextensiondistances =	AcadSurface.edgeextensiondistances
	maintainassociativity =     AcadSurface.maintainassociativity
	showassociativity =         AcadSurface.showassociativity
	surfacetype =               AcadSurface.surfacetype
	surftrimassociativity =     AcadSurface.surftrimassociativity
	uisolinedensity =           AcadSurface.uisolinedensity
	visolinedensity =           AcadSurface.visolinedensity
	wireframetype =             AcadSurface.wireframetype
	# Properties
	@property
	def closed(self) -> bool:
		"Specfies whether loft object is open or closed"
		# TODO: Check arguments
		# ['out', 'retval'] bClosed:bool
		return self.com_parent.Closed
	@closed.setter
	def _(self, bClosed:bool):
		# ['in'] bClosed:bool
		self.com_parent.Closed = bClosed

	@property
	def enddraftangle(self) -> float:
		"Specifies the draft angle of the surface for the last cross section"
		# TODO: Check arguments
		# ['out', 'retval'] EndDraftAngle:float
		return self.com_parent.EndDraftAngle
	@enddraftangle.setter
	def _(self, EndDraftAngle:float):
		# ['in'] EndDraftAngle:float
		self.com_parent.EndDraftAngle = EndDraftAngle

	@property
	def enddraftmagnitude(self) -> float:
		"Specifies the draft magnitude of the surface for the last cross section"
		# TODO: Check arguments
		# ['out', 'retval'] endDraftMag:float
		return self.com_parent.EndDraftMagnitude
	@enddraftmagnitude.setter
	def _(self, endDraftMag:float):
		# ['in'] endDraftMag:float
		self.com_parent.EndDraftMagnitude = endDraftMag

	@property
	def endsmoothcontinuity(self) -> int:
		"Specifies smooth continuity of the surface for the last cross section"
		# TODO: Check arguments
		# ['out', 'retval'] EndSmoothContinuity:int | ENUM?
		return self.com_parent.EndSmoothContinuity
	@endsmoothcontinuity.setter
	def _(self, EndSmoothContinuity:int):
		# ['in'] EndSmoothContinuity:int
		self.com_parent.EndSmoothContinuity = EndSmoothContinuity

	@property
	def endsmoothmagnitude(self) -> float:
		"Specifies smooth magnitude of the surface for the last cross section"
		# TODO: Check arguments
		# ['out', 'retval'] endSmoothMag:float
		return self.com_parent.EndSmoothMagnitude
	@endsmoothmagnitude.setter
	def _(self, endSmoothMag:float):
		# ['in'] endSmoothMag:float
		self.com_parent.EndSmoothMagnitude = endSmoothMag

	@property
	def numcrosssections(self) -> int:
		"Displays the number of cross-section curves used"
		# TODO: Check arguments
		# ['out', 'retval'] NumCrossSections:int
		return self.com_parent.NumCrossSections

	@property
	def numguidepaths(self) -> int:
		"Displays the number of guide paths used"
		# TODO: Check arguments
		# ['out', 'retval'] NumGuidePaths:int
		return self.com_parent.NumGuidePaths

	@property
	def periodic(self) -> bool:
		"Specfies whether loft object is periodic."
		# TODO: Check arguments
		# ['out', 'retval'] bPeriodic:bool
		return self.com_parent.Periodic
	@periodic.setter
	def _(self, bPeriodic:bool):
		# ['in'] bPeriodic:bool
		self.com_parent.Periodic = bPeriodic

	@property
	def startdraftangle(self) -> float:
		"Specifies the draft angle of the surface for the first cross section"
		# TODO: Check arguments
		# ['out', 'retval'] StartDraftAngle:float
		return self.com_parent.StartDraftAngle
	@startdraftangle.setter
	def _(self, StartDraftAngle:float):
		# ['in'] StartDraftAngle:float
		self.com_parent.StartDraftAngle = StartDraftAngle

	@property
	def startdraftmagnitude(self) -> float:
		"Specifies the draft magnitude of the surface for the first cross section"
		# TODO: Check arguments
		# ['out', 'retval'] startDraftMag:float
		return self.com_parent.StartDraftMagnitude
	@startdraftmagnitude.setter
	def _(self, startDraftMag:float):
		# ['in'] startDraftMag:float
		self.com_parent.StartDraftMagnitude = startDraftMag

	@property
	def startsmoothcontinuity(self) -> int:
		"Specifies smooth continuity of the surface for the first cross section"
		# TODO: Check arguments
		# ['out', 'retval'] StartSmoothContinuity:int | ENUM?
		return self.com_parent.StartSmoothContinuity
	@startsmoothcontinuity.setter
	def _(self, StartSmoothContinuity:int):
		# ['in'] StartSmoothContinuity:int
		self.com_parent.StartSmoothContinuity = StartSmoothContinuity

	@property
	def startsmoothmagnitude(self) -> float:
		"Specifies smooth magnitude of the surface for the first cross section"
		# TODO: Check arguments
		# ['out', 'retval'] startSmoothMag:float
		return self.com_parent.StartSmoothMagnitude
	@startsmoothmagnitude.setter
	def _(self, startSmoothMag:float):
		# ['in'] startSmoothMag:float
		self.com_parent.StartSmoothMagnitude = startSmoothMag

	@property
	def surfacenormals(self) -> int:
		"Specifies for which cross-section curves the surface is normal to the cross section"
		# TODO: Check arguments
		# ['out', 'retval'] surfaceNormal:int
		return self.com_parent.SurfaceNormals
	@surfacenormals.setter
	def _(self, surfaceNormal:int):
		# ['in'] surfaceNormal:int
		self.com_parent.SurfaceNormals = surfaceNormal


class AcadMInsertBlock(POINTER(_dll.IAcadMInsertBlock), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadMInsertBlock
	#	IAcadBlockReference
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadMInsertBlock VBA-class wrapped as AcadMInsertBlock python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	converttoanonymousblock		= AcadBlockReference.converttoanonymousblock
	converttostaticblock		= AcadBlockReference.converttostaticblock
	effectivename				= AcadBlockReference.effectivename
	explode						= AcadBlockReference.explode
	getattributes				= AcadBlockReference.getattributes
	getconstantattributes		= AcadBlockReference.getconstantattributes
	getdynamicblockproperties	= AcadBlockReference.getdynamicblockproperties
	hasattributes				= AcadBlockReference.hasattributes
	insertionpoint				= AcadBlockReference.insertionpoint
	insunits					= AcadBlockReference.insunits
	insunitsfactor				= AcadBlockReference.insunitsfactor
	isdynamicblock				= AcadBlockReference.isdynamicblock
	name						= AcadBlockReference.name
	normal						= AcadBlockReference.normal
	resetblock					= AcadBlockReference.resetblock
	rotation					= AcadBlockReference.rotation
	xeffectivescalefactor		= AcadBlockReference.xeffectivescalefactor
	xscalefactor				= AcadBlockReference.xscalefactor
	yeffectivescalefactor		= AcadBlockReference.yeffectivescalefactor
	yscalefactor				= AcadBlockReference.yscalefactor
	zeffectivescalefactor		= AcadBlockReference.zeffectivescalefactor
	zscalefactor				= AcadBlockReference.zscalefactor
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
	# Properties
	@property
	def columns(self) -> int:
		"Specifies the number of columns in the block array"
		# TODO: Check arguments
		# ['out', 'retval'] NumColumns:int
		return self.com_parent.Columns
	@columns.setter
	def _(self, NumColumns:int):
		# ['in'] NumColumns:int
		self.com_parent.Columns = NumColumns

	@property
	def columnspacing(self) -> float:
		"Specifies the column spacing in the block array"
		# TODO: Check arguments
		# ['out', 'retval'] Spacing:float
		return self.com_parent.ColumnSpacing
	@columnspacing.setter
	def _(self, Spacing:float):
		# ['in'] Spacing:float
		self.com_parent.ColumnSpacing = Spacing

	@property
	def rows(self) -> int:
		"Determines the number of columns in the block array"
		# TODO: Check arguments
		# ['out', 'retval'] NumRows:int
		return self.com_parent.Rows
	@rows.setter
	def _(self, NumRows:int):
		# ['in'] NumRows:int
		self.com_parent.Rows = NumRows

	@property
	def rowspacing(self) -> float:
		"Specifies the row spacing in the block array"
		# TODO: Check arguments
		# ['out', 'retval'] Spacing:float
		return self.com_parent.RowSpacing
	@rowspacing.setter
	def _(self, Spacing:float):
		# ['in'] Spacing:float
		self.com_parent.RowSpacing = Spacing


class AcadMLeader(POINTER(_dll.IAcadMLeader), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadMLeader
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadMLeader VBA-class wrapped as AcadMLeader python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def addleader(self) -> int:
		"Adds a new leader cluster to this multileader object"
		# TODO: Check arguments
		# ['out', 'retval'] leaderIndex:int
		# VBA: leaderIndex = object.AddLeader ()
		return self.com_parent.AddLeader()

	def addleaderline(self, leaderIndex: int, pointArray: A3Vertex) -> int:
		"Adds a leader line to the leader cluster with specified index"
		# TODO: Check arguments
		# ['in'] leaderIndex:int
		# ['in'] pointArray:tagVARIANT | A3Vertex
		# ['out', 'retval'] leaderLineIndex:int
		# VBA: leaderLineIndex = object.AddLeaderLine (leaderIndex, pointArray)
		return self.com_parent.AddLeaderLine(leaderIndex, pointArray)

	def addleaderlineex(self, pointArray: A3Vertex) -> int:
		"Adds a new leader line to this multileader object determined by input point which will be the first point of new leader line"
		# TODO: Check arguments
		# ['in'] pointArray:tagVARIANT | A3Vertex
		# ['out', 'retval'] leaderLineIndex:int
		# VBA: leaderLineIndex = object.AddLeaderLineEx (pointArray)
		return self.com_parent.AddLeaderLineEx(pointArray)

	def getblockattributevalue(self, attdefId: int) -> str:
		"Gets attribute value in block content determined by attribute definition id"
		# TODO: Check arguments
		# ['in'] attdefId:int
		# ['out', 'retval'] Value:str
		# VBA: Value = object.GetBlockAttributeValue (attdefId)
		return self.com_parent.GetBlockAttributeValue(attdefId)

	def getdoglegdirection(self, leaderIndex: int) -> A3Vertex:
		"Gets the dog leg direction of the specific leader"
		# TODO: Check arguments
		# ['in'] leaderIndex:int
		# ['out', 'retval'] dirVec:tagVARIANT | A3Vertex
		# VBA: dirVec = object.GetDoglegDirection (leaderIndex)
		return A3Vertex(self.com_parent.GetDoglegDirection(leaderIndex))

	def getleaderindex(self, leaderLineIndex: int) -> int:
		"Gets the index of leader cluster which the specified leader line is in"
		# TODO: Check arguments
		# ['in'] leaderLineIndex:int
		# ['out', 'retval'] leaderIndex:int
		# VBA: leaderIndex = object.GetLeaderIndex (leaderLineIndex)
		return self.com_parent.GetLeaderIndex(leaderLineIndex)

	def getleaderlineindexes(self, leaderIndex: int) -> A3Vertex:
		"Gets the indexes of leader lines of the specific leader"
		# TODO: Check arguments
		# ['in'] leaderIndex:int
		# ['out', 'retval'] leaderLineIndexes:tagVARIANT | A3Vertex ????????????????????
		# VBA: leaderLineIndexes = object.GetLeaderLineIndexes (leaderIndex)
		return A3Vertex(self.com_parent.GetLeaderLineIndexes(leaderIndex))

	def getleaderlinevertices(self, leaderLineIndex: int) -> A3Vertexes:
		"Specifies the vertices of leader line with specified index"
		# TODO: Check arguments
		# ['in'] leaderLineIndex:int
		# ['out', 'retval'] pointArray:tagVARIANT | A3Vertexes ???????????????????????????
		# VBA: pointArray = object.GetLeaderLineVertices (leaderLineIndex)
		return A3Vertexes(self.com_parent.GetLeaderLineVertices(leaderLineIndex))

	def getvertexcount(self, leaderLineIndex: int) -> int:
		"Gets the number of vertices in the specified leader line"
		# TODO: Check arguments
		# ['in'] leaderLineIndex:int
		# ['out', 'retval'] number:int
		# VBA: number = object.GetVertexCount (leaderLineIndex)
		return self.com_parent.GetVertexCount(leaderLineIndex)

	def removeleader(self, leaderIndex: int):
		"Removes the leader cluster with specified index"
		# ['in'] leaderIndex:int
		# VBA: object.RemoveLeader leaderIndex
		self.com_parent.RemoveLeader(leaderIndex)

	def removeleaderline(self, leaderLineIndex: int):
		"Removes the leader line with specified index"
		# ['in'] leaderLineIndex:int
		# VBA: object.RemoveLeaderLine leaderLineIndex
		self.com_parent.RemoveLeaderLine(leaderLineIndex)

	def setblockattributevalue(self, attdefId: int, Value: str):
		"Sets attribute value in block content with attribute definition id"
		# ['in'] attdefId:int
		# ['in'] Value:str
		# VBA: object.SetBlockAttributeValue attdefId, Value
		self.com_parent.SetBlockAttributeValue(attdefId, Value)

	def setdoglegdirection(self, leaderIndex: int, dirVec: A3Vertex):
		"Sets the dog leg direction of the specific leader"
		# TODO: Check arguments
		# ['in'] leaderIndex:int
		# ['in'] dirVec:tagVARIANT | A3Vertex ????????????????
		# VBA: object.SetDoglegDirection leaderIndex, dirVec
		self.com_parent.SetDoglegDirection(leaderIndex, dirVec)

	def setleaderlinevertices(self, leaderLineIndex: int, pointArray: A3Vertex):
		"Specifies the vertices of leader line with specified index"
		# TODO: Check arguments
		# ['in'] leaderLineIndex:int
		# ['in'] pointArray:tagVARIANT | A3Vertex ????????????????????
		# VBA: object.SetLeaderLineVertices leaderLineIndex, pointArray
		self.com_parent.SetLeaderLineVertices(leaderLineIndex, pointArray)

	# Properties
	@property
	def arrowheadblock(self) -> str:
		"Specifies the block to use as the custom arrowhead for leader lines of multileader"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ArrowheadBlock
	@arrowheadblock.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ArrowheadBlock = BlockName

	@property
	def arrowheadsize(self) -> float:
		"Specifies the size of leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@property
	def arrowheadtype(self) -> int:
		"Specifies the type of leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:int | ENUM?
		return self.com_parent.ArrowheadType
	@arrowheadtype.setter
	def _(self, BlockName:int):
		# ['in'] BlockName:int
		self.com_parent.ArrowheadType = BlockName

	@property
	def blockconnectiontype(self) -> int:
		"Specify how leaders connect with content block"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.BlockConnectionType
	@blockconnectiontype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.BlockConnectionType = Type

	@property
	def blockscale(self) -> float:
		"Specify how leaders connect with content block"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.BlockScale
	@blockscale.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.BlockScale = factor

	@property
	def contentblockname(self) -> str:
		"Specify the name of multileader's content block"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ContentBlockName
	@contentblockname.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ContentBlockName = BlockName

	@property
	def contentblocktype(self) -> int:
		"Specifies the content block of multileader"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ContentBlockType
	@contentblocktype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ContentBlockType = Type

	@property
	def contenttype(self) -> int:
		"Specifies the content type of this multileader object"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.ContentType
	@contenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ContentType = Type

	@property
	def doglegged(self) -> bool:
		"Enable/Disable horizontal landing of multileader"
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.DogLegged
	@doglegged.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.DogLegged = val

	@property
	def dogleglength(self) -> float:
		"Specify the landing distance"
		# TODO: Check arguments
		# ['out', 'retval'] DoglegLength:float
		return self.com_parent.DoglegLength
	@dogleglength.setter
	def _(self, DoglegLength:float):
		# ['in'] DoglegLength:float
		self.com_parent.DoglegLength = DoglegLength

	@property
	def landinggap(self) -> float:
		"Specify the text landing gap"
		# TODO: Check arguments
		# ['out', 'retval'] gap:float
		return self.com_parent.LandingGap
	@landinggap.setter
	def _(self, gap:float):
		# ['in'] gap:float
		self.com_parent.LandingGap = gap

	@property
	def leadercount(self) -> int:
		"Gets the number of leader line clusters in this multileader object"
		# TODO: Check arguments
		# ['out', 'retval'] number:int
		return self.com_parent.LeaderCount

	@property
	def leaderlinecolor(self) -> AcadAcCmColor:
		"Specifies the color of the leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Type:AcadAcCmColor
		return self.com_parent.LeaderLineColor
	@leaderlinecolor.setter
	def _(self, Type:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] Type:AcadAcCmColor
		self.com_parent.LeaderLineColor = Type

	@property
	def leaderlinetype(self) -> str:
		"Specifies the linetype of leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.LeaderLinetype
	@leaderlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.LeaderLinetype = Linetype

	@property
	def leaderlineweight(self) -> int:
		"Specifies the line weight of leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int | ENUM?
		return self.com_parent.LeaderLineWeight
	@leaderlineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.LeaderLineWeight = Lineweight

	@property
	def leadertype(self) -> int:
		"Specifies the leader type"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.LeaderType
	@leadertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.LeaderType = Type

	@property
	def scalefactor(self) -> float:
		"Specifies the overall scale factor of this multileader object"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.ScaleFactor = scale

	@property
	def stylename(self) -> str:
		"Specifies the style name of this multileader object"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.StyleName = Name

	@property
	def textattachmentdirection(self) -> int:
		"Specifies if leaders connect with the text horizontally or vertically"
		# TODO: Check arguments
		# ['out', 'retval'] dir:int | ENUM?
		return self.com_parent.TextAttachmentDirection
	@textattachmentdirection.setter
	def _(self, dir:int):
		# ['in'] dir:int
		self.com_parent.TextAttachmentDirection = dir

	@property
	def textbackgroundfill(self) -> bool:
		"Specifies use Background Mask"
		# TODO: Check arguments
		# ['out', 'retval'] bUseBackgroundFill:bool
		return self.com_parent.TextBackgroundFill
	@textbackgroundfill.setter
	def _(self, bUseBackgroundFill:bool):
		# ['in'] bUseBackgroundFill:bool
		self.com_parent.TextBackgroundFill = bUseBackgroundFill

	@property
	def textbottomattachmenttype(self) -> int:
		"Specifies how leaders on the bottom connect with the text"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.TextBottomAttachmentType
	@textbottomattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextBottomAttachmentType = Type

	@property
	def textdirection(self) -> int:
		"Specifies the drawing direction of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] drawDir:int | ENUM?
		return self.com_parent.TextDirection
	@textdirection.setter
	def _(self, drawDir:int):
		# ['in'] drawDir:int
		self.com_parent.TextDirection = drawDir

	@property
	def textframedisplay(self) -> bool:
		"Display/hide text frame of multileader content"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.TextFrameDisplay
	@textframedisplay.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.TextFrameDisplay = pVal

	@property
	def textheight(self) -> float:
		"Specifies the height of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.TextHeight
	@textheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.TextHeight = Height

	@property
	def textjustify(self) -> int:
		"Specifies the attachment point of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] attPoint:int | ENUM?
		return self.com_parent.TextJustify
	@textjustify.setter
	def _(self, attPoint:int):
		# ['in'] attPoint:int
		self.com_parent.TextJustify = attPoint

	@property
	def textleftattachmenttype(self) -> int:
		"Specify how leaders on the left side connect with the text"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.TextLeftAttachmentType
	@textleftattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextLeftAttachmentType = Type

	@property
	def textlinespacingdistance(self) -> float:
		"Specifies the line spacing distance of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Value:float
		return self.com_parent.TextLineSpacingDistance
	@textlinespacingdistance.setter
	def _(self, Value:float):
		# ['in'] Value:float
		self.com_parent.TextLineSpacingDistance = Value

	@property
	def textlinespacingfactor(self) -> float:
		"Specifies the line spacing factor of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.TextLineSpacingFactor
	@textlinespacingfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.TextLineSpacingFactor = factor

	@property
	def textlinespacingstyle(self) -> int:
		"Specifies the line spacing style of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] style:int | ENUM?
		return self.com_parent.TextLineSpacingStyle
	@textlinespacingstyle.setter
	def _(self, style:int):
		# ['in'] style:int
		self.com_parent.TextLineSpacingStyle = style

	@property
	def textrightattachmenttype(self) -> int:
		"Gets the dog leg direction of the specific leader"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.TextRightAttachmentType
	@textrightattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextRightAttachmentType = Type

	@property
	def textrotation(self) -> float:
		"Specifies the rotation angle of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.TextRotation
	@textrotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.TextRotation = rotAngle

	@property
	def textstring(self) -> str:
		"Specifies the text string of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def textstylename(self) -> str:
		"Specifies the style name of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.TextStyleName
	@textstylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.TextStyleName = bstrName

	@property
	def texttopattachmenttype(self) -> int:
		"Specifies how leaders on the top connect with the text"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.TextTopAttachmentType
	@texttopattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextTopAttachmentType = Type

	@property
	def textwidth(self) -> float:
		"Specifies the width of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.TextWidth
	@textwidth.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.TextWidth = Width


class AcadMLine(POINTER(_dll.IAcadMLine), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadMLine
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadMLine VBA-class wrapped as AcadMLine python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	# Properties
	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the coordinates for each vertex in the object"
		# TODO: Check arguments
		# ['out', 'retval'] Vertices:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Vertices:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Vertices:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = Vertices.flatten

	@property
	def justification(self) -> int:
		"Specifies the justification of the MLine"
		# TODO: Check arguments
		# ['out', 'retval'] Justification:int | ENUM?
		return self.com_parent.Justification
	@justification.setter
	def _(self, Justification:int):
		# ['in'] Justification:int
		self.com_parent.Justification = Justification

	@property
	def mlinescale(self) -> float:
		"Specifies the scale of the MLine"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.MLineScale
	@mlinescale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.MLineScale = scale

	@property
	def stylename(self) -> str:
		"Specifies the Mline style name"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.StyleName


class AcadMText(POINTER(_dll.IAcadMText), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadMText
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadMText VBA-class wrapped as AcadMText python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def fieldcode(self) -> str:
		"Returns the text string with field codes of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		# VBA: bstrText = object.FieldCode ()
		return self.com_parent.FieldCode()

	# Properties
	@property
	def attachmentpoint(self) -> int:
		"Specifies both text height and text orientation by designating the endpoints of the baseline"
		# TODO: Check arguments
		# ['out', 'retval'] attPoint:int
		return self.com_parent.AttachmentPoint
	@attachmentpoint.setter
	def _(self, attPoint:int):
		# ['in'] attPoint:int
		self.com_parent.AttachmentPoint = attPoint

	@property
	def backgroundfill(self) -> bool:
		"Specifies use Background mask"
		# TODO: Check arguments
		# ['out', 'retval'] bUseBackgroundFill:bool
		return self.com_parent.BackgroundFill
	@backgroundfill.setter
	def _(self, bUseBackgroundFill:bool):
		# ['in'] bUseBackgroundFill:bool
		self.com_parent.BackgroundFill = bUseBackgroundFill

	@property
	def drawingdirection(self) -> int:
		"Specifies the drawing direction of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] drawDir:int | ENUM?
		return self.com_parent.DrawingDirection
	@drawingdirection.setter
	def _(self, drawDir:int):
		# ['in'] drawDir:int
		self.com_parent.DrawingDirection = drawDir

	@property
	def height(self) -> float:
		"Specifies the text height of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the insertion point of the Mtext or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def linespacingdistance(self) -> float:
		"Specifies the line spacing distance of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Value:float
		return self.com_parent.LineSpacingDistance
	@linespacingdistance.setter
	def _(self, Value:float):
		# ['in'] Value:float
		self.com_parent.LineSpacingDistance = Value

	@property
	def linespacingfactor(self) -> float:
		"Specifies the line spacing factor of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.LineSpacingFactor
	@linespacingfactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.LineSpacingFactor = factor

	@property
	def linespacingstyle(self) -> int:
		"Specifies the line spacing style of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] style:int | ENUM?
		return self.com_parent.LineSpacingStyle
	@linespacingstyle.setter
	def _(self, style:int):
		# ['in'] style:int
		self.com_parent.LineSpacingStyle = style

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def stylename(self) -> str:
		"Specifies the style name of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def textstring(self) -> str:
		"Specifies the text string of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def width(self) -> float:
		"Specifies the defined width of the Mtext"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadNurbSurface(POINTER(_dll.IAcadNurbSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadNurbSurface
	#	IAcadSurface
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadNurbSurface VBA-class wrapped as AcadNurbSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
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
	edgeextensiondistances =	AcadSurface.edgeextensiondistances
	maintainassociativity =     AcadSurface.maintainassociativity
	showassociativity =         AcadSurface.showassociativity
	surfacetype =               AcadSurface.surfacetype
	surftrimassociativity =     AcadSurface.surftrimassociativity
	uisolinedensity =           AcadSurface.uisolinedensity
	visolinedensity =           AcadSurface.visolinedensity
	wireframetype =             AcadSurface.wireframetype
	# Properties
	@property
	def cvhulldisplay(self) -> bool:
		"Specifies whether displaying the CV Hull for NURBS surface"
		# TODO: Check arguments
		# ['out', 'retval'] Display:bool
		return self.com_parent.CvHullDisplay
	@cvhulldisplay.setter
	def _(self, Display:bool):
		# ['in'] Display:bool
		self.com_parent.CvHullDisplay = Display


class AcadOle(POINTER(_dll.IAcadOle), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadOle
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadOle VBA-class wrapped as AcadOle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def height(self) -> float:
		"Specifies the height of the OLE object box"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specifies the origin coordinates (upper left corner) of the OLE object"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def lockaspectratio(self) -> bool:
		"Ensures the width and height of the object stay in proportion"
		# TODO: Check arguments
		# ['out', 'retval'] aspect:bool
		return self.com_parent.LockAspectRatio
	@lockaspectratio.setter
	def _(self, aspect:bool):
		# ['in'] aspect:bool
		self.com_parent.LockAspectRatio = aspect

	@property
	def oleitemtype(self) -> int:
		"Specifies whether the OLE object is linked to the original pasted file when opening object for editing"
		# TODO: Check arguments
		# ['out', 'retval'] pType:int | ENUM?
		return self.com_parent.OleItemType
	@oleitemtype.setter
	def _(self, pType:int):
		# ['in'] pType:int
		self.com_parent.OleItemType = pType

	@property
	def oleplotquality(self) -> int:
		"Controls plot quality of OLE object based on file type selected from list"
		# TODO: Check arguments
		# ['out', 'retval'] pPQuality:int | ENUM?
		return self.com_parent.OlePlotQuality
	@oleplotquality.setter
	def _(self, pPQuality:int):
		# ['in'] pPQuality:int
		self.com_parent.OlePlotQuality = pPQuality

	@property
	def olesourceapp(self) -> str:
		"Application for editing OLE object"
		# TODO: Check arguments
		# ['out', 'retval'] srcApp:str
		return self.com_parent.OleSourceApp
	@olesourceapp.setter
	def _(self, srcApp:str):
		# ['in'] srcApp:str
		self.com_parent.OleSourceApp = srcApp

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the OLE object"
		# TODO: Check arguments
		# ['out', 'retval'] rot:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rot:float):
		# ['in'] rot:float
		self.com_parent.Rotation = rot

	@property
	def scaleheight(self) -> float:
		"Specifies the height of the object as a percentage of original height"
		# TODO: Check arguments
		# ['out', 'retval'] sheight:float
		return self.com_parent.ScaleHeight
	@scaleheight.setter
	def _(self, sheight:float):
		# ['in'] sheight:float
		self.com_parent.ScaleHeight = sheight

	@property
	def scalewidth(self) -> float:
		"Specifies the width of the object as a percentage of original width"
		# TODO: Check arguments
		# ['out', 'retval'] swidth:float
		return self.com_parent.ScaleWidth
	@scalewidth.setter
	def _(self, swidth:float):
		# ['in'] swidth:float
		self.com_parent.ScaleWidth = swidth

	@property
	def width(self) -> float:
		"Specifies the width of the OLE object box"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadPViewport(POINTER(_dll.IAcadPViewport), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPViewport
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPViewport VBA-class wrapped as AcadPViewport python-class
	# TODO list:
		# 1. COM-types to python-types vars and props +
		# 2. ByRef inputs/outputs
		# 3. Inherits +
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def display(self, bStatus: bool):
		"Determines whether viewport is On or Off"
		# ['in'] bStatus:bool
		# VBA: object.Display bStatus
		self.com_parent.Display(bStatus)

	def getgridspacing(self):
		"Specifies the grid spacing for the viewport"
		# TODO: Check arguments
		# ['out'] XSpacing:float
		# ['out'] YSpacing:float
		# VBA: object.GetGridSpacing XSpacing, YSpacing
		return self.com_parent.GetGridSpacing()

	def getsnapspacing(self):
		"Specifies the snap spacing for the viewport"
		# TODO: Check arguments
		# ['out'] XSpacing:float
		# ['out'] YSpacing:float
		# VBA: object.GetSnapSpacing XSpacing, YSpacing
		return self.com_parent.GetSnapSpacing()

	def setgridspacing(self, XSpacing: float, YSpacing: float):
		"Sets the grid spacing for the viewport"
		# ['in'] XSpacing:float
		# ['in'] YSpacing:float
		# VBA: object.SetGridSpacing XSpacing, YSpacing
		self.com_parent.SetGridSpacing(XSpacing, YSpacing)

	def setsnapspacing(self, XSpacing: float, YSpacing: float):
		"Sets the snap spacing for the viewport"
		# ['in'] XSpacing:float
		# ['in'] YSpacing:float
		# VBA: object.SetSnapSpacing XSpacing, YSpacing
		self.com_parent.SetSnapSpacing(XSpacing, YSpacing)

	def syncmodelview(self):
		"Updates the viewport parameters with the parameters in the associated model view."
		# VBA: object.SyncModelView 
		self.com_parent.SyncModelView()

	# Properties
	@property
	def arcsmoothness(self) -> int:
		"Specifies the smoothness of circles, arcs, and ellipses"
		# TODO: Check arguments
		# ['out', 'retval'] arcSmooth:int | ENUM?
		return self.com_parent.ArcSmoothness
	@arcsmoothness.setter
	def _(self, arcSmooth:int):
		# ['in'] arcSmooth:int
		self.com_parent.ArcSmoothness = arcSmooth

	@property
	def center(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the center of the viewport or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] CenterPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Center)
	@center.setter
	def _(self, CenterPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] CenterPoint:tagVARIANT | A3Vertex
		self.com_parent.Center = CenterPoint

	@property
	def clipped(self) -> bool:
		"Specifies that standard viewport border is replaced with user defined boundary"
		# TODO: Check arguments
		# ['out', 'retval'] bClipped:bool
		return self.com_parent.Clipped

	@property
	def customscale(self) -> float:
		"Specifies the custom scale for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.CustomScale
	@customscale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.CustomScale = scale

	@property
	def direction(self) -> A3Vertex:
		"Specifies the viewing direction for a 3D visualization of the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] dirVector:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Direction)
	@direction.setter
	def _(self, dirVector:A3Vertex):
		# TODO: Check arguments
		# ['in'] dirVector:tagVARIANT
		self.com_parent.Direction = dirVector

	@property
	def displaylocked(self) -> bool:
		"Determines whether viewport is in locked state or not"
		# TODO: Check arguments
		# ['out', 'retval'] bLocked:bool
		return self.com_parent.DisplayLocked
	@displaylocked.setter
	def _(self, bLocked:bool):
		# ['in'] bLocked:bool
		self.com_parent.DisplayLocked = bLocked

	@property
	def gridon(self) -> bool:
		"Specifies the status of the viewport grid"
		# TODO: Check arguments
		# ['out', 'retval'] bGridOn:bool
		return self.com_parent.GridOn
	@gridon.setter
	def _(self, bGridOn:bool):
		# ['in'] bGridOn:bool
		self.com_parent.GridOn = bGridOn

	@property
	def hassheetview(self) -> bool:
		"Specifies whether the viewport is linked to a corresponding sheet view"
		# TODO: Check arguments
		# ['out', 'retval'] bSheetView:bool
		return self.com_parent.HasSheetView

	@property
	def height(self) -> float:
		"Specifies the height of the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def labelblockid(self) -> int:
		"Returns and sets the label block id associated with the viewport."
		# TODO: Check arguments
		# ['out', 'retval'] ObjectID:int
		return self.com_parent.LabelBlockId
	@labelblockid.setter
	def _(self, ObjectID:int):
		# TODO: Check arguments
		# ['in'] ObjectID:int
		self.com_parent.LabelBlockId = ObjectID

	@property
	def layerpropertyoverrides(self) -> bool:
		"Specifies whether the viewport has layer property overrides."
		# TODO: Check arguments
		# ['out', 'retval'] bOverrides:bool
		return self.com_parent.LayerPropertyOverrides

	@property
	def lenslength(self) -> float:
		"Specifies the lens length used in perspective viewing"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.LensLength
	@lenslength.setter
	def _(self, Length:float):
		# ['in'] Length:float
		self.com_parent.LensLength = Length

	@property
	def modelview(self) -> AcadView:
		"Returns and sets the model view associated with the viewport."
		# TODO: Check arguments
		# ['out', 'retval'] View:AcadView
		return AcadView(self.com_parent.ModelView)
	@modelview.setter
	def _(self, View:AcadView):
		# TODO: Check arguments
		# ['in'] View:AcadView
		self.com_parent.ModelView = View

	@property
	def removehiddenlines(self) -> bool:
		"Determines whether hidden line removal is On or Off"
		# TODO: Check arguments
		# ['out', 'retval'] bRemoval:bool
		return self.com_parent.RemoveHiddenLines
	@removehiddenlines.setter
	def _(self, bRemoval:bool):
		# ['in'] bRemoval:bool
		self.com_parent.RemoveHiddenLines = bRemoval

	@property
	def shadeplot(self) -> int:
		"Specifies the shade plot mode of the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] pShadePlotIndex:int | ENUM?
		return self.com_parent.ShadePlot
	@shadeplot.setter
	def _(self, pShadePlotIndex:int):
		# ['in'] pShadePlotIndex:int
		self.com_parent.ShadePlot = pShadePlotIndex

	@property
	def sheetview(self) -> AcadView:
		"Returns and sets the sheet view associated with the viewport."
		# TODO: Check arguments
		# ['out', 'retval'] View:AcadView
		return CastManager.cast(self.com_parent.SheetView)
	@sheetview.setter
	def _(self, View:AcadView):
		# TODO: Check arguments
		# ['in'] View:AcadView
		self.com_parent.SheetView = View

	@property
	def snapbasepoint(self) -> A3Vertex:
		"Specifies the snap base point for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] lowLeft:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.SnapBasePoint)
	@snapbasepoint.setter
	def _(self, lowLeft:A3Vertex):
		# TODO: Check arguments
		# ['in'] lowLeft:tagVARIANT | A3Vertex
		self.com_parent.SnapBasePoint = lowLeft

	@property
	def snapon(self) -> bool:
		"Specifies the status of snap"
		# TODO: Check arguments
		# ['out', 'retval'] bSnapOn:bool
		return self.com_parent.SnapOn
	@snapon.setter
	def _(self, bSnapOn:bool):
		# ['in'] bSnapOn:bool
		self.com_parent.SnapOn = bSnapOn

	@property
	def snaprotationangle(self) -> float:
		"Specifies the snap rotation angle of the viewport relative to the current UCS"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.SnapRotationAngle
	@snaprotationangle.setter
	def _(self, Angle:float):
		# ['in'] Angle:float
		self.com_parent.SnapRotationAngle = Angle

	@property
	def standardscale(self) -> int:
		"Specifies the standard scale for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] scale:int | ENUM?
		return self.com_parent.StandardScale
	@standardscale.setter
	def _(self, scale:int):
		# ['in'] scale:int
		self.com_parent.StandardScale = scale

	@property
	def standardscale2(self) -> int:
		"Specifies the standard scale for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] scale:int
		return self.com_parent.StandardScale2
	@standardscale2.setter
	def _(self, scale:int):
		# ['in'] scale:int
		self.com_parent.StandardScale2 = scale

	@property
	def stylesheet(self) -> str:
		"Returns the style sheet to use"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.StyleSheet
	@stylesheet.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.StyleSheet = pName

	@property
	def target(self) -> A3Vertex:
		"Specifies the target point for the view or viewport"
		# TODO: Check arguments
		# ['out', 'retval'] targetPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Target)
	@target.setter
	def _(self, targetPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] targetPoint:tagVARIANT | A3Vertex
		self.com_parent.Target = targetPoint

	@property
	def twistangle(self) -> float:
		"Specifies the twist angle for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.TwistAngle
	@twistangle.setter
	def _(self, Angle:float):
		# ['in'] Angle:float
		self.com_parent.TwistAngle = Angle

	@property
	def ucsiconatorigin(self) -> bool:
		"Specifies if the UCS icon is displayed at the origin"
		# TODO: Check arguments
		# ['out', 'retval'] bIconAtOrigin:bool
		return self.com_parent.UCSIconAtOrigin
	@ucsiconatorigin.setter
	def _(self, bIconAtOrigin:bool):
		# ['in'] bIconAtOrigin:bool
		self.com_parent.UCSIconAtOrigin = bIconAtOrigin

	@property
	def ucsiconon(self) -> bool:
		"Specifies if the UCS icon is on"
		# TODO: Check arguments
		# ['out', 'retval'] bIconOn:bool
		return self.com_parent.UCSIconOn
	@ucsiconon.setter
	def _(self, bIconOn:bool):
		# ['in'] bIconOn:bool
		self.com_parent.UCSIconOn = bIconOn

	@property
	def ucsperviewport(self) -> bool:
		"Determines whether the UCS is saved with the viewport or not"
		# TODO: Check arguments
		# ['out', 'retval'] UCSSaved:bool
		return self.com_parent.UCSPerViewport
	@ucsperviewport.setter
	def _(self, UCSSaved:bool):
		# ['in'] UCSSaved:bool
		self.com_parent.UCSPerViewport = UCSSaved

	@property
	def viewporton(self) -> bool:
		"Determines whether the viewport is On or Off"
		# TODO: Check arguments
		# ['out', 'retval'] bOn:bool
		return self.com_parent.ViewportOn
	@viewporton.setter
	def _(self, bOn:bool):
		# ['in'] bOn:bool
		self.com_parent.ViewportOn = bOn

	@property
	def visualstyle(self) -> int:
		"Specifies the visual style of the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] pVisualStyleIndex:int
		return self.com_parent.VisualStyle
	@visualstyle.setter
	def _(self, pVisualStyleIndex:int):
		# ['in'] pVisualStyleIndex:int
		self.com_parent.VisualStyle = pVisualStyleIndex

	@property
	def width(self) -> float:
		"Specifies the width of the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadPoint(POINTER(_dll.IAcadPoint), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPoint
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPoint VBA-class wrapped as AcadPoint python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def coordinates(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the position of the point or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A3Vertex):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT | A3Vertex
		self.com_parent.Coordinates = Coordinates

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the point"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadPointCloud(POINTER(_dll.IAcadPointCloud), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPointCloud
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPointCloud VBA-class wrapped as AcadPointCloud python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def height(self) -> float:
		"Specifies the height of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.Height
	@height.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.Height = val

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specifies the insertion point of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] EndPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, EndPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] EndPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = EndPoint

	@property
	def intensitycolorscheme(self) -> int:
		"Specifies the color scheme to use for displaying intensity values."
		# TODO: Check arguments
		# ['out', 'retval'] val:int |ENUM?
		return self.com_parent.IntensityColorScheme
	@intensitycolorscheme.setter
	def _(self, val:int):
		self.com_parent.IntensityColorScheme = val

	@property
	def length(self) -> float:
		"Specifies the length of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.Length
	@length.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.Length = val

	@property
	def locked(self) -> bool:
		"Specifies if the point cloud is locked."
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.Locked
	@locked.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.Locked = val

	@property
	def name(self) -> str:
		"Specifies the name of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Name

	@property
	def path(self) -> str:
		"Specifies the path to the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Path

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.Rotation = val

	@property
	def scale(self) -> float:
		"Specifies the scale value of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.scale
	@scale.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.scale = val

	@property
	def showclipped(self) -> bool:
		"Enables or disables the clipping boundary of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.ShowClipped
	@showclipped.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.ShowClipped = val

	@property
	def showintensity(self) -> bool:
		"""Specifies whether to display point cloud intensity using a shaded color scheme. 
	You can only see the intensity color mapping effect in 3D visual style and when hardware acceleration is on."""
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.ShowIntensity
	@showintensity.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.ShowIntensity = val

	@property
	def stylization(self) -> int:
		"Specifies color stylization for selected point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:int | ENUM?
		return self.com_parent.Stylization
	@stylization.setter
	def _(self, val:int):
		# ['in'] val:int
		self.com_parent.Stylization = val

	@property
	def unit(self) -> str:
		"Specifies the unit of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Unit

	@property
	def unitfactor(self) -> float:
		"Specifies insert unit factor of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.UnitFactor

	@property
	def useentitycolor(self) -> int:
		"Specifies the point cloud color source."
		# TODO: Check arguments
		# ['out', 'retval'] val:int | ENUM?
		return self.com_parent.UseEntityColor
	@useentitycolor.setter
	def _(self, val:int):
		# ['in'] val:int
		self.com_parent.UseEntityColor = val

	@property
	def width(self) -> float:
		"Specifies the width of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.Width
	@width.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.Width = val


class AcadPointCloudEx(POINTER(_dll.IAcadPointCloudEx), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPointCloudEx
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPointCloudEx VBA-class wrapped as AcadPointCloudEx python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	#	_IAcadPointCloudEx__com__get_ColorScheme
	#	_IAcadPointCloudEx__com__get_Geolocate
	#	_IAcadPointCloudEx__com__get_InsertionPoint
	#	_IAcadPointCloudEx__com__get_Locked
	#	_IAcadPointCloudEx__com__get_Name
	#	_IAcadPointCloudEx__com__get_Path
	#	_IAcadPointCloudEx__com__get_Rotation
	#	_IAcadPointCloudEx__com__get_ShowCropped
	#	_IAcadPointCloudEx__com__get_Stylization
	#	_IAcadPointCloudEx__com__get_Unit
	#	_IAcadPointCloudEx__com__get_UnitFactor
	#	_IAcadPointCloudEx__com__get_scale
	
	#	_IAcadPointCloudEx__com__set_ColorScheme
	#	_IAcadPointCloudEx__com__set_Geolocate
	#	_IAcadPointCloudEx__com__set_InsertionPoint
	#	_IAcadPointCloudEx__com__set_Locked
	#	_IAcadPointCloudEx__com__set_Name
	#	_IAcadPointCloudEx__com__set_Rotation
	#	_IAcadPointCloudEx__com__set_ShowCropped
	#	_IAcadPointCloudEx__com__set_Stylization
	#	_IAcadPointCloudEx__com__set_scale
	# Properties
	@property
	def colorscheme(self) -> str:
		"Specifies the color scheme to display point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.ColorScheme
	@colorscheme.setter
	def _(self, val:int):
		# ['in'] val:int
		self.com_parent.ColorScheme = val

	@property
	def geolocate(self) -> bool:
		"Specifies if the point cloud is geolocated."
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.Geolocate
	@geolocate.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.Geolocate = val

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specifies the insertion point of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] EndPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, EndPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] EndPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = EndPoint

	@property
	def locked(self) -> bool:
		"Specifies if the point cloud is locked."
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.Locked
	@locked.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.Locked = val

	@property
	def name(self) -> str:
		"Specifies the name of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Name
	@name.setter
	def _(self, val:str):
		# ['in'] val:str
		self.com_parent.Name = val

	@property
	def path(self) -> str:
		"Specifies the path to the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Path

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.Rotation = val

	@property
	def scale(self) -> float:
		"Specifies the scale value of the point cloud."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.scale
	@scale.setter
	def _(self, val:float):
		# ['in'] val:float
		self.com_parent.scale = val

	@property
	def showcropped(self) -> bool:
		"Specifies if the cropping is shown."
		# TODO: Check arguments
		# ['out', 'retval'] val:bool
		return self.com_parent.ShowCropped
	@showcropped.setter
	def _(self, val:bool):
		# ['in'] val:bool
		self.com_parent.ShowCropped = val

	@property
	def stylization(self) -> int:
		"Specifies the point cloud color source."
		# TODO: Check arguments
		# ['out', 'retval'] val:int | ENUM?
		return self.com_parent.Stylization
	@stylization.setter
	def _(self, val:int):
		# ['in'] val:int
		self.com_parent.Stylization = val

	@property
	def unit(self) -> str:
		"Specifies the unit of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Unit

	@property
	def unitfactor(self) -> float:
		"Specifies insert unit factor of the point cloud file."
		# TODO: Check arguments
		# ['out', 'retval'] val:float
		return self.com_parent.UnitFactor


class AcadPointCloudEx2(POINTER(_dll.IAcadPointCloudEx2), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPointCloudEx2
	#	IAcadPointCloudEx
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadPointCloudEx2 VBA-class wrapped as AcadPointCloudEx2 python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	colorscheme =		AcadPointCloudEx.colorscheme
	geolocate =			AcadPointCloudEx.geolocate
	insertionpoint =	AcadPointCloudEx.insertionpoint
	locked =			AcadPointCloudEx.locked
	name =				AcadPointCloudEx.name
	path =				AcadPointCloudEx.path
	rotation =			AcadPointCloudEx.rotation
	scale =				AcadPointCloudEx.scale
	showcropped =		AcadPointCloudEx.showcropped
	stylization =		AcadPointCloudEx.stylization
	unit =				AcadPointCloudEx.unit
	unitfactor =		AcadPointCloudEx.unitfactor
	# Properties
	@property
	def segmentation(self) -> str:
		"Specifies if the point cloud has segmentation."
		# TODO: Check arguments
		# ['out', 'retval'] val:str
		return self.com_parent.Segmentation


class AcadPolyfaceMesh(POINTER(_dll.IAcadPolyfaceMesh), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPolyfaceMesh
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPolyfaceMesh VBA-class wrapped as AcadPolyfaceMesh python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the vertices of the mesh"
		# TODO: Check arguments
		# ['out', 'retval'] Vertices:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Vertices:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Vertices:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = Vertices.flatten

	# ??????????????????????
	@property
	def faces(self):
		Exception("Can't GET Faces value")
	@faces.setter
	def _(self, rhs): 
		# TODO: Check arguments
		# ['in'] rhs:tagVARIANT
		self.com_parent.Faces = rhs

	@property
	def numberoffaces(self) -> int:
		"Specifies the number of faces in the mesh"
		# TODO: Check arguments
		# ['out', 'retval'] NumFaces:int
		return self.com_parent.NumberOfFaces

	@property
	def numberofvertices(self) -> int:
		"Specifies the number of vertices in the mesh"
		# TODO: Check arguments
		# ['out', 'retval'] NumVertices:int
		return self.com_parent.NumberOfVertices


class AcadPolygonMesh(POINTER(_dll.IAcadPolygonMesh), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPolygonMesh
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPolygonMesh VBA-class wrapped as AcadPolygonMesh python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def appendvertex(self, vertex: A3Vertex):
		"Appends a vertex to the polygonmesh"
		# TODO: Check arguments
		# ['in'] vertex:tagVARIANT | A3Vertex
		# VBA: object.AppendVertex vertex
		self.com_parent.AppendVertex(vertex)

	def explode(self) -> list:
		"Explodes the polygonmesh and returns the sub-entities as an array of object"
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret

	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the coordinates of the polygonmesh"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = Coordinates.flatten

	@property
	def mclose(self) -> bool:
		"Specifies mesh style for M direction, Open or Closed"
		# TODO: Check arguments
		# ['out', 'retval'] bClose:bool
		return self.com_parent.MClose
	@mclose.setter
	def _(self, bClose:bool):
		# ['in'] bClose:bool
		self.com_parent.MClose = bClose

	@property
	def mdensity(self) -> int:
		"Specifies M density value of the polygonmesh; valid values 3-201"
		# TODO: Check arguments
		# ['out', 'retval'] density:int
		return self.com_parent.MDensity
	@mdensity.setter
	def _(self, density:int):
		# ['in'] density:int
		self.com_parent.MDensity = density

	@property
	def mvertexcount(self) -> int:
		"Returns the M Vertex number of the polygonmesh"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.MVertexCount

	@property
	def nclose(self) -> bool:
		"Specifies mesh style for N direction, Open or Closed"
		# TODO: Check arguments
		# ['out', 'retval'] bClose:bool
		return self.com_parent.NClose
	@nclose.setter
	def _(self, bClose:bool):
		# ['in'] bClose:bool
		self.com_parent.NClose = bClose

	@property
	def ndensity(self) -> int:
		"Specifies N density value of the polygonmesh; valid values 3-201"
		# TODO: Check arguments
		# ['out', 'retval'] density:int
		return self.com_parent.NDensity
	@ndensity.setter
	def _(self, density:int):
		# ['in'] density:int
		self.com_parent.NDensity = density

	@property
	def nvertexcount(self) -> int:
		"Specifies the N Vertex number of the polygonmesh"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.NVertexCount

	@property
	def type(self) -> int:
		"Specifies the type of the polygonmesh"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Type
	@type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Type = Type


class AcadPolyline(POINTER(_dll.IAcadPolyline), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadPolyline
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPolyline VBA-class wrapped as AcadPolyline python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def appendvertex(self, vertex: A3Vertex):
		"Appends a vertex to the polyline"
		# TODO: Check arguments
		# ['in'] vertex:tagVARIANT | A3Vertex
		# VBA: object.AppendVertex vertex
		self.com_parent.AppendVertex(vertex)

	def explode(self) -> list:
		"Explodes the polyline and returns the sub-entities as an array of Object"
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT | list
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret

	def getbulge(self, Index: int) -> float:
		"Returns the vertex bulge of the polyline"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] bulge:float
		# VBA: bulge = object.GetBulge (Index)
		return self.com_parent.GetBulge(Index)

	def getwidth(self, Index: int) -> float:
		"Returns segment width of the polyline"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out'] StartWidth:float
		# [] EndWidth:float
		# VBA: object.GetWidth Index, StartWidth, EndWidth
		return self.com_parent.GetWidth(Index)

	def offset(self, Distance: float) -> list:
		"Creates a new entity object by offsetting the polyline by a specified distance"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return ret

	def setbulge(self, Index: int, bulge: float):
		"Sets the vertex bulge of the polyline"
		# ['in'] Index:int
		# ['in'] bulge:float
		# VBA: object.SetBulge Index, bulge
		self.com_parent.SetBulge(Index, bulge)

	def setwidth(self, Index: int, StartWidth: float):
		"Sets the segment width of the polyline"
		# ['in'] Index:int
		# ['in'] StartWidth:float
		# [] EndWidth:float
		# VBA: object.SetWidth Index, StartWidth, EndWidth
		self.com_parent.SetWidth(Index, StartWidth)

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def closed(self) -> bool:
		"Determines whether polyline is Open or Closed. Closed draws a line segment from current position to starting point of the polyline."
		# TODO: Check arguments
		# ['out', 'retval'] fClose:bool
		return self.com_parent.Closed
	@closed.setter
	def _(self, fClose:bool):
		# ['in'] fClose:bool
		self.com_parent.Closed = fClose

	@property
	def constantwidth(self) -> float:
		"Specifies the constant width for the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.ConstantWidth
	@constantwidth.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.ConstantWidth = Width

	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the current vertex of the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Coordinates:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, Coordinates:A3Vertexes):
		# TODO: Check arguments
		# ['in'] Coordinates:tagVARIANT
		self.com_parent.Coordinates = Coordinates.flatten

	@property
	def elevation(self) -> float:
		"Specifies the elevation of the polyline relative to the Z axis of the objects' coordinate system"
		# TODO: Check arguments
		# ['out', 'retval'] Elevation:float
		return self.com_parent.Elevation
	@elevation.setter
	def _(self, Elevation:float):
		# ['in'] Elevation:float
		self.com_parent.Elevation = Elevation

	@property
	def length(self) -> float:
		"Specifies the length of the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Length

	@property
	def linetypegeneration(self) -> bool:
		"Generates linetype in a continuous pattern through the vertices of the polyline. When turned off, linetype is generated starting and ending with a dash at each vertex."
		# TODO: Check arguments
		# ['out', 'retval'] bLinetypeGen:bool
		return self.com_parent.LinetypeGeneration
	@linetypegeneration.setter
	def _(self, bLinetypeGen:bool):
		# ['in'] bLinetypeGen:bool
		self.com_parent.LinetypeGeneration = bLinetypeGen

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

	@property
	def type(self) -> int:
		"Applies a fit curve or spline type to a 2D polyline"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.Type
	@type.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.Type = Type


class AcadRay(POINTER(_dll.IAcadRay), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadRay
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadRay VBA-class wrapped as AcadRay python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@indexedproperty
	def basepoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the basepoint of the ray or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] BasePoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.BasePoint)
	@basepoint.setter
	def _(self, BasePoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] BasePoint:tagVARIANT | A3Vertex
		self.com_parent.BasePoint = BasePoint

	@indexedproperty
	def directionvector(self) -> A3Vertex:
		"Specify the X, Y, Z direction vectors of the ray"
		# TODO: Check arguments
		# ['out', 'retval'] dirVector:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.DirectionVector)
	@directionvector.setter
	def _(self, dirVector:A3Vertex):
		# TODO: Check arguments
		# ['in'] dirVector:tagVARIANT | A3Vertex
		self.com_parent.DirectionVector = dirVector

	@indexedproperty
	def secondpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the second point of the ray or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] SecondPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.SecondPoint)
	@secondpoint.setter
	def _(self, SecondPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] SecondPoint:tagVARIANT | A3Vertex
		self.com_parent.SecondPoint = SecondPoint


class AcadRegion(POINTER(_dll.IAcadRegion), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadRegion
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadRegion VBA-class wrapped as AcadRegion python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def boolean(self, Operation: int, Object: AcadRegion):
		"Perform a Boolean operation against another region."
		# TODO: Check arguments
		# ['in'] Operation:int | ENUM?
		# ['in'] Object:AcadRegion
		# VBA: object.Boolean Operation, Object
		self.com_parent.Boolean(Operation, Object)

	def explode(self) -> list:
		"Explodes the region and returns the sub-entities as an array of object."
		# TODO: Check arguments
		# ['out', 'retval'] pArrayObjs:tagVARIANT
		# VBA: pArrayObjs = object.Explode ()
		ret = []
		for e in self.com_parent.Explode():
			ret.append(CastManager.cast(e))
		return ret

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the region"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def centroid(self) -> A3Vertex:
		"Gets the center of area or mass for a region or solid"
		# TODO: Check arguments
		# ['out', 'retval'] Centroid:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Centroid)

	@property
	def momentofinertia(self) -> A3Vertex:
		"Gets the moment of inertia for the solid"
		# TODO: Check arguments
		# ['out', 'retval'] momentInertia:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.MomentOfInertia)

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)

	@property
	def perimeter(self) -> float:
		"Specifies the perimeter of the region"
		# TODO: Check arguments
		# ['out', 'retval'] Perimeter:float
		return self.com_parent.Perimeter

	@property
	def principaldirections(self) -> A3Vertex:
		"Gets the principal directions of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prinDir:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.PrincipalDirections)

	@property
	def principalmoments(self) -> A3Vertex:
		"Gets the principal moments property of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prinMoments:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.PrincipalMoments)

	@property
	def productofinertia(self) -> float:
		"Gets the product of inertia of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] prodInertia:float
		return self.com_parent.ProductOfInertia

	@property
	def radiiofgyration(self) -> A3Vertex:
		"Gets the radius of gyration of the solid or region"
		# TODO: Check arguments
		# ['out', 'retval'] radiiGyration:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.RadiiOfGyration)


class AcadRevolvedSurface(POINTER(_dll.IAcadRevolvedSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadRevolvedSurface
	#	IAcadSurface
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadRevolvedSurface VBA-class wrapped as AcadRevolvedSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	edgeextensiondistances =	AcadSurface.edgeextensiondistances
	maintainassociativity =     AcadSurface.maintainassociativity
	showassociativity =         AcadSurface.showassociativity
	surfacetype =               AcadSurface.surfacetype
	surftrimassociativity =     AcadSurface.surftrimassociativity
	uisolinedensity =           AcadSurface.uisolinedensity
	visolinedensity =           AcadSurface.visolinedensity
	wireframetype =             AcadSurface.wireframetype
	# Properties
	@indexedproperty
	def axisdirection(self) -> A3Vertex:
		"Displays the direction of the axis of revolution"
		# TODO: Check arguments
		# ['out', 'retval'] AxisDirection:tagVARIANT | A3Vertex ???
		return A3Vertex(self.com_parent.AxisDirection)

	@indexedproperty
	def axisposition(self) -> A3Vertex:
		"Specifies the start point of the axis of revolution"
		# TODO: Check arguments
		# ['out', 'retval'] AxisPosition:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.AxisPosition)
	@axisposition.setter
	def _(self, AxisPosition:A3Vertex):
		# TODO: Check arguments
		# ['in'] AxisPosition:tagVARIANT | A3Vertex
		self.com_parent.AxisPosition = AxisPosition

	@indexedproperty
	def revolutionangle(self) -> float:
		"Specifies the angle of revolution"
		# TODO: Check arguments
		# ['out', 'retval'] revAngle:float
		return self.com_parent.RevolutionAngle
	@revolutionangle.setter
	def _(self, revAngle:float):
		# ['in'] revAngle:float
		self.com_parent.RevolutionAngle = revAngle


class AcadSection(POINTER(_dll.IAcadSection), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSection
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadSection VBA-class wrapped as AcadSection python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def addvertex(self, nIndex: int, val: A3Vertex):
		"Adds a new vertex to the section line"
		# TODO: Check arguments
		# ['in'] nIndex:int
		# ['in'] val:tagVARIANT | A3Vertex
		# VBA: object.AddVertex nIndex, val
		self.com_parent.AddVertex(nIndex, val)

	def createjog(self, varPt: A3Vertex):
		"Creates a jog on the section plane"
		# TODO: Check arguments
		# ['in'] varPt:tagVARIANT | A3Vertex
		# VBA: object.CreateJog varPt
		self.com_parent.CreateJog(varPt)

	def generatesectiongeometry(self, pEntity: AcadEntity):
		"Generates 2D or 3D section geometry"
		# TODO: Check arguments
		# ['in'] pEntity:AcadEntity
		# ['out'] pIntersectionBoundaryObjs:tagVARIANT
		# ['out'] pIntersectionFillObjs:tagVARIANT
		# ['out'] pBackgroudnObjs:tagVARIANT
		# ['out'] pForegroudObjs:tagVARIANT
		# ['out'] pCurveTangencyObjs:tagVARIANT
		# VBA: object.GenerateSectionGeometry pEntity, pIntersectionBoundaryObjs, pIntersectionFillObjs, pBackgroudnObjs, pForegroudObjs, pCurveTangencyObjs
		# TODO: fix this
		ret = self.com_parent.GenerateSectionGeometry(pEntity)
		return ret

	def hittest(self, varPtHit: A3Vertex):
		"Does hit test on section plane"
		# TODO: Check arguments
		# ['in'] varPtHit:tagVARIANT | A3Vertex
		# ['out'] pHit:bool
		# ['out'] pSegmentIndex:int
		# ['out'] pPtOnSegment:tagVARIANT | A3Vertex
		# ['out'] pSubItem:int | ENUM?
		# VBA: object.HitTest varPtHit, pHit, pSegmentIndex, pPtOnSegment, pSubItem
		ret = self.com_parent.HitTest(varPtHit)
		ret[2] = A3Vertex(ret[2])
		return ret

	def removevertex(self, nIndex: int):
		"Removes a vertex in the section line"
		# ['in'] nIndex:int
		# VBA: object.RemoveVertex nIndex
		self.com_parent.RemoveVertex(nIndex)

	# Properties
	@property
	def bottomheight(self) -> float:
		"Specifies elevation of section plane bottom extents relative to the object's elevation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.BottomHeight
	@bottomheight.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.BottomHeight = pVal

	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the co-ordinate of the specified vertex"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def elevation(self) -> float:
		"Specifies elevation of section plane line"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.Elevation
	@elevation.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.Elevation = pVal

	@property
	def indicatorfillcolor(self) -> AcadAcCmColor:
		"Specifies color of section plane when shading is turned on"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return AcadAcCmColor(self.com_parent.IndicatorFillColor)
	@indicatorfillcolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.IndicatorFillColor = pColor

	@property
	def indicatortransparency(self) -> int:
		"Specifies transparency of section plane when shading is turned on"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.IndicatorTransparency
	@indicatortransparency.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.IndicatorTransparency = pVal

	@property
	def livesectionenabled(self) -> bool:
		"Turns live section on or off for this section object"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.LiveSectionEnabled
	@livesectionenabled.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.LiveSectionEnabled = pVal

	@property
	def name(self) -> str:
		"Specifies section object name"
		# TODO: Check arguments
		# ['out', 'retval'] pbstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, pbstrName:str):
		# ['in'] pbstrName:str
		self.com_parent.Name = pbstrName

	@property
	def normal(self) -> A3Vertex:
		"Specifies normal for the section plane"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)

	@property
	def numvertices(self) -> int:
		"Gets the number of vertices in the section line"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.NumVertices

	@property
	def settings(self) -> AcadSectionSettings:
		"Gets the section settings object"
		# TODO: Check arguments
		# ['out', 'retval'] pUnk:AcadSectionSettings
		return AcadSectionSettings(self.com_parent.Settings)

	@property
	def state(self) -> int:
		"Specifies section object type"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int | ENUM?
		return self.com_parent.State
	@state.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.State = pVal

	@property
	def topheight(self) -> float:
		"Specifies elevation of section plane top extents relative to the object's elevation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.TopHeight
	@topheight.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.TopHeight = pVal

	@property
	def verticaldirection(self) -> A3Vertex:
		"Specifies the vertical direction for the section plane"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.VerticalDirection)
	@verticaldirection.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.VerticalDirection = pVal

	@property
	def vertices(self) -> A3Vertexes:
		"Gets the vertices in the section line"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Vertices)
	@vertices.setter
	def _(self, pVal:A3Vertexes):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertexes
		self.com_parent.Vertices = pVal

	@property
	def viewingdirection(self) -> A3Vertex:
		"Specifies the viewing direction for the section plane"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.ViewingDirection)
	@viewingdirection.setter
	def _(self, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.ViewingDirection = pVal


class AcadSection2(POINTER(_dll.IAcadSection2), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSection2
	#	IAcadSection
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadSection2 VBA-class wrapped as AcadSection2 python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	addvertex				= AcadSection.addvertex
	createjog				= AcadSection.createjog
	generatesectiongeometry	= AcadSection.generatesectiongeometry
	hittest					= AcadSection.hittest
	removevertex			= AcadSection.removevertex
	bottomheight			= AcadSection.bottomheight
	coordinate				= AcadSection.coordinate
	elevation				= AcadSection.elevation
	indicatorfillcolor		= AcadSection.indicatorfillcolor
	indicatortransparency	= AcadSection.indicatortransparency
	livesectionenabled		= AcadSection.livesectionenabled
	name					= AcadSection.name
	normal					= AcadSection.normal
	numvertices				= AcadSection.numvertices
	settings				= AcadSection.settings
	state					= AcadSection.state
	topheight				= AcadSection.topheight
	verticaldirection		= AcadSection.verticaldirection
	vertices				= AcadSection.vertices
	viewingdirection		= AcadSection.viewingdirection
	# Properties
	@property
	def sectionplaneoffset(self) -> float:
		"Specifies off set of section plane"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.SectionPlaneOffset
	@sectionplaneoffset.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.SectionPlaneOffset = pVal

	@property
	def slicedepth(self) -> float:
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.SliceDepth
	@slicedepth.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.SliceDepth = pVal

	@property
	def state2(self) -> int:
		"Specifies section object type"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int | ENUM?
		return self.com_parent.State2
	@state2.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.State2 = pVal


class AcadShape(POINTER(_dll.IAcadShape), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadShape
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadShape VBA-class wrapped as AcadShape python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def height(self) -> float:
		"Specifies the height of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify X, Y, Z coordinate for the insertion point of the shape or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def name(self) -> str:
		"Specifies the name of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def obliqueangle(self) -> float:
		"Specifies the oblique angle of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] obliAngle:float
		return self.com_parent.ObliqueAngle
	@obliqueangle.setter
	def _(self, obliAngle:float):
		# ['in'] obliAngle:float
		self.com_parent.ObliqueAngle = obliAngle

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the width scale factor of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] scalFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scalFactor:float):
		# ['in'] scalFactor:float
		self.com_parent.ScaleFactor = scalFactor

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the shape"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadSolid(POINTER(_dll.IAcadSolid), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSolid
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadSolid VBA-class wrapped as AcadSolid python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the current vertex of the solid"
		# TODO: Check arguments
		# ['out', 'retval'] corners:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, corners:A3Vertexes):
		# TODO: Check arguments
		# ['in'] corners:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = corners.flatten

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the solid"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadSpline(POINTER(_dll.IAcadSpline), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSpline
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadSpline VBA-class wrapped as AcadSpline python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def addfitpoint(self, Index: int, fitPoint: A3Vertex):
		"Adds the fit point to the spline at a given index"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] fitPoint:tagVARIANT | A3Vertex
		# VBA: object.AddFitPoint Index, fitPoint
		self.com_parent.AddFitPoint(Index, fitPoint)

	def deletefitpoint(self, Index: int):
		"Deletes the fit point of the spline at a given index"
		# ['in'] Index:int
		# VBA: object.DeleteFitPoint Index
		self.com_parent.DeleteFitPoint(Index)

	def elevateorder(self, Order: int):
		"Elevates the order of the spline"
		# ['in'] Order:int
		# VBA: object.ElevateOrder Order
		self.com_parent.ElevateOrder(Order)

	def getcontrolpoint(self, Index: int) -> A3Vertex:
		"Returns the control point of the spline at a given index"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] controlPoint:tagVARIANT | A3Vertex
		# VBA: controlPoint = object.GetControlPoint (Index)
		return A3Vertex(self.com_parent.GetControlPoint(Index))

	def getfitpoint(self, Index: int) -> A3Vertex:
		"Returns the fit point of the spline at a given index"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] fitPoint:tagVARIANT | A3Vertex
		# VBA: fitPoint = object.GetFitPoint (Index)
		return A3Vertex(self.com_parent.GetFitPoint(Index))

	def getweight(self, Index: int) -> float:
		"Returns the weight of the spline at a given control point index"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] weight:float
		# VBA: weight = object.GetWeight (Index)
		return self.com_parent.GetWeight(Index)

	def offset(self, Distance: float) -> list:
		"Creates a new entity object by offsetting the spline by a given value"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT | list
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return e

	def purgefitdata(self):
		"Purges the fit data of the spline"
		# VBA: object.PurgeFitData 
		self.com_parent.PurgeFitData()

	def reverse(self):
		"Reverses the direction of the spline"
		# VBA: object.Reverse 
		self.com_parent.Reverse()

	def setcontrolpoint(self, Index: int, controlPoint: A3Vertex):
		"Sets the indexed control point of the spline at a specified point"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] controlPoint:tagVARIANT | A3Vertex
		# VBA: object.SetControlPoint Index, controlPoint
		self.com_parent.SetControlPoint(Index, controlPoint)

	def setfitpoint(self, Index: int, fitPoint: A3Vertex):
		"Sets the indexed fit point of the spline at a specified point"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] fitPoint:tagVARIANT | A3Vertex
		# VBA: object.SetFitPoint Index, fitPoint
		self.com_parent.SetFitPoint(Index, fitPoint)

	def setweight(self, Index: int, weight: float):
		"Sets the weight of the spline at a given control point index"
		# ['in'] Index:int
		# ['in'] weight:float
		# VBA: object.SetWeight Index, weight
		self.com_parent.SetWeight(Index, weight)

	# Properties
	@property
	def area(self) -> float:
		"Specifies the area of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] Area:float
		return self.com_parent.Area

	@property
	def closed(self) -> bool:
		"Specifies whether the spline is open or closed"
		# TODO: Check arguments
		# ['out', 'retval'] fClose:bool
		return self.com_parent.Closed

	@property
	def closed2(self) -> bool:
		"Specifies whether the spline is open or closed"
		# TODO: Check arguments
		# ['out', 'retval'] fClose:bool
		return self.com_parent.Closed2
	@closed2.setter
	def _(self, fClose:bool):
		# ['in'] fClose:bool
		self.com_parent.Closed2 = fClose

	@property
	def controlpoints(self) -> A3Vertexes:
		"Specifies the current control point of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] controlPoint:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.ControlPoints)
	@controlpoints.setter
	def _(self, controlPoint:A3Vertexes):
		# TODO: Check arguments
		# ['in'] controlPoint:tagVARIANT | A3Vertexes
		self.com_parent.ControlPoints = controlPoint.flatten

	@property
	def degree(self) -> int:
		"Specifies the degree of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] Degree:int
		return self.com_parent.Degree

	@property
	def degree2(self) -> int:
		"Specifies the degree of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] Degree:int
		return self.com_parent.Degree2
	@degree2.setter
	def _(self, Degree:int):
		# ['in'] Degree:int
		self.com_parent.Degree2 = Degree

	@property
	def endtangent(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for end tangent of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] EndTangent:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.EndTangent)
	@endtangent.setter
	def _(self, EndTangent:A3Vertex):
		# TODO: Check arguments
		# ['in'] EndTangent:tagVARIANT | A3Vertex
		self.com_parent.EndTangent = EndTangent

	@property
	def fitpoints(self) -> A3Vertexes:
		"Specifies the current fit point of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] fitPoint:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.FitPoints)
	@fitpoints.setter
	def _(self, fitPoint:A3Vertexes):
		# TODO: Check arguments
		# ['in'] fitPoint:tagVARIANT | A3Vertexes
		self.com_parent.FitPoints = fitPoint.flatten

	@property
	def fittolerance(self) -> float:
		"Specifies the fit tolerance of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] fitTol:float
		return self.com_parent.FitTolerance
	@fittolerance.setter
	def _(self, fitTol:float):
		# ['in'] fitTol:float
		self.com_parent.FitTolerance = fitTol

	@property
	def isperiodic(self) -> bool:
		"Determines if the given spline is periodic"
		# TODO: Check arguments
		# ['out', 'retval'] fPeriodic:bool
		return self.com_parent.IsPeriodic

	@property
	def isplanar(self) -> bool:
		"Determines the whether the spline is planar"
		# TODO: Check arguments
		# ['out', 'retval'] fPlanar:bool
		return self.com_parent.IsPlanar

	@property
	def isrational(self) -> bool:
		"Determines if the given spline is planar"
		# TODO: Check arguments
		# ['out', 'retval'] fRational:bool
		return self.com_parent.IsRational

	@property
	def knotparameterization(self) -> int:
		"Specifies knot spacing when spline was created"
		# TODO: Check arguments
		# ['out', 'retval'] knotParamVal:int | ENUM?
		return self.com_parent.KnotParameterization
	@knotparameterization.setter
	def _(self, knotParamVal:int):
		# ['in'] knotParamVal:int
		self.com_parent.KnotParameterization = knotParamVal

	@property
	def knots(self) -> A3Vertex:
		"Gets the knot vector for a spline"
		# TODO: Check arguments
		# ['out', 'retval'] KnotValues:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Knots)
	@knots.setter
	def _(self, KnotValues:A3Vertex):
		# TODO: Check arguments
		# ['in'] KnotValues:tagVARIANT | A3Vertex
		self.com_parent.Knots = KnotValues

	@property
	def numberofcontrolpoints(self) -> int:
		"Specifies the number of control points of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] numCtrlPoints:int
		return self.com_parent.NumberOfControlPoints

	@property
	def numberoffitpoints(self) -> int:
		"Specifies the number of fit points of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] numFitPoints:int
		return self.com_parent.NumberOfFitPoints

	@property
	def splineframe(self) -> int:
		"Specifies whether displaying the CV Hull for spline"
		# TODO: Check arguments
		# ['out', 'retval'] show:int
		return self.com_parent.SplineFrame
	@splineframe.setter
	def _(self, show:int):
		# ['in'] show:int
		self.com_parent.SplineFrame = show

	@property
	def splinemethod(self) -> int:
		"Specifies whether fit points or CV's are displayed when selected"
		# TODO: Check arguments
		# ['out', 'retval'] method:int
		return self.com_parent.SplineMethod
	@splinemethod.setter
	def _(self, method:int):
		# ['in'] method:int
		self.com_parent.SplineMethod = method

	@property
	def starttangent(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for start tangent of the spline"
		# TODO: Check arguments
		# ['out', 'retval'] StartTangent:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.StartTangent)
	@starttangent.setter
	def _(self, StartTangent:A3Vertex):
		# TODO: Check arguments
		# ['in'] StartTangent:tagVARIANT | A3Vertex
		self.com_parent.StartTangent = StartTangent

	@property
	def weights(self) -> A3Vertex:
		"Gets the weight vector for spline"
		# TODO: Check arguments
		# ['out', 'retval'] WeightValues:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Weights)
	@weights.setter
	def _(self, WeightValues:A3Vertex):
		# TODO: Check arguments
		# ['in'] WeightValues:tagVARIANT | A3Vertex
		self.com_parent.Weights = WeightValues


class AcadSubDMesh(POINTER(_dll.IAcadSubDMesh), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSubDMesh
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadSubDMesh VBA-class wrapped as AcadSubDMesh python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Returns the coordinate of the vertex at a given index"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the current vertex on the mesh"
		# TODO: Check arguments
		# ['out', 'retval'] corners:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, corners:A3Vertexes):
		# TODO: Check arguments
		# ['in'] corners:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = corners.flatten

	@property
	def facecount(self) -> int:
		"Specifies the number of faces for the unsmooth mesh"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.FaceCount

	@property
	def smoothness(self) -> int:
		"Specifies the smoothing level for the mesh"
		# TODO: Check arguments
		# ['out', 'retval'] level:int
		return self.com_parent.Smoothness
	@smoothness.setter
	def _(self, level:int):
		# ['in'] level:int
		self.com_parent.Smoothness = level

	@property
	def vertexcount(self) -> int:
		"Specifies the number of vertices for the unsmooth mesh"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.VertexCount


class AcadSweptSurface(POINTER(_dll.IAcadSweptSurface), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadSweptSurface
	#	IAcadSurface
	#		IAcadEntity
	#			IAcadObject
	#				IDispatch
	#					IUnknown
	#						object
	# Prototype for IAcadSweptSurface VBA-class wrapped as AcadSweptSurface python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	edgeextensiondistances =	AcadSurface.edgeextensiondistances
	maintainassociativity =     AcadSurface.maintainassociativity
	showassociativity =         AcadSurface.showassociativity
	surfacetype =               AcadSurface.surfacetype
	surftrimassociativity =     AcadSurface.surftrimassociativity
	uisolinedensity =           AcadSurface.uisolinedensity
	visolinedensity =           AcadSurface.visolinedensity
	wireframetype =             AcadSurface.wireframetype
	# Properties
	@property
	def bank(self) -> bool:
		"Specifies whether or not the profile curve twists and rotates along a 3D path"
		# TODO: Check arguments
		# ['out', 'retval'] bBank:bool
		return self.com_parent.Bank
	@bank.setter
	def _(self, bBank:bool):
		# ['in'] bBank:bool
		self.com_parent.Bank = bBank

	@property
	def length(self) -> float:
		"Specifies the length of the sweep path"
		# TODO: Check arguments
		# ['out', 'retval'] Length:float
		return self.com_parent.Length

	@property
	def profilerotation(self) -> float:
		"Specifies the rotation of the sweep profile"
		# TODO: Check arguments
		# ['out', 'retval'] profileRotationAngle:float
		return self.com_parent.ProfileRotation
	@profilerotation.setter
	def _(self, profileRotationAngle:float):
		# ['in'] profileRotationAngle:float
		self.com_parent.ProfileRotation = profileRotationAngle

	@property
	def scale(self) -> float:
		"Specifies the scale factor from start to the end of the sweep path"
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.scale
	@scale.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.scale = scale

	@property
	def twist(self) -> float:
		"Specifies the amount of rotation along the entire length of the sweep path"
		# TODO: Check arguments
		# ['out', 'retval'] TwistAngle:float
		return self.com_parent.Twist
	@twist.setter
	def _(self, TwistAngle:float):
		# ['in'] TwistAngle:float
		self.com_parent.Twist = TwistAngle


class AcadTable(POINTER(_dll.IAcadTable), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadTable
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadTable VBA-class wrapped as AcadTable python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def clearsubselection(self):
		"ClearSubSelection."
		# VBA: object.ClearSubSelection 
		self.com_parent.ClearSubSelection()

	def cleartablestyleoverrides(self, flag: int):
		"Clears the tableStyleOverrides."
		# ['in'] flag:int | ENUM?
		# VBA: object.ClearTableStyleOverrides flag
		self.com_parent.ClearTableStyleOverrides(flag)

	def createcontent(self, nRow: int, nCol: int, nIndex: int) -> int:
		"Creates new content in a cell"
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nIndex:int
		# ['out', 'retval'] pInt:int
		# VBA: pInt = object.CreateContent (nRow, nCol, nIndex)
		return self.com_parent.CreateContent(nRow, nCol, nIndex)

	def deletecellcontent(self, row: int, col: int):
		"Deletes the cell content for the specified row and coluumn."
		# ['in'] row:int
		# ['in'] col:int
		# VBA: object.DeleteCellContent row, col
		self.com_parent.DeleteCellContent(row, col)

	def deletecolumns(self, col: int, cols: int=1):
		"deletes the column(s) from the specified column index."
		# ['in'] col:int
		# ['in'] cols:int
		# VBA: object.DeleteColumns col, cols
		self.com_parent.DeleteColumns(col, cols)

	def deletecontent(self, nRow: int, nCol: int):
		"Deletes a content from a cell"
		# ['in'] nRow:int
		# ['in'] nCol:int
		# VBA: object.DeleteContent nRow, nCol
		self.com_parent.DeleteContent(nRow, nCol)

	def deleterows(self, row: int, Rows: int=1):
		"deletes the row(s) from the specified row index."
		# ['in'] row:int
		# ['in'] Rows:int
		# VBA: object.DeleteRows row, Rows
		self.com_parent.DeleteRows(row, Rows)

	def enablemergeall(self, nRow: int, nCol: int, bEnable: bool):
		"Enables or disables the merge all flag in row or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] bEnable:bool
		# VBA: object.EnableMergeAll nRow, nCol, bEnable
		self.com_parent.EnableMergeAll(nRow, nCol, bEnable)

	def formatvalue(self, row: int, col: int):
		"Gets the formatted text string for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# [] nOption:int
		# [] pVal:str
		# VBA: object.FormatValue row, col, nOption, pVal
		self.com_parent.FormatValue(row, col)

	def generatelayout(self):
		"Generate layout."
		# VBA: object.GenerateLayout 
		self.com_parent.GenerateLayout()

	def getalignment(self, rowType: int) -> int:
		"Returns the cell alignment for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] pCellAlignment:int | ENUM?
		# VBA: pCellAlignment = object.GetAlignment (rowType)
		return self.com_parent.GetAlignment(rowType)

	def getattachmentpoint(self, row: int, col: int) -> A3Vertex:
		"Gets the attachment point for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pAttachmentPoint:tagVARIANT
		# VBA: pAttachmentPoint = object.GetAttachmentPoint (row, col)
		return A3Vertex(self.com_parent.GetAttachmentPoint(row, col))

	def getautoscale(self, row: int, col: int) -> bool:
		"Returns the auto scale flag value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetAutoScale (row, col)
		return self.com_parent.GetAutoScale(row, col)

	def getautoscale2(self, nRow: int, nCol: int, nContent: int) -> bool:
		"Returns the auto scale flag value for the specified row and column  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] bAutoScale:bool
		# VBA: bAutoScale = object.GetAutoScale2 (nRow, nCol, nContent)
		return self.com_parent.GetAutoScale2(nRow, nCol, nContent)

	def getbackgroundcolor(self, rowType: int) -> AcadAcCmColor:
		"Returns the background true color value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetBackgroundColor (rowType)
		return AcadAcCmColor(self.com_parent.GetBackgroundColor(rowType))

	def getbackgroundcolornone(self, rowType: int) -> bool:
		"Returns the backgroundColorNone flag value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetBackgroundColorNone (rowType)
		return self.com_parent.GetBackgroundColorNone(rowType)

	def getblockattributevalue(self, row: int, col: int, attdefId: int) -> str:
		"Returns the attribute value from the Specified block cell for the attribute definition object contained in the block."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] attdefId:int
		# ['out', 'retval'] bstrValue:str
		# VBA: bstrValue = object.GetBlockAttributeValue (row, col, attdefId)
		return self.com_parent.GetBlockAttributeValue(row, col, attdefId)

	def getblockattributevalue2(self, nRow: int, nCol: int, nContent: int, blkId: int) -> str:
		"Returns the attribute value from the Specified block cell for the attribute definition object contained in the block  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] blkId:int
		# ['out', 'retval'] Value:str
		# VBA: Value = object.GetBlockAttributeValue2 (nRow, nCol, nContent, blkId)
		return self.com_parent.GetBlockAttributeValue2(nRow, nCol, nContent, blkId)

	def getblockrotation(self, row: int, col: int) -> float:
		"Returns the block rotation for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] blkRotation:float
		# VBA: blkRotation = object.GetBlockRotation (row, col)
		return self.com_parent.GetBlockRotation(row, col)

	def getblockscale(self, row: int, col: int) -> float:
		"Returns the block scale value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] blkScale:float
		# VBA: blkScale = object.GetBlockScale (row, col)
		return self.com_parent.GetBlockScale(row, col)

	def getblocktablerecordid(self, row: int, col: int) -> int:
		"Returns the block table record id associated to the block-type cell."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] blkId:int
		# VBA: blkId = object.GetBlockTableRecordId (row, col)
		return self.com_parent.GetBlockTableRecordId(row, col)

	def getblocktablerecordid2(self, nRow: int, nCol: int, nContent: int) -> int:
		"Gets the block table record id associated to the block-type cell  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pAcDbObjectId:int
		# VBA: pAcDbObjectId = object.GetBlockTableRecordId2 (nRow, nCol, nContent)
		return self.com_parent.GetBlockTableRecordId2(nRow, nCol, nContent)

	def getbreakheight(self, nIndex: int) -> float:
		"Returns the break height of the specified table when table breaking is enabled."
		# TODO: Check arguments
		# ['in'] nIndex:int
		# ['out', 'retval'] pHeight:float
		# VBA: pHeight = object.GetBreakHeight (nIndex)
		return self.com_parent.GetBreakHeight(nIndex)

	def getcellalignment(self, row: int, col: int) -> int:
		"Returns the alignment for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pCellAlignment:int | ENUM?
		# VBA: pCellAlignment = object.GetCellAlignment (row, col)
		return self.com_parent.GetCellAlignment(row, col)

	def getcellbackgroundcolor(self, row: int, col: int) -> AcadAcCmColor:
		"Returns the background true color value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetCellBackgroundColor (row, col)
		return AcadAcCmColor(self.com_parent.GetCellBackgroundColor(row, col))

	def getcellbackgroundcolornone(self, row: int, col: int) -> bool:
		"Returns the backgroundColorNone flag value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetCellBackgroundColorNone (row, col)
		return self.com_parent.GetCellBackgroundColorNone(row, col)

	def getcellcontentcolor(self, row: int, col: int) -> AcadAcCmColor:
		"Returns the true color value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetCellContentColor (row, col)
		return AcadAcCmColor(self.com_parent.GetCellContentColor(row, col))

	def getcelldatatype(self, row: int, col: int):
		"Gets the cell data type and unit type for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out'] pDataType:int | ENUM?
		# ['out'] pUnitType:int | ENUM?
		# VBA: object.GetCellDataType row, col, pDataType, pUnitType
		return self.com_parent.GetCellDataType(row, col)

	def getcellextents(self, row: int, col: int, bOuterCell: bool): # -> tagVARIANT:
		"Gets the cell extents for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] bOuterCell:bool
		# ['out', 'retval'] pPts:tagVARIANT ????????????????????????????????
		# VBA: pPts = object.GetCellExtents (row, col, bOuterCell)
		return self.com_parent.GetCellExtents(row, col, bOuterCell)

	def getcellformat(self, row: int, col: int) -> str:
		"Gets the cell format for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pFormat:str
		# VBA: pFormat = object.GetCellFormat (row, col)
		return self.com_parent.GetCellFormat(row, col)

	def getcellgridcolor(self, row: int, col: int, edge: int) -> AcadAcCmColor:
		"Returns the gridColor value for the given edge of specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edge:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetCellGridColor (row, col, edge)
		return AcadAcCmColor(self.com_parent.GetCellGridColor(row, col, edge))

	def getcellgridlineweight(self, row: int, col: int, edge: int) -> int:
		"Returns the gridLineWeight value for the given edge of specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edge:int
		# ['out', 'retval'] plineweight:int | ENUM?
		# VBA: plineweight = object.GetCellGridLineWeight (row, col, edge)
		return self.com_parent.GetCellGridLineWeight(row, col, edge)

	def getcellgridvisibility(self, row: int, col: int, edge: int) -> bool:
		"Returns the gridVisibility value for the given edge of specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edge:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetCellGridVisibility (row, col, edge)
		return self.com_parent.GetCellGridVisibility(row, col, edge)

	def getcellstate(self, nRow: int, nCol: int) -> int:
		"Gets the cell state."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] pCellState:int | ENUM?
		# VBA: pCellState = object.GetCellState (nRow, nCol)
		return self.com_parent.GetCellState(nRow, nCol)

	def getcellstyle(self, nRow: int, nCol: int) -> str:
		"Gets the cell style of cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] pCellStyle:str
		# VBA: pCellStyle = object.GetCellStyle (nRow, nCol)
		return self.com_parent.GetCellStyle(nRow, nCol)

	def getcellstyleoverrides(self, row: int, col: int): # -> tagVARIANT:
		"Returns the cellStyleOverrides."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pIntArray:tagVARIANT ?????????????????
		# VBA: pIntArray = object.GetCellStyleOverrides (row, col)
		return self.com_parent.GetCellStyleOverrides(row, col)

	def getcelltextheight(self, row: int, col: int) -> float:
		"Returns the text height for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pTextHeight:float
		# VBA: pTextHeight = object.GetCellTextHeight (row, col)
		return self.com_parent.GetCellTextHeight(row, col)

	def getcelltextstyle(self, row: int, col: int) -> str:
		"Returns the text style name for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] bstrName:str
		# VBA: bstrName = object.GetCellTextStyle (row, col)
		return self.com_parent.GetCellTextStyle(row, col)

	def getcelltype(self, row: int, col: int) -> int:
		"Gets the cell type for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pCellType:int | ENUM?
		# VBA: pCellType = object.GetCellType (row, col)
		return self.com_parent.GetCellType(row, col)

	def getcellvalue(self, row: int, col: int): # -> tagVARIANT:
		"Gets the cell value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pVal:tagVARIANT ?????????????
		# VBA: pVal = object.GetCellValue (row, col)
		return self.com_parent.GetCellValue(row, col)

	def getcolumnname(self, nIndex: int) -> str:
		"Gets the columns name."
		# TODO: Check arguments
		# ['in'] nIndex:int
		# ['out', 'retval'] Name:str
		# VBA: Name = object.GetColumnName (nIndex)
		return self.com_parent.GetColumnName(nIndex)

	def getcolumnwidth(self, col: int) -> float:
		"Returns the column width for the specified column."
		# TODO: Check arguments
		# ['in'] col:int
		# ['out', 'retval'] pWidth:float
		# VBA: pWidth = object.GetColumnWidth (col)
		return self.com_parent.GetColumnWidth(col)

	def getcontentcolor(self, rowType: int) -> AcadAcCmColor:
		"Returns the true color value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetContentColor (rowType)
		return AcadAcCmColor(self.com_parent.GetContentColor(rowType))

	def getcontentcolor2(self, nRow: int, nCol: int, nContent: int) -> AcadAcCmColor:
		"Returns the true color value for the specified row type  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetContentColor2 (nRow, nCol, nContent)
		return AcadAcCmColor(self.com_parent.GetContentColor2(nRow, nCol, nContent))

	def getcontentlayout(self, row: int, col: int) -> int:
		"Gets the content layout of the cell."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pLayout:int
		# VBA: pLayout = object.GetContentLayout (row, col)
		return self.com_parent.GetContentLayout(row, col)

	def getcontenttype(self, nRow: int, nCol: int) -> int:
		"Gets the content type of the content at the specified content index."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] pType:int | ENUM?
		# VBA: pType = object.GetContentType (nRow, nCol)
		return self.com_parent.GetContentType(nRow, nCol)

	def getcustomdata(self, nRow: int, nCol: int, szKey: str): # -> tagVARIANT:
		"Gets the custom data value set in cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] szKey:str
		# ['out'] pData:tagVARIANT ?????????????
		# VBA: object.GetCustomData nRow, nCol, szKey, pData
		return self.com_parent.GetCustomData(nRow, nCol, szKey)

	def getdataformat(self, nRow: int, nCol: int, nContent: int) -> str:
		"Gets the cell format for the specified row and column and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pValue:str
		# VBA: pValue = object.GetDataFormat (nRow, nCol, nContent)
		return self.com_parent.GetDataFormat(nRow, nCol, nContent)

	def getdatatype(self, rowType: int):
		"Gets the row data type and unit type for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out'] pDataType:int | ENUM?
		# ['out'] pUnitType:int | ENUM?
		# VBA: object.GetDataType rowType, pDataType, pUnitType
		return self.com_parent.GetDataType(rowType)

	def getdatatype2(self, nRow: int, nCol: int, nContent: int):
		"Gets the row data type and unit type for the specified row type  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out'] pDataType:int | ENUM?
		# ['out'] pUnitType:int | ENUM?
		# VBA: object.GetDataType2 nRow, nCol, nContent, pDataType, pUnitType
		return self.com_parent.GetDataType2(nRow, nCol, nContent)

	def getfieldid(self, row: int, col: int) -> int:
		"Returns the field object id associated to the specifed cell."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] fieldId:int
		# VBA: fieldId = object.GetFieldId (row, col)
		return self.com_parent.GetFieldId(row, col)

	def getfieldid2(self, nRow: int, nCol: int, nContent: int) -> int:
		"Returns the field object id associated to the specifed cell  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pAcDbObjectId:int
		# VBA: pAcDbObjectId = object.GetFieldId2 (nRow, nCol, nContent)
		return self.com_parent.GetFieldId2(nRow, nCol, nContent)

	def getformat(self, rowType: int) -> str:
		"Gets the format for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pFormat:str
		# VBA: pFormat = object.GetFormat (rowType)
		return self.com_parent.GetFormat(rowType)

	def getformula(self, nRow: int, nCol: int, nContent: int) -> str:
		"Gets the formula if the content at the specified content index has a formula."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pszFormula:str
		# VBA: pszFormula = object.GetFormula (nRow, nCol, nContent)
		return self.com_parent.GetFormula(nRow, nCol, nContent)

	def getgridcolor(self, gridLineType: int, rowType: int) -> AcadAcCmColor:
		"Returns the gridColor value for the specified gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int
		# ['in'] rowType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetGridColor (gridLineType, rowType)
		return AcadAcCmColor(self.com_parent.GetGridColor(gridLineType, rowType))

	def getgridcolor2(self, nRow: int, nCol: int, nGridLineType: int) -> AcadAcCmColor:
		"Returns the gridColor value for the specified gridLineType and row type  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetGridColor2 (nRow, nCol, nGridLineType)
		return AcadAcCmColor(self.com_parent.GetGridColor2(nRow, nCol, nGridLineType))

	def getgriddoublelinespacing(self, nRow: int, nCol: int, nGridLineType: int) -> float:
		"Gets the grid double line spacing from cell, row, or column"
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['out', 'retval'] pValue:float
		# VBA: pValue = object.GetGridDoubleLineSpacing (nRow, nCol, nGridLineType)
		return self.com_parent.GetGridDoubleLineSpacing(nRow, nCol, nGridLineType)

	def getgridlinestyle(self, nRow: int, nCol: int, nGridLineType: int) -> int:
		"Gets the grid line style of cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['out', 'retval'] pStyle:int | ENUM?
		# VBA: pStyle = object.GetGridLineStyle (nRow, nCol, nGridLineType)
		return self.com_parent.GetGridLineStyle(nRow, nCol, nGridLineType)

	def getgridlinetype(self, nRow: int, nCol: int, nGridLineType: int) -> int:
		"Gets the grid line type of cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['out', 'retval'] pacDbObjId:int | ENUM?
		# VBA: pacDbObjId = object.GetGridLinetype (nRow, nCol, nGridLineType)
		return self.com_parent.GetGridLinetype(nRow, nCol, nGridLineType)

	def getgridlineweight(self, gridLineType: int, rowType: int) -> int:
		"Returns the gridLineWeight value for the specified gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] Lineweight:int | ENUM?
		# VBA: Lineweight = object.GetGridLineWeight (gridLineType, rowType)
		return self.com_parent.GetGridLineWeight(gridLineType, rowType)

	def getgridlineweight2(self, nRow: int, nCol: int, nGridLineType: int) -> int:
		"Gets the gridLineWeight value for the specified gridLineType(s) and row type(s)   and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['out', 'retval'] plineweight:int | ENUM?
		# VBA: plineweight = object.GetGridLineWeight2 (nRow, nCol, nGridLineType)
		return self.com_parent.GetGridLineWeight2(nRow, nCol, nGridLineType)

	def getgridvisibility(self, gridLineType: int, rowType: int) -> bool:
		"Returns the gridVisibility value for the specified gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int | ENUM?
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetGridVisibility (gridLineType, rowType)
		return self.com_parent.GetGridVisibility(gridLineType, rowType)

	def getgridvisibility2(self, nRow: int, nCol: int, nGridLineType: int) -> bool:
		"Returns the gridVisibility value for the specified gridLineType and row type."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['out', 'retval'] bVisible:bool
		# VBA: bVisible = object.GetGridVisibility2 (nRow, nCol, nGridLineType)
		return self.com_parent.GetGridVisibility2(nRow, nCol, nGridLineType)

	def gethasformula(self, nRow: int, nCol: int, nContent: int) -> bool:
		"Returns true if the content at the specified index is a formula."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetHasFormula (nRow, nCol, nContent)
		return self.com_parent.GetHasFormula(nRow, nCol, nContent)

	def getmargin(self, nRow: int, nCol: int, nMargin: int) -> float:
		"Gets the margin of cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nMargin:int | ENUM?
		# ['out', 'retval'] pValue:float
		# VBA: pValue = object.GetMargin (nRow, nCol, nMargin)
		return self.com_parent.GetMargin(nRow, nCol, nMargin)

	def getminimumcolumnwidth(self, col: int) -> float:
		"Gets the minimum column width for the specified column."
		# TODO: Check arguments
		# ['in'] col:int
		# ['out', 'retval'] pWidth:float
		# VBA: pWidth = object.GetMinimumColumnWidth (col)
		return self.com_parent.GetMinimumColumnWidth(col)

	def getminimumrowheight(self, row: int) -> float:
		"Gets the minimum row height for the specified row."
		# TODO: Check arguments
		# ['in'] row:int
		# ['out', 'retval'] pHeight:float
		# VBA: pHeight = object.GetMinimumRowHeight (row)
		return self.com_parent.GetMinimumRowHeight(row)

	def getoverride(self, nRow: int, nCol: int, nContent: int) -> int:
		"Gets the override in cell, row, column, or content."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pValue:int | ENUM?
		# VBA: pValue = object.GetOverride (nRow, nCol, nContent)
		return self.com_parent.GetOverride(nRow, nCol, nContent)

	def getrotation(self, nRow: int, nCol: int, nContent: int) -> float:
		"Gets the rotation angle of the content at the specified content index."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pValue:float
		# VBA: pValue = object.GetRotation (nRow, nCol, nContent)
		return self.com_parent.GetRotation(nRow, nCol, nContent)

	def getrowheight(self, row: int) -> float:
		"Returns the row height for the specified row."
		# TODO: Check arguments
		# ['in'] row:int
		# ['out', 'retval'] pHeight:float
		# VBA: pHeight = object.GetRowHeight (row)
		return self.com_parent.GetRowHeight(row)

	def getrowtype(self, row: int) -> int:
		"Gets the row type for the specified row."
		# TODO: Check arguments
		# ['in'] row:int
		# ['out', 'retval'] pRowType:int | ENUM?
		# VBA: pRowType = object.GetRowType (row)
		return self.com_parent.GetRowType(row)

	def getscale(self, nRow: int, nCol: int, nContent: int) -> float:
		"Gets the scale of the content at the specified content index."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pScale:float
		# VBA: pScale = object.GetScale (nRow, nCol, nContent)
		return self.com_parent.GetScale(nRow, nCol, nContent)

	def getsubselection(self):
		"GetSubSelection."
		# TODO: Check arguments
		# ['out'] rowMin:int
		# ['out'] rowMax:int
		# ['out'] colMin:int
		# ['out'] colMax:int
		# VBA: object.GetSubSelection rowMin, rowMax, colMin, colMax
		return self.com_parent.GetSubSelection()

	def gettext(self, row: int, col: int) -> str:
		"Returns the text value value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] pStr:str
		# VBA: pStr = object.GetText (row, col)
		return self.com_parent.GetText(row, col)

	def gettextheight(self, rowType: int) -> float:
		"Returns the text height for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] pTextHeight:float
		# VBA: pTextHeight = object.GetTextHeight (rowType)
		return self.com_parent.GetTextHeight(rowType)

	def gettextheight2(self, nRow: int, nCol: int, nContent: int) -> float:
		"Returns the text height for the specified row and column  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pHeight:float
		# VBA: pHeight = object.GetTextHeight2 (nRow, nCol, nContent)
		return self.com_parent.GetTextHeight2(nRow, nCol, nContent)

	def gettextrotation(self, row: int, col: int) -> int:
		"Returns the text rotation for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out', 'retval'] TextRotation:int | ENUM?
		# VBA: TextRotation = object.GetTextRotation (row, col)
		return self.com_parent.GetTextRotation(row, col)

	def gettextstring(self, nRow: int, nCol: int, nContent: int) -> str:
		"Gets the text value value for the specified row and column  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pTextString:str
		# VBA: pTextString = object.GetTextString (nRow, nCol, nContent)
		return self.com_parent.GetTextString(nRow, nCol, nContent)

	def gettextstyle(self, rowType: int) -> str:
		"Returns the text style name for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int | ENUM?
		# ['out', 'retval'] bstrName:str
		# VBA: bstrName = object.GetTextStyle (rowType)
		return self.com_parent.GetTextStyle(rowType)

	def gettextstyle2(self, nRow: int, nCol: int, nContent: int) -> str:
		"Gets the text style name for the specified row and column  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pbstrStyleName:str
		# VBA: pbstrStyleName = object.GetTextStyle2 (nRow, nCol, nContent)
		return self.com_parent.GetTextStyle2(nRow, nCol, nContent)

	def getvalue(self, nRow: int, nCol: int, nContent: int): # -> tagVARIANT:
		"Gets the cell value for the specified row and column and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['out', 'retval'] pAcValue:tagVARIANT
		# VBA: pAcValue = object.GetValue (nRow, nCol, nContent)
		return self.com_parent.GetValue(nRow, nCol, nContent)

	def hittest(self, wpt: A3Vertex, wviewVec: A3Vertex):
		"Hit test."
		# TODO: Check arguments
		# ['in'] wpt:tagVARIANT | A3Vertex
		# ['in'] wviewVec:tagVARIANT | A3Vertex
		# ['out'] resultRowIndex:int
		# ['out'] resultColumnIndex:int
		# ['out', 'retval'] bReturn:bool
		# VBA: bReturn = object.HitTest (wpt, wviewVec, resultRowIndex, resultColumnIndex)
		return self.com_parent.HitTest(wpt, wviewVec)

	def insertcolumns(self, col: int, Width: float, cols: int=1):
		"Inserts the column(s) of specified width."
		# ['in'] col:int
		# ['in'] Width:float
		# ['in'] cols:int
		# VBA: object.InsertColumns col, Width, cols
		self.com_parent.InsertColumns(col, Width, cols)

	def insertcolumnsandinherit(self, col: int, nInheritFrom: int, nNumCols: int=1):
		"Inserts one or more columns at the specified index and inherits the column properties from specified column."
		# ['in'] col:int
		# ['in'] nInheritFrom:int
		# ['in'] nNumCols:int
		# VBA: object.InsertColumnsAndInherit col, nInheritFrom, nNumCols
		self.com_parent.InsertColumnsAndInherit(col, nInheritFrom, nNumCols)

	def insertrows(self, row: int, Height: float, Rows: int=1):
		"Inserts the row(s) of specified height."
		# ['in'] row:int
		# ['in'] Height:float
		# ['in'] Rows:int
		# VBA: object.InsertRows row, Height, Rows
		self.com_parent.InsertRows(row, Height, Rows)

	def insertrowsandinherit(self, nIndex: int, nInheritFrom: int, nNumRows: int=1):
		"Inserts one or more rows at the specified index and inherits the row properties from specified row."
		# ['in'] nIndex:int
		# ['in'] nInheritFrom:int
		# ['in'] nNumRows:int
		# VBA: object.InsertRowsAndInherit nIndex, nInheritFrom, nNumRows
		self.com_parent.InsertRowsAndInherit(nIndex, nInheritFrom, nNumRows)

	def iscontenteditable(self, nRow: int, nCol: int) -> bool:
		"Checks if the content of the specified cell can be modified."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.IsContentEditable (nRow, nCol)
		return self.com_parent.IsContentEditable(nRow, nCol)

	def isempty(self, nRow: int, nCol: int) -> bool:
		"Checks if the content of the specified cell is empty."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.IsEmpty (nRow, nCol)
		return self.com_parent.IsEmpty(nRow, nCol)

	def isformateditable(self, nRow: int, nCol: int) -> bool:
		"Checks if the format of the specified cell can be modified."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.IsFormatEditable (nRow, nCol)
		return self.com_parent.IsFormatEditable(nRow, nCol)

	def ismergeallenabled(self, nRow: int, nCol: int) -> bool:
		"Returns whether merge all flag is enabled or not in row or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.IsMergeAllEnabled (nRow, nCol)
		return self.com_parent.IsMergeAllEnabled(nRow, nCol)

	def ismergedcell(self, row: int, col: int):
		"is Merged Cell."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['out'] minRow:int
		# ['out'] maxRow:int
		# ['out'] minCol:int
		# ['out'] maxCol:int
		# ['out', 'retval'] pbValue:bool
		# VBA: pbValue = object.IsMergedCell (row, col, minRow, maxRow, minCol, maxCol)
		return self.com_parent.IsMergedCell(row, col)

	def mergecells(self, minRow: int, maxRow: int, minCol: int, maxCol: int):
		"merge cells."
		# ['in'] minRow:int
		# ['in'] maxRow:int
		# ['in'] minCol:int
		# ['in'] maxCol:int
		# VBA: object.MergeCells minRow, maxRow, minCol, maxCol
		self.com_parent.MergeCells(minRow, maxRow, minCol, maxCol)

	def movecontent(self, nRow: int, nCol: int, nFromIndex: int, nToIndex: int):
		"Moves a content in a cell from one position to another position within the cell"
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nFromIndex:int
		# ['in'] nToIndex:int
		# VBA: object.MoveContent nRow, nCol, nFromIndex, nToIndex
		self.com_parent.MoveContent(nRow, nCol, nFromIndex, nToIndex)

	def recomputetableblock(self, bForceUpdate: bool):
		"Recompute TableBlock."
		# ['in'] bForceUpdate:bool
		# VBA: object.RecomputeTableBlock bForceUpdate
		self.com_parent.RecomputeTableBlock(bForceUpdate)

	def removealloverrides(self, nRow: int, nCol: int):
		"Removes all the overrides in cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# VBA: object.RemoveAllOverrides nRow, nCol
		self.com_parent.RemoveAllOverrides(nRow, nCol)

	def reselectsubregion(self):
		"Re select SubRegion."
		# VBA: object.ReselectSubRegion 
		self.com_parent.ReselectSubRegion()

	def resetcellvalue(self, row: int, col: int):
		"Resets the cell value for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# VBA: object.ResetCellValue row, col
		self.com_parent.ResetCellValue(row, col)

	def select(self, wpt: A3Vertex, wvwVec: A3Vertex, wvwxVec: A3Vertex, wxaper: float=0.0, wyaper: float=0.0, allowOutside: bool=False):
		"Select."
		# TODO: Check arguments
		# ['in'] wpt:tagVARIANT | A3Vertex
		# ['in'] wvwVec:tagVARIANT | A3Vertex
		# ['in'] wvwxVec:tagVARIANT | A3Vertex
		# ['in'] wxaper:float
		# ['in'] wyaper:float
		# ['in'] allowOutside:bool
		# ['out'] resultRowIndex:int
		# ['out'] resultColumnIndex:int
		# VBA: object.Select wpt, wvwVec, wvwxVec, wxaper, wyaper, allowOutside, resultRowIndex, resultColumnIndex
		return self.com_parent.Select(wpt, wvwVec, wvwxVec, wxaper, wyaper, allowOutside)

	def selectsubregion(self, wpt1: A3Vertex, wpt2: A3Vertex, wvwVec: A3Vertex, wvwxVec: A3Vertex, seltype: int, bIncludeCurrentSelection: bool):
		"Select SubRegion."
		# TODO: Check arguments
		# ['in'] wpt1:tagVARIANT | A3Vertex
		# ['in'] wpt2:tagVARIANT | A3Vertex
		# ['in'] wvwVec:tagVARIANT | A3Vertex
		# ['in'] wvwxVec:tagVARIANT | A3Vertex
		# ['in'] seltype:int | ENUM?
		# ['in'] bIncludeCurrentSelection:bool
		# ['out'] rowMin:int
		# ['out'] rowMax:int
		# ['out'] colMin:int
		# ['out'] colMax:int
		# VBA: object.SelectSubRegion wpt1, wpt2, wvwVec, wvwxVec, seltype, bIncludeCurrentSelection, rowMin, rowMax, colMin, colMax
		return self.com_parent.SelectSubRegion(wpt1, wpt2, wvwVec, wvwxVec, seltype, bIncludeCurrentSelection)

	def setalignment(self, rowTypes: int, cellAlignment: int):
		"Sets the cell alignment for the specified row types."
		# ['in'] rowTypes:int | ENUM?
		# ['in'] cellAlignment:int | ENUM?
		# VBA: object.SetAlignment rowTypes, cellAlignment
		self.com_parent.SetAlignment(rowTypes, cellAlignment)

	def setautoscale(self, row: int, col: int, bValue: bool):
		"Sets the auto scale flag value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] bValue:bool
		# VBA: object.SetAutoScale row, col, bValue
		self.com_parent.SetAutoScale(row, col, bValue)

	def setautoscale2(self, nRow: int, nCol: int, nContent: int, bAutoFit: bool):
		"Sets the auto scale flag value for the specified row and column  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] bAutoFit:bool
		# VBA: object.SetAutoScale2 nRow, nCol, nContent, bAutoFit
		self.com_parent.SetAutoScale2(nRow, nCol, nContent, bAutoFit)

	def setbackgroundcolor(self, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the background true color value for the specified row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int | ENUM?
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetBackgroundColor rowTypes, pColor
		self.com_parent.SetBackgroundColor(rowTypes, pColor)

	def setbackgroundcolornone(self, rowTypes: int, bValue: bool):
		"Sets the backgroundColorNone flag value for the specified row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int | ENUM?
		# ['in'] bValue:bool
		# VBA: object.SetBackgroundColorNone rowTypes, bValue
		self.com_parent.SetBackgroundColorNone(rowTypes, bValue)

	def setblockattributevalue(self, row: int, col: int, attdefId: int, bstrValue: str):
		"Sets the attribute value to the Specified block cell for the attribute definition object contained in the block."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] attdefId:int
		# ['in'] bstrValue:str
		# VBA: object.SetBlockAttributeValue row, col, attdefId, bstrValue
		self.com_parent.SetBlockAttributeValue(row, col, attdefId, bstrValue)

	def setblockattributevalue2(self, nRow: int, nCol: int, nContent: int, blkId: int, Value: str):
		"Sets the attribute value from the Specified block cell for the attribute definition object contained in the block  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] blkId:int
		# ['in'] Value:str
		# VBA: object.SetBlockAttributeValue2 nRow, nCol, nContent, blkId, Value
		self.com_parent.SetBlockAttributeValue2(nRow, nCol, nContent, blkId, Value)

	def setblockrotation(self, row: int, col: int, blkRotation: float):
		"Sets the block rotation for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] blkRotation:float
		# VBA: object.SetBlockRotation row, col, blkRotation
		self.com_parent.SetBlockRotation(row, col, blkRotation)

	def setblockscale(self, row: int, col: int, blkScale: float):
		"Sets the block scale value for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] blkScale:float
		# VBA: object.SetBlockScale row, col, blkScale
		self.com_parent.SetBlockScale(row, col, blkScale)

	def setblocktablerecordid(self, row: int, col: int, blkId: int, bAutoFit: bool):
		"Sets the block table record id associated to the block-type cell."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] blkId:int
		# ['in'] bAutoFit:bool
		# VBA: object.SetBlockTableRecordId row, col, blkId, bAutoFit
		self.com_parent.SetBlockTableRecordId(row, col, blkId, bAutoFit)

	def setblocktablerecordid2(self, nRow: int, nCol: int, nContent: int, blkId: int, autoFit: bool):
		"Sets the block table record id associated to the block-type cell  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] blkId:int
		# ['in'] autoFit:bool
		# VBA: object.SetBlockTableRecordId2 nRow, nCol, nContent, blkId, autoFit
		self.com_parent.SetBlockTableRecordId2(nRow, nCol, nContent, blkId, autoFit)

	def setbreakheight(self, nIndex: int, Height: float):
		"Sets the break height of the specified table when table breaking is enabled."
		# ['in'] nIndex:int
		# ['in'] Height:float
		# VBA: object.SetBreakHeight nIndex, Height
		self.com_parent.SetBreakHeight(nIndex, Height)

	def setcellalignment(self, row: int, col: int, cellAlignment: int):
		"Sets the cell alignment for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] cellAlignment:int | ENUM?
		# VBA: object.SetCellAlignment row, col, cellAlignment
		self.com_parent.SetCellAlignment(row, col, cellAlignment)

	def setcellbackgroundcolor(self, row: int, col: int, pColor: AcadAcCmColor):
		"Sets the background true color value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetCellBackgroundColor row, col, pColor
		self.com_parent.SetCellBackgroundColor(row, col, pColor)

	def setcellbackgroundcolornone(self, row: int, col: int, bValue: bool):
		"Sets the backgroundColorNone flag value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] bValue:bool
		# VBA: object.SetCellBackgroundColorNone row, col, bValue
		self.com_parent.SetCellBackgroundColorNone(row, col, bValue)

	def setcellcontentcolor(self, row: int, col: int, pColor: AcadAcCmColor):
		"Sets the true color value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetCellContentColor row, col, pColor
		self.com_parent.SetCellContentColor(row, col, pColor)

	def setcelldatatype(self, row: int, col: int, dataType: int, unitType: int):
		"Sets the cell data type and unit type for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# [] dataType:int | ENUM?
		# [] unitType:int | ENUM?
		# VBA: object.SetCellDataType row, col, dataType, unitType
		self.com_parent.SetCellDataType(row, col, dataType, unitType)

	def setcellformat(self, row: int, col: int, pFormat: str):
		"Sets the cell format for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# [] pFormat:str
		# VBA: object.SetCellFormat row, col, pFormat
		self.com_parent.SetCellFormat(row, col, pFormat)

	def setcellgridcolor(self, row: int, col: int, edges: int, pColor: AcadAcCmColor):
		"Sets the gridColor value for the given edges of specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edges:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetCellGridColor row, col, edges, pColor
		self.com_parent.SetCellGridColor(row, col, edges, pColor)

	def setcellgridlineweight(self, row: int, col: int, edges: int, Lineweight: int):
		"Sets the gridLineWeight value for the given edges of specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edges:int
		# ['in'] Lineweight:int | ENUM?
		# VBA: object.SetCellGridLineWeight row, col, edges, Lineweight
		self.com_parent.SetCellGridLineWeight(row, col, edges, Lineweight)

	def setcellgridvisibility(self, row: int, col: int, edges: int, bValue: bool):
		"Sets the gridVisibility value for the given edges of specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] edges:int
		# ['in'] bValue:bool
		# VBA: object.SetCellGridVisibility row, col, edges, bValue
		self.com_parent.SetCellGridVisibility(row, col, edges, bValue)

	def setcellstate(self, nRow: int, nCol: int, nLock: int):
		"Sets the cell state."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nLock:int
		# VBA: object.SetCellState nRow, nCol, nLock
		self.com_parent.SetCellState(nRow, nCol, nLock)

	def setcellstyle(self, nRow: int, nCol: int, szCellStyle: str):
		"Sets the the cell style of cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] szCellStyle:str
		# VBA: object.SetCellStyle nRow, nCol, szCellStyle
		self.com_parent.SetCellStyle(nRow, nCol, szCellStyle)

	def setcelltextheight(self, row: int, col: int, TextHeight: float):
		"Sets the text height for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] TextHeight:float
		# VBA: object.SetCellTextHeight row, col, TextHeight
		self.com_parent.SetCellTextHeight(row, col, TextHeight)

	def setcelltextstyle(self, row: int, col: int, bstrName: str):
		"Sets the text style name for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] bstrName:str
		# VBA: object.SetCellTextStyle row, col, bstrName
		self.com_parent.SetCellTextStyle(row, col, bstrName)

	def setcelltype(self, row: int, col: int, CellType: int):
		"Sets the cell type for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] CellType:int | ENUM?
		# VBA: object.SetCellType row, col, CellType
		self.com_parent.SetCellType(row, col, CellType)

	def setcellvalue(self, row: int, col: int, val):
		"Sets the cell value for the specified row and column."
		# TODO: Check arguments
		# ['in'] row:int
		# ['in'] col:int
		# [] val:tagVARIANT
		# VBA: object.SetCellValue row, col, val
		self.com_parent.SetCellValue(row, col, val)

	def setcellvaluefromtext(self, row: int, col: int, val: str, nOption: int):
		"Sets the cell value by parsing the text for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] val:str
		# ['in'] nOption:int | ENUM?
		# VBA: object.SetCellValueFromText row, col, val, nOption
		self.com_parent.SetCellValueFromText(row, col, val, nOption)

	def setcolumnname(self, nIndex: int, Name: str):
		"Sets the columns name."
		# ['in'] nIndex:int
		# ['in'] Name:str
		# VBA: object.SetColumnName nIndex, Name
		self.com_parent.SetColumnName(nIndex, Name)

	def setcolumnwidth(self, col: int, Width: float):
		"Sets the column width for the specified column."
		# ['in'] col:int
		# ['in'] Width:float
		# VBA: object.SetColumnWidth col, Width
		self.com_parent.SetColumnWidth(col, Width)

	def setcontentcolor(self, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the true color value for the specified row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int | ENUM?
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetContentColor rowTypes, pColor
		self.com_parent.SetContentColor(rowTypes, pColor)

	def setcontentcolor2(self, nRow: int, nCol: int, nContent: int, pColor: AcadAcCmColor):
		"Sets the true color value for the specified row type  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetContentColor2 nRow, nCol, nContent, pColor
		self.com_parent.SetContentColor2(nRow, nCol, nContent, pColor)

	def setcontentlayout(self, row: int, col: int, nLayout: int):
		"Sets the content layout of the cell."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] nLayout:int | ENUM?
		# VBA: object.SetContentLayout row, col, nLayout
		self.com_parent.SetContentLayout(row, col, nLayout)

	def setcustomdata(self, nRow: int, nCol: int, szKey: str, data):
		"Sets the custom data value set in cell, row, or column."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] szKey:str
		# ['in'] data:tagVARIANT
		# VBA: object.SetCustomData nRow, nCol, szKey, data
		self.com_parent.SetCustomData(nRow, nCol, szKey, data)

	def setdataformat(self, nRow: int, nCol: int, nContent: int, szFormat: str):
		"Sets the cell format for the specified row and column and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] szFormat:str
		# VBA: object.SetDataFormat nRow, nCol, nContent, szFormat
		self.com_parent.SetDataFormat(nRow, nCol, nContent, szFormat)

	def setdatatype(self, rowTypes: int, dataType: int, unitType: int):
		"Sets the row data type and unit type for the specified row type."
		# ['in'] rowTypes:int | ENUM?
		# ['in'] dataType:int | ENUM?
		# ['in'] unitType:int | ENUM?
		# VBA: object.SetDataType rowTypes, dataType, unitType
		self.com_parent.SetDataType(rowTypes, dataType, unitType)

	def setdatatype2(self, nRow: int, nCol: int, nContent: int, dataType: int, unitType: int):
		"Sets the row data type and unit type for the specified row type  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] dataType:int | ENUM?
		# ['in'] unitType:int | ENUM?
		# VBA: object.SetDataType2 nRow, nCol, nContent, dataType, unitType
		self.com_parent.SetDataType2(nRow, nCol, nContent, dataType, unitType)

	def setfieldid(self, row: int, col: int, fieldId: int):
		"Sets the field object id in the specifed cell."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] fieldId:int
		# VBA: object.SetFieldId row, col, fieldId
		self.com_parent.SetFieldId(row, col, fieldId)

	def setfieldid2(self, nRow: int, nCol: int, nContent: int, acDbObjectId: int, nflag: int):
		"Sets  the field object id associated to the specifed cell  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] acDbObjectId:int
		# ['in'] nflag:int | ENUM?
		# VBA: object.SetFieldId2 nRow, nCol, nContent, acDbObjectId, nflag
		self.com_parent.SetFieldId2(nRow, nCol, nContent, acDbObjectId, nflag)

	def setformat(self, rowTypes: int, pFormat:str):
		"Sets the format for the specified row type."
		# ['in'] rowTypes:int | ENUM?
		# [] pFormat:str
		# VBA: object.SetFormat rowTypes, pFormat
		self.com_parent.SetFormat(rowTypes, pFormat)

	def setformula(self, nRow: int, nCol: int, nContent: int, pszFormula: str):
		"Sets the formula at the specified content index."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] pszFormula:str
		# VBA: object.SetFormula nRow, nCol, nContent, pszFormula
		self.com_parent.SetFormula(nRow, nCol, nContent, pszFormula)

	def setgridcolor(self, gridLineTypes: int, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the gridColor value for the specified gridLineType(s) and row type(s)."
		# TODO: Check arguments
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetGridColor gridLineTypes, rowTypes, pColor
		self.com_parent.SetGridColor(gridLineTypes, rowTypes, pColor)

	def setgridcolor2(self, nRow: int, nCol: int, nGridLineType: int, pColor: AcadAcCmColor):
		"Sets the gridColor value for the specified gridLineType and row type  and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetGridColor2 nRow, nCol, nGridLineType, pColor
		self.com_parent.SetGridColor2(nRow, nCol, nGridLineType, pColor)

	def setgriddoublelinespacing(self, nRow: int, nCol: int, nGridLineType: int, fSpacing: float):
		"Sets the grid double line spacing in cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['in'] fSpacing:float
		# VBA: object.SetGridDoubleLineSpacing nRow, nCol, nGridLineType, fSpacing
		self.com_parent.SetGridDoubleLineSpacing(nRow, nCol, nGridLineType, fSpacing)

	def setgridlinestyle(self, nRow: int, nCol: int, nGridLineTypes: int, nLineStyle: int):
		"Sets the grid line style of cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineTypes:int | ENUM?
		# ['in'] nLineStyle:int | ENUM?
		# VBA: object.SetGridLineStyle nRow, nCol, nGridLineTypes, nLineStyle
		self.com_parent.SetGridLineStyle(nRow, nCol, nGridLineTypes, nLineStyle)

	def setgridlinetype(self, nRow: int, nCol: int, nGridLineType: int, idLinetype: int):
		"Sets the grid line type of cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['in'] idLinetype:int | ENUM?
		# VBA: object.SetGridLinetype nRow, nCol, nGridLineType, idLinetype
		self.com_parent.SetGridLinetype(nRow, nCol, nGridLineType, idLinetype)

	def setgridlineweight(self, gridLineTypes: int, rowTypes: int, Lineweight: int):
		"Sets the gridLineWeight value for the specified gridLineType(s) and row type(s)."
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] Lineweight:int | ENUM?
		# VBA: object.SetGridLineWeight gridLineTypes, rowTypes, Lineweight
		self.com_parent.SetGridLineWeight(gridLineTypes, rowTypes, Lineweight)

	def setgridlineweight2(self, nRow: int, nCol: int, nGridLineType: int, Lineweight: int):
		"Sets the gridLineWeight value for the specified gridLineType(s) and row type(s)   and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['in'] Lineweight:int | ENUM?
		# VBA: object.SetGridLineWeight2 nRow, nCol, nGridLineType, Lineweight
		self.com_parent.SetGridLineWeight2(nRow, nCol, nGridLineType, Lineweight)

	def setgridvisibility(self, gridLineTypes: int, rowTypes: int, bValue: bool):
		"Sets the gridVisibility value for the specified gridLineType(s) and row type(s)."
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] bValue:bool
		# VBA: object.SetGridVisibility gridLineTypes, rowTypes, bValue
		self.com_parent.SetGridVisibility(gridLineTypes, rowTypes, bValue)

	def setgridvisibility2(self, nRow: int, nCol: int, nGridLineType: int, bVisible: bool):
		"Sets the gridVisibility value for the specified gridLineType and row type."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nGridLineType:int | ENUM?
		# ['in'] bVisible:bool
		# VBA: object.SetGridVisibility2 nRow, nCol, nGridLineType, bVisible
		self.com_parent.SetGridVisibility2(nRow, nCol, nGridLineType, bVisible)

	def setmargin(self, nRow: int, nCol: int, nMargins: int, fMargin: float):
		"Sets the margin of cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nMargins:int | ENUM?
		# ['in'] fMargin:float
		# VBA: object.SetMargin nRow, nCol, nMargins, fMargin
		self.com_parent.SetMargin(nRow, nCol, nMargins, fMargin)

	def setoverride(self, nRow: int, nCol: int, nContent: int, nProp: int):
		"Sets the override in cell, row, column, or content."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] nProp:int | ENUM?
		# VBA: object.SetOverride nRow, nCol, nContent, nProp
		self.com_parent.SetOverride(nRow, nCol, nContent, nProp)

	def setrotation(self, nRow: int, nCol: int, nContent: int, Value: float):
		"Sets the rotation angle of the content at the specified content index."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] Value:float
		# VBA: object.SetRotation nRow, nCol, nContent, Value
		self.com_parent.SetRotation(nRow, nCol, nContent, Value)

	def setrowheight(self, row: int, Height: float):
		"Sets the row height for the specified row."
		# ['in'] row:int
		# ['in'] Height:float
		# VBA: object.SetRowHeight row, Height
		self.com_parent.SetRowHeight(row, Height)

	def setscale(self, nRow: int, nCol: int, nContent: int, scale: float):
		"Sets the scale of the content at the specified content index."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] scale:float
		# VBA: object.SetScale nRow, nCol, nContent, scale
		self.com_parent.SetScale(nRow, nCol, nContent, scale)

	def setsubselection(self, rowMin: int, rowMax: int, colMin: int, colMax: int):
		"SetSubSelection."
		# ['in'] rowMin:int
		# ['in'] rowMax:int
		# ['in'] colMin:int
		# ['in'] colMax:int
		# VBA: object.SetSubSelection rowMin, rowMax, colMin, colMax
		self.com_parent.SetSubSelection(rowMin, rowMax, colMin, colMax)

	def settext(self, row: int, col: int, pStr: str):
		"Sets the text value value for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] pStr:str
		# VBA: object.SetText row, col, pStr
		self.com_parent.SetText(row, col, pStr)

	def settextheight(self, rowTypes: int, TextHeight: float):
		"Sets the text height for the specified row types."
		# ['in'] rowTypes:int
		# ['in'] TextHeight:float
		# VBA: object.SetTextHeight rowTypes, TextHeight
		self.com_parent.SetTextHeight(rowTypes, TextHeight)

	def settextheight2(self, nRow: int, nCol: int, nContent: int, Height: float):
		"Gets the text height for the specified row and column  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] Height:float
		# VBA: object.SetTextHeight2 nRow, nCol, nContent, Height
		self.com_parent.SetTextHeight2(nRow, nCol, nContent, Height)

	def settextrotation(self, row: int, col: int, TextRotation: int):
		"Sets the text rotation for the specified row and column."
		# ['in'] row:int
		# ['in'] col:int
		# ['in'] TextRotation:int | ENUM?
		# VBA: object.SetTextRotation row, col, TextRotation
		self.com_parent.SetTextRotation(row, col, TextRotation)

	def settextstring(self, nRow: int, nCol: int, nContent: int, Text: str):
		"Sets the text value value for the specified row and column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] Text:str
		# VBA: object.SetTextString nRow, nCol, nContent, Text
		self.com_parent.SetTextString(nRow, nCol, nContent, Text)

	def settextstyle(self, rowTypes: int, bstrName: str):
		"Sets the text style name for the specified row types."
		# ['in'] rowTypes:int
		# ['in'] bstrName:str
		# VBA: object.SetTextStyle rowTypes, bstrName
		self.com_parent.SetTextStyle(rowTypes, bstrName)

	def settextstyle2(self, nRow: int, nCol: int, nContent: int, bstrStyleName: str):
		"Sets the text style name for the specified row and column  and nContent."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] bstrStyleName:str
		# VBA: object.SetTextStyle2 nRow, nCol, nContent, bstrStyleName
		self.com_parent.SetTextStyle2(nRow, nCol, nContent, bstrStyleName)

	def settooltip(self, nRow: int, nCol: int, tip: str):
		"Sets the tooltip string for cell, row, or column."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] tip:str
		# VBA: object.SetToolTip nRow, nCol, tip
		self.com_parent.SetToolTip(nRow, nCol, tip)

	def setvalue(self, nRow: int, nCol: int, nContent: int, acValue):
		"Sets the cell value by parsing the text for the specified row and column and nContent."
		# TODO: Check arguments
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] acValue:tagVARIANT ??????????????????????????
		# VBA: object.SetValue nRow, nCol, nContent, acValue
		self.com_parent.SetValue(nRow, nCol, nContent, acValue)

	def setvaluefromtext(self, nRow: int, nCol: int, nContent: int, szText: str, nOption: int):
		"Sets the value of the content at the specified content index."
		# ['in'] nRow:int
		# ['in'] nCol:int
		# ['in'] nContent:int
		# ['in'] szText:str
		# ['in'] nOption:int | ENUM?
		# VBA: object.SetValueFromText nRow, nCol, nContent, szText, nOption
		self.com_parent.SetValueFromText(nRow, nCol, nContent, szText, nOption)

	def unmergecells(self, minRow: int, maxRow: int, minCol: int, maxCol: int):
		"Unmerge cells."
		# ['in'] minRow:int
		# ['in'] maxRow:int
		# ['in'] minCol:int
		# ['in'] maxCol:int
		# VBA: object.UnmergeCells minRow, maxRow, minCol, maxCol
		self.com_parent.UnmergeCells(minRow, maxRow, minCol, maxCol)

	# Properties
	@property
	def allowmanualheights(self) -> bool:
		"Allows the heights of broken table parts to have their own breaking height. When set to No, all table parts will break at the height of the initial table part."
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.AllowManualHeights
	@allowmanualheights.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.AllowManualHeights = bEnabled

	@property
	def allowmanualpositions(self) -> bool:
		"When enabled, each table part can be moved outside of the boundary. When not enabled, the table parts are contained within a rectangular boundary."
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.AllowManualPositions
	@allowmanualpositions.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.AllowManualPositions = bEnabled

	@property
	def breaksenabled(self) -> bool:
		"Determines whether table breaking is in use. When enabled, the table will break automatically at the current specified height."
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.BreaksEnabled
	@breaksenabled.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.BreaksEnabled = bEnabled

	@property
	def breakspacing(self) -> float:
		"Controls the spacing between the broken table parts. Depending on the break direction this will be a horizontal or vertical spacing."
		# TODO: Check arguments
		# ['out', 'retval'] pSpacing:float
		return self.com_parent.BreakSpacing
	@breakspacing.setter
	def _(self, pSpacing:float):
		# ['in'] pSpacing:float
		self.com_parent.BreakSpacing = pSpacing

	@property
	def columns(self) -> int:
		"Specifies the columns in the Table"
		# TODO: Check arguments
		# ['out', 'retval'] pColumns:int
		return self.com_parent.Columns
	@columns.setter
	def _(self, pColumns:int):
		# ['in'] pColumns:int
		self.com_parent.Columns = pColumns

	@property
	def columnwidth(self):
		"Sets the uniform column width for all the columns in the table."
		Exception("Can't GET ColumnWidth value")
	@columnwidth.setter
	def _(self, rhs:float):
		# ['in'] rhs:float
		self.com_parent.ColumnWidth = rhs

	@property
	def direction(self) -> A3Vertex:
		"Specifies the direction vector of the table"
		# TODO: Check arguments
		# ['out', 'retval'] DirectionVector:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Direction)
	@direction.setter
	def _(self, DirectionVector:A3Vertex):
		# TODO: Check arguments
		# ['in'] DirectionVector:tagVARIANT | A3Vertex
		self.com_parent.Direction = DirectionVector

	@property
	def enablebreak(self):
		"Enables or disables table breaking"
		Exception("Can't GET EnableBreak value")
	@enablebreak.setter
	def _(self, rhs:bool):
		# ['in'] rhs:bool
		self.com_parent.EnableBreak = rhs

	@property
	def flowdirection(self) -> int:
		"Specifies the Table flow direction"
		# TODO: Check arguments
		# ['out', 'retval'] pFlow:int | ENUM?
		return self.com_parent.FlowDirection
	@flowdirection.setter
	def _(self, pFlow:int):
		# ['in'] pFlow:int | ENUM?
		self.com_parent.FlowDirection = pFlow

	@property
	def hassubselection(self) -> bool:
		"HasSubSelection."
		# TODO: Check arguments
		# ['out', 'retval'] pbValue:bool
		return self.com_parent.HasSubSelection

	@property
	def headersuppressed(self) -> bool:
		"Returns and sets the header suppressed flag value."
		# TODO: Check arguments
		# ['out', 'retval'] bValue:bool
		return self.com_parent.HeaderSuppressed
	@headersuppressed.setter
	def _(self, bValue:bool):
		# ['in'] bValue:bool
		self.com_parent.HeaderSuppressed = bValue

	@property
	def height(self) -> float:
		"Specifies the Table height"
		# TODO: Check arguments
		# ['out', 'retval'] pHeight:float
		return self.com_parent.Height
	@height.setter
	def _(self, pHeight:float):
		# ['in'] pHeight:float
		self.com_parent.Height = pHeight

	@property
	def horzcellmargin(self) -> float:
		"Specifies the horizontal distance between text and edge of cell"
		# TODO: Check arguments
		# ['out', 'retval'] pGap:float
		return self.com_parent.HorzCellMargin
	@horzcellmargin.setter
	def _(self, pGap:float):
		# ['in'] pGap:float
		self.com_parent.HorzCellMargin = pGap

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specifies the insertion point of the table"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def minimumtableheight(self) -> float:
		"Gets the minimum height for the table."
		# TODO: Check arguments
		# ['out', 'retval'] pHeight:float
		return self.com_parent.MinimumTableHeight

	@property
	def minimumtablewidth(self) -> float:
		"Gets the minimum width for the table."
		# TODO: Check arguments
		# ['out', 'retval'] pWidth:float
		return self.com_parent.MinimumTableWidth

	@property
	def regeneratetablesuppressed(self) -> bool:
		"Enables or disables the regeneration of table block"
		# TODO: Check arguments
		# ['out', 'retval'] bValue:bool
		return self.com_parent.RegenerateTableSuppressed
	@regeneratetablesuppressed.setter
	def _(self, bValue:bool):
		# ['in'] bValue:bool
		self.com_parent.RegenerateTableSuppressed = bValue

	@property
	def repeatbottomlabels(self) -> bool:
		"Determines whether the bottom set of label rows is repeated at the bottom of each broken table part."
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.RepeatBottomLabels
	@repeatbottomlabels.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.RepeatBottomLabels = bEnabled

	@property
	def repeattoplabels(self) -> bool:
		"Determines whether the first set of label rows will be repeated at the top of each broken table part."
		# TODO: Check arguments
		# ['out', 'retval'] bEnabled:bool
		return self.com_parent.RepeatTopLabels
	@repeattoplabels.setter
	def _(self, bEnabled:bool):
		# ['in'] bEnabled:bool
		self.com_parent.RepeatTopLabels = bEnabled

	@property
	def rowheight(self):
		"Sets the uniform row height for all the rows in the table."
		Exception("Can't GET RowHeight value")
	@rowheight.setter
	def _(self, rhs:float):
		# ['in'] rhs:float
		self.com_parent.RowHeight = rhs

	@property
	def rows(self) -> int:
		"Specifies the rows in the Table"
		# TODO: Check arguments
		# ['out', 'retval'] pRows:int
		return self.com_parent.Rows
	@rows.setter
	def _(self, pRows:int):
		# ['in'] pRows:int
		self.com_parent.Rows = pRows

	@property
	def stylename(self) -> str:
		"Specifies the style name of the Table"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def tablebreakflowdirection(self) -> int:
		"Determines the direction that parts of the table flow."
		# TODO: Check arguments
		# ['out', 'retval'] pDir:int | ENUM?
		return self.com_parent.TableBreakFlowDirection
	@tablebreakflowdirection.setter
	def _(self, pDir:int):
		# ['in'] pDir:int | ENUM?
		self.com_parent.TableBreakFlowDirection = pDir

	@property
	def tablebreakheight(self) -> float:
		"Sets the breaking height for the initial table part and any other table parts that do not have manual heights set."
		# TODO: Check arguments
		# ['out', 'retval'] pHeight:float
		return self.com_parent.TableBreakHeight
	@tablebreakheight.setter
	def _(self, pHeight:float):
		# ['in'] pHeight:float
		self.com_parent.TableBreakHeight = pHeight

	@property
	def tablestyleoverrides(self): # -> tagVARIANT:
		"Returns the tableStyleOverrides."
		# TODO: Check arguments
		# ['out', 'retval'] pIntArray:tagVARIANT
		return self.com_parent.TableStyleOverrides

	@property
	def titlesuppressed(self) -> bool:
		"Returns and sets the title suppressed flag value."
		# TODO: Check arguments
		# ['out', 'retval'] bValue:bool
		return self.com_parent.TitleSuppressed
	@titlesuppressed.setter
	def _(self, bValue:bool):
		# ['in'] bValue:bool
		self.com_parent.TitleSuppressed = bValue

	@property
	def vertcellmargin(self) -> float:
		"Specifies the vertical distance between text and edge of cell"
		# TODO: Check arguments
		# ['out', 'retval'] pGap:float
		return self.com_parent.VertCellMargin
	@vertcellmargin.setter
	def _(self, pGap:float):
		# ['in'] pGap:float
		self.com_parent.VertCellMargin = pGap

	@property
	def width(self) -> float:
		"Specifies the Table width"
		# TODO: Check arguments
		# ['out', 'retval'] pWidth:float
		return self.com_parent.Width
	@width.setter
	def _(self, pWidth:float):
		# ['in'] pWidth:float
		self.com_parent.Width = pWidth


class AcadText(POINTER(_dll.IAcadText), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadText
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadText VBA-class wrapped as AcadText python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def fieldcode(self) -> str:
		"Returns the text string with field codes of the text"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		# VBA: bstrText = object.FieldCode ()
		return self.com_parent.FieldCode()

	# Properties
	@property
	def alignment(self) -> int:
		"Specifies both text height and text orientation by designating the endpoints of the baseline"
		# TODO: Check arguments
		# ['out', 'retval'] align:int | ENUM?
		return self.com_parent.Alignment
	@alignment.setter
	def _(self, align:int):
		# ['in'] align:int
		self.com_parent.Alignment = align

	@property
	def backward(self) -> bool:
		"Determines whether the text is backward or not"
		# TODO: Check arguments
		# ['out', 'retval'] Backward:bool
		return self.com_parent.Backward
	@backward.setter
	def _(self, Backward:bool):
		# ['in'] Backward:bool
		self.com_parent.Backward = Backward

	@property
	def height(self) -> float:
		"Specifies the height of the text"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@property
	def horizontalalignment(self) -> int:
		"Specifies the horizontal alignment of the text"
		# TODO: Check arguments
		# ['out', 'retval'] horizAlign:int | ENUM?
		return self.com_parent.HorizontalAlignment
	@horizontalalignment.setter
	def _(self, horizAlign:int):
		# ['in'] horizAlign:int
		self.com_parent.HorizontalAlignment = horizAlign

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the insertion point of the text"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def obliqueangle(self) -> float:
		"Specifies the oblique angle of the text"
		# TODO: Check arguments
		# ['out', 'retval'] obliAngle:float
		return self.com_parent.ObliqueAngle
	@obliqueangle.setter
	def _(self, obliAngle:float):
		# ['in'] obliAngle:float
		self.com_parent.ObliqueAngle = obliAngle

	@property
	def rotation(self) -> float:
		"Specifies the rotation angle of the text"
		# TODO: Check arguments
		# ['out', 'retval'] rotAngle:float
		return self.com_parent.Rotation
	@rotation.setter
	def _(self, rotAngle:float):
		# ['in'] rotAngle:float
		self.com_parent.Rotation = rotAngle

	@property
	def scalefactor(self) -> float:
		"Specifies the width scale factor of the text"
		# TODO: Check arguments
		# ['out', 'retval'] scalFactor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scalFactor:float):
		# ['in'] scalFactor:float
		self.com_parent.ScaleFactor = scalFactor

	@property
	def stylename(self) -> str:
		"Specifies the style name of the text"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def textalignmentpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate of the alignment point of the text"
		# TODO: Check arguments
		# ['out', 'retval'] alignPoint:tagVARIANT | A3Vertex
		return self.com_parent.TextAlignmentPoint
	@textalignmentpoint.setter
	def _(self, alignPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] alignPoint:tagVARIANT | A3Vertex
		self.com_parent.TextAlignmentPoint = alignPoint

	@property
	def textgenerationflag(self) -> int:
		"Specifies the attribute text generation flag"
		# TODO: Check arguments
		# ['out', 'retval'] textGenFlag:int
		return self.com_parent.TextGenerationFlag
	@textgenerationflag.setter
	def _(self, textGenFlag:int):
		# ['in'] textGenFlag:int
		self.com_parent.TextGenerationFlag = textGenFlag

	@property
	def textstring(self) -> str:
		"Specifies the text string of the text"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the text"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness

	@property
	def upsidedown(self) -> bool:
		"Determines whether the text is upside down or not"
		# TODO: Check arguments
		# ['out', 'retval'] UpsideDown:bool
		return self.com_parent.UpsideDown
	@upsidedown.setter
	def _(self, UpsideDown:bool):
		# ['in'] UpsideDown:bool
		self.com_parent.UpsideDown = UpsideDown

	@property
	def verticalalignment(self) -> int:
		"Specifies the vertical alignment of the text"
		# TODO: Check arguments
		# ['out', 'retval'] vertiAlign:int
		return self.com_parent.VerticalAlignment
	@verticalalignment.setter
	def _(self, vertiAlign:int):
		# ['in'] vertiAlign:int
		self.com_parent.VerticalAlignment = vertiAlign


class AcadTolerance(POINTER(_dll.IAcadTolerance), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadTolerance
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadTolerance VBA-class wrapped as AcadTolerance python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@property
	def dimensionlinecolor(self) -> int:
		"Specifies the color of the dimension lines"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int | ENUM?
		return self.com_parent.DimensionLineColor
	@dimensionlinecolor.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DimensionLineColor = Type

	@property
	def directionvector(self) -> A3Vertex:
		"Specifies the direction for the ray, tolerance, or xline through a vector"
		# TODO: Check arguments
		# ['out', 'retval'] dirVector:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.DirectionVector)
	@directionvector.setter
	def _(self, dirVector:A3Vertex):
		# TODO: Check arguments
		# ['in'] dirVector:tagVARIANT | A3Vertex
		self.com_parent.DirectionVector = dirVector

	@property
	def insertionpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for insertion point of the tolerance or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] insPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.InsertionPoint)
	@insertionpoint.setter
	def _(self, insPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] insPoint:tagVARIANT | A3Vertex
		self.com_parent.InsertionPoint = insPoint

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def scalefactor(self) -> float:
		"Specifies the overall scale factor applied to properties that specify sizes, distances, or offsets"
		# TODO: Check arguments
		# ['out', 'retval'] factor:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, factor:float):
		# ['in'] factor:float
		self.com_parent.ScaleFactor = factor

	@property
	def stylename(self) -> str:
		"Specifies the style name of the tolerance"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.StyleName
	@stylename.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.StyleName = bstrName

	@property
	def textcolor(self) -> int:
		"Specifies the color of the dimension text"
		# TODO: Check arguments
		# ['out', 'retval'] color:int | ENUM?
		return self.com_parent.TextColor
	@textcolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.TextColor = color

	@property
	def textheight(self) -> float:
		"Specifies the text height of the tolerance"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.TextHeight
	@textheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.TextHeight = Height

	@property
	def textstring(self) -> str:
		"Specifies the text string of the tolerance"
		# TODO: Check arguments
		# ['out', 'retval'] bstrText:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, bstrText:str):
		# ['in'] bstrText:str
		self.com_parent.TextString = bstrText

	@property
	def textstyle(self) -> str:
		"Specifies the text style of the tolerance"
		# TODO: Check arguments
		# ['out', 'retval'] style:str
		return self.com_parent.TextStyle
	@textstyle.setter
	def _(self, style:str):
		# ['in'] style:str
		self.com_parent.TextStyle = style


class AcadTrace(POINTER(_dll.IAcadTrace), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadTrace
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadTrace VBA-class wrapped as AcadTrace python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Properties
	@indexedproperty
	def coordinate(self, Index:int) -> A3Vertex:
		"Specifies the coordinate of a single vertex in the object"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pVal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Coordinate[Index])
	@coordinate.setter
	def _(self, Index:int, pVal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Index:int
		# ['in'] pVal:tagVARIANT | A3Vertex
		self.com_parent.Coordinate[Index] = pVal

	@property
	def coordinates(self) -> A3Vertexes:
		"Specifies the coordinates of the trace"
		# TODO: Check arguments
		# ['out', 'retval'] corners:tagVARIANT | A3Vertexes
		return A3Vertexes(self.com_parent.Coordinates)
	@coordinates.setter
	def _(self, corners:A3Vertexes):
		# TODO: Check arguments
		# ['in'] corners:tagVARIANT | A3Vertexes
		self.com_parent.Coordinates = corners.flatten

	@property
	def normal(self) -> A3Vertex:
		"Specifies the three-dimensional normal unit vector for the entity"
		# TODO: Check arguments
		# ['out', 'retval'] Normal:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.Normal)
	@normal.setter
	def _(self, Normal:A3Vertex):
		# TODO: Check arguments
		# ['in'] Normal:tagVARIANT | A3Vertex
		self.com_parent.Normal = Normal

	@property
	def thickness(self) -> float:
		"Specifies the thickness of the trace"
		# TODO: Check arguments
		# ['out', 'retval'] Thickness:float
		return self.com_parent.Thickness
	@thickness.setter
	def _(self, Thickness:float):
		# ['in'] Thickness:float
		self.com_parent.Thickness = Thickness


class AcadXline(POINTER(_dll.IAcadXline), _ez_ptr):# ENTITY
	"TODO: ADD DOC"
	#IAcadXline
	#	IAcadEntity
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadXline VBA-class wrapped as AcadXline python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
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
	# Methods
	def offset(self, Distance: float) -> list:
		"Creates a new entity object by offsetting the Xline by a specified distance"
		# TODO: Check arguments
		# ['in'] Distance:float
		# ['out', 'retval'] pOffsetCurves:tagVARIANT
		# VBA: pOffsetCurves = object.Offset (Distance)
		ret = []
		for e in self.com_parent.Offset(Distance):
			ret.append(CastManager.cast(e))
		return e

	# Properties
	@property
	def basepoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the base point of the Xline or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] BasePoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.BasePoint)
	@basepoint.setter
	def _(self, BasePoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] BasePoint:tagVARIANT | A3Vertex
		self.com_parent.BasePoint = BasePoint

	@property
	def directionvector(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the direction vector of the Xline"
		# TODO: Check arguments
		# ['out', 'retval'] dirVector:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.DirectionVector)
	@directionvector.setter
	def _(self, dirVector:A3Vertex):
		# TODO: Check arguments
		# ['in'] dirVector:tagVARIANT | A3Vertex
		self.com_parent.DirectionVector = dirVector

	@property
	def secondpoint(self) -> A3Vertex:
		"Specify the X, Y, Z coordinate for the second point of the Xline or use the Pick Point button to set X, Y, Z values simultaneously"
		# TODO: Check arguments
		# ['out', 'retval'] SecondPoint:tagVARIANT | A3Vertex
		return A3Vertex(self.com_parent.SecondPoint)
	@secondpoint.setter
	def _(self, SecondPoint:A3Vertex):
		# TODO: Check arguments
		# ['in'] SecondPoint:tagVARIANT | A3Vertex
		self.com_parent.SecondPoint = SecondPoint

