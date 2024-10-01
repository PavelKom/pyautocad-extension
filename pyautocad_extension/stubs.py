from comtypes import POINTER
from utils import _ez_ptr, CastManager
from api import acad_dll
_dll = acad_dll.dll

class Acad3DFace(POINTER(_dll.IAcad3DFace), _ez_ptr):
	pass

class Acad3DPolyline(POINTER(_dll.IAcad3DPolyline), _ez_ptr):
	pass

class Acad3DSolid(POINTER(_dll.IAcad3DSolid), _ez_ptr):
	pass

class AcadAcCmColor(POINTER(_dll.IAcadAcCmColor), _ez_ptr):
	pass

class AcadApplication(POINTER(_dll.IAcadApplication), _ez_ptr):
	pass

class AcadArc(POINTER(_dll.IAcadArc), _ez_ptr):
	pass

class AcadAttribute(POINTER(_dll.IAcadAttribute), _ez_ptr):
	pass

class AcadAttributeReference(POINTER(_dll.IAcadAttributeReference), _ez_ptr):
	pass

class AcadBlock(POINTER(_dll.IAcadBlock), _ez_ptr):
	pass

class AcadBlockReference(POINTER(_dll.IAcadBlockReference), _ez_ptr):
	pass

class AcadBlocks(POINTER(_dll.IAcadBlocks), _ez_ptr):
	pass

class AcadCircle(POINTER(_dll.IAcadCircle), _ez_ptr):
	pass

class AcadDatabase(POINTER(_dll.IAcadDatabase), _ez_ptr):
	pass

class AcadDatabasePreferences(POINTER(_dll.IAcadDatabasePreferences), _ez_ptr):
	pass

class AcadDictionaries(POINTER(_dll.IAcadDictionaries), _ez_ptr):
	pass

class AcadDictionary(POINTER(_dll.IAcadDictionary), _ez_ptr):
	pass

class AcadDim3PointAngular(POINTER(_dll.IAcadDim3PointAngular), _ez_ptr):
	pass

class AcadDimAligned(POINTER(_dll.IAcadDimAligned), _ez_ptr):
	pass

class AcadDimAngular(POINTER(_dll.IAcadDimAngular), _ez_ptr):
	pass

class AcadDimArcLength(POINTER(_dll.IAcadDimArcLength), _ez_ptr):
	pass

class AcadDimDiametric(POINTER(_dll.IAcadDimDiametric), _ez_ptr):
	pass

class AcadDimOrdinate(POINTER(_dll.IAcadDimOrdinate), _ez_ptr):
	pass

class AcadDimRadial(POINTER(_dll.IAcadDimRadial), _ez_ptr):
	pass

class AcadDimRadialLarge(POINTER(_dll.IAcadDimRadialLarge), _ez_ptr):
	pass

class AcadDimRotated(POINTER(_dll.IAcadDimRotated), _ez_ptr):
	pass

class AcadDimStyle(POINTER(_dll.IAcadDimStyle), _ez_ptr):
	pass

class AcadDimStyles(POINTER(_dll.IAcadDimStyles), _ez_ptr):
	pass

class AcadDimension(POINTER(_dll.IAcadDimension), _ez_ptr):
	pass

class AcadDocument(POINTER(_dll.IAcadDocument), _ez_ptr):
	pass

class AcadDocuments(POINTER(_dll.IAcadDocuments), _ez_ptr):
	pass

class AcadDwfUnderlay(POINTER(_dll.IAcadDwfUnderlay), _ez_ptr):
	pass

class AcadDynamicBlockReferenceProperty(POINTER(_dll.IAcadDynamicBlockReferenceProperty), _ez_ptr):
	pass

class AcadEllipse(POINTER(_dll.IAcadEllipse), _ez_ptr):
	pass

class AcadEntity(POINTER(_dll.IAcadEntity), _ez_ptr):
	pass

class AcadExternalReference(POINTER(_dll.IAcadExternalReference), _ez_ptr):
	pass

