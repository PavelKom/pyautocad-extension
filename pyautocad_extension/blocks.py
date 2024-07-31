from comtypes import POINTER
from comtypes.automation import VARIANT
from utils import _ez_ptr, CastManager, dict_fix
from objects import AcadObject # TODO: objects -> .objects
from enums import AcBlockScaling, AcInsertUnits, AcHatchObjectType
from api import acad_dll
_dll = acad_dll.dll


class AcadBlock(POINTER(_dll.IAcadBlock), _ez_ptr):
    def __new__(cls, InsertionPoint, Name, source=None):
        from app import AcadApplication
        from doc import AcadDocument
        if source is None:
            source = AcadApplication()
        if isinstance(source, AcadApplication):
            if source.Documents.Count == 0:
                source.Documents.Add()
            source = source.ActiveDocument
        if isinstance(source, AcadDocument):
            source = source.Blocks
        return source.Blocks.Add(InsertionPoint, Name)

    # Inherits from AcadObject
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

    # VBA methods
    def add3dface(self, Point1, Point2, Point3, Point4):
        'Creates a 3DFace object given four vertices'
        return CastManager.cast(self.com_parent.Add3DFace(Point1, Point2, Point3, Point4))
    def add3dmesh(self, M, N, PointsMatrix):
        'Creates a free-form 3D mesh, given the number of points in the M and N directions and the coordinates of the points in the M and N directions'
        return CastManager.cast(self.com_parent.Add3DMesh(M, N, PointsMatrix))
    def add3dpoly(self, PointsArray):
        'Creates a 3D polyline from the given array of coordinates'
        return CastManager.cast(self.com_parent.Add3DPoly(PointsArray))
    def addarc(self, Center, Radius, StartAngle, EndAngle):
        'Creates an arc given the center, radius, start angle, and end angle of the arc'
        return CastManager.cast(self.com_parent.AddArc(Center, Radius, StartAngle, EndAngle))
    def addattribute(self, Height, Mode, Prompt, InsertionPoint, Tag, Value):
        'Creates an attribute definition at the given location with the specified properties'
        return CastManager.cast(self.com_parent.AddAttribute(Height, Mode, Prompt, InsertionPoint, Tag, Value))
    def addbox(self, Origin, Length, Width, Height):
        'Creates a 3D solid box with edges parallel to the axes of the WCS'
        return CastManager.cast(self.com_parent.AddBox(Origin, Length, Width, Height))
    def addcircle(self, Center, Radius):
        'Creates a circle given a center point and radius'
        return CastManager.cast(self.com_parent.AddCircle(Center, Radius))
    def addcone(self, Center, BaseRadius, Height):
        'Creates a 3D solid cone with the base on the XY plane of the WCS'
        return CastManager.cast(self.com_parent.AddCone(Center, BaseRadius, Height))
    def addcustomobject(self, ClassName):
        'Creates a Custom object'
        return CastManager.cast(self.com_parent.AddCustomObject(ClassName))
    def addcylinder(self, Center, Radius, Height):
        'Creates a 3D solid cylinder whose base is on the XY plane of the WCS'
        return CastManager.cast(self.com_parent.AddCylinder(Center, Radius, Height))
    def adddim3pointangular(self, AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint):
        'Creates an angular dimension for an arc, two lines, or a circle'
        return CastManager.cast(self.com_parent.AddDim3PointAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint))
    def adddimaligned(self, ExtLine1Point, ExtLine2Point, TextPosition):
        'Creates an aligned dimension object'
        return CastManager.cast(self.com_parent.AddDimAligned(ExtLine1Point, ExtLine2Point, TextPosition))
    def adddimangular(self, AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint):
        'Creates an angular dimension for an arc, two lines, or a circle'
        return CastManager.cast(self.com_parent.AddDimAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint))
    def adddimarc(self, ArcCenter, FirstEndPoint, SecondEndPoint, ArcPoint):
        'Creates an arc length dimension for an arc'
        return CastManager.cast(self.com_parent.AddDimArc(ArcCenter, FirstEndPoint, SecondEndPoint, ArcPoint))
    def adddimdiametric(self, ChordPoint, FarChordPoint, LeaderLength):
        'Creates a diametric dimension for a circle or arc given the two points on the diameter and the length of the leader line'
        return CastManager.cast(self.com_parent.AddDimDiametric(ChordPoint, FarChordPoint, LeaderLength))
    def adddimordinate(self, DefinitionPoint, LeaderEndPoint, UseXAxis):
        'Creates an ordinate dimension given the definition point, and leader endpoint'
        return CastManager.cast(self.com_parent.AddDimOrdinate(DefinitionPoint, LeaderEndPoint, UseXAxis))
    def adddimradial(self, Center, ChordPoint, LeaderLength):
        'Creates a radial dimension for the selected object at the given location'
        return CastManager.cast(self.com_parent.AddDimRadial(Center, ChordPoint, LeaderLengths))
    def adddimradiallarge(self, Center, ChordPoint, OverrideCenter, JogPoint, JogAngle):
        'Creates a jogged radial dimension for an arc, circle, or polyline arc segment'
        return CastManager.cast(self.com_parent.AddDimRadialLarge(Center, ChordPoint, OverrideCenter, JogPoint, JogAngle))
    def adddimrotated(self, ExtLine1Point, ExtLine2Point, DimLineLocation, RotationAngle):
        'Creates a rotated linear dimension'
        return CastManager.cast(self.com_parent.AddDimRadialLarge(ExtLine1Point, ExtLine2Point, DimLineLocation, RotationAngle))
    def addellipse(self, Center, MajorAxis, RadiusRatio):
        'Creates an ellipse in the XY plane of the WCS given the center point, a point on the major axis, and the radius ratio'
        return CastManager.cast(self.com_parent.AddEllipse(Center, MajorAxis, RadiusRatio))
    def addellipticalcone(self, Center, MajorRadius, MinorRadius, Height):
        'Creates a 3D solid elliptical cone on the XY plane of the WCS given the Center, MajorRadius, MinorRadius, and Height'
        return CastManager.cast(self.com_parent.AddEllipticalCone(Center, MajorRadius, MinorRadius, Height))
    def addellipticalcylinder(self, Center, MajorRadius, MinorRadius, Height):
        'Creates a 3D solid elliptical cylinder whose base is on the XY plane of the WCS, given the Center, MajorRadius, MinorRadius, and Height'
        return CastManager.cast(self.com_parent.AddEllipticalCylinder(Center, MajorRadius, MinorRadius, Height))
    def addextrudedsolid(self, Profile, Height, TaperAngle):
        'Creates an extruded solid given the Profile, Height, and TaperAngle'
        return CastManager.cast(self.com_parent.AddExtrudedSolid(Profile, Height, TaperAngle))
    def addextrudedsolidalongpath(self, Profile, Path):
        'Creates an extruded solid given the profile and an extrusion path'
        return CastManager.cast(self.com_parent.AddExtrudedSolidAlongPath(Profile, Path))
    def addhatch(self, PatternType, PatternName, Associativity, HatchObjectType: AcHatchObjectType=None):
        'Creates a Hatch object'
        return CastManager.cast(self.com_parent.AddHatch(
            PatternType.value, PatternName, Associativity,
            VARIANT() if HatchObjectType.value is None else HatchObjectType
        ))
    def addleader(self, PointsArray, Annotation, Type):
        'Creates a leader line, given the coordinates of the points'
        return CastManager.cast(self.com_parent.AddLeader(PointsArray, Annotation, Type))
    def addlightweightpolyline(self, VerticesList):
        'Creates a lightweight polyline from a list of vertices'
        return CastManager.cast(self.com_parent.AddLightWeightPolyline(VerticesList))
    def addline(self, StartPoint, EndPoint):
        'Creates a line passing through two points'
        return CastManager.cast(self.com_parent.AddLine(StartPoint, EndPoint))
    def addminsertblock(self, InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, NumRows, NumColumns, RowSpacing, ColumnSpacing, Password=None):
        'Inserts an array of blocks'
        kw = {
            "InsertionPoint": InsertionPoint,
            "Name": Name,
            "Xscale": Xscale,
            "Yscale": Yscale,
            "Zscale": Zscale,
            "Rotation": Rotation,
            "NumRows": NumRows,
            "NumColumns": NumColumns,
            "RowSpacing": RowSpacing,
            "ColumnSpacing": ColumnSpacing,
            "Password": Password
        }
        dict_fix(kw)
        return CastManager.cast(self.com_parent.AddMInsertBlock(kw))
    def addmleader(self, PointsArray, leaderLineIndex):
        'Creates a multileader'
        return CastManager.cast(self.com_parent.AddMLeader(PointsArray, leaderLineIndex))
    def addmline(self, VertexList):
        'Creates a polyface mesh from a list of vertices'
        return CastManager.cast(self.com_parent.AddMLine(VertexList))
    def addmtext(self, InsertionPoint, Width, Text):
        'Creates an MText entity in a rectangle defined by the insertion point and width of the bounding box'
        return CastManager.cast(self.com_parent.AddMText(InsertionPoint, Width, Text))
    def addpoint(self, Point):
        'Creates a Point object at a given location'
        return CastManager.cast(self.com_parent.AddPoint(Point))
    def addpolyfacemesh(self, VertexList, FaceList):
        'Creates a polyface mesh from a list of vertices'
        return CastManager.cast(self.com_parent.AddPolyfaceMesh(VertexList, FaceList))
    def addpolyline(self, VerticesList):
        'Creates a polyline from a list of vertices'
        return CastManager.cast(self.com_parent.AddPolyline(VerticesList))
    def addraster(self, imageFileName, InsertionPoint, ScaleFactor, RotationAngle):
        'Creates a new raster image based on an existing image file'
        return CastManager.cast(self.com_parent.AddRaster(imageFileName, InsertionPoint, ScaleFactor, RotationAngle))
    def addray(self, Point1, Point2):
        'Creates a ray passing through two unique points'
        return CastManager.cast(self.com_parent.AddRay(Point1, Point2))
    def addregion(self, ObjectList):
        'Creates a region from a set of entities. The given entities must form a closed coplanar region'
        return CastManager.cast(self.com_parent.AddRegion(ObjectList))
    def addrevolvedsolid(self, Profile, AxisPoint, AxisDir, Angle):
        'Creates a revolved solid, given the region around an axis'
        return CastManager.cast(self.com_parent.AddRevolvedSolid(Profile, AxisPoint, AxisDir, Angle))
    def addsection(self, FromPoint, ToPoint, planeVector):
        'Creates a section plane'
        return CastManager.cast(self.com_parent.AddSection(FromPoint, ToPoint, planeVector))
    def addshape(self, Name, InsertionPoint, ScaleFactor, RotationAngle):
        'Creates a Shape object based on a template identified by name, at the given insertion point, scale factor, and rotation'
        return CastManager.cast(self.com_parent.AddShape(Name, InsertionPoint, ScaleFactor, RotationAngle))
    def addsolid(self, Point1, Point2, Point3, Point4):
        'Creates a 2D solid polygon'
        return CastManager.cast(self.com_parent.AddSolid(Point1, Point2, Point3, Point4))
    def addsphere(self, Center, Radius):
        'Creates a sphere given the center and radius'
        return CastManager.cast(self.com_parent.AddSphere(Center, Radius))
    def addspline(self, PointsArray, StartTangent, EndTangent):
        'Creates a quadratic or cubic NURBS (nonuniform rational B-spline) curve'
        return CastManager.cast(self.com_parent.AddSpline(PointsArray, StartTangent, EndTangent))
    def addtable(self, InsertionPoint, NumRows, NumColumns, RowHeight, ColWidth):
        'Creates a table at the given insertion point, given the number of rows, number of columns, row height and column width'
        return CastManager.cast(self.com_parent.AddTable(InsertionPoint, NumRows, NumColumns, RowHeight, ColWidth))
    def addtext(self, TextString, InsertionPoint, Height):
        'Creates a single line of text'
        return CastManager.cast(self.com_parent.AddText(TextString, InsertionPoint, Height))
    def addtolerance(self, Text, InsertionPoint, Direction):
        'Creates a tolerance entity'
        return CastManager.cast(self.com_parent.AddTolerance(Text, InsertionPoint, Direction))
    def addtorus(self, Center, TorusRadius, TubeRadius):
        'Creates a torus at the given location'
        return CastManager.cast(self.com_parent.AddTorus(Center, TorusRadius, TubeRadius))
    def addtrace(self, PointsArray):
        'Creates a Trace object from an array of points'
        return CastManager.cast(self.com_parent.AddTrace(PointsArray))
    def addwedge(self, Center, Length, Width, Height):
        'Creates a wedge with edges parallel to the axes given the length, width, and height'
        return CastManager.cast(self.com_parent.AddWedge(Center, Length, Width, Height))
    def addxline(self, Point1, Point2):
        'Creates an xline (an infinite line) passing through two specified points'
        return CastManager.cast(self.com_parent.AddXline(Point1, Point2))
    def attachexternalreference(self, PathName, Name, InsertionPoint, Xscale, Yscale, Zscale, Rotation, bOverlay, Password=None):
        'Attaches an external reference (xref) to the drawing'
        kw = {
            "PathName": PathName,
            "Name": Name,
            "InsertionPoint": InsertionPoint,
            "Xscale": Xscale,
            "Yscale": Yscale,
            "Zscale": Zscale,
            "Rotation": Rotation,
            "bOverlay": bOverlay,
            "Password": Password
        }
        dict_fix(kw)
        return CastManager.cast(self.com_parent.AttachExternalReference(kw))
    def bind(self, bPrefixName):
        'Binds an external reference (xref) to a drawing'
        self.com_parent.Bind(bPrefixName)
    def detach(self):
        self.com_parent.Detach()
    def insertblock(self, InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, Password=None):
        'Inserts a drawing file or a named block that has been defined in the current drawing'
        kw = {
            "InsertionPoint": InsertionPoint,
            "Name": Name,
            "Xscale": Xscale,
            "Yscale": Yscale,
            "Zscale": Zscale,
            "Rotation": Rotation,
            "Password": Password
        }
        dict_fix(kw)
        return CastManager.cast(self.com_parent.InsertBlock(kw))
    def item(self, Index):
        'Gets the member object at a given index in a collection, group, or selection set'
        return CastManager.cast(self.com_parent.Item(Index))
    def reload(self):
        'Reloads the external reference (xref)'
        self.com_parent.Reload()
    def unload(self):
        'Unloads the menu group or external reference'
        self.com_parent.Unload()
        
    # VBA properties
    @property
    def blockscaling(self):
        'Specifies the allowed scaling for the block'
        return AcBlockScaling(self.com_parent.BlockScaling)
    @blockscaling.setter
    def _(self, value: AcBlockScaling):
        self.com_parent.BlockScaling = value.value
    
    @property
    def comments(self):
        'Specifies the comments for the block'
        return self.com_parent.Comments
    @comments.setter
    def _(self, value: str):
        self.com_parent.Comments = value
    
    @property
    def count(self):
        'Gets the number of items in the collection, dictionary, group, or selection set'
        return self.com_parent.Count
    
    @property
    def explodable(self):
        'Specifies whether the block can be exploded'
        return self.com_parent.Explodable
    @explodable.setter
    def _(self, value: bool):
        self.com_parent.Explodable = value
    
    @property
    def isdynamicblock(self):
        'Specifies if this is a dynamic block'
        return self.com_parent.IsDynamicBlock
    
    @property
    def islayout(self):
        'Determines if the given block is a layout block'
        return self.com_parent.IsLayout
    
    @property
    def isxref(self):
        'Determines if the given block is an XRef block'
        return self.com_parent.IsXRef
    
    @property
    def layout(self):
        'Determines if the given block is an XRef block'
        return CastManager.cast(self.com_parent.Layout)
    
    @property
    def name(self):
        'Specifies the name of the object'
        return self.com_parent.Name
    @name.setter
    def _(self, value: str):
        self.com_parent.Name = value
    
    @property
    def origin(self):
        'Specifies the origin of the UCS, block, layout, or raster image in WCS coordinates'
        return self.com_parent.Origin
    @origin.setter
    def _(self, value):
        self.com_parent.Origin = value
    
    @property
    def path(self):
        'Specifies the path of the external reference'
        return self.com_parent.Path
    @path.setter
    def _(self, value: str):
        self.com_parent.Path = value
    
    @property
    def units(self):
        'Specifies the native units of measure for the block'
        return AcInsertUnits(self.com_parent.Units)
    @units.setter
    def _(self, value: AcInsertUnits):
        self.com_parent.Units = value.value
    
    @property
    def xrefdatabase(self):
        'Gets the Database object that defines the contents of the block'
        return CastManager.cast(self.com_parent.XRefDatabase)
    
    # _NewEnum - iterator
    

