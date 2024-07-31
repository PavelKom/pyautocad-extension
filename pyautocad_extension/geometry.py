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