class AcadExternalReference2(POINTER(_dll.IAcadExternalReference2), _ez_ptr):
	pass

class AcadExtrudedSurface(POINTER(_dll.IAcadExtrudedSurface), _ez_ptr):
	pass

class AcadGeoPositionMarker(POINTER(_dll.IAcadGeoPositionMarker), _ez_ptr):
	pass

class AcadGeomapImage(POINTER(_dll.IAcadGeomapImage), _ez_ptr):
	pass

class AcadGroup(POINTER(_dll.IAcadGroup), _ez_ptr):
	pass

class AcadGroups(POINTER(_dll.IAcadGroups), _ez_ptr):
	pass

class AcadHatch(POINTER(_dll.IAcadHatch), _ez_ptr):
	pass

class AcadHelix(POINTER(_dll.IAcadHelix), _ez_ptr):
	pass

class AcadHyperlink(POINTER(_dll.IAcadHyperlink), _ez_ptr):
	pass

class AcadHyperlinks(POINTER(_dll.IAcadHyperlinks), _ez_ptr):
	pass

class AcadIdPair(POINTER(_dll.IAcadIdPair), _ez_ptr):
	pass

class AcadLWPolyline(POINTER(_dll.IAcadLWPolyline), _ez_ptr):
	pass

class AcadLayer(POINTER(_dll.IAcadLayer), _ez_ptr):
	pass

class AcadLayerStateManager(POINTER(_dll.IAcadLayerStateManager), _ez_ptr):
	pass

class AcadLayers(POINTER(_dll.IAcadLayers), _ez_ptr):
	pass

class AcadLayout(POINTER(_dll.IAcadLayout), _ez_ptr):
	pass

class AcadLayouts(POINTER(_dll.IAcadLayouts), _ez_ptr):
	pass

class AcadLeader(POINTER(_dll.IAcadLeader), _ez_ptr):
	pass

class AcadLine(POINTER(_dll.IAcadLine), _ez_ptr):
	pass

class AcadLineType(POINTER(_dll.IAcadLineType), _ez_ptr):
	pass

class AcadLineTypes(POINTER(_dll.IAcadLineTypes), _ez_ptr):
	pass

class AcadLoftedSurface(POINTER(_dll.IAcadLoftedSurface), _ez_ptr):
	pass

class AcadMInsertBlock(POINTER(_dll.IAcadMInsertBlock), _ez_ptr):
	pass

class AcadMLeader(POINTER(_dll.IAcadMLeader), _ez_ptr):
	pass

class AcadMLeaderLeader(POINTER(_dll.IAcadMLeaderLeader), _ez_ptr):
	pass

class AcadMLeaderStyle(POINTER(_dll.IAcadMLeaderStyle), _ez_ptr):
	pass

class AcadMLine(POINTER(_dll.IAcadMLine), _ez_ptr):
	pass

class AcadMText(POINTER(_dll.IAcadMText), _ez_ptr):
	pass

class AcadMaterial(POINTER(_dll.IAcadMaterial), _ez_ptr):
	pass

class AcadMaterials(POINTER(_dll.IAcadMaterials), _ez_ptr):
	pass

class AcadMenuBar(POINTER(_dll.IAcadMenuBar), _ez_ptr):
	pass

class AcadMenuGroup(POINTER(_dll.IAcadMenuGroup), _ez_ptr):
	pass

class AcadMenuGroups(POINTER(_dll.IAcadMenuGroups), _ez_ptr):
	pass

class AcadNurbSurface(POINTER(_dll.IAcadNurbSurface), _ez_ptr):
	pass

class AcadObject(POINTER(_dll.IAcadObject), _ez_ptr):
	pass

class AcadObjectEvents(POINTER(_dll.IAcadObjectEvents), _ez_ptr):
	pass

class AcadOle(POINTER(_dll.IAcadOle), _ez_ptr):
	pass

class AcadPViewport(POINTER(_dll.IAcadPViewport), _ez_ptr):
	pass

class AcadPaperSpace(POINTER(_dll.IAcadPaperSpace), _ez_ptr):
	pass

