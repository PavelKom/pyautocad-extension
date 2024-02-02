#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api import acad_dll as _dll
from .object import AcadEntity, A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
from .util import arr_check, recast as _recast, uncast as _uncast, dict_fix, get_obj_block_source, non_neg, angle_radian_scope, str_cut256
from multimethod import overload
import math


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadArc
"""	
class AcadArc(AcadEntity, POINTER(_dll.IAcadArc)):
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
	# ALL FROM PARENT / WITHOUT CHANGE
	def offset(self, Distance: float):
		return _recast(super().Offset(Distance))
	
	# VBA-properties with recasting
	arclength = COM_Property("ArcLength", float, None, True)
	area = COM_Property("Area", float, None, True)
	center = COM_Property("Center", A3Vertex)
	endangle = COM_Property("EndAngle", float, value_wrapper=angle_radian_scope)
	endpoint = COM_Property("EndPoint", A3Vertex, None, True)
	end_point = endpoint
	normal = COM_Property("Normal", A3Vertex)
	plotstylename = COM_Property("PlotStyleName", str)
	radius = COM_Property("Radius", float, value_wrapper=non_neg)
	startangle = COM_Property("StartAngle", float, value_wrapper=angle_radian_scope)
	startpoint = COM_Property("StartPoint", A3Vertex, None, True)
	thickness = COM_Property("Thickness", float)
	totalangle = COM_Property("TotalAngle", float, None, True)


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
class AcadAttribute(AcadEntity, POINTER(_dll.IAcadAttribute)):
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
	# ALL FROM PARENT / WITHOUT CHANGES
	# UpdateMTextAttribute - without changes
	
	# VBA-properties with recasting
	alignment = COM_Property("Alignment", int) # <acAlignment enum>
	backward = COM_Property("Backward", bool)
	constant = COM_Property("Constant", bool)
	fieldlength = COM_Property("FieldLength", int)
	height = COM_Property("Height", float, value_wrapper=non_neg)
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	invisible = COM_Property("Invisible", bool)
	lockposition = COM_Property("LockPosition", bool)
	lock_position = lockposition
	mode = COM_Property("Mode", int)# <acAttributeMode enum>
	mtextattribute = COM_Property("MTextAttribute", bool)
	mtext_attribute = mtextattribute
	mtextattributecontent = COM_Property("MTextAttributeContent", str)
	mtext_attribute_content = mtextattributecontent
	mtextboundarywidth = COM_Property("MTextBoundaryWidth", float)
	mtext_boundary_width = mtextboundarywidth
	MTextDrawingDirection = COM_Property("MTextDrawingDirection", int) # <AcDrawingDirection enum>
	normal = COM_Property("Normal", A3Vertex)
	obliqueangle = COM_Property("ObliqueAngle", float, value_wrapper=oblique_angle_scope)
	plotstylename = COM_Property("PlotStyleName", str)
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
	thickness = COM_Property("Thickness", float)
	upsidedown = COM_Property("UpsideDown", bool)
	upside_down = upsidedown
	verify = COM_Property("Verify", bool)
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadAttributeReference
"""	
class AcadAttributeReference(AcadEntity, POINTER(_dll.IAcadAttributeReference)):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use Block.GetAttributes() for getting all stored attributes.""".format(cls))
	
	# VBA-methods with recasting
	# UpdateMTextAttribute - without changes
	
	# VBA-properties with recasting
	alignment = COM_Property("Alignment", int) # <acAlignment enum>
	backward = COM_Property("Backward", bool)
	constant = COM_Property("Constant", bool, None, True)
	fieldlength = COM_Property("FieldLength", int)
	height = COM_Property("Height", float, value_wrapper=non_neg)
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	invisible = COM_Property("Invisible", bool)
	lockposition = COM_Property("LockPosition", bool, None, True)
	lock_position = lockposition
	mtextattribute = COM_Property("MTextAttribute", bool)
	mtext_attribute = mtextattribute
	mtextattributecontent = COM_Property("MTextAttributeContent", str)
	mtext_attribute_content = mtextattributecontent
	mtextboundarywidth = COM_Property("MTextBoundaryWidth", float)
	mtext_boundary_width = mtextboundarywidth
	MTextDrawingDirection = COM_Property("MTextDrawingDirection", int) # <AcDrawingDirection enum>
	normal = COM_Property("Normal", A3Vertex)
	obliqueangle = COM_Property("ObliqueAngle", float, value_wrapper=oblique_angle_scope)
	plotstylename = COM_Property("PlotStyleName", str)
	rotation = COM_Property("Rotation", float)
	scalefactor = COM_Property("ScaleFactor", float, value_wrapper=non_neg)
	stylename = COM_Property("StyleName", str)
	tagstring = COM_Property("TagString", str)
	textalignmentpoint = COM_Property("TextAlignmentPoint", A3Vertex)
	text_alignment_point = textalignmentpoint
	textgenerationflag = COM_Property("TextGenerationFlag", int) # <acTextGenerationFlag enum>
	textstring = COM_Property("TextString", str, value_wrapper=str_cut256)
	text_string = textstring
	thickness = COM_Property("Thickness", float)
	upsidedown = COM_Property("UpsideDown", bool)
	upside_down = upsidedown
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
"""	
class AcadBlockReference(AcadEntity, POINTER(_dll.IAcadBlockReference)):
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
	# Highlight<bool> - without changes
	# ResetBlock - without changes
	
	# VBA-properties with recasting
	effectivename = COM_Property("EffectiveName", str)
	effective_name = effectivename
	hasattributes = COM_Property("HasAttributes", bool)
	has_attributes = hasattributes
	insertionpoint = COM_Property("InsertionPoint", A3Vertex)
	insertion_point = insertionpoint
	insunits = COM_Property("InsUnits", str, None, True)
	ins_units = insunits
	insunitsfactor = COM_Property("InsUnitsFactor", float, None, True)
	ins_units_factor = insunitsfactor
	isdynamicblock = COM_Property("IsDynamicBlock", bool, None, True)
	is_dynamic_block = isdynamicblock
	name = COM_Property("Name", str)
	normal = COM_Property("Normal", A3Vertex)
	plotstylename = COM_Property("PlotStyleName", str)
	rotation = COM_Property("Rotation", float)
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
class AcadExternalReference(AcadBlockReference, POINTER(_dll.IAcadExternalReference)):
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
	
	# VBA-properties with recasting
	layerpropertyoverrides = COM_Property("LayerPropertyOverrides", bool, None, True)
	layer_property_overrides = layerpropertyoverrides
	path = COM_Property("Path", bool)


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
			└─ AcadExternalReference
				└─ AcadComparedReference