class AcadModelSpace(POINTER(_dll.IAcadModelSpace), _ez_ptr):
    add3dface = AcadBlock.add3dface
    add3dmesh = AcadBlock.add3dmesh
    add3dpoly = AcadBlock.add3dpoly
    addarc = AcadBlock.addarc
    addattribute = AcadBlock.addattribute
    addbox = AcadBlock.addbox
    addcircle = AcadBlock.addcircle
    addcone = AcadBlock.addcone
    addcustomobject = AcadBlock.addcustomobject
    addcylinder = AcadBlock.addcylinder
    adddim3pointangular = AcadBlock.adddim3pointangular
    adddimaligned = AcadBlock.adddimaligned
    adddimangular = AcadBlock.adddimangular
    adddimarc = AcadBlock.adddimarc
    adddimdiametric = AcadBlock.adddimdiametric
    adddimordinate = AcadBlock.adddimordinate
    adddimradial = AcadBlock.adddimradial
    adddimradiallarge = AcadBlock.adddimradiallarge
    adddimrotated = AcadBlock.adddimrotated
    addellipse = AcadBlock.addellipse
    addellipticalcone = AcadBlock.addellipticalcone
    addellipticalcylinder = AcadBlock.addellipticalcylinder
    addextrudedsolid = AcadBlock.addextrudedsolid
    addextrudedsolidalongpath = AcadBlock.addextrudedsolidalongpath
    addhatch = AcadBlock.addhatch
    addleader = AcadBlock.addleader
    addlightweightpolyline = AcadBlock.addlightweightpolyline
    addline = AcadBlock.addline
    addminsertblock = AcadBlock.addminsertblock
    addmleader = AcadBlock.addmleader
    addmline = AcadBlock.addmline
    addmtext = AcadBlock.addmtext
    addpoint = AcadBlock.addpoint
    addpolyfacemesh = AcadBlock.addpolyfacemesh
    addpolyline = AcadBlock.addpolyline
    addraster = AcadBlock.addraster
    addray = AcadBlock.addray
    addregion = AcadBlock.addregion
    addrevolvedsolid = AcadBlock.addrevolvedsolid
    addsection = AcadBlock.addsection
    addshape = AcadBlock.addshape
    addsolid = AcadBlock.addsolid
    addsphere = AcadBlock.addsphere
    addspline = AcadBlock.addspline
    addtable = AcadBlock.addtable
    addtext = AcadBlock.addtext
    addtolerance = AcadBlock.addtolerance
    addtorus = AcadBlock.addtorus
    addtrace = AcadBlock.addtrace
    addwedge = AcadBlock.addwedge
    addxline = AcadBlock.addxline
    attachexternalreference = AcadBlock.attachexternalreference
    bind = AcadBlock.bind
    detach = AcadBlock.detach
    insertblock = AcadBlock.insertblock
    item = AcadBlock.item
    reload = AcadBlock.reload
    unload = AcadBlock.unload
    
    blockscaling = AcadBlock.blockscaling
    comments = AcadBlock.comments
    count = AcadBlock.count
    explodable = AcadBlock.explodable
    isdynamicblock = AcadBlock.isdynamicblock
    islayout = AcadBlock.islayout
    isxref = AcadBlock.isxref
    layout = AcadBlock.layout
    name = AcadBlock.name
    origin = AcadBlock.origin
    path = AcadBlock.path
    units = AcadBlock.units
    xrefdatabase = AcadBlock.xrefdatabase
    
    delete = AcadBlock.delete
    erase = AcadBlock.erase
    getextensiondictionary = AcadBlock.getextensiondictionary
    getxdata = AcadBlock.getxdata
    setxdata = AcadBlock.setxdata
    
    application = AcadBlock.application
    database = AcadBlock.database
    document = AcadBlock.document
    handle = AcadBlock.handle
    hasextensiondictionary = AcadBlock.hasextensiondictionary
    objectid = AcadBlock.objectid
    objectname = AcadBlock.objectname
    ownerid = AcadBlock.ownerid