class AcadPlot(POINTER(_dll.IAcadPlot), _ez_ptr):
	pass

class AcadPlotConfiguration(POINTER(_dll.IAcadPlotConfiguration), _ez_ptr):
	pass

class AcadPlotConfigurations(POINTER(_dll.IAcadPlotConfigurations), _ez_ptr):
	pass

class AcadPoint(POINTER(_dll.IAcadPoint), _ez_ptr):
	pass

class AcadPointCloud(POINTER(_dll.IAcadPointCloud), _ez_ptr):
	pass

class AcadPointCloudEx(POINTER(_dll.IAcadPointCloudEx), _ez_ptr):
	pass

class AcadPointCloudEx2(POINTER(_dll.IAcadPointCloudEx2), _ez_ptr):
	pass

class AcadPolyfaceMesh(POINTER(_dll.IAcadPolyfaceMesh), _ez_ptr):
	pass

class AcadPolygonMesh(POINTER(_dll.IAcadPolygonMesh), _ez_ptr):
	pass

class AcadPolyline(POINTER(_dll.IAcadPolyline), _ez_ptr):
	pass

class AcadPopupMenu(POINTER(_dll.IAcadPopupMenu), _ez_ptr):
	pass

class AcadPopupMenuItem(POINTER(_dll.IAcadPopupMenuItem), _ez_ptr):
	pass

class AcadPopupMenus(POINTER(_dll.IAcadPopupMenus), _ez_ptr):
	pass

class AcadPreferences(POINTER(_dll.IAcadPreferences), _ez_ptr):
	pass

class AcadPreferencesDisplay(POINTER(_dll.IAcadPreferencesDisplay), _ez_ptr):
	pass

class AcadPreferencesDrafting(POINTER(_dll.IAcadPreferencesDrafting), _ez_ptr):
	pass

class AcadPreferencesFiles(POINTER(_dll.IAcadPreferencesFiles), _ez_ptr):
	pass

class AcadPreferencesOpenSave(POINTER(_dll.IAcadPreferencesOpenSave), _ez_ptr):
	pass

class AcadPreferencesOutput(POINTER(_dll.IAcadPreferencesOutput), _ez_ptr):
	pass

class AcadPreferencesProfiles(POINTER(_dll.IAcadPreferencesProfiles), _ez_ptr):
	pass

class AcadPreferencesSelection(POINTER(_dll.IAcadPreferencesSelection), _ez_ptr):
	pass

class AcadPreferencesSystem(POINTER(_dll.IAcadPreferencesSystem), _ez_ptr):
	pass

class AcadPreferencesUser(POINTER(_dll.IAcadPreferencesUser), _ez_ptr):
	pass

class AcadRasterImage(POINTER(_dll.IAcadRasterImage), _ez_ptr):
	pass

class AcadRay(POINTER(_dll.IAcadRay), _ez_ptr):
	pass

class AcadRegion(POINTER(_dll.IAcadRegion), _ez_ptr):
	pass

class AcadRegisteredApplication(POINTER(_dll.IAcadRegisteredApplication), _ez_ptr):
	pass

class AcadRegisteredApplications(POINTER(_dll.IAcadRegisteredApplications), _ez_ptr):
	pass

class AcadRevolvedSurface(POINTER(_dll.IAcadRevolvedSurface), _ez_ptr):
	pass

class AcadSection(POINTER(_dll.IAcadSection), _ez_ptr):
	pass

class AcadSection2(POINTER(_dll.IAcadSection2), _ez_ptr):
	pass

class AcadSectionManager(POINTER(_dll.IAcadSectionManager), _ez_ptr):
	pass

class AcadSectionSettings(POINTER(_dll.IAcadSectionSettings), _ez_ptr):
	pass

class AcadSectionTypeSettings(POINTER(_dll.IAcadSectionTypeSettings), _ez_ptr):
	pass

class AcadSectionTypeSettings2(POINTER(_dll.IAcadSectionTypeSettings2), _ez_ptr):
	pass

