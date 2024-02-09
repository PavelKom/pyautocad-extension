#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api import acad_dll as _dll
from .object import AcadEntity, A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
from .util import arr_check, recast as _recast, uncast as _uncast, dict_fix, get_obj_block_source, non_neg, angle_radian_scope, str_cut256, vertexes_flatten
from multimethod import overload
import math


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadArc
"""	
class AcadArc(POINTER(_dll.IAcadArc), AcadEntity):
	def __new__(cls, Center: A3Vertex, Radius: float, StartAngle: float, EndAngle: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"Radius": Radius,
			"StartAngle": StartAngle,
			"EndAngle": EndAngle
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AcadArc(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	arclength = COM_Property("ArcLength", float, None, True)
	area = COM_Property("Area", float, None, True)
	center = COM_Property("Center", A3Vertex)
	document = AcadEntity.document
	endangle = COM_Property("EndAngle", float, value_wrapper=angle_radian_scope)
	endpoint = COM_Property("EndPoint", A3Vertex, None, True)
	end_point = endpoint
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	radius = COM_Property("Radius", float, value_wrapper=non_neg)
	startangle = COM_Property("StartAngle", float, value_wrapper=angle_radian_scope)
	startpoint = COM_Property("StartPoint", A3Vertex, None, True)
	thickness = COM_Property("Thickness", float)
	totalangle = COM_Property("TotalAngle", float, None, True)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible


def oblique_angle_scope(value: float):
	if value > 85: return 85
	if value < -85: return -85
	return value

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadAttribute
"""	
class AcadAttribute(POINTER(_dll.IAcadAttribute), AcadEntity):
	def __new__(cls, Height:float=0.0, Mode:int, Prompt: str, InsertionPoint: A3Vertex, Tag: str, Value: str, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Height": Height,
			"Mode": Mode,
			"Prompt": Prompt,
			"InsertionPoint": InsertionPoint,
			"Tag": Tag,
			"Value": Value
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddAttribute(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	# UpdateMTextAttribute - without changes
	
	# VBA-properties with recasting
	alignment = COM_Property("Alignment", int) # <acAlignment enum>
	application = AcadEntity.application
	backward = COM_Property("Backward", bool)
	constant = COM_Property("Constant", bool)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	fieldlength = COM_Property("FieldLength", int)
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	invisible = COM_Property("Invisible", bool)
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	lockposition = COM_Property("LockPosition", bool)
	lock_position = lockposition
	material = AcadEntity.material
	mode = COM_Property("Mode", int)# <acAttributeMode enum>
	mtextattribute = COM_Property("MTextAttribute", bool)
	mtext_attribute = mtextattribute
	mtextattributecontent = COM_Property("MTextAttributeContent", str)
	mtext_attribute_content = mtextattributecontent
	mtextboundarywidth = COM_Property("MTextBoundaryWidth", float)
	mtext_boundary_width = mtextboundarywidth
	MTextDrawingDirection = COM_Property("MTextDrawingDirection", int) # <AcDrawingDirection enum>
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	obliqueangle = COM_Property("ObliqueAngle", float, value_wrapper=oblique_angle_scope)
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	preset = COM_Property("Preset", bool)
	promptstring = COM_Property("PromptString", str)
	rotation = COM_Property("Rotation", float)
	scalefactor = COM_Property("ScaleFactor", float, value_wrapper=non_neg)
	stylename = COM_Property("StyleName", str)
	tagstring = COM_Property("TagString", str)
	textalignmentpoint = COM_Property("TextAlignmentPoint", A3Vertex)
	text_alignment_point = textalignmentpoint
	textgenerationflag = COM_Property("TextGenerationFlag", int) # <acTextGenerationFlag enum>
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	text_string = textstring
	thickness = AcadEntity.thickness
	truecolor = AcadEntity.truecolor
	upsidedown = COM_Property("UpsideDown", bool)
	upside_down = upsidedown
	verify = COM_Property("Verify", bool)
	visible = AcadEntity.visible
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadAttributeReference
"""	
class AcadAttributeReference(POINTER(_dll.IAcadAttributeReference), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use Block.GetAttributes() for getting all stored attributes.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	# UpdateMTextAttribute - without changes
	
	# VBA-properties with recasting
	alignment = COM_Property("Alignment", int) # <acAlignment enum>
	application = AcadEntity.application
	backward = COM_Property("Backward", bool)
	constant = COM_Property("Constant", bool, None, True)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	fieldlength = COM_Property("FieldLength", int)
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	invisible = COM_Property("Invisible", bool)
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	lockposition = COM_Property("LockPosition", bool, None, True)
	lock_position = lockposition
	material = AcadEntity.material
	mtextattribute = COM_Property("MTextAttribute", bool)
	mtext_attribute = mtextattribute
	mtextattributecontent = COM_Property("MTextAttributeContent", str)
	mtext_attribute_content = mtextattributecontent
	mtextboundarywidth = COM_Property("MTextBoundaryWidth", float)
	mtext_boundary_width = mtextboundarywidth
	mtextdrawingdirection = COM_Property("MTextDrawingDirection", int) # <AcDrawingDirection enum>
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	obliqueangle = COM_Property("ObliqueAngle", float, value_wrapper=oblique_angle_scope)
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	scalefactor = COM_Property("ScaleFactor", float, value_wrapper=non_neg)
	stylename = COM_Property("StyleName", str)
	tagstring = COM_Property("TagString", str)
	textalignmentpoint = COM_Property("TextAlignmentPoint", A3Vertex)
	text_alignment_point = textalignmentpoint
	textgenerationflag = COM_Property("TextGenerationFlag", int) # <acTextGenerationFlag enum>
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	text_string = textstring
	thickness = AcadEntity.thickness
	truecolor = AcadEntity.truecolor
	upsidedown = COM_Property("UpsideDown", bool)
	upside_down = upsidedown
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
"""	
class AcadBlockReference(POINTER(_dll.IAcadBlockReference), AcadEntity):
	def __new__(cls, *args, **kw):
		return cls.__new(*args, **kw)
	@overload
	def __new(cls, InsertionPoint: A3Vertex, Name: str, Xscale: float=1.0, Yscale: float=1.0, ZScale: float=1.0, Rotation: float=0.0, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# AcadAttributeReference(pos, name)								2-args
		# AcadAttributeReference(pos, name, x, y, z)					5-args
		# AcadAttributeReference(pos, name, x, y, z, rot)				6-args
		# AcadAttributeReference(pos, name, x, y, z, rot, pass)			7-args
		# AcadAttributeReference(pos, name, x, y, z, rot, pass, source)	8-args ALL
		kw = {
			"InsertionPoint": InsertionPoint,
			"Name": Name,
			"Xscale": Xscale,
			"Yscale": Yscale,
			"ZScale": ZScale,
			"Rotation": Rotation,
			"Password": Password
		}
		dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).InsertBlock(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	@__new.register
	def _(cls, InsertionPoint: A3Vertex, Name: str, Scale: A3Vertex, Rotation: float=0.0, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(InsertionPoint, Name, Scale.x, Scale.y, Scale.z, Rotation, Password, source)
	
	__new = classmethod(__new)
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	# ConvertToAnonymousBlock() - without changes
	# ConvertToStaticBlock(<str>) - without changes
	copy = AcadEntity.copy
	# Delete - without changes
	def explode(self):
		objs = super().Explode()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	def getattributes(self):
		objs = super().GetAttributes()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	get_attributes = getattributes
	getboundingbox = AcadEntity.getboundingbox
	def getconstantattributes(self):
		objs = super().GetConstantAttributes()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	get_constant_attributes = getconstantattributes
	def getdynamicblockproperties(self):
		objs = super().GetDynamicBlockProperties()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	get_dynamic_block_properties = getdynamicblockproperties
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	# ResetBlock - without changes
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	document = AcadEntity.document
	effectivename = COM_Property("EffectiveName", str, None, True)
	effective_name = effectivename
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasattributes = COM_Property("HasAttributes", bool, None, True)
	has_attributes = hasattributes
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	insunits = COM_Property("InsUnits", str, None, True)
	ins_units = insunits
	insunitsfactor = COM_Property("InsUnitsFactor", float, None, True)
	ins_units_factor = insunitsfactor
	isdynamicblock = COM_Property("IsDynamicBlock", bool, None, True)
	is_dynamic_block = isdynamicblock
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	name = COM_Property("Name", str)
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	xeffectivescalefactor = COM_Property("XEffectiveScaleFactor", float, value_wrapper=non_neg)
	x_effective_scale_factor = xeffectivescalefactor
	xscalefactor = COM_Property("XScaleFactor", float, value_wrapper=non_neg)
	x_scale_factor = xscalefactor
	yeffectivescalefactor = COM_Property("YEffectiveScaleFactor", float, value_wrapper=non_neg)
	y_effective_scale_factor = yeffectivescalefactor
	yscalefactor = COM_Property("YScaleFactor", float, value_wrapper=non_neg)
	y_scale_factor = yscalefactor
	zeffectivescalefactor = COM_Property("ZEffectiveScaleFactor", float, value_wrapper=non_neg)
	z_effective_scale_factor = zeffectivescalefactor
	zscalefactor = COM_Property("ZScaleFactor", float, value_wrapper=non_neg)
	z_scale_factor = zscalefactor
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
			└─ AcadExternalReference
"""	
class AcadExternalReference(POINTER(_dll.IAcadExternalReference), AcadBlockReference):
	def __new__(cls, *args, **kw):
		return cls.__new(*args, **kw)
	@overload
	def __new(cls, PathName: str, Name: str, InsertionPoint: A3Vertex, XScale: float=1.0, YScale: float=1.0, ZScale: float=1.0, Rotation: float=0.0, Overlay: bool=False, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"PathName": PathName,
			"Name": Name,
			"InsertionPoint": InsertionPoint,
			"Xscale": Xscale,
			"Yscale": Yscale,
			"ZScale": ZScale,
			"Rotation": Rotation,
			"Overlay": Overlay,
			"Password": Password
		}
		dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AttachExternalReference(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	@__new.register
	def _(cls, PathName: str, Name: str, InsertionPoint: A3Vertex, Scale: A3Vertex, Rotation: float=0.0, Overlay: bool=False, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(PathName, Name, InsertionPoint, Scale.x, Scale.y, Scale.z, Rotation, Overlay, Password, source)
	__new = classmethod(__new)
	
	# VBA-methods with recasting
	arraypolar = AcadBlockReference.arraypolar
	arrayrectangular = AcadBlockReference.arrayrectangular
	# ConvertToAnonymousBlock() - without changes
	# ConvertToStaticBlock(<str>) - without changes
	copy = AcadBlockReference.copy
	# Delete - without changes
	explode = AcadBlockReference.explode
	getattributes = AcadBlockReference.getattributes
	getboundingbox = AcadBlockReference.getboundingbox
	getconstantattributes = AcadBlockReference.getconstantattributes
	getdynamicblockproperties = AcadBlockReference.getdynamicblockproperties
	getextensiondictionary = AcadBlockReference.getextensiondictionary
	getxdata = AcadBlockReference.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadBlockReference.intersectwith
	mirror = AcadBlockReference.mirror
	mirror3d = AcadBlockReference.mirror3d
	move = AcadBlockReference.move
	# ResetBlock - without changes
	rotate = AcadBlockReference.rotate
	rotate3d = AcadBlockReference.rotate3d
	scaleentity = AcadBlockReference.scaleentity
	setxdata = AcadBlockReference.setxdata
	transformby = AcadBlockReference.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadBlockReference.application
	document = AcadBlockReference.document
	effectivename = AcadBlockReference.effectivename
	entitytransparency = AcadBlockReference.entitytransparency
	handle = AcadBlockReference.handle
	hasattributes = AcadBlockReference.hasattributes
	hasextensiondictionary = AcadBlockReference.hasextensiondictionary
	hyperlinks = AcadBlockReference.hyperlinks
	insertionpoint = AcadBlockReference.insertionpoint
	insunits = AcadBlockReference.insunits
	insunitsfactor = AcadBlockReference.insunitsfactor
	isdynamicblock = AcadBlockReference.isdynamicblock
	layer = AcadBlockReference.layer
	layerpropertyoverrides = COM_Property("LayerPropertyOverrides", bool, None, True)
	layer_property_overrides = layerpropertyoverrides
	linetype = AcadBlockReference.linetype
	linetypescale = AcadBlockReference.linetypescale
	lineweight = AcadBlockReference.lineweight
	material = AcadBlockReference.material
	name = AcadBlockReference.name
	normal = AcadBlockReference.normal
	objectid = AcadBlockReference.objectid
	objectname = AcadBlockReference.objectname
	ownerid = AcadBlockReference.ownerid
	path = COM_Property("Path", bool)
	plotstylename = AcadBlockReference.plotstylename
	rotation = AcadBlockReference.rotation
	truecolor = AcadBlockReference.truecolor
	visible = AcadBlockReference.visible
	xeffectivescalefactor = AcadBlockReference.xeffectivescalefactor
	xscalefactor = AcadBlockReference.xscalefactor
	yeffectivescalefactor = AcadBlockReference.yeffectivescalefactor
	yscalefactor = AcadBlockReference.yscalefactor
	zeffectivescalefactor = AcadBlockReference.zeffectivescalefactor
	zscalefactor = AcadBlockReference.zscalefactor


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
			└─ AcadExternalReference
				└─ AcadComparedReference
"""	
class AcadComparedReference(POINTER(_dll.IAcadComparedReference), AcadExternalReference):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use Block.GetAttributes() for getting all stored attributes.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadExternalReference.arraypolar
	arrayrectangular = AcadExternalReference.arrayrectangular
	# ConvertToAnonymousBlock() - without changes
	# ConvertToStaticBlock(<str>) - without changes
	copy = AcadExternalReference.copy
	# Delete - without changes
	explode = AcadExternalReference.explode
	getattributes = AcadExternalReference.getattributes
	getboundingbox = AcadExternalReference.getboundingbox
	getconstantattributes = AcadExternalReference.getconstantattributes
	getdynamicblockproperties = AcadExternalReference.getdynamicblockproperties
	getextensiondictionary = AcadExternalReference.getextensiondictionary
	getxdata = AcadExternalReference.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadExternalReference.intersectwith
	mirror = AcadExternalReference.mirror
	mirror3d = AcadExternalReference.mirror3d
	move = AcadExternalReference.move
	# ResetBlock - without changes
	rotate = AcadExternalReference.rotate
	rotate3d = AcadExternalReference.rotate3d
	scaleentity = AcadExternalReference.scaleentity
	setxdata = AcadExternalReference.setxdata
	transformby = AcadExternalReference.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadExternalReference.application
	document = AcadExternalReference.document
	effectivename = AcadExternalReference.effectivename
	entitytransparency = AcadExternalReference.entitytransparency
	handle = AcadExternalReference.handle
	hasattributes = AcadExternalReference.hasattributes
	hasextensiondictionary = AcadExternalReference.hasextensiondictionary
	hyperlinks = AcadExternalReference.hyperlinks
	insertionpoint = AcadExternalReference.insertionpoint
	insunits = AcadExternalReference.insunits
	insunitsfactor = AcadExternalReference.insunitsfactor
	isdynamicblock = AcadExternalReference.isdynamicblock
	layer = AcadExternalReference.layer
	layerpropertyoverrides = AcadExternalReference.layerpropertyoverrides
	linetype = AcadExternalReference.linetype
	linetypescale = AcadExternalReference.linetypescale
	lineweight = AcadExternalReference.lineweight
	material = AcadExternalReference.material
	name = AcadExternalReference.name
	normal = AcadExternalReference.normal
	objectid = AcadExternalReference.objectid
	objectname = AcadExternalReference.objectname
	ownerid = AcadExternalReference.ownerid
	path = AcadExternalReference.path
	plotstylename = AcadExternalReference.plotstylename
	rotation = AcadExternalReference.rotation
	truecolor = AcadExternalReference.truecolor
	visible = AcadExternalReference.visible
	xeffectivescalefactor = AcadExternalReference.xeffectivescalefactor
	xscalefactor = AcadExternalReference.xscalefactor
	yeffectivescalefactor = AcadExternalReference.yeffectivescalefactor
	yscalefactor = AcadExternalReference.yscalefactor
	zeffectivescalefactor = AcadExternalReference.zeffectivescalefactor
	zscalefactor = AcadExternalReference.zscalefactor
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
			└─ AcadMInsertBlock
"""	
class AcadMInsertBlock(POINTER(_dll.IAcadMInsertBlock), AcadBlockReference):
	def __new__(cls, *args, **kw):
		return cls.__new(*args, **kw)
	@overload
	def __new(cls, InsertionPoint: A3Vertex, Name: str, XScale: float=1.0, YScale: float=1.0, ZScale: float=1.0, Rotation: float=0.0, NumRows: int=1, NumColumns: int=1, RowSpacing: float=0.0, ColumnSpacing: float=0.0, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"InsertionPoint": InsertionPoint,
			"Name": Name,
			"Xscale": Xscale,
			"Yscale": Yscale,
			"ZScale": ZScale,
			"Rotation": Rotation,
			"NumRows": NumRows,
			"NumColumns": NumColumns,
			"RowSpacing": RowSpacing,
			"ColumnSpacing": ColumnSpacing,
			"Password": Password
		}
		dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddMInsertBlock(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	@__new.register
	def _(cls, InsertionPoint: A3Vertex, Name: str, Scale: A3Vertex, Rotation: float=0.0, NumRows: int=1, NumColumns: int=1, RowSpacing: float=0.0, ColumnSpacing: float=0.0, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(InsertionPoint, Name, Scale.x, Scale.y, Scale.z, Rotation, NumRows, NumColumns, RowSpacing, ColumnSpacing, Password, source)
	@__new.register
	def _(cls, InsertionPoint: A3Vertex, Name: str, Scale: A3Vertex, Rotation: float=0.0, NumRC: A2Vertex, RowSpacing: float=0.0, ColumnSpacing: float=0.0, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(InsertionPoint, Name, Scale.x, Scale.y, Scale.z, Rotation, int(NumRC.x), int(NumRC.y), RowSpacing, ColumnSpacing, Password, source)
	@__new.register
	def _(cls, InsertionPoint: A3Vertex, Name: str, Scale: A3Vertex, Rotation: float=0.0, NumRC: A2Vertex, RCSpacing: A2Vertex, Password=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(InsertionPoint, Name, Scale.x, Scale.y, Scale.z, Rotation, int(NumRC.x), int(NumRC.y), RCSpacing.z, RCSpacing.y, Password, source)
	__new = classmethod(__new)
	
	# VBA-methods with recasting
	arraypolar = AcadBlockReference.arraypolar
	arrayrectangular = AcadBlockReference.arrayrectangular
	# ConvertToAnonymousBlock - without changes
	# ConvertToStaticBlock(newBlockName<String>)
	copy = AcadBlockReference.copy
	# Delete - without changes
	explode = AcadBlockReference.explode
	getattributes = AcadBlockReference.getattributes
	getboundingbox = AcadBlockReference.getboundingbox
	getconstantattributes = AcadBlockReference.getconstantattributes
	getdynamicblockproperties = AcadBlockReference.getdynamicblockproperties
	getextensiondictionary = AcadBlockReference.getextensiondictionary
	getxdata = AcadBlockReference.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadBlockReference.intersectwith
	mirror = AcadBlockReference.mirror
	mirror3d = AcadBlockReference.mirror3d
	move = AcadBlockReference.move
	# ResetBlock - without changes
	rotate = AcadBlockReference.rotate
	rotate3d = AcadBlockReference.rotate3d
	scaleentity = AcadBlockReference.scaleentity
	setxdata = AcadBlockReference.setxdata
	transformby = AcadBlockReference.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadBlockReference.application
	columns = COM_Property("Columns", int)
	columnspacing = COM_Property("ColumnSpacing", float)
	effectivename = AcadBlockReference.effectivename
	entitytransparency = AcadBlockReference.entitytransparency
	handle = AcadBlockReference.handle
	hasattributes = AcadBlockReference.hasattributes
	hasextensiondictionary = AcadBlockReference.hasextensiondictionary
	hyperlinks = AcadBlockReference.hyperlinks
	insertionpoint = AcadBlockReference.insertionpoint
	insunits = AcadBlockReference.insunits
	insunitsfactor = AcadBlockReference.insunitsfactor
	isdynamicblock = AcadBlockReference.isdynamicblock
	layer = AcadBlockReference.layer
	linetype = AcadBlockReference.linetype
	linetypescale = AcadBlockReference.linetypescale
	lineweight = AcadBlockReference.lineweight
	material = AcadBlockReference.material
	name = AcadBlockReference.name
	normal = AcadBlockReference.normal
	objectid = AcadBlockReference.objectid
	objectname = AcadBlockReference.objectname
	ownerid = AcadBlockReference.ownerid
	plotstylename = AcadBlockReference.plotstylename
	rotation = AcadBlockReference.rotation
	rows = COM_Property("Rows", int)
	rowspacing = COM_Property("RowSpacing", float)
	truecolor = AcadBlockReference.truecolor
	visible = AcadBlockReference.visible
	xeffectivescalefactor = AcadBlockReference.xeffectivescalefactor
	xscalefactor = AcadBlockReference.xscalefactor
	yeffectivescalefactor = AcadBlockReference.yeffectivescalefactor
	yscalefactor = AcadBlockReference.yscalefactor
	zeffectivescalefactor = AcadBlockReference.zeffectivescalefactor
	zscalefactor = AcadBlockReference.zscalefactor
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadCircle
"""
def AcadCircle(POINTER(_dll.IAcadCircle), AcadEntity):
	def __new__(cls, Center: A3Vertex, Radius: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"Radius": Radius
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddCircle(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	area = COM_Property("Area", float)
	center = COM_Property("Center", A3Vertex)
	circumference = COM_Property("Circumference", float)
	diameter = COM_Property("Diameter", float)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	radius = COM_Property("Radius", float, value_wrapper=non_neg)
	thickness = COM_Property("Thickness", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadEllipse
"""
class AcadEllipse(POINTER(_dll.IAcadEllipse), AcadEntity):
	def __new__(cls, *args, **kw):
		return cls.__new(*args, **kw)
	@overload
	def __new(cls, Center: A3Vertex, MajorAxis: float, RadiusRatio: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		if MajorAxis == 0.0:
			raise ValueError("Ellepse MajorAxis axis can't be equal 0")
		elif RadiusRatio == 0.0:
			raise ValueError("Ellepse RadiusRatio axis can't be equal 0")
		kw = {
			"Center": Center,
			"MajorAxis": abs(MajorAxis),
			"RadiusRatio": abs(RadiusRatio)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddEllipse(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	@__new.register
	def _(cls, Center: A3Vertex, Size: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		if Size.x == 0.0 or Size.y == 0.0:
			raise ValueError("Ellepse axis can't be equal 0")
		return cls.__new(Center, Size.x, Size.y / Size.x, source)
	__new = classmethod(__new)

	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes

	# VBA-properties with recasting
	application = AcadEntity.application
	area = COM_Property("Area", float, None, True)
	center = COM_Property("Center", A3Vertex)
	document = AcadEntity.document
	endangle = COM_Property("EndAngle", float, value_wrapper=angle_radian_scope)
	endparameter = COM_Property("EndParameter", float, value_wrapper=angle_radian_scope)
	endpoint = COM_Property("EndPoint", A3Vertex, None, True)
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	majoraxis = COM_Property("MajorAxis", A3Vertex)
	major_axis = majoraxis
	majorradius = COM_Property("MajorRadius", float)
	material = AcadEntity.material
	minoraxis = COM_Property("MinorAxis", A3Vertex)
	minor_axis = minoraxis
	minorradius = COM_Property("MinorRadius", float)
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	radiusratio = COM_Property("RadiusRatio", float, value_wrapper=non_neg)
	startangle = COM_Property("StartAngle", float, value_wrapper=angle_radian_scope)
	startparameter = COM_Property("StartParameter", float, value_wrapper=angle_radian_scope)
	startpoint = COM_Property("StartPoint", A3Vertex, None, True)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadGeoPositionMarker
"""	
def AcadGeoPositionMarker(POINTER(_dll.IAcadGeoPositionMarker), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))

	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	altitude = COM_Property("Altitude", float)
	application = AcadEntity.application
	backgroundfill = COM_Property("BackgroundFill", bool)
	document = AcadEntity.document
	drawingdirection = COM_Property("DrawingDirection", int) # acDrawingDirection enum
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	landinggap = COM_Property("LandingGap", float)
	latitude = COM_Property("Latitude", float)
	layer = AcadEntity.layer
	linespacingdistance = COM_Property("LineSpacingDistance", float)
	linespacingfactor = COM_Property("LineSpacingFactor", float, value_wrapper=float_as_linespacingfactor)
	linespacingstyle = COM_Property("LineSpacingStyle", int) # acLineSpacingStyle enum
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	longitude = COM_Property("Longitude", float)
	material = AcadEntity.material
	notes = COM_Property("Notes", str)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	position = COM_Property("Position", A3Vertex)
	radius = COM_Property("Radius", float)
	rotation = COM_Property("Rotation", float)
	textframedisplay = COM_Property("TextFrameDisplay", bool)
	textjustify = COM_Property("TextJustify", int) # AcAttachmentPoint enum
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	textstylename = COM_Property("TextStyleName", str)
	textwidth = COM_Property("TextWidth", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible


def float_as_linespacingfactor(value: float):
	if value < 0.25: return 0.25
	elif value > 4.0: return 4.0
	return value


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadHatch
"""	
def AcadHatch(POINTER(_dll.IAcadHatch), AcadEntity):
	def __new__(cls, *args, **kw):
		return cls.__new(*args, **kw)
	@overload
	def __new(cls, PatternType: int, PatternName: str, Associativity: bool, HatchObjectType: int=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"PatternType": PatternType,
			"PatternName": PatternName,
			"Associativity": Associativity,
			"HatchObjectType": HatchObjectType
		}
		dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddHatch(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	@__new.register
	def _(cls, PatternType: int, PatternName: str, Associativity: bool, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return cls.__new(PatternType, PatternName, Associativity, None, source)
	__new = classmethod(__new)
	
	def appendinnerloop(self, Loop: list):
		for obj in Loop:
			if not isinstance(obj, (AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline)):
				raise TypeError("[AcadHatch.AppendInnerLoop] Object must be on of the types: AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline")
		super().AppendInnerLoop(Loop)
	append_inner_loop = appendinnerloop
	
	def appendouterloop(self, Loop: list):
		for obj in Loop:
			if not isinstance(obj, (AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline)):
				raise TypeError("[AcadHatch.AppendOuterLoop] Object must be on of the types: AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline")
		super().AppendOuterLoop(Loop)
	append_outer_loop = appendouterloop
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	# Evaluate - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	def getloopat(self, Index: int, Loop: list=list()): # ToDo: need test
		super().GetLoopAt(Index, Loop)
		return Loop
	get_loop_at = getloopat
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	def insertloopat(self, Index: int, LoopType: int, Loop: list):
		for obj in Loop:
			if not isinstance(obj, (AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline)):
				raise TypeError("[AcadHatch.AppendOuterLoop] Object must be on of the types: AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline")
		super().InsertLoopAt(Index, LoopType, Loop)
	insert_loop_at = insertloopat
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	# SetPattern(< AcPatternType enum>, <String>) - without changes
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	area = COM_Property("Area", float, None, True)
	associativehatch = COM_Property("AssociativeHatch", bool, None, True)
	backgroundcolor = COM_PropertyRecast("BackgroundColor", AcadAcCmColor)
	background_color = backgroundcolor
	document = AcadEntity.document
	elevation = COM_Property("Elevation", float)
	entitytransparency = AcadEntity.entitytransparency
	gradientangle = COM_Property("GradientAngle", float)
	gradientcentered = COM_Property("GradientCentered", bool)
	gradientcolor1 = COM_PropertyRecast("GradientColor1", AcadAcCmColor)
	gradient_color1 = gradientcolor1
	gradientcolor2 = COM_PropertyRecast("GradientColor2", AcadAcCmColor)
	gradient_color2 = gradientcolor2
	GradientName = COM_Property("GradientName", str, value_wrapper=str_as_gradientname)
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hatchobjecttype = COM_Property("HatchObjectType", int) # AcHatchObjectType enum
	hatchstyle = COM_Property("HatchStyle", int) # acHatchStyle enum
	hyperlinks = AcadEntity.hyperlinks
	isopenwidth = COM_Property("ISOPenWidth", int) # <acISOPenWidth enum>
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	numberofloops = COM_Property("NumberOfLoops", int, None, True)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	origin = COM_Property("Origin", A3Vertex)
	ownerid = AcadEntity.ownerid

	patternangle = COM_Property("PatternAngle", float)
	patterndouble = COM_Property("PatternDouble", bool)
	patternname = COM_Property("PatternName", str)
	patternscale = COM_Property("PatternScale", float)
	patternspace = COM_Property("PatternSpace", float)
	patterntype = COM_Property("PatternType", int, None, True) # <acPatternType enum>
	plotstylename = AcadEntity.plotstylename
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	
def str_as_gradientname(value: str):
	if str_as_gradientname.d is None:
		str_as_gradientname.d = (
		"Linear", "Cylinder", "InvCylinder",
		"Spherical", "HemiSpherical", "Curved",
		"InvSpherical", "InvHemiSpherical", "InvCurved")
	if value not in str_as_gradientname.d:
		raise ValueError("[AcadEntity.Linetype] Value must be {0}".format(str_as_gradientname.d))
	return value
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadHelix
"""	
class AcadHelix(POINTER(_dll.IAcadHelix), AcadEntity):
	def __new__(cls, *args, **kw):
		# ToDo: Helix can be created by command _HELIX
		# Remarks
		# The Helix object encapsulates a Spline object that helps it maintain its basic shape. You can use ActiveX to query and edit Helix entities in an AutoCAD drawing. However, you cannot create a Helix object with ActiveX.
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight(<bool>) - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	baseradius = COM_Property("BaseRadius", float)
	constrain = COM_Property("Constrain", int) # acHelixConstrainType enum
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	position = COM_Property("Position", A3Vertex)
	topradius = COM_Property("TopRadius", float)
	totallength = COM_Property("TotalLength", float)
	truecolor = AcadEntity.truecolor
	turnheight = COM_Property("TurnHeight", float)
	turns = COM_Property("Turns", float)
	turnslope = COM_Property("TurnSlope", float)
	twist = COM_Property("Twist", int) # AcHelixTwistType enum
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadLeader
"""	
def AcadLeader(POINTER(_dll.IAcadLeader), AcadEntity):
	def __new__(cls, PointsArray: A3Vertexes, Annotation: (AcadBlockReference, AcadMtext, AcadTolerance)=None, Type: int, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Type as AcLeaderType enum
		if len(PointsArray) < 2:
			raise ValueError("[AcadLeader] PointsArray must provide at least two points to define the leader.")
		kw = {
			"PointsArray": PointsArray.flatten,
			"Annotation": Annotation,
			"Type": Type
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddLeader(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	# Evaluate - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight(<bool>) - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	annotation = COM_PropertyRecast("Annotation", (AcadBlockReference, AcadMtext, AcadTolerance))
	application = AcadEntity.application
	arrowheadblock = COM_Property("ArrowheadBlock", str)
	arrowheadsize = COM_Property("ArrowheadSize", float, value_wrapper=non_neg)
	arrowheadtype = COM_Property("ArrowheadType", int) # acDimArrowheadType enum
	# Don't use Coordinate(i) for getting/setting point coordinate
	# Just get/set item like array AcadLeader[i]
	# Or use get_coordinate / set_coordinate for getting/setting point coordinate
	@deprecated
	def coordinate(self, *args, **kw):
	 	raise DeprecationWarning("Don't use Coordinate(i) for getting/setting point coordinat.e\nJust get/set item like array AcadLeader[i].\nOr use get_coordinate / set_coordinate for getting/setting point coordinate.")
	def get_coordinate(self, index: int):
	 	return A3Vertex(super().Coordinate(index))
	def set_coordinate(self, index: int, pos: A3Vertex):
	 	super().Coordinate(index) = pos
	# coordinate = COM_Property("Coordinate", A3Vertexes)
	coordinates = COM_Property("Coordinates", A3Vertexes, value_wrapper=vertexes_flatten)
	dimensionlinecolor = COM_Property("DimensionLineColor", int) # acColor enum
	dimensionlineweight = COM_Property("DimensionLineWeight", int) # acLineWeight enum
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	scalefactor = COM_Property("ScaleFactor", float, value_wrapper=non_neg)
	stylename = COM_Property("StyleName", str)
	textgap = COM_Property("TextGap", float)
	truecolor = AcadEntity.truecolor
	type = COM_Property("Type", int) # ac3DPolylineType enum
	visible = AcadEntity.visible
	
	# MAGIC
	def __len__(self):
		return len(self.coordinates)
	
	def __iter__(self):
		for coord in sefl.coordinates:
			yield coord
	
	def __getitem__(self, index: int):
		return self.get_coordinate(index)
	
	def __setitem__(self, index: int, value: A3Vertex):
		self.set_coordinate(index, value)
	
	
	"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadLWPolyline
"""	
def AcadLWPolyline(POINTER(_dll.IAcadLWPolyline), AcadEntity):
	def __new__(cls, VerticesList: A2Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"VerticesList": VerticesList.flatten()
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddLightWeightPolyline(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	# VBA-methods with recasting
	def AddVertex(self, Index: int, Point: A2Vertex):
		super().AddVertex(Index, Point)
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	def explode(self):
		objs = super().Explode()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	getboundingbox = AcadEntity.getboundingbox
	# GetBulge(<int>)<double> - without changes
	getextensiondictionary = AcadEntity.getextensiondictionary
	def getwidth(self, Index: int , StartWidth: float=float(), EndWidth: float=float()):
		super().GetWidth(Index, StartWidth, EndWidth)
		return StartWidth, EndWidth
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	# SetBulge(Index<int>, Value<float>)
	# SetWidth (SegmentIndex<int>, StartWidth<float>, EndWidth<float>)
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	area = COM_Property("Area", float, None, True)
	closed = COM_Property("Closed", bool)
	constantwidth = COM_Property("ConstantWidth", float)
	@deprecated
	def coordinate(self, *args, **kw):
		raise DeprecationWarning("Don't use Coordinate(i) for getting/setting point coordinat.e\nJust get/set item like array AcadLWPolyline[i].\nOr use get_coordinate / set_coordinate for getting/setting point coordinate.")
	def get_coordinate(self, index: int):
		return A2Vertex(super().Coordinate(index))
	def set_coordinate(self, index: int, pos: A2Vertex):
		super().Coordinate(index) = pos
	coordinates = COM_Property("Coordinates", A2Vertexes, value_wrapper=vertexes_flatten)
	document = AcadEntity.document
	elevation = COM_Property("Elevation", float)
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	length = COM_Property("Length", float, None, True)
	linetype = AcadEntity.linetype
	linetypegeneration = COM_Property("LinetypeGeneration", bool)
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	thickness = COM_Property("Thickness", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadLine
"""	
class AcadLine(POINTER(_dll.IAcadLine), AcadEntity):
	def __new__(cls, StartPoint: A3Vertex, EndPoint: A3Vertex):
		kw = {
			"StartPoint": StartPoint,
			"EndPoint": EndPoint
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddLine(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	angle = COM_Property("Angle", float, None, True)
	application = AcadEntity.application
	delta = COM_Property("Delta", A3Vertex, None, True)
	document = AcadEntity.document
	endpoint = COM_Property("EndPoint", A3Vertex)
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	startpoint = COM_Property("StartPoint", A3Vertex)
	thickness = COM_Property("Thickness", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadLoftedSurface
"""	
class AcadLoftedSurface(POINTER(_dll.IAcadLoftedSurface), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	closed = COM_Property("Closed", bool)
	document = AcadEntity.document
	edgeextensiondistances = COM_Property("EdgeExtensionDistances", list) # NEED TEST
	enddraftangle = COM_Property("EndDraftAngle", int)
	enddraftmagnitude = COM_Property("EndDraftMagnitude", int)
	endsmoothcontinuity = COM_Property("EndSmoothContinuity", int)
	endsmoothmagnitude = COM_Property("EndSmoothMagnitude", float)
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	maintainassociativity = COM_Property("MaintainAssociativity", int)
	material = AcadEntity.material
	numcrosssections = COM_Property("NumCrossSections", None, int) # WRITE_ONLY????????
	numguidepaths = COM_Property("NumGuidePaths", None, int) # WRITE_ONLY????????
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	periodic = COM_Property("Periodic", bool)
	plotstylename = AcadEntity.plotstylename
	showassociativity = COM_Property("ShowAssociativity", bool)
	startdraftangle = COM_Property("StartDraftAngle", float)
	startdraftmagnitude = COM_Property("StartDraftMagnitude", int)
	startsmoothcontinuity = COM_Property("StartSmoothContinuity", int)
	startsmoothmagnitude = COM_Property("StartSmoothMagnitude", float)
	surfacenormals = COM_Property("SurfaceNormals", int)
	surfacetype = COM_Property("SurfaceType", str, value_wrapper=str_as_surfacetype)
	surftrimassociativity = COM_Property("SurfTrimAssociativity", bool)
	truecolor = AcadEntity.truecolor
	uisolinedensity = COM_Property("UIsolineDensity", int)
	visible = AcadEntity.visible
	visolinedensity = COM_Property("VIsolineDensity", int)
	wireframetype = COM_Property("WireframeType", int) # acWireframeType enum
	
	
def str_as_surfacetype(value: str):
	if str_as_surfacetype.d is None:
		str_as_surfacetype.d = (
		"AcadExtrudedSurface", "AcadRevolvedSurface", "AcadLoftedSurface",
		"AcadLoftedSurface", "AcadLoftedSurface", "AcadSweptSurface",
		"AcadPlaneSurface", "AcadNetworkSurface", "AcadNurbSurface")
	if value not in str_as_surfacetype.d:
		raise ValueError("[AcadLoftedSurface.SurfaceType] Value must be {0}".format(str_as_surfacetype.d))
	return value
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadMLeader
"""	
class AcadMLeader(POINTER(_dll.IAcadMLeader), AcadEntity):
	def __new__(cls, pointsArray: A3Vertexes, leaderLineIndex: int, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"pointsArray": VerticesList.flatten(),
			"leaderLineIndex":leaderLineIndex
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddMLeader(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	# VBA-methods with recasting
	# AddLeader<int> - without changes
	def addleaderline(self, leaderIndex: int, pointArray: A3Vertexes):
		return super().AddLeaderLine(leaderIndex, pointArray.flatten())
	def AddLeaderLineEx(self, pointArray: A3Vertex):
		return super().AddLeaderLineEx(pointArray)
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	# Evaluate - without changes
	# GetBlockAttributeValue(attdefId<Long_PTR>)<str> ?????
	getboundingbox = AcadEntity.getboundingbox
	def getdoglegdirection(self, leaderIndex:int):
		return A3Vertex(super().GetDoglegDirection(leaderIndex))
	getextensiondictionary = AcadEntity.getextensiondictionary
	# GetLeaderIndex(leaderLineIndex<int>)<int>
	def getleaderlineindexes(self, leaderIndex:int):
		return A3Vertex(super().GetLeaderLineIndexes(leaderIndex))
	def getleaderlinevertices(self, leaderLineIndex:int):
		return A3Vertex(super().GetLeaderLineVertices(leaderLineIndex))
	# GetVertexCount(leaderLineIndex<int>)<int>
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	# RemoveLeader(leaderIndex<int>)
	# RemoveLeaderLine(leaderLineIndex<int>)
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	# SetBlockAttributeValue(attdefId<Long_PTR>, value<str>)
	def setdoglegdirection(self, leaderIndex: int, dirVec: A3Vertexes):
		super().SetDoglegDirection(leaderIndex, dirVec.flatten())
	def setleaderlinevertices (self, leaderLineIndex: int, pointArray: A3Vertexes):
		super().SetLeaderLineVertices(leaderLineIndex, pointArray.flatten())
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	arrowheadblock = COM_Property("ArrowheadBlock", str)
	arrowheadsize = COM_Property("ArrowheadSize", float, value_wrapper=non_neg)
	arrowheadtype = COM_Property("ArrowheadType", int) # acDimArrowheadType enum
	blockconnectiontype = COM_Property("BlockConnectionType", int) # acBlockConnectionType enum
	blockscale = COM_Property("BlockScale", int)
	contentblockname = COM_Property("ContentBlockName", str)
	contentblocktype = COM_Property("ContentBlockType", int) # acPredefBlockType enum
	contenttype = COM_Property("ContentType", int) # acMLeaderContentType enum
	document = AcadEntity.document
	doglegged = COM_Property("DogLegged", bool)
	dogleglength = COM_Property("DoglegLength", float)
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	landinggap = COM_Property("LandingGap", float)
	layer = AcadEntity.layer
	leadercount = COM_Property("LeaderCount", int, None, True)
	leaderlinecolor = COM_PropertyRecast("LeaderLineColor", AcadAcCmColor)
	leaderlinetype = COM_Property("LeaderLinetype", int)
	leaderlineweight = COM_Property("LeaderLineWeight", float)
	leadertype = COM_Property("LeaderType", int) # AcMLeaderType enum
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	scalefactor = COM_Property("ScaleFactor", float, value_wrapper=non_neg)
	stylename = COM_Property("StyleName", str)
	textattachmentdirection = COM_Property("TextAttachmentDirection", int) # AcTextAttachmentDirection enum
	textbackgroundfill = COM_Property("TextBackgroundFill", bool)
	textbottomattachmenttype = COM_Property("TextBottomAttachmentType", int) # AcVerticalTextAttachmentType enum
	textdirection = COM_Property("TextDirection", int) # AcDrawingDirection enum
	textframedisplay = COM_Property("TextFrameDisplay", bool)
	textheight = COM_Property("TextHeight", float)
	textjustify = COM_Property("TextJustify", int) # AcAttachmentPoint enum
	textleftattachmenttype = COM_Property("TextLeftAttachmentType", int) # AcTextAttachmentType enum
	textlinespacingdistance = COM_Property("TextLineSpacingDistance", float)
	textlinespacingfactor = COM_Property("TextLineSpacingFactor", float)
	textlinespacingstyle = COM_Property("TextLineSpacingStyle", int) # AcLineSpacingStyle enum
	textrightattachmenttype = COM_Property("TextRightAttachmentType", int) # AcTextAttachmentType enum
	textrotation = COM_Property("TextRotation", float)
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	textstylename = COM_Property("TextStyleName", str)
	texttopattachmenttype = COM_Property("TextTopAttachmentType", int) # AcVerticalTextAttachmentType enum
	textwidth = COM_Property("TextWidth", float)
	truecolor = AcadEntity.truecolor
	type = COM_Property("Type", int) # ac3DPolylineType enum
	visible = AcadEntity.visible

	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadMLine
"""	
class AcadMLine(POINTER(_dll.IAcadMLine), AcadEntity):
	def __new__(cls, VertexList: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"VertexList": VertexList.flatten()
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddMLine(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	justification = COM_Property("Justification", int) # AcMLineJustification enum
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	mlinescale = COM_Property("MLineScale", float)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	stylename = COM_Property("StyleName", str, None, True)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadMLine
"""	
class AcadMLine(POINTER(_dll.IAcadMLine), AcadEntity):
	def __new__(cls, InsertionPoint: A3Vertex, Width: float, Text: str, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"InsertionPoint": InsertionPoint,
			"Width": Width,
			"Text": Text
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddMText(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	# FieldCode<str> - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	AttachmentPoint = COM_Property("AttachmentPoint", int) # acAttachmentPoint enum
	backgroundfill = COM_Property("BackgroundFill", bool)
	document = AcadEntity.document
	drawingdirection = COM_Property("DrawingDirection", int) # acDrawingDirection enum
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	layer = AcadEntity.layer
	linespacingdistance = COM_Property("LineSpacingDistance", float)
	linespacingfactor = COM_Property("LineSpacingFactor", float, value_wrapper=float_as_linespacingfactor)
	linespacingstyle = COM_Property("LineSpacingStyle", int) # acLineSpacingStyle enum
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	stylename = COM_Property("StyleName", str)
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	width = COM_Property("Width", float)
	
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadOle
"""	
class AcadOle(POINTER(_dll.IAcadOle), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	lockaspectratio = COM_Property("LockAspectRatio", bool)
	material = AcadEntity.material
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	oleitemtype = COM_Property("OleItemType", int) # AcOleType enum
	oleplotquality = COM_Property("OlePlotQuality", int) # AcOlePlotQuality enum
	olesourceapp = COM_Property("OleSourceApp", str)
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	scaleheight = COM_Property("ScaleHeight", float)
	scalewidth = COM_Property("ScaleWidth", float)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	width = COM_Property("Width", float)
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadPoint
"""	
class AcadPoint(POINTER(_dll.IAcadPoint), AcadEntity):
	def __new__(self, Point: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Point": Point
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddPoint(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	coordinates = COM_Property("Coordinates", A3Vertex)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	normal = COM_Property("Normal", A3Vertex)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	thickness = COM_Property("Thickness", float, value_wrapper=abs)
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadPointCloud
"""	
class AcadPointCloud(POINTER(_dll.IAcadPointCloud), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	height = COM_Property("Height", float, value_wrapper=non_neg)
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	intensitycolorscheme = COM_Property("IntensityColorScheme", int) # AcPointCloudIntensityStyle enum
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	locked = COM_Property("Locked", bool)
	material = AcadEntity.material
	name = COM_Property("Name", str)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	scale = COM_Property("Scale", float)
	showclipped = COM_Property("ShowClipped", bool)
	showintensity = COM_Property("ShowIntensity", bool)
	stylization = COM_Property("Stylization", int) # AcPointCloudStylizationType enum
	truecolor = AcadEntity.truecolor
	unit = COM_Property("Unit", str)
	unitfactor = COM_Property("UnitFactor", float)
	useentitycolor = COM_Property("UseEntityColor", int) # AcPointCloudColorType enum
	visible = AcadEntity.visible
	width = COM_Property("Width", float)
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadPointCloudEx
"""	
class AcadPointCloudEx(POINTER(_dll.IAcadPointCloudEx), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use iter(Block) for getting all stored entities.""".format(cls))
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	colorscheme = COM_Property("ColorScheme", str)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	geolocate = COM_Property("Geolocate", bool)
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	locked = COM_Property("Locked", bool)
	material = AcadEntity.material
	name = COM_Property("Name", str)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	path = COM_Property("Path", str, None, True)
	plotstylename = AcadEntity.plotstylename
	rotation = COM_Property("Rotation", float)
	scale = COM_Property("Scale", float)
	segmentation = COM_Property("Segmentation", str, None, True)
	showcropped = COM_Property("ShowCropped", bool)
	stylization = COM_Property("Stylization", int) # AcPointCloudStylizationType enum
	truecolor = AcadEntity.truecolor
	unit = COM_Property("Unit", str)
	unitfactor = COM_Property("UnitFactor", float)
	visible = AcadEntity.visible
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadPolyfaceMesh
"""	
class AcadPolyfaceMesh(POINTER(_dll.IAcadPolyfaceMesh), AcadEntity):
	def __new__(cls, VerticesList: A3Vertexes, FaceList: list[int]):
		for val in FaceList:
			if not isinstance(val, int):
				raise TypeError("[AcadPolyfaceMesh] FaceList must ONLY contain integers")
			kw = {
			"VerticesList": VerticesList.flatten(),
			"FaceList": FaceList
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddPolyfaceMesh(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	@deprecated
	def coordinate(self, *args, **kw):
	 	raise DeprecationWarning("Don't use Coordinate(i) for getting/setting point coordinat.e\nJust get/set item like array AcadLeader[i].\nOr use get_coordinate / set_coordinate for getting/setting point coordinate.")
	def get_coordinate(self, index: int):
	 	return A3Vertex(super().Coordinate(index))
	def set_coordinate(self, index: int, pos: A3Vertex):
	 	super().Coordinate(index) = pos
	coordinates = COM_Property("Coordinates", A3Vertexes, value_wrapper=vertexes_flatten)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	numberoffaces = COM_Property("NumberOfFaces", int)
	numberofvertices = COM_Property("NumberOfVertices", int)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	truecolor = AcadEntity.truecolor
	visible = AcadEntity.visible
	
	# MAGIC
	def __len__(self):
		return len(self.coordinates)
	
	def __iter__(self):
		for coord in sefl.coordinates:
			yield coord
	
	def __getitem__(self, index: int):
		return self.get_coordinate(index)
	
	def __setitem__(self, index: int, value: A3Vertex):
		self.set_coordinate(index, value)
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadPolygonMesh
"""	
class AcadPolygonMesh(POINTER(_dll.IAcadPolygonMesh), AcadEntity):
	'''
	???????????????????
	AddPolygonMesh
	???????????????????
	def __new__(cls, VerticesList: A3Vertexes, FaceList: list[int]):
		for val in FaceList:
			if not isinstance(val, int):
				raise TypeError("[AcadPolyfaceMesh] FaceList must ONLY contain integers")
			kw = {
			"VerticesList": VerticesList.flatten(),
			"FaceList": FaceList
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddPolyfaceMesh(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	'''	
	# VBA-methods with recasting
	arraypolar = AcadEntity.arraypolar
	arrayrectangular = AcadEntity.arrayrectangular
	copy = AcadEntity.copy
	# Delete - without changes
	def appendvertex(self, Point: A3Vertex):
		super().AppendVertex(Point)
	def explode(self):
		objs = super().Explode()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return ret
	getboundingbox = AcadEntity.getboundingbox
	getextensiondictionary = AcadEntity.getextensiondictionary
	getxdata = AcadEntity.getxdata
	# Highlight<bool> - without changes
	intersectwith = AcadEntity.intersectwith
	mirror = AcadEntity.mirror
	mirror3d = AcadEntity.mirror3d
	move = AcadEntity.move
	rotate = AcadEntity.rotate
	rotate3d = AcadEntity.rotate3d
	scaleentity = AcadEntity.scaleentity
	setxdata = AcadEntity.setxdata
	transformby = AcadEntity.transformby
	# Update - without changes
	
	# VBA-properties with recasting
	application = AcadEntity.application
	@deprecated
	def coordinate(self, *args, **kw):
	 	raise DeprecationWarning("Don't use Coordinate(i) for getting/setting point coordinat.e\nJust get/set item like array AcadLeader[i].\nOr use get_coordinate / set_coordinate for getting/setting point coordinate.")
	def get_coordinate(self, index: int):
	 	return A3Vertex(super().Coordinate(index))
	def set_coordinate(self, index: int, pos: A3Vertex):
	 	super().Coordinate(index) = pos
	coordinates = COM_Property("Coordinates", A2Vertexes, value_wrapper=vertexes_flatten)
	document = AcadEntity.document
	entitytransparency = AcadEntity.entitytransparency
	handle = AcadEntity.handle
	hasextensiondictionary = AcadEntity.hasextensiondictionary
	hyperlinks = AcadEntity.hyperlinks
	layer = AcadEntity.layer
	linetype = AcadEntity.linetype
	linetypescale = AcadEntity.linetypescale
	lineweight = AcadEntity.lineweight
	material = AcadEntity.material
	mclose = COM_Property("MClose", bool)
	mdensity = COM_Property("MDensity", int, value_wrapper=int_between_2_256)
	mvertexcount = COM_Property("MVertexCount", int, value_wrapper=int_between_2_256)
	nclose = COM_Property("NClose", bool)
	ndensity = COM_Property("NDensity", int)
	nvertexcount = COM_Property("NVertexCount", int, value_wrapper=int_between_2_256)
	objectid = AcadEntity.objectid
	objectname = AcadEntity.objectname
	ownerid = AcadEntity.ownerid
	plotstylename = AcadEntity.plotstylename
	truecolor = AcadEntity.truecolor
	type = COM_Property("Type", int) # acPolymeshType enum
	visible = AcadEntity.visible
	
	# MAGIC
	def __len__(self):
		return len(self.coordinates)
	
	def __iter__(self):
		for coord in sefl.coordinates:
			yield coord
	
	def __getitem__(self, index: int):
		return self.get_coordinate(index)
	
	def __setitem__(self, index: int, value: A3Vertex):
		self.set_coordinate(index, value)
	
	
def int_between_2_256(value: int):
	if value > 256: return 256
	elif value < 2: return 2
	return value
	
	
	
	
	


