from .acad_colls import _AcadCollPre
from .object import AcadObject

from pyautocad import APoint






# Adder class
class _EntityAdder:
	def __init__(self, parent):
		self._me = parent.raw
		self._parent = parent
	
	# Dimensions
	def Dim3PointAngular(self, angle_vertex: APoint, first_end_point: APoint, second_end_point: APoint, text_point: APoint):
		"""
		Creates an angular dimension for an arc, two lines, or a circle.
		:param angle_vertex: APoint. The 3D WCS coordinates specifying the vertex of the angle to be measured.
		:param first_end_point: APoint. he 3D WCS coordinates specifying the point through which the first extension line passes.
		:param second_end_point: APoint. The 3D WCS coordinates specifying the point through which the second extension line passes.
		:param text_point: APoint. The 3D WCS coordinates specifying the point at which the dimension text is to be displayed.
		:return: AcadDim3PointAngular. The newly created angular dimension.
		"""
		kwargs = {
			"AngleVertex": angle_vertex,
			"FirstEndPoint": first_end_point,
			"SecondEndPoint": second_end_point,
			"TextPoint": text_point
		}
		obj = self._me.Cylinder(**kwargs)
		return self._add(obj)

	def DimAligned(self, ext_line_1_point: APoint, ext_line_2_point: APoint, text_position: APoint):
		"""
		Creates an aligned dimension object.
		:param ext_line_1_point: APoint. The 3D WCS coordinates specifying the first endpoint of the extension line.
		:param ext_line_2_point: APoint. The 3D WCS coordinates specifying the second endpoint of the extension line.
		:param text_position: APoint. The 3D WCS coordinates specifying the text position.
		:return: AcadDimAligned. The newly created aligned dimension.
		"""
		kwargs = {
			"ExtLine1Point": ext_line_1_point,
			"ExtLine2Point": ext_line_2_point,
			"TextPosition": text_position
		}
		obj = self._me.AddDimAligned(**kwargs)
		return self._add(obj)

	def DimAngular(self, angle_vertex: APoint, first_end_point: APoint, second_end_point: APoint, text_point: APoint):
		"""
		Creates an angular dimension for an arc, two lines, or a circle.
		:param angle_vertex: APoint. The 3D WCS coordinates specifying the center of the circle or arc, or the common vertex between the two dimensioned lines.
		:param first_end_point: APoint. The 3D WCS coordinates specifying the point through which the first extension line passes.
		:param second_end_point: APoint. The 3D WCS coordinates specifying the point through which the second extension line passes.
		:param text_point: APoint. The 3D WCS coordinates specifying the point at which the dimension text is to be displayed.
		:return: AcadDimAngular. The newly created angular dimension.
		"""
		kwargs = {
			"AngleVertex": angle_vertex,
			"FirstEndPoint": first_end_point,
			"SecondEndPoint": second_end_point,
			"TextPoint": text_point
		}
		obj = self._me.AddDimAngular(**kwargs)
		return self._add(obj)

	def DimArc(self, arc_center: APoint, first_end_point: APoint, second_end_point: APoint, arc_point: APoint):
		"""
		Creates an arc length dimension for an arc.
		:param arc_center: APoint. The 3D WCS coordinates specifying the center of the arc.
		:param first_end_point: APoint. The 3D WCS coordinates specifying the point through which the first extension line passes.
		:param second_end_point: APoint. The 3D WCS coordinates specifying the point through which the second extension line passes.
		:param arc_point: APoint. The 3D WCS coordinates specifying a point on the arc.
		:return: AcadDimArcLength. The newly created arc length dimension.
		"""
		kwargs = {
			"ArcCenter": arc_center,
			"FirstEndPoint": first_end_point,
			"SecondEndPoint": second_end_point,
			"ArcPoint": arc_point
		}
		obj = self._me.AddDimArc(**kwargs)
		return self._add(obj)

	def DimDiametric(self, chord_point: APoint, far_chord_point: APoint, leader_length: float):
		"""
		Creates a diametric dimension for a circle or arc given the two points on the diameter and the length of the leader line.
		:param chord_point: APoint. The 3D WCS coordinates specifying the first diameter point on the circle or arc.
		:param far_chord_point: APoint. The 3D WCS coordinates specifying the second diameter point on the circle or arc.
		:param leader_length: APoint. The positive value representing the length from the ChordPoint to the annotation text or dogleg.
		:return: AcadDimDiametric. The newly created diameter dimension object.
		"""
		kwargs = {
			"ChordPoint": chord_point,
			"FarChordPoint": far_chord_point,
			"LeaderLength": abs(leader_length)
		}
		obj = self._me.AddDimDiametric(**kwargs)
		return self._add(obj)

	def DimOrdinate(self, definition_point: APoint, leader_end_point: APoint, use_xaxis: bool):
		"""
		Creates an ordinate dimension given the definition point, and leader endpoint.
		:param definition_point: APoint. The 3D WCS coordinates specifying the point to be dimensioned.
		:param leader_end_point: APoint. The 3D WCS coordinates specifying the endpoint of the leader. This will be the location at which the dimension text is displayed.
		:param use_xaxis: bool. True: Creates an ordinate dimension displaying the X axis value. False: Creates an ordinate dimension displaying the Y axis value.
		:return: AcadDimOrdinate. The newly created ordinate dimension object.
		"""
		kwargs = {
			"DefinitionPoint": definition_point,
			"LeaderEndPoint": leader_end_point,
			"UseXAxis": int(use_xaxis)
		}
		obj = self._me.AddDimOrdinate(**kwargs)
		return self._add(obj)

	def DimRadial(self, center: APoint, chord_point: APoint, leader_length: float):
		"""
		Creates a radial dimension for the selected object at the given location
		:param center: APoint. The 3D WCS coordinates specifying the center point on the circle or arc.
		:param chord_point: APoint. The 3D WCS coordinates specifying the point on the circle or arc to attach the leader line.
		:param leader_length: float. The positive value representing the length from the ChordPoint to the annotation text or dogleg.
		:return: AcadDimRadial. The newly created radius dimension object.
		"""
		kwargs = {
			"Center": center,
			"ChordPoint": chord_point,
			"LeaderLength": leader_length
		}
		obj = self._me.AddDimRadial(**kwargs)
		return self._add(obj)

	def DimRadialLarge(self, center: APoint, chord_point: APoint, override_center: APoint, jog_point: APoint, jog_angle: float):
		"""
		Creates a jogged radial dimension for an arc, circle, or polyline arc segment
		:param center: APoint. The 3D WCS coordinates specifying the center of the arc, circle, or polyline arc segment.
		:param chord_point: APoint. The 3D WCS coordinates specifying the chord point for the arc.
		:param override_center: APoint. The 3D WCS coordinates specifying the override center location or pick point.
		:param jog_point: APoint. The 3D WCS coordinates specifying the jog location or pick point.
		:param jog_angle: float. The value for the jog angle.
		:return: AcadDimRadialLarge. The newly created jogged radius dimension.
		"""
		kwargs = {
			"Center": center,
			"ChordPoint": chord_point,
			"OverrideCenter": override_center,
			"JogPoint": jog_point,
			"JogAngle": jog_angle
		}
		obj = self._me.AddDimRadialLarge(**kwargs)
		return self._add(obj)

	def DimRotated(self, ext_line_1_point: APoint, ext_line_2_point: APoint, dim_line_location: APoint, rotation_angle: float):
		"""
		Creates a rotated linear dimension
		:param ext_line_1_point: APoint. The 3D WCS coordinates specifying the first end of the linear dimension to be measured. This is where the first extension line will be attached.
		:param ext_line_2_point: APoint. The 3D WCS coordinates specifying the second end of the linear dimension to be measured. This is where the second extension line will be attached.
		:param dim_line_location: APoint. The 3D WCS coordinates specifying a point on the dimension line. This will define the placement of the dimension line and the dimension text.
		:param rotation_angle: float. The angle, in radians, of rotation displaying the linear dimension. 
		:return: AcadDimRotated. The newly created rotated linear dimension object.
		"""
		kwargs = {
			"ExtLine1Point": ext_line_1_point,
			"ExtLine2Point": ext_line_2_point,
			"DimLineLocation": dim_line_location,
			"RotationAngle": rotation_angle
		}
		obj = self._me.AddDimRotated(**kwargs)
		return self._add(obj)

	# 3DSolid entities
	def Box(self, origin: APoint, length: float, width: float, height:float):
		"""
		Creates a 3D solid box with edges parallel to the axes of the WCS.
		:param origin: APoint. The 3D WCS coordinates specifying the origin of the box. This coordinate represents the center of the bounding box for the object, not a corner.
		:param length: float. The length of the box. Must be a positive number.
		:param width: float. The width of the box. Must be a positive number.
		:param height: float. The height of the box. Must be a positive number.
		:return: Acad3DSolid. A 3DSolid object as the newly created box.
		"""
		_origin = APoint(origin)
		_origin.x -= min(0.0, length)
		_origin.y -= min(0.0, width)
		_origin.z -= min(0.0, height)

		kwargs = {
			"Origin": _origin,
			"Length": abs(length),
			"Width": abs(width),
			"Height": abs(height)
		}
		obj = self._me.AddBox(**kwargs)
		return self._add(obj)

	def Cone(self, center: APoint, base_radius: float, height: float):
		"""
		Creates a 3D solid cone with the base on the XY plane of the WCS.
		:param center: APoint. The 3D WCS coordinates specifying the center of the bounding box.
		:param base_radius: float. The radius of the cone base. Must be a positive number.
		:param height: float. The height of the cone. Must be a positive number.
		:return: Acad3DSolid. A 3DSolid object as the newly created cone.
		"""
		kwargs = {
			"Center": center,
			"BaseRadius": abs(base_radius),
			"Height": abs(height)
		}
		obj = self._me.AddCone(**kwargs)
		return self._add(obj)

	def Cylinder(self, center: APoint, radius: float, height: float):
		"""
		Creates a 3D solid cylinder whose base is on the XY plane of the WCS.
		:param center: APoint. A 3D WCS coordinates specifying the CENTER OF THE BOUNDING BOX.
		:param radius: float. The cylinder radius. Must be a positive number.
		:param height: float. The cylinder height. Must be a positive number.
		:return: Acad3DSolid. A 3DSolid object as the newly created cylinder.
		"""
		kwargs = {
			"Center": center,
			"Radius": abs(radius),
			"Height": abs(height)
		}
		obj = self._me.Cylinder(**kwargs)
		return self._add(obj)

	def EllipticalCone(self, center: APoint, majorradius: float, minorradius: float, height: float):
		#TODO
		kwargs = {
			"Center": center,
			"MajorRadius": abs(radius),
			"MinorRadius": abs(height),
			"Height": abs(height)
		}
		obj = self._me.AddEllipticalCone(**kwargs)
		return self._add(obj)

	def EllipticalCylinder(self, center: APoint, majorradius: float, minorradius: float, height: float):
		#TODO
		kwargs = {
			"Center": center,
			"MajorRadius": abs(radius),
			"MinorRadius": abs(height),
			"Height": abs(height)
		}
		obj = self._me.AddEllipticalCylinder(**kwargs)
		return self._add(obj)

	def ExtrudedSolid(self, profile, height: float, taper_angle: float):
		#TODO: Profile As AcadRegion
		kwargs = {
			"Profile": profile,
			"Height": height,
			"TaperAngle": taper_angle
		}
		obj = self._me.AddExtrudedSolid(**kwargs)
		return self._add(obj)

	def ExtrudedSolidAlongPath(self, profile, path):
		#TODO: Profile As AcadRegion, Path As Object
		kwargs = {
			"Profile": profile,
			"Path": path
		}
		obj = self._me.AddExtrudedSolidAlongPath(**kwargs)
		return self._add(obj)




	
	# 3D other entities
	def Face3D(self, p1: APoint, p2: APoint, p3: APoint, p4: APoint):
		"""
		Creates a 3DFace object given four vertices.
		:param p1: APoint. The 1st 3D WCS coordinates specifying a point on the 3DFace object.
		:param p2: APoint. The 2nd 3D WCS coordinates specifying a point on the 3DFace object.
		:param p3: APoint. The 3rd 3D WCS coordinates specifying a point on the 3DFace object.
		:param p4: APoint. The 4th 3D WCS coordinates specifying a point on the 3DFace object.
		:return: Acad3DFace. The newly created 3DFace object.
		"""
		kwargs = {
			"Point1": p1,
			"Point2": p2,
			"point3": p3,
			"Point4": p4
		}
		obj = self._me.Add3DFace(**kwargs)
		return self._add(obj)

	def Mesh3D(self, m: int, n: int, points_matrix: tuple[APoint]):
		"""
		Creates a free-form 3D mesh, given the number of points in the M and N directions and the coordinates of the points in the M and N directions.
		:param m: int. Dimension of the point array. The size of the mesh on direction is limited to between 2 and 256.
		:param n: int. Dimension of the point array. The size of the mesh on direction is limited to between 2 and 256.
		:param points_matrix: list<APoint>. M x N matrix of 3D WCS coordinates. Defining vertices begins with vertex (0,0). Supplying the coordinate locations for each vertex in row M must be done before specifying vertices in row M + 1.
		:return: AcadPolygonMesh. A PolygonMesh as the newly created 3DMesh object.
		"""
		_check(points_matrix, APoint)
		points = _cont(points_matrix)
		kwargs = {
			"M": m,
			"N": n,
			"PointsMatrix": points
		}
		obj = self._me.Add3DMesh(**kwargs)
		return self._add(obj)

	def Poly3D(self, points_array: tuple[APoint]):
		"""
		Creates a 3D polyline from the given array of coordinates.
		:param points_array: tuple<APoint>. An array of 3D WCS coordinates. The polyline will be created according to the order of the coordinates in the array. The number of elements in the array must be a multiple of three. (Three elements define a single coordinate.)
		:return: Acad3DPolyline. The newly created 3DPolyline object.
		"""
		_check(points_array, APoint)
		points = _cont(points_array)
		kwargs = {
			"PointsArray": points
		}
		obj = self._me.Add3DPoly(**kwargs)
		return self._add(obj)

	
	# 2D entities
	def Arc(self, center: APoint, radius: float, start_angle: float, end_angle: float):
		"""
		Creates an arc given the center, radius, start angle, and end angle of the arc.
		:param center: APoint. The 3D WCS coordinates specifying the center point of the arc.
		:param radius: float. The radius of the arc.
		:param start_angle: float. The start angle in radians, defining the arc. A start angle greater than an end angle defines a counterclockwise arc.
		:param end_angle: float. The end angle in radians, defining the arc.
		:return: AcadArc. The newly created Arc object.
		"""
		kwargs = {
			"Center": center,
			"Radius": radius,
			"StartAngle": start_angle,
			"EndAngle": end_angle
		}
		obj = self._me.AddArc(**kwargs)
		return self._add(obj)

	def Circle(self, center: APoint, radius: float):
		"""
		Creates a circle given a center point and radius.
		:param center: APoint. The 3D WCS coordinates specifying the circle's center.
		:param radius: float. The radius of the circle. Must be a positive number.
		:return: AcadCircle. The newly created Circle object.
		"""
		kwargs = {
			"Center": center,
			"Radius": abs(radius)
		}
		obj = self._me.AddCircle(**kwargs)
		return self._add(obj)

	def Ellipse(self, center: APoint, major_axis: APoint, radius_ratio: float):
		"""
		Creates an ellipse in the XY plane of the WCS given the center point, a point on the major axis, and the radius ratio.
		:param center: APoint. The 3D WCS coordinates specifying the center of the ellipse.
		:param major_axis: APoint. A vector defining the major axis of the ellipse.
		:param radius_ratio: float. A positive value defining the major to minor axis ratio of an ellipse. A radius ratio of 1.0 defines a circle.
		:return: AcadEllipse. The newly created Ellipse object.
		"""
		kwargs = {
			"Center": center,
			"MajorAxis": major_axis,
			"RadiusRatio": radius_ratio
		}
		obj = self._me.AddEllipse(**kwargs)
		return self._add(obj)

	def Hatch(self, patterntype: int, patternname: str, associativity: bool, hatch_object_type=None):
		#TODO: PatternType as AcPatternType or AcGradientPatternType enum
		# HatchObjectType = AcHatchObjectType enum
		kwargs = {
			"PatternType": patterntype,
			"PatternName": patternname,
			"Associativity": associativity,
			"HatchObjectType": hatch_object_type
		}
		obj = self._me.AddHatch(**kwargs)
		return self._add(obj)
	
	
	
	# Other entities
	def Attribute(self, height: float, mode, prompt: str, insertion_point, tag: str, value: str):
		"""
		Creates an attribute definition at the given location with the specified properties.
		:param height: float. The text height in the current drawing unit.
		:param mode: AcAttributeMode enum. 
		:param prompt: str. This string appears when a block containing this attribute is inserted. The default for this string is the Tag string. Inputting acAttributeModeConstant for the Mode parameter disables the prompt.
		:param insertion_point: APoint. The 3D WCS coordinates specifying the location for the attribute.
		:param tag: str. This non-null string identifies each occurrence of the attribute. Enter any characters except spaces or exclamation points. AutoCAD changes lowercase letters to uppercase.
		:param value: str. This non-null string is the default attribute value.
		:return: AcadAttribute. The newly created Attribute object.
		"""
		kwargs = {
			"Height": height,
			"Mode": mode,
			"Prompt": prompt,
			"InsertionPoint": insertion_point,
			"Tag": tag.replace(" ", "_").replace("\t", "_").replace("!", "."),
			"Value": value
		}
		obj = self._me.AddAttribute(**kwargs)
		return self._add(obj)

	def CustomObject(self, class_name: str):
		"""
		Creates a Custom object.
		:param class_name: str. The rxClassName must be defined in an ObjectARX® application (ObjectARX DLL) or the method will fail.
		:return: Object. The newly created Custom object.
		"""
		kwargs = {
			"ClassName": class_name
		}
		obj = self._me.CustomObject(**kwargs)
		return self._add(obj)

	def Leader(self, points_array: tuple[APoint], annotation: AcadEntity, i_type: int):
		#TODO: Type As AcLeaderType
		_check(points_array, APoint)
		points = _cont(points_array)
		kwargs = {
			"PointsArray": points,
			"Annotation": annotation,
			"Type": i_type
		}
		obj = self._me.AddLeader(**kwargs)
		return self._add(obj)
	
	








	def _add(self, obj):
		"""
		Add object to item list
		:param obj:
		:return:
		"""
		self._parent.list.append(AcadObject(obj).parse())
		return self._parent.list[-1]