class AcadSecurityParams(POINTER(_dll.IAcadSecurityParams), _ez_ptr):
	pass

class AcadSelectionSet(POINTER(_dll.IAcadSelectionSet), _ez_ptr):
	pass

class AcadSelectionSets(POINTER(_dll.IAcadSelectionSets), _ez_ptr):
	pass

class AcadShadowDisplay(POINTER(_dll.IAcadShadowDisplay), _ez_ptr):
	pass

class AcadShape(POINTER(_dll.IAcadShape), _ez_ptr):
	pass

class AcadSolid(POINTER(_dll.IAcadSolid), _ez_ptr):
	pass

class AcadSortentsTable(POINTER(_dll.IAcadSortentsTable), _ez_ptr):
	pass

class AcadSpline(POINTER(_dll.IAcadSpline), _ez_ptr):
	pass

class AcadState(POINTER(_dll.IAcadState), _ez_ptr):
	pass

class AcadSubDMesh(POINTER(_dll.IAcadSubDMesh), _ez_ptr):
	pass

class AcadSubDMeshEdge(POINTER(_dll.IAcadSubDMeshEdge), _ez_ptr):
	pass

class AcadSubDMeshFace(POINTER(_dll.IAcadSubDMeshFace), _ez_ptr):
	pass

class AcadSubDMeshVertex(POINTER(_dll.IAcadSubDMeshVertex), _ez_ptr):
	pass

class AcadSubEntSolidFace(POINTER(_dll.IAcadSubEntSolidFace), _ez_ptr):
	pass

class AcadSubEntity(POINTER(_dll.IAcadSubEntity), _ez_ptr):
	pass

class AcadSummaryInfo(POINTER(_dll.IAcadSummaryInfo), _ez_ptr):
	pass

class AcadSurface(POINTER(_dll.IAcadSurface), _ez_ptr):
	pass

class AcadSweptSurface(POINTER(_dll.IAcadSweptSurface), _ez_ptr):
	pass

class AcadTable(POINTER(_dll.IAcadTable), _ez_ptr):
	pass

class AcadTableStyle(POINTER(_dll.IAcadTableStyle), _ez_ptr):
	pass

class AcadText(POINTER(_dll.IAcadText), _ez_ptr):
	pass

class AcadTextStyle(POINTER(_dll.IAcadTextStyle), _ez_ptr):
	pass

class AcadTextStyles(POINTER(_dll.IAcadTextStyles), _ez_ptr):
	pass

class AcadTolerance(POINTER(_dll.IAcadTolerance), _ez_ptr):
	pass

class AcadToolbar(POINTER(_dll.IAcadToolbar), _ez_ptr):
	pass

class AcadToolbarItem(POINTER(_dll.IAcadToolbarItem), _ez_ptr):
	pass

class AcadToolbars(POINTER(_dll.IAcadToolbars), _ez_ptr):
	pass

class AcadTrace(POINTER(_dll.IAcadTrace), _ez_ptr):
	pass

class AcadUCS(POINTER(_dll.IAcadUCS), _ez_ptr):
	pass

class AcadUCSs(POINTER(_dll.IAcadUCSs), _ez_ptr):
	pass

class AcadUnderlay(POINTER(_dll.IAcadUnderlay), _ez_ptr):
	pass

class AcadUtility(POINTER(_dll.IAcadUtility), _ez_ptr):
	pass

class AcadView(POINTER(_dll.IAcadView), _ez_ptr):
	pass

class AcadViewport(POINTER(_dll.IAcadViewport), _ez_ptr):
	pass

class AcadViewports(POINTER(_dll.IAcadViewports), _ez_ptr):
	pass

class AcadViews(POINTER(_dll.IAcadViews), _ez_ptr):
	pass

class AcadXRecord(POINTER(_dll.IAcadXRecord), _ez_ptr):
	pass

class AcadXline(POINTER(_dll.IAcadXline), _ez_ptr):
	pass
	

# for debugging
if __name__ == "__main__":
    pass