"""	
class AcadComparedReference(AcadExternalReference, POINTER(_dll.IAcadComparedReference)):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use Block.GetAttributes() for getting all stored attributes.""".format(cls))
	
	# VBA-methods with recasting
	
	# VBA-properties with recasting
	# EffectiveName<String> - without changes
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasAttributes<bool>- without changes
	# HasExtensionDictionary<bool>- without changes
	# Hyperlinks - from parent
	# InsertionPoint - from parent
	# InsUnits<String> - without changes
	# InsUnitsFactor<Double> - without changes
	# IsDynamicBlock<Boolean> - without changes
	# Layer<String> - without changes
	# LayerPropertyOverrides<Boolean> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Name<String> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# Path<String> - without changes
	plotstylename = COM_Property("PlotStyleName", str)
	rotation = COM_Property("Rotation", float)
	# TrueColor<bool> - without changes
	# Visible<bool> - without changes
	# XEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# XScaleFactor<Double>  - without changes
	# YEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# YScaleFactor<Double>  - without changes
	# ZEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# ZScaleFactor<Double>  - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadBlockReference
			└─ AcadMInsertBlock
"""	
class AcadMInsertBlock(AcadBlockReference, POINTER(_dll.IAcadMInsertBlock)):
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
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# ConvertToAnonymousBlock - without changes
	# ConvertToStaticBlock(newBlockName<String>)
	# Copy - from parent
	# Delete - without changes
	# Explode - from parent
	# GetAttributes - from parent
	# GetBoundingBox - from parent
	# GetConstantAttributes - from parent
	# GetDynamicBlockProperties - from parent
	# GetExtensionDictionary - from parent
	# GetXData - from parent
	# Highlight<bool> - without changes
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	# ResetBlock - without changes
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes
	
	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# Columns<Long> - without changes
	# ColumnSpacing<Double> - without changes
	# EffectiveName<String> - without changes
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasAttributes<bool>- without changes
	# HasExtensionDictionary<bool>- without changes
	# Hyperlinks - from parent
	# InsertionPoint - from parent
	# InsUnits<String> - without changes
	# InsUnitsFactor<Double> - without changes
	# IsDynamicBlock<Boolean> - without changes
	# Layer<String> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Name<String> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	plotstylename = COM_Property("PlotStyleName", str)
	rotation = COM_Property("Rotation", float)
	# Rows<Long> - without changes
	# RowSpacing<Double> - without changes
	# TrueColor<bool> - without changes
	# Visible<bool> - without changes
	# XEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# XScaleFactor<Double>  - without changes
	# YEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# YScaleFactor<Double>  - without changes
	# ZEffectiveScaleFactor<ACAD_NOUNITS>  - without changes
	# ZScaleFactor<Double>  - without changes
	
	
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
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes
	# GetBoundingBox - from parent
	# GetExtensionDictionary - from parent
	# GetXData - from parent
	# Highlight<bool> - without changes
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes
	
	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# Area<Double> - without changes
	@property
	def center(self):
		return A3Vertex(super().Center)
	@center.setter
	def center(self, value: A3Vertex):
		super().Center = value
	# Circumference<Double> - without changes
	# Diameter - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	@property
	def normal(self):
		return A3Vertex(super().Normal)
	@normal.setter
	def normal(self, value: A3Vertex):
		super().Normal = value
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	plotstylename = COM_Property("PlotStyleName", str)
	# Radius<Double> - without changes
	thickness = COM_Property("Thickness", float)
	# TrueColor<bool> - without changes
	# Visible<bool> - without changes
	

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadEllipse
"""
def AcadEllipse(POINTER(_dll.IAcadEllipse), AcadEntity):
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
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes
	# GetBoundingBox - from parent
	# GetExtensionDictionary - from parent
	# GetXData - from parent
	# Highlight<bool> - without changes
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	def offset(self, Distance: float):
		obj = _recast(super().Offset(Distance))
		obj.connect_to_sink(self.sink)
		return obj
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes

	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# Area<Double> - without changes
	@property
	def center(self):
		return A3Vertex(super().Center)
	@center.setter
	def center(self, value: A3Vertex):
		super().Center = value
	# Document<AcadDocument> - from parent
	# EndAngle<Double> - without changes
	# EndParameter<Double> - without changes
	@property
	def endpoint(self):
		return A3Vertex(super().EndPoint)
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Length<float>  - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	@property
	def majoraxis(self):
		return A3Vertex(super().MajorAxis)
	@majoraxis.setter
	def majoraxis(self, value: A3Vertex):
		super().MajorAxis = value
	major_axis = majoraxis
	# MajorRadius<Double> - without changes
	# Material<String> - without changes
	@property
	def minoraxis(self):
		return A3Vertex(super().MinorAxis)
	@minoraxis.setter
	def minoraxis(self, value: A3Vertex):
		super().MinorAxis = value
	minor_axis = minoraxis
	# MinorRadius<Double> - without changes
	@property
	def normal(self):
		return A3Vertex(super().Normal)
	@normal.setter
	def normal(self, value: A3Vertex):
		super().Normal = value
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	plotstylename = COM_Property("PlotStyleName", str)
	# RadiusRatio<Double> - without changes
	# StartAngle<Double> - without changes
	# StartParameter<Double> - without changes
	@property
	def startpoint(self):
		return A3Vertex(super().StartPoint)
	# TrueColor<bool> - without changes
	# Visible<bool> - without changes


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
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes
	# Evaluate - without changes
	# GetBoundingBox - from parent
	# GetExtensionDictionary - from parent
	def getloopat(self, Index: int, Loop: list=list()): # ToDo: need test
		super().GetLoopAt(Index, Loop)
		return Loop
	get_loop_at = getloopat
	# GetXData - from parent
	# Highlight<bool> - without changes
	def insertloopat(self, Index: int, LoopType: int, Loop: list):
		for obj in Loop:
			if not isinstance(obj, (AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline)):
				raise TypeError("[AcadHatch.AppendOuterLoop] Object must be on of the types: AcadArc, AcadCircle, AcadEllipse, AcadLine, AcadPolyline, AcadRegion, AcadSpline")
		super().InsertLoopAt(Index, LoopType, Loop)
	insert_loop_at = insertloopat
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetPattern(< AcPatternType enum>, <String>) - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes
	
	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# Area<Double> - without changes
	# AssociativeHatch<Boolean> - without changes
	@property
	def backgroundcolor(self):
		return _recast(super().BackgroundColor)
	@backgroundcolor.setter
	def backgroundcolor(self, value: AcCmColor):
		super().BackgroundColor = AcCmColor
	background_color = backgroundcolor
	# Document<AcadDocument> - from parent
	# Elevation<Double> - without changes
	# EntityTransparency<String> - from parent
	# GradientAngle<ACAD_ANGLE> - without changes
	# GradientCentered<Boolean> - without changes
	@property
	def gradientcolor1(self):
		return _recast(super().GradientColor1)
	@gradientcolor1.setter
	def gradientcolor1(self, value: AcCmColor):
		super().GradientColor1 = AcCmColor
	gradient_color1 = gradientcolor1
	@property
	def gradientcolor2(self):
		return _recast(super().GradientColor2)
	@gradientcolor2.setter
	def gradientcolor2(self, value: AcCmColor):
		super().GradientColor2 = AcCmColor
	gradient_color2 = gradientcolor2
	# GradientName<String> - without changes
		# "Linear"
		# "Cylinder"
		# "InvCylinder"
		# "Spherical"
		# "HemiSpherical"
		# "Curved"
		# "InvSpherical"
		# "InvHemiSpherical"
		# "InvCurved"
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HatchObjectType<AcHatchObjectType enum> - without changes
	# HatchStyle<acHatchStyle enum> - without changes
	# Hyperlinks - from parent
	# ISOPenWidth<acISOPenWidth enum> - without changes
	# Layer<String> - without changes
	# Length<float>  - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	@property
	def normal(self):
		return A3Vertex(super().Normal)
	@normal.setter
	def normal(self, value: A3Vertex):
		super().Normal = value
	# NumberOfLoops<Integer> - without changes
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	@property
	def origin(self):
		return A3Vertex(super().Origin)
	@origin.setter
	def origin(self, value: A3Vertex):
		super().Origin = value
	# OwnerID<Long_Ptr> - without changes. Alias from parent

	# PatternAngle<Double> - without changes
	# PatternDouble<Boolean> - without changes
	# PatternName<String> - without changes
	# PatternScale<Double> - without changes
	# PatternSpace<Double> - without changes
	# PatternType<acPatternType enum> - without changes
	plotstylename = COM_Property("PlotStyleName", str)
	# TrueColor<bool> - without changes
	# Visible<bool> - without changes
	
	
	
	
	
	
	
	

