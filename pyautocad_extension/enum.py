#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Some enums ported from AutoCAD VBA. Based on AutoCAD 2018

import enum

class AcSaveAsType(enum.Enum):
	ac2000_dwg = 12
	ac2000_dxf = 13
	ac2000_Template = 14
	ac2004_dwg = 24
	ac2004_dxf = 25
	ac2004_Template = 26
	ac2007_dwg = 36
	ac2007_dxf = 37
	ac2007_Template = 38
	ac2010_dwg = 48
	ac2010_dxf = 49
	ac2010_Template = 50
	ac2013_dwg = 60
	ac2013_dxf = 61
	ac2013_Template = 62
	ac2018_dwg = 64
	ac2018_dxf = 65
	ac2018_Template = 66
	acR12_dxf = 1
	acR13_dwg = 4
	acR13_dxf = 5
	acR14_dwg = 8
	acR14_dxf = 9
	acR15_dwg = 12
	acR15_dxf = 13
	acR15_Template = 14
	acR18_dwg = 24
	acR18_dxf = 25
	acR18_Template=26
	acUnknown = -1 #0xFFFFFFFF
	acNative = 64 #For AutoCAD 2018; ToDo: add support cross-version. Or just omit this parameter in SaveAs()
	
	
	

"""
TODO:

Ac3DPolylineType
AcActiveSpace
ACAD_COLOR
ACAD_LWEIGHT
-----------
AcadSecurityParamsConstants
AcadSecurityParamsType
-----------
AcAlignment
AcAlignmentPointAcquisition
AcAngleUnits
AcARXDemandLoad
AcAttachmentPoint
AcAttributeMode
AcBlockConnectionType
AcBlockScaling
AcBoolean
AcBooleanType
AcCellAlignment
AcCellContentLayout
AcCellContentType
AcCellEdgeMask
AcCellMargin
AcCellOption
AcCellProperty
AcCellState
AcCellType
AcColor
AcColorMethod
AcCoordinateSystem
AcDataLinkUpdateDirection
AcDataLinkUpdateOption
AcDimArcLengthSymbol
AcDimArrowheadType
AcDimCenterType
AcDimFit
AcDimFractionType
AcDimHorizontalJustification
AcDimLUnits
AcDimPrecision
AcDimTextMovement
AcDimToleranceJustify
AcDimToleranceMethod
AcDimUnits
AcDimVerticalJustification
AcDragDisplayMode
AcDrawingAreaSCMCommand
AcDrawingAreaSCMDefault
AcDrawingAreaSCMEdit
AcDrawingAreaShortCutMenu
AcDrawingDirection
AcDrawLeaderOrderType
AcDrawMLeaderOrderType
AcDynamicBlockReferencePropertyUnitsType
AcEntityName
AcExtendOption
AcFormatOption
AcGradientPatternType
AcGridLineStyle
AcGridLineType
AcHatchObjectType
AcHatchStyle
AcHelixConstrainType
AcHelixTwistType
AcHorizontalAlignment
AcInsertUnits
AcInsertUnitsAction
AcISOPenWidth
AcKeyboardAccelerator
AcKeyboardPriority
AcLayerStateMask
AcLeaderType
AcLineSpacingStyle
AcLineWeight
AcLoadPalette
AcLoftedSurfaceNormalType
AcLoopType
AcMeasurementUnits
AcMenuFileType
AcMenuGroupType
AcMenuItemType
AcMergeCellStyleOption
AcMeshCreaseType
AcMLeaderContentType
AcMLeaderType
AcMLineJustification
AcOlePlotQuality
AcOleQuality
AcOleType
AcOnOff
AcParseOption
AcPatternType
AcPlotOrientation
AcPlotPaperUnits
AcPlotPolicy
AcPlotPolicyForLegacyDwgs
AcPlotPolicyForNewDwgs
AcPlotRotation
AcPlotScale
AcPlotType
AcPointCloudColorType
AcPointCloudExStylizationType
AcPointCloudIntensityStyle
AcPointCloudStylizationType
AcPolylineType
AcPolymeshType
AcPredefBlockType
AcPreviewMode
AcPrinterSpoolAlert
AcProxyImage
AcRegenType
AcRotationAngle
AcRowType

AcSectionGeneration
AcSectionState
AcSectionState2
AcSectionSubItem
AcSectionType
AcSegmentAngleType
AcSelect
AcSelectType
AcShadePlot
AcShadowDisplayType
AcSplineFrameType
AcSplineKnotParameterizationType
AcSplineMethodType
AcTableDirection
AcTableFlowDirection
AcTableStyleOverrides
AcTextAlignmentType
AcTextAngleType
AcTextAttachmentDirection
AcTextAttachmentType
AcTextFontStyle
AcTextGenerationFlag
AcToolbarDockStatus
AcToolbarItemType
AcUnderlayLayerOverrideType
AcUnits
AcValueDataType
AcValueUnitType
AcVerticalAlignment
AcVerticalTextAttachmentType
AcViewportScale
AcViewportSplitType
AcWindowState
AcWireframeType
AcXRefDemandLoad
AcZoomScaleType
"""