#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api import acad_dll as _dll
from .object import AcadEntity, A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
from .util import arr_check, recast as _recast, uncast as _uncast, dict_fix, get_obj_block_source
from multimethod import overload
import math

"""
Dimension objects
"""

"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
"""
class AcadDimension(POINTER(_dll.IAcadDimension), AcadEntity):
	def __new__(self, *args, **kw):
		raise TypeError("""You can't create {0}. Use {0}.%type%. Allowed types:
		++Dim3PointAngular(...), ++DimAligned(...) ++DimAngular(...), DimArc(...), DimDiametric(...), DimOrdinate(...), DimRadial(...), DimRadialLarge(...), DimRotated(...)""".format(cls))
	# ToDo: Add classmethods for creating ^^^
	@classmethod
	def Point3Angular(cls, AngleVertex: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, TextPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDim3PointAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint, source)
	@classmethod
	def Aligned(cls, ExtLine1Point: A3Vertex, ExtLine2Point: A3Vertex, TextPosition: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimAligned(ExtLine1Point, ExtLine2Point, TextPosition, source)
	@classmethod
	def Angular(cls, AngleVertex: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, TextPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint, source)
	@classmethod
	def Arc(cls, ArcCenter: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, ArcPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimArcLength(ArcCenter, FirstEndPoint, ArcPoint, TextPoint, source)
	@classmethod
	def Diametric(cls, ChordPoint: A3Vertex, FarChordPoint: A3Vertex, LeaderLength: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimDiametric(ChordPoint, FarChordPoint, LeaderLength, source)
	@classmethod
	def Ordinate(cls, DefinitionPoint: A3Vertex, LeaderEndPoint: A3Vertex, UseXAxis: bool, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimOrdinate(DefinitionPoint, LeaderEndPoint, UseXAxis, source)
	@classmethod
	def Radial(cls, Center: A3Vertex, ChordPoint: A3Vertex, LeaderLength: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimAngular(Center, ChordPoint, LeaderLength, source)
	@classmethod
	def RadialLarge(cls, Center: A3Vertex, ChordPoint: A3Vertex, OverrideCenter: A3Vertex, JogPoint: A3Vertex, JogAngle: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		return AcadDimRadialLarge(Center, ChordPoint, OverrideCenter, JogPoint, JogAngle, source)
	
	# VBA-methods with recasting
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes# GetBoundingBox - from parent
	# GetBoundingBox - from parent
	# GetExtensionDictionary - from parent
	# GetXData - from parent
	# Highlight<bool> - without changes
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes
	
	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# DecimalSeparator<String> - without changes
	# DimTxtDirection<Boolean> - without changes
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
	# PlotStyleName<String> - without changes
	# Rotation<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	@property
	def textoverride(self):
		return super().TextOverride
	@textoverride.setter
	def textoverride(self, value: str):
		super().TextOverride = value if len(value) <= 256 else value[:256]
	text_override = textoverride
	@property
	def textposition(self):
		return A3Vertex(super().TextPosition)
	@textposition.setter
	def textposition(self, value: A3Vertex):
		super().TextPosition = value
	text_position = textposition
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDim3PointAngular
"""
class AcadDim3PointAngular(POINTER(_dll.IAcadDim3PointAngular), AcadDimension):
	def __new__(cls, AngleVertex: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, TextPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"AngleVertex": AngleVertex,
			"FirstEndPoint": FirstEndPoint,
			"SecondEndPoint": SecondEndPoint,
			"TextPoint": TextPoint
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDim3PointAngular(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AngleFormat<acAngleUnits enum> - without changes
	@property
	def anglevertex(self):
		return A3Vertex(super().AngleVertex)
	@anglevertex.setter
	def anglevertex(self, value: A3Vertex):
		super().AngleVertex = value
	angle_vertex = anglevertex
	# Application<AcadApplication> - from parent
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowSize<Long> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimLineInside<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineExtend<Boolean> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	@property
	def extline1endpoint(self):
		return A3Vertex(super().ExtLine1EndPoint)
	@extline1endpoint.setter
	def extline1endpoint(self, value: A3Vertex):
		super().ExtLine1EndPoint = value
	extline_1_endpoint = extline1endpoint
	# ExtLine1Linetype<String> - without changes
	# ExtLine1Suppress<Boolean> - without changes
	@property
	def extline2endpoint(self):
		return A3Vertex(super().ExtLine2EndPoint)
	@extline2endpoint.setter
	def extline2endpoint(self, value: A3Vertex):
		super().ExtLine2EndPoint = value
	extline_2_endpoint = extline2endpoint
	# ExtLine2Linetype<String> - without changes
	# ExtLine2Suppress<Boolean> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HorizontalTextPosition<acDimHorizontalJustification enum> - without changes
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# Rotation<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrecision<acDimPrecision enum> - without changes
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimAligned
"""
class AcadDimAligned(POINTER(_dll.IAcadDimAligned), AcadDimension):
	def __new__(cls, ExtLine1Point: A3Vertex, ExtLine2Point: A3Vertex, TextPosition: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"ExtLine1Point": ExtLine1Point,
			"ExtLine2Point": ExtLine2Point,
			"TextPosition": TextPosition
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimAligned(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSubUnitsFactor<Double> - without changes
	# AltSubUnitsSuffix<String> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowheadSize<Double> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLineExtend<Double> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimLineInside<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineExtend<Boolean> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	# ExtLine1Linetype<String> - without changes
	@property
	def extline1point(self):
		return A3Vertex(super().ExtLine1Point)
	@extline1point.setter
	def extline1point(self, value: A3Vertex):
		super().ExtLine1Point = value
	extline_1_point = extline1point
	# ExtLine1Suppress<Boolean> - without changes
	# ExtLine2Linetype<String> - without changes
	@property
	def extline2point(self):
		return A3Vertex(super().ExtLine2Point)
	@extline2point.setter
	def extline2point(self, value: A3Vertex):
		super().ExtLine2Point = value
	extline_2_point = extline2point
	# ExtLine2Suppress<Boolean> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HorizontalTextPosition<acDimHorizontalJustification enum> - without changes
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SubUnitsFactor<Double> - without changes
	# SubUnitsSuffix<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimAngular
"""
class AcadDimAngular(POINTER(_dll.IAcadDimAngular), AcadDimension):
	def __new__(cls, AngleVertex: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, TextPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"AngleVertex": AngleVertex,
			"FirstEndPoint": FirstEndPoint,
			"SecondEndPoint": SecondEndPoint,
			"TextPoint": TextPoint
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimAngular(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AngleFormat<acAngleUnits enum> - without changes
	# Application<AcadApplication> - from parent
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowheadSize<Double> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimLineInside<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineExtend<Boolean> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	@property
	def extline1endpoint(self):
		return A3Vertex(super().ExtLine1EndPoint)
	@extline1endpoint.setter
	def extline1endpoint(self, value: A3Vertex):
		super().ExtLine1EndPoint = value
	extline_1_endpoint = extline1endpoint
	# ExtLine1Linetype<String> - without changes
	@property
	def extline1startpoint(self):
		return A3Vertex(super().ExtLine1StartPoint)
	@extline1startpoint.setter
	def extline1startpoint(self, value: A3Vertex):
		super().ExtLine1StartPoint = value
	extline_1_startpoint = extline1startpoint
	# ExtLine1Suppress<Boolean> - without changes
	@property
	def extline2endpoint(self):
		return A3Vertex(super().ExtLine2EndPoint)
	@extline2endpoint.setter
	def extline2endpoint(self, value: A3Vertex):
		super().ExtLine2EndPoint = value
	extline_2_endpoint = extline2endpoint
	# ExtLine2Linetype<String> - without changes
	@property
	def extline2startpoint(self):
		return A3Vertex(super().ExtLine2StartPoint)
	@extline2startpoint.setter
	def extline2startpoint(self, value: A3Vertex):
		super().ExtLine2StartPoint = value
	extline_2_startpoint = extline2startpoint
	# ExtLine2Suppress<Boolean> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HorizontalTextPosition<acDimHorizontalJustification enum> - without changes
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# Rotation<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrecision<acDimPrecision enum> - without changes
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimArcLength
"""
class AcadDimArcLength(POINTER(_dll.IAcadDimArcLength), AcadDimension):
	def __new__(cls, ArcCenter: A3Vertex, FirstEndPoint: A3Vertex, SecondEndPoint: A3Vertex, ArcPoint: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"ArcCenter": ArcCenter,
			"FirstEndPoint": FirstEndPoint,
			"SecondEndPoint": SecondEndPoint,
			"ArcPoint": ArcPoint
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimArc(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSubUnitsFactor<Double> - without changes
	# AltSubUnitsSuffix<String> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# ArcEndParam<Double> - without changes
	@property
	def arcpoint(self):
		return A3Vertex(super().ArcPoint)
	@arcpoint.setter
	def arcpoint(self, value: A3Vertex):
		super().ArcPoint = value
	arc_point = arcpoint
	# ArcStartParam<Double> - without changes
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowheadSize<Double> - without changes
	@property
	def centerpoint(self):
		return A3Vertex(super().CenterPoint)
	@centerpoint.setter
	def centerpoint(self, value: A3Vertex):
		super().CenterPoint = value
	center_point = centerpoint
	# DecimalSeparator<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLineExtend<Double> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimLineInside<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineExtend<Boolean> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	# ExtLine1Linetype<String> - without changes
	@property
	def extline1point(self):
		return A3Vertex(super().ExtLine1Point)
	@extline1point.setter
	def extline1point(self, value: A3Vertex):
		super().ExtLine1Point = value
	extline_1_point = extline1point
	# ExtLine1Suppress<Boolean> - without changes
	# ExtLine2Linetype<String> - without changes
	@property
	def extline2point(self):
		return A3Vertex(super().ExtLine2Point)
	@extline2point.setter
	def extline2point(self, value: A3Vertex):
		super().ExtLine2Point = value
	extline_2_point = extline2point
	# ExtLine2Suppress<Boolean> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HasLeader<Boolean> - without changes
	# HorizontalTextPosition<acDimHorizontalJustification enum> - without changes
	# Hyperlinks - from parent
	# IsPartial<Boolean> - without changes
	# Layer<String> - without changes
	@property
	def leader1point(self):
		return A3Vertex(super().Leader1Point)
	@leader1point.setter
	def leader1point(self, value: A3Vertex):
		super().Leader1Point = value
	leader_1_point = leader1point
	@property
	def leader2point(self):
		return A3Vertex(super().Leader2Point)
	@leader2point.setter
	def leader2point(self, value: A3Vertex):
		super().Leader2Point = value
	leader_2_point = leader2point
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SubUnitsFactor<Double> - without changes
	# SubUnitsSuffix<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# SymbolPosition<AcDimArcLengthSymbol enum> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimDiametric
"""
class AcadDimDiametric(POINTER(_dll.IAcadDimDiametric), AcadDimension):
	def __new__(cls, ChordPoint: A3Vertex, FarChordPoint: A3Vertex, LeaderLength: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"ChordPoint": ChordPoint,
			"FarChordPoint": FarChordPoint,
			"LeaderLength": LeaderLength
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimDiametric(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowheadSize<Double> - without changes
	# CenterMarkSize<Double> - without changes
	# CenterType<acDimCenterType enum> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# LeaderLength<Double> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimOrdinate
"""
class AcadDimOrdinate(POINTER(_dll.IAcadDimOrdinate), AcadDimension):
	def __new__(cls, DefinitionPoint: A3Vertex, LeaderEndPoint: A3Vertex, UseXAxis: bool, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"DefinitionPoint": DefinitionPoint,
			"LeaderEndPoint": LeaderEndPoint,
			"UseXAxis": int(UseXAxis)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimOrdinate(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSubUnitsFactor<Double> - without changes
	# AltSubUnitsSuffix<String> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# ArrowheadSize<Double> - without changes
	# DecimalSeparator<String> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - from parent
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SubUnitsFactor<Double> - without changes
	# SubUnitsSuffix<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimRadial
"""
class AcadDimRadial(POINTER(_dll.IAcadDimRadial), AcadDimension):
	def __new__(cls, Center: A3Vertex, ChordPoint: A3Vertex, LeaderLength: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"ChordPoint": ChordPoint,
			"LeaderLength": LeaderLength
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimRadial(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# ArrowheadBlock<String> - without changes
	# ArrowheadSize<Double> - without changes
	# ArrowheadType<acDimArrowheadType enum> - without changes
	# CenterMarkSize<Double> - without changes
	# CenterType<acDimCenterType enum> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLineSuppress<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# LeaderLength<Double> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimRadialLarge
"""
class AcadDimRadialLarge(POINTER(_dll.IAcadDimRadialLarge), AcadDimension):
	def __new__(cls, Center: A3Vertex, ChordPoint: A3Vertex, OverrideCenter: A3Vertex, JogPoint: A3Vertex, JogAngle: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"ChordPoint": ChordPoint,
			"OverrideCenter": OverrideCenter,
			"JogPoint": JogPoint,
			"JogAngle": JogAngle
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimRadialLarge(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# ArrowheadBlock<String> - without changes
	# ArrowheadSize<Double> - without changes
	# ArrowheadType<acDimArrowheadType enum> - without changes
	@property
	def center(self):
		return A3Vertex(super().Center)
	@center.setter
	def center(self, value: A3Vertex):
		super().Center = value
	# CenterMarkSize<Double> - without changes
	# CenterType<acDimCenterType enum> - without changes
	@property
	def chordpoint(self):
		return A3Vertex(super().ChordPoint)
	@chordpoint.setter
	def chordpoint(self, value: A3Vertex):
		super().ChordPoint = value
	chord_point = chordpoint
	# DecimalSeparator<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLineSuppress<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# JogAngle<ACAD_ANGLE> - without changes
	@property
	def joglocation(self):
		return A3Vertex(super().JogLocation)
	@joglocation.setter
	def joglocation(self, value: A3Vertex):
		super().JogLocation = value
	jog_location = joglocation
	# Layer<String> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	@property
	def overridecenter(self):
		return A3Vertex(super().OverrideCenter)
	@overridecenter.setter
	def overridecenter(self, value: A3Vertex):
		super().OverrideCenter = value
	override_center = overridecenter
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
	
	
"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ AcadDimension
			└─ AcadDimRotated
"""
class AcadDimRotated(POINTER(_dll.IAcadDimRotated), AcadDimension):
	def __new__(cls, XLine1Point: A3Vertex, XLine2Point: A3Vertex, DimLineLocation: A3Vertex, RotationAngle: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"XLine1Point": XLine1Point,
			"XLine2Point": XLine2Point,
			"DimLineLocation": DimLineLocation,
			"RotationAngle": RotationAngle
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddDimRotated(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	# VBA-methods with recasting
	# ALL FROM PARENT
	
	# VBA-properties with recasting
	# AltRoundDistance<Double> - without changes
	# AltSubUnitsFactor<Double> - without changes
	# AltSubUnitsSuffix<String> - without changes
	# AltSuppressLeadingZeros<Boolean> - without changes
	# AltSuppressTrailingZeros<Boolean> - without changes
	# AltSuppressZeroFeet<Boolean> - without changes
	# AltSuppressZeroInches<Boolean> - without changes
	# AltTextPrefix<String> - without changes
	# AltTextSuffix<String> - without changes
	# AltTolerancePrecision<acDimPrecision enum> - without changes
	# AltToleranceSuppressLeadingZeros<Boolean> - without changes
	# AltToleranceSuppressTrailingZeros<Boolean> - without changes
	# AltToleranceSuppressZeroFeet<Boolean> - without changes
	# AltToleranceSuppressZeroInches<Boolean> - without changes
	# AltUnits<Boolean> - without changes
	# AltUnitsFormat<acDimUnits enum> - without changes
	# AltUnitsPrecision<acDimPrecision enum> - without changes
	# AltUnitsScale<Double> - without changes
	# Application<AcadApplication> - from parent
	# Arrowhead1Block<String> - without changes
	# Arrowhead1Type<acDimArrowheadType enum> - without changes
	# Arrowhead2Block<String> - without changes
	# Arrowhead2Type<acDimArrowheadType enum> - without changes
	# ArrowheadSize<Double> - without changes
	# DecimalSeparator<String> - without changes
	# DimConstrDesc<String> - without changes
	# DimConstrExpression<String> - without changes
	# DimConstrForm<Boolean> - without changes
	# DimConstrName<String> - without changes
	# DimConstrReference<Boolean> - without changes
	# DimConstrValue<String> - without changes
	# DimensionLineColor<acColor enum> - without changes
	# DimensionLineExtend<Double> - without changes
	# DimensionLinetype<String> - without changes
	# DimensionLineWeight<acLineWeight enum> - without changes
	# DimLine1Suppress<Boolean> - without changes
	# DimLine2Suppress<Boolean> - without changes
	# DimLineInside<Boolean> - without changes
	# DimTxtDirection<Boolean> - without changes
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - without changes
	# ExtensionLineColor<acColor enum> - without changes
	# ExtensionLineExtend<Boolean> - without changes
	# ExtensionLineOffset<Double> - without changes
	# ExtensionLineWeight<acLineWeight enum> - without changes
	# ExtLine1Linetype<String> - without changes
	# ExtLine1Suppress<Boolean> - without changes
	# ExtLine2Linetype<String> - without changes
	# ExtLine2Suppress<Boolean> - without changes
	# ExtLineFixedLen<Double> - without changes
	# ExtLineFixedLenSuppress<Boolean> - without changes
	# Fit<acDimFit enum> - without changes
	# ForceLineInside<Boolean> - without changes
	# FractionFormat<acDimFractionType enum> - without changes
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# HorizontalTextPosition<acDimHorizontalJustification enum> - without changes
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# LinearScaleFactor<Double> - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# Measurement<Double> - without changes
	# Normal - from parent
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# PrimaryUnitsPrecision<acDimPrecision enum> - without changes
	# Rotation<Double> - without changes
	# RoundDistance<Double> - without changes
	# ScaleFactor<Double> - without changes
	# StyleName<String> - without changes
	# SubUnitsFactor<Double> - without changes
	# SubUnitsSuffix<String> - without changes
	# SuppressLeadingZeros<Boolean> - without changes
	# SuppressTrailingZeros<Boolean> - without changes
	# SuppressZeroFeet<Boolean> - without changes
	# SuppressZeroInches<Boolean> - without changes
	# TextColor<acColor enum> - without changes
	# TextFill<Boolean> - without changes
	# TextFillColor<ACAD_COLOR> - without changes
	# TextGap<Double> - without changes
	# TextHeight<Double> - without changes
	# TextInside<Boolean> - without changes
	# TextInsideAlign<Boolean> - without changes
	# TextMovement<acDimTextMovement enum> - without changes
	# TextOutsideAlign<Boolean> - without changes
	# TextOverride<String> - from parent
	# TextPosition<A3Vertex> - from parent
	# TextPrefix<String> - without changes
	# TextRotation<Double> - without changes
	# TextStyle<String> - without changes
	# TextSuffix<String> - without changes
	# ToleranceDisplay<acDimToleranceMethod enum> - without changes
	# ToleranceHeightScale<Double> - without changes
	# ToleranceJustification<acDimToleranceJustify enum> - without changes
	# ToleranceLowerLimit<Double> - without changes
	# TolerancePrecision<acDimPrecision enum> - without changes
	# ToleranceSuppressLeadingZeros<Boolean> - without changes
	# ToleranceSuppressTrailingZeros<Boolean> - without changes
	# ToleranceSuppressZeroFeet<Boolean> - without changes
	# ToleranceSuppressZeroInches<Boolean> - without changes
	# ToleranceUpperLimit<Double> - without changes
	# TrueColor<bool> - without changes
	# UnitsFormat<acDimLUnits enum> - without changes
	# VerticalTextPosition<acDimVerticalJustification enum> - without changes
	# Visible<bool> - without changes