class AcadBlock(_AcadCollPre):
	"""
	A block definition containing a name and a set of objects
	"""
	def __init__(self, obj, parent=None):
		super().__init__(obj, parent)
		delattr(self, "add")
		self.add = _EntityAdder()

	# VBA-Methods
	def attach_external_reference(
			self,
			path_name: str,
			name: str,
			insertion_point,
			x_scale: float,
			y_scale: float,
			z_scale: float,
			rotation: float,
			b_overlay: bool,
			password=None
	):
		"""
		Attaches an external reference (xref) to the drawing
		:param path_name:
		:param name:
		:param insertion_point:
		:param x_scale:
		:param y_scale:
		:param z_scale:
		:param rotation:
		:param b_overlay:
		:param password:
		:return: AcadExternalReference
		"""
		kwargs = {
			"PathName": path_name,
			"Name": name,
			"InsertionPoint": insertion_point,
			"Xscale": x_scale,
			"Yscale": y_scale,
			"Zscale": z_scale,
			"Rotation": rotation,
			"bOverlay": b_overlay,
			"Password": password
		}
		return AcadObject(self._me.AttachExternalReference(**kwargs)).parse()

	def bind(self, prefix: bool):
		self._me.Bind(prefix)

	def detach(self):
		self._me.Detach()

	def insert_block(
			self,
			insertion_point,
			name: str,
			x_scale: float,
			y_scale: float,
			z_scale: float,
			rotation: float,
			password=None
	):
		kwargs = {
			"InsertionPoint": insertion_point,
			"Name": name,
			"Xscale": x_scale,
			"Yscale": y_scale,
			"Zscale": z_scale,
			"Rotation": rotation,
			"Password": password
		}
		return AcadObject(self._me.InsertBlock(**kwargs)).parse()

	def reload(self):
		self._me.Reload()

	def unload(self):
		self._me.Unload()

	# VBA-Properties
	@property
	def block_scaling(self):
		return self._me.BlockScaling

	@block_scaling.setter
	def block_scaling(self, value):
		self._me.BlockScaling = value

	@property
	def comments(self) -> str:
		return self._me.Comments

	@comments.setter
	def comments(self, value: str):
		self._me.Comments = value

	@property
	def explodable(self) -> str:
		return self._me.Explodable

	@explodable.setter
	def explodable(self, value: str):
		self._me.Explodable = value

	@property
	def is_dynamic_block(self) -> bool:
		return self._me.IsDynamicBlock

	@property
	def is_layout(self) -> bool:
		return self._me.IsLayout

	@property
	def is_xref(self) -> bool:
		return self._me.IsXRef

	@property
	def layout(self):
		return self._me.Layout

	@property
	def name(self) -> str:
		return self._me.Name

	@name.setter
	def name(self, value: str):
		self._me.Name = value

	@property
	def origin(self):
		return self._me.Origin

	@origin.setter
	def origin(self, value):
		self._me.Origin = value

	@property
	def path(self) -> str:
		return self._me.Path

	@path.setter
	def path(self, value: str):
		self._me.Path = value

	@property
	def units(self):
		return self._me.Units

	@units.setter
	def units(self, value):
		self._me.Units = value

	@property
	def xref_database(self):
		return self._me.XRefDatabase