class AcadPaperSpace(POINTER(_dll.IAcadPaperSpace), _ez_ptr):
    add3dface = AcadBlock.add3dface
    add3dmesh = AcadBlock.add3dmesh
    add3dpoly = AcadBlock.add3dpoly
    addarc = AcadBlock.addarc
    addattribute = AcadBlock.addattribute
    addbox = AcadBlock.addbox
    addcircle = AcadBlock.addcircle
    addcone = AcadBlock.addcone
    addcustomobject = AcadBlock.addcustomobject
    addcylinder = AcadBlock.addcylinder
    adddim3pointangular = AcadBlock.adddim3pointangular
    adddimaligned = AcadBlock.adddimaligned
    adddimangular = AcadBlock.adddimangular
    adddimarc = AcadBlock.adddimarc
    adddimdiametric = AcadBlock.adddimdiametric
    adddimordinate = AcadBlock.adddimordinate
    adddimradial = AcadBlock.adddimradial
    adddimradiallarge = AcadBlock.adddimradiallarge
    adddimrotated = AcadBlock.adddimrotated
    addellipse = AcadBlock.addellipse
    addellipticalcone = AcadBlock.addellipticalcone
    addellipticalcylinder = AcadBlock.addellipticalcylinder
    addextrudedsolid = AcadBlock.addextrudedsolid
    addextrudedsolidalongpath = AcadBlock.addextrudedsolidalongpath
    addhatch = AcadBlock.addhatch
    addleader = AcadBlock.addleader
    addlightweightpolyline = AcadBlock.addlightweightpolyline
    addline = AcadBlock.addline
    addminsertblock = AcadBlock.addminsertblock
    addmleader = AcadBlock.addmleader
    addmline = AcadBlock.addmline
    addmtext = AcadBlock.addmtext
    addpoint = AcadBlock.addpoint
    addpolyfacemesh = AcadBlock.addpolyfacemesh
    addpolyline = AcadBlock.addpolyline
    addraster = AcadBlock.addraster
    addray = AcadBlock.addray
    addregion = AcadBlock.addregion
    addrevolvedsolid = AcadBlock.addrevolvedsolid
    addsection = AcadBlock.addsection
    addshape = AcadBlock.addshape
    addsolid = AcadBlock.addsolid
    addsphere = AcadBlock.addsphere
    addspline = AcadBlock.addspline
    addtable = AcadBlock.addtable
    addtext = AcadBlock.addtext
    addtolerance = AcadBlock.addtolerance
    addtorus = AcadBlock.addtorus
    addtrace = AcadBlock.addtrace
    addwedge = AcadBlock.addwedge
    addxline = AcadBlock.addxline
    attachexternalreference = AcadBlock.attachexternalreference
    bind = AcadBlock.bind
    detach = AcadBlock.detach
    insertblock = AcadBlock.insertblock
    item = AcadBlock.item
    reload = AcadBlock.reload
    unload = AcadBlock.unload
    
    blockscaling = AcadBlock.blockscaling
    comments = AcadBlock.comments
    count = AcadBlock.count
    explodable = AcadBlock.explodable
    isdynamicblock = AcadBlock.isdynamicblock
    islayout = AcadBlock.islayout
    isxref = AcadBlock.isxref
    layout = AcadBlock.layout
    name = AcadBlock.name
    origin = AcadBlock.origin
    path = AcadBlock.path
    units = AcadBlock.units
    xrefdatabase = AcadBlock.xrefdatabase
    
    delete = AcadBlock.delete
    erase = AcadBlock.erase
    getextensiondictionary = AcadBlock.getextensiondictionary
    getxdata = AcadBlock.getxdata
    setxdata = AcadBlock.setxdata
    
    application = AcadBlock.application
    database = AcadBlock.database
    document = AcadBlock.document
    handle = AcadBlock.handle
    hasextensiondictionary = AcadBlock.hasextensiondictionary
    objectid = AcadBlock.objectid
    objectname = AcadBlock.objectname
    ownerid = AcadBlock.ownerid
    
    def AddPViewport(self, Center, Width, Height):
        return CastManager.cast(self.com_parent.AddPViewport(Center, Width, Height))


class AcadBlocks(POINTER(_dll.IAcadBlocks), _ez_ptr):
    # Inherits from AcadObject
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
    
    def add(self, InsertionPoint, Name):
        'Creates a member object and adds it to the appropriate collection'
        return CastManager.cast(self.com_parent.Add(InsertionPoint, Name))
    
    def item(self, Index):
        'Gets the member object at a given index in a collection, group, or selection set'
        return CastManager.cast(self.com_parent.Item(Index))
    
    @property
    def count(self):
        return self.com_parent.Count
    
    # _IAcadBlocks__com__get__NewEnum - iterator


__all__ = (
    "AcadBlock",
    "AcadModelSpace",
    "AcadPaperSpace",
    "AcadBlocks",
)