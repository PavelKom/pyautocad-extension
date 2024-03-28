#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api import acad_dll as _dll
from .object import AcadEntity, A3Vertex, A3Vertexes, A2Vertex, A2Vertexes
from .util import arr_check, recast as _recast, uncast as _uncast, dict_fix, get_obj_block_source
from multimethod import overload
import math

"""
3D objects
"""


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ Acad3DFace
"""
class Acad3DFace(POINTER(_dll.IAcad3DFace), AcadEntity):
	def __new__(cls, *args, **kwargs):
		return cls.__new(*args, **kwargs)

	
	@overload
	def __new(cls, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex, Point4: A3Vertex=None, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Default route
		kw = {"Point1": Point1, "Point2": Point2, "Point3": Point3, "Point4": Point4}
		dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).Add3DFace(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	@__new.register
	def _(cls, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)): # Without 4th point
		return cls.__new(Point1, Point2, Point3, None, source)
	
	__new = classmethod(__new)
		
	# VBA-methods with recasting
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes
	# GetBoundingBox - from parent
	# GetExtensionDictionary - from parent
	# GetInvisibleEdge<bool>(int) - without changes
	# GetXData - from parent
	# Highlight<bool> - without changes
	# IntersectWith - from parent
	# Mirror - from parent
	# Mirror3D - from parent
	# Move - without changes
	# Rotate - without changes
	# Rotate3D - without changes
	# ScaleEntity - without changes
	# SetInvisibleEdge(int, bool) - without changes
	# SetXData - from parent
	# TransformBy - from parent
	# Update - without changes

	
	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	# @property # Maybe as method???
	coordinate = None
	def get_coordinate(self, index: int):
		return A3Vertex(super().Coordinate(index))
	
	def set_coordinate(self, index: int, value: A3Vertex):
		super().Coordinate(index) = value
	
	@property
	def coordinates(self):
		return A3Vertexes(super().Coordinates)
	@coordinates.setter
	def coordinates(self):
		super().Coordinates = A3Vertexes.unpack()

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
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# TrueColor<bool> - without changes
	# VisibilityEdge1<bool> - without changes
	# VisibilityEdge2<bool> - without changes
	# VisibilityEdge3<bool> - without changes
	# VisibilityEdge4<bool>	 - without changes
	# Visible<bool> - without changes

	def __iter__(self):
		# Return coordinate and visibility
		for i in range(1,5):
			yield self[i], self(i)
	
	def __getitem__(self, index: int):
		return self.coordinate(index)
	
	def __setitem__(self, index: int, value: A3Vertex):
		self.set_coordinate(index, value)

	def __call__(self, index: int, value: bool=None):
		# Face(2, true) - set 2-nd edge invisivble
		if value is None:
			return self.GetInvisibleEdge(index)
		self.SetInvisibleEdge(index, value)


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ Acad3DPolyline
"""
class Acad3DPolyline(POINTER(_dll.IAcad3DPolyline), AcadEntity):
	def __new__(cls, PointsArray: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {"PointsArray": PointsArray.unpack()}
		#dict_fix(kw)
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).Add3DPoly(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	# VBA-methods with recasting
	# AppendVertex<A3Vertex> - without changes
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	# Copy - from parent
	# Delete - without changes
	def explode(self):
		objs = super().Explode()
		ret = []
		for obj in objs:
			ret.append(_recast(obj))
			ret[-1].connect_to_sink(self.sink)
		return tuple(ret)
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
	@property
	def closed(self):
		return super().Closed
	@closed.setter
	def closed(self, value):
		super().Closed = value
		
	# @property # Maybe as method???
	def coordinate(self, index: int):
		return A3Vertex(super().Coordinate(index))
	
	def set_coordinate(self, index: int, value: A3Vertex):
		super().Coordinate(index) = value
	
	@property
	def coordinates(self):
		return A3Vertexes(super().Coordinates)
	@coordinates.setter
	def coordinates(self):
		super().Coordinates = A3Vertexes.unpack()
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Length<float>  - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	# TrueColor<bool> - without changes
	# Type<ac3DPolylineType> - without changes
	# Visible<bool> - without changes
	
	def __len__(self):
		return math.floor(len(self.Coordinates) / 3)
		
	def __iter__(self):
		# Return coordinate and visibility
		for i in range(1, len(self)+1):
			yield self[i]
			
	def __getitem__(self, index: int):
		if index > self(len):
			raise ValueError("Invalid index for Acad3DPolyline coordinate getter")
		return self.coordinate(index) if index > 0 else len(self)
	
	def __setitem__(self, index: int, value: A3Vertex):
		if index <= 0 or index > self(len):
			raise ValueError("Invalid index for Acad3DPolyline coordinate setter")
		self.set_coordinate(index, value)


"""
Object
└─ AcadObject
	└─ AcadEntity
		└─ Acad3DSolid
"""
class Acad3DSolid(POINTER(_dll.IAcad3DSolid), AcadEntity):
	def __new__(cls, *args, **kw):
		raise TypeError("""You can't create {0}. Use {0}.%type%. Allowed types:
		Box(...), Cone(...) Cylinder(...), EllipticalCone(...), EllipticalCylinder(...), ExtrudedSolid(...), ExtrudedSolidAlongPath(...), RevolvedSolid(...), Sphere(...), Torus(...), Wedge(...)""".format(cls))
		
	@overload
	def box(cls, Origin: A3Vertex, Length=0.0, Width: float=0.0, Height: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Default AddBox route
		# If size is negative, move Origin
		A, B = bounding_box(Origin, Origin + A3Vertex(Length, Width, Height))
		kw = {
			"Origin": A,
			"Length": B.x - A.x,
			"Width": B.y - A.y,
			"Height": B.z - A.z
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddBox(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	@box.register
	def _(cls, Origin: A3Vertex, Size: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Origin and size
		return cls.box(Origin, Size.x, Size.y, Size.z, source)
		
	@box.register
	def _(cls, BoundingBox: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# As BoundingBox
		if len(BoundingBox) < 2:
			raise ValueError("[Acad3DSolid.Box] BoundingBox must contain 2 points")
		return cls.box(BoundingBox[0], BoundingBox[1] - BoundingBox[0])
	
	box = classmethod(box)
	
	@overload
	def cone(cls, Center: A3Vertex, BaseRadius: float=0.0, Height: float=0.0, Offset: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Default route for AddCone
		# Offset == 0.0 - use center
		# Offset > 0 - center.z - offset * (height/2)
		# Offset < 0 - center.z + offset * (height/2)
		# If you need Center as point on Base, use offset=-1.0
		# If you need Center is Top of the cone use offset=1.0
		center = A3Vertex(Center)
		center.z -= Offset * (Height / 2.0)
		kw = {
			"Center": center,
			"BaseRadius": abs(BaseRadius),
			"Height": abs(Height)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddCone(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	@cone.register
	def _(cls, Center: A3Vertex, Size3D: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Like size (with offset)
		return cls.cone(Center, Size3D.x, Size3D.y, Size3D.z, source)
	
	@cone.register
	def _(cls, Center: A3Vertex, Size2D: A2Vertex, offset: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Like size (without offset) and offset
		return cls.cone(Center, Size2D.x, Size2D.y, offset, source)

	@cone.register
	def _(cls, BoundingBox: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# As BoundingBox
		if len(ConeInfo) < 2:
			raise ValueError("[Acad3DSolid.Cone] BoundingBox must contain 2 points")
		Center = (BoundingBox[0] + BoundingBox[1]) / 2.0
		Size = abs(BoundingBox[0] - BoundingBox[1])
		return cls.cone(Center, Size.x / 2.0, Size.z, 0, source)

	cone = classmethod(cone)

	@overload
	def cylinder(cls, Center: A3Vertex, Radius: float=0.0, Height: float=0.0, Offset: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None)
		# Default route for AddCylinder
		# Offset == 0.0 - use center
		# Offset > 0 - center.z - offset * (height/2)
		# Offset < 0 - center.z + offset * (height/2)
		# If you need Center as point on Base, use offset=-1.0
		# If you need Center as point on Top, use offset=1.0
		center = A3Vertex(Center)
		center.z -= Offset * (Height / 2.0)
		kw = {
			"Center": center,
			"Radius": abs(Radius),
			"Height": abs(Height)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddCylinder(kw))
		obj.connect_to_sink(_source.sink)
		return obj
	
	@cylinder.register
	def _(cls, Center: A3Vertex, Size3D: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Like size (with offset)
		return cls.cylinder(Center, Size3D.x, Size3D.y, Size3D.z, source)
		
	@cylinder.register
	def _(cls, Center: A3Vertex, Size2D: A2Vertex, offset: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Like size (without offset) and offset
		return cls.cylinder(Center, Size2D.x, Size2D.y, offset, source)
	
	@cylinder.register
	def _(cls, BoundingBox: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Center and size in A3Vertexes
		if len(CylinderInfo) < 2:
			raise ValueError("[Acad3DSolid.Cylinder] BoundingBox must contain 2 points")
		Center = (BoundingBox[0] + BoundingBox[1]) / 2.0
		Size = abs(BoundingBox[0] - BoundingBox[1])
		return cls.cylinder(Center, Size.x / 2.0, Size.z, 0.0, source)
	
	cylinder = classmethod(cylinder)
	
	@overload
	def ellipticalcone(cls, Center: A3Vertex, MajorRadiu: floats=0.0, MinorRadius: float=0.0, Height: float=0.0, Offset: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Default route for AddEllipticalCone
		# Offset == 0.0 - use center
		# Offset > 0 - center.z - offset * (height/2)
		# Offset < 0 - center.z + offset * (height/2)
		# If you need Center as point on Base, use offset=-1.0
		# If you need Center as point on Top, use offset=1.0
		center = A3Vertex(Center)
		center.z -= Offset * (Height / 2.0)
		kw = {
			"Center": center,
			"MajorRadius": abs(MajorRadius),
			"MinorRadius": abs(MinorRadius),
			"Height": abs(Height)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddEllipticalCone(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	@ellipticalcone.register
	def _(cls, Center: A3Vertex, Size: A3Vertex, Offset=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Center, Size and offset
		return cls.ellipticalcone(Center, Size.x, Size.y, Size.z, offset, source)
	
	@ellipticalcone.register
	def _(cls, Center: A3Vertex, Size: A3Vertex, source: (AcadApplication, AcadDocument, AcadBlock)):
		# Overload
		# Center, Size. without offset
		return cls.ellipticalcone(Center, Size, 0.0, source)
		
	@ellipticalcone.register
	def _(cls, BoundingBox: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# As BoundingBox
		if len(EConeInfo) < 2:
			raise ValueError("[Acad3DSolid.EllipticalCone] EConeInfo must contain 2 points")
		Center = (BoundingBox[0] + BoundingBox[1]) / 2.0
		Size = abs(BoundingBox[0] - BoundingBox[1])
		return cls.ellipticalcone(Center, Size.x / 2.0, Size.y / 2.0, Size.z, 0.0, source)
	
	ellipticalcone = classmethod(ellipticalcone)
	elliptical_cone = ellipticalcone
		
	@overload
	def ellipticalcylinder(cls, Center: A3Vertex, MajorRadius: floats=0.0, MinorRadius: floats=0.0, Height: floats=0.0, Offset: floats=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Default route for AddEllipticalCylinder
		# Offset == 0.0 - use center
		# Offset > 0 - center.z - offset * (height/2)
		# Offset < 0 - center.z + offset * (height/2)
		# If you need Center as point on Base, use offset=-1.0
		# If you need Center as point on Top, use offset=1.0
		center = A3Vertex(Center)
		center.z -= Offset * (Height / 2.0)
		kw = {
			"Center": center,
			"MajorRadius": abs(MajorRadius),
			"MinorRadius": abs(MinorRadius),
			"Height": abs(Height)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddEllipticalCylinder(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	@ellipticalcylinder.register
	def _(cls, Center: A3Vertex, Size: A3Vertex, Offset: floats=0.0, source: floats=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# Center, Size and offset
		return cls.ellipticalcylinder(Center, Size.x, Size.y, Size.z, offset, source)
		
	@ellipticalcylinder.register
	def _(cls, BoundingBox: A3Vertexes, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		# Overload
		# As BoundingBox
		if len(EConeInfo) < 2:
			raise ValueError("[Acad3DSolid.EllipticalCylinder] BoundingBox must contain 2 points")
		Center = (BoundingBox[0] + BoundingBox[1]) / 2.0
		Size = abs(BoundingBox[0] - BoundingBox[1])
		return cls.ellipticalcylinder(Center, Size.x / 2.0, Size.y / 2.0, Size.z, 0.0, source)

	ellipticalcylinder = classmethod(ellipticalcylinder)
	elliptical_cylinder = ellipticalcylinder
	
	@classmethod
	def extrudedsolid(cls, Profile: AcadRegion, Height: float, TaperAngle: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Profile": Profile,
			"Height": Height,
			"TaperAngle": TaperAngle
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddExtrudedSolid(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	extruded_solid = extrudedsolid

	@classmethod
	def extrudedsolidalongpath(cls, Profile: AcadRegion, Path: (AcadArc, AcadCircle, AcadEllipse, AcadPolyline, AcadSpline), source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Profile": Profile,
			"Path": Path
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddExtrudedSolidAlongPath(kw))
		obj.connect_to_sink(_source.sink)
		return obj
		
	extruded_solid_along_path = extrudedsolidalongpath

	@classmethod
	def revolvedsolid(cls, Profile: AcadRegion, AxisPoint: A3Vertex, AxisDir: A3Vertex, Angle: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Profile": Profile,
			"AxisPoint": AxisPoint,
			"AxisDir": AxisDir,
			"Angle": Angle
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddRevolvedSolid(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	revolved_solid = revolvedsolid

	@classmethod
	def sphere(cls, Center: A3Vertex, Radius: float, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"Radius": abs(Radius)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddSphere(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	@classmethod
	def torus(cls, Center: A3Vertex, TorusRadius: float=0.0, TubeRadius: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"TorusRadius": abs(TorusRadius),
			"TubeRadius": abs(TubeRadius)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddTorus(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	@classmethod
	def wedge(cls, Center: A3Vertex, Length: float=0.0, Width: float=0.0, Height: float=0.0, source: (AcadApplication, AcadDocument, AcadBlock)=None):
		kw = {
			"Center": Center,
			"Length": abs(Length),
			"Width": abs(Width),
			"Height": abs(Height)
		}
		_source = get_obj_block_source(source)
		obj = _recast(_uncast(_source).AddWedge(kw))
		obj.connect_to_sink(_source.sink)
		return obj

	# VBA-methods with recasting
	# ArrayPolar - from parent
	# ArrayRectangular - from parent
	def boolean(self, Operation: int, Object: (Acad3DSolid, AcadRegion)):
		super().Boolean(Operation, Object)
	
	def checkinterference(self, Object: Acad3DSolid, CreateInterferenceSolid: bool, SolidsInterfere: bool):
		return _recast(super().CheckInterference(Object, CreateInterferenceSolid, SolidsInterfere))
	check_interference = checkinterference
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
	# Rotate - without changes
	# Rotate3D - without changes ?????????
	# ScaleEntity - without changes
	def SectionSolid(self, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex):
		return _recast(super().SectionSolid(Point1, Point2, Point3))
	# SetXData - from parent
	def SliceSolid(self, Point1: A3Vertex, Point2: A3Vertex, Point3: A3Vertex, Negative: bool):
		return _recast(super().SliceSolid(Point1, Point2, Point3, Negative))
	# TransformBy - from parent
	# Update - without changes

	# VBA-properties with recasting
	# Application<AcadApplication> - from parent
	@property
	def centroid(self):
		return A2Vertex(super().Centroid)
	# Document<AcadDocument> - from parent
	# EntityTransparency<String> - from parent
	# Handle<String> - without changes
	# HasExtensionDictionary<bool>- without changes. Alias from parent
	# History<bool> - without changes
	# Hyperlinks - from parent
	# Layer<String> - without changes
	# Length<float>  - without changes
	# Linetype<String> - without changes
	# LinetypeScale<Double> - without changes
	# Lineweight<acLineWeight enum> - without changes
	# Material<String> - without changes
	@property
	def momentofinertia(self):
		return A3Vertex(super().MomentOfInertia)
	moment_of_inertia = momentofinertia
	# ObjectID<Long_Ptr> - without changes. Alias from parent
	# ObjectName<String> - without changes. Alias from parent
	# OwnerID<Long_Ptr> - without changes. Alias from parent
	# PlotStyleName<String> - without changes
	@property
	def position(self):
		return A3Vertex(super().Position)
	@position.setter
	def position(self, value: A3Vertex):
		super().Position = value
	
	@property
	def principaldirections(self):
		return A3Vertex(super().PrincipalDirections)
	principal_directions = principaldirections
	
	@property
	def principalmoments(self):
		return A3Vertex(super().PrincipalMoments)
	principal_moments = principalmoments
	
	@property
	def productofinertia(self):
		return A3Vertex(super().ProductOfInertia)
	product_of_inertia = productofinertia
	
	@property
	def radiiofgyration(self):
		return A3Vertex(super().RadiiOfGyration)
	radii_of_gyration = radiiofgyration
	
	# ShowHistory<bool> - without changes
	# SolidType<String> - without changes
	# Type<ac3DPolylineType> - without changes
	# Visible<bool> - without changes
	# Volume<Double> - without changes
