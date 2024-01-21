from .acad_colls import _AcadCollPre
from .object import AcadObject

from pyautocad import APoint


def _cont(var):
	try:
		res = []
		for v in var:
			res.extend(_cont(v))
		return res
	except:
		return [var]


def _check(var, t):
	try:
		for item in var:
			if not isinstance(item, t):
				raise TypeError("Variable '{0}' from '{1}' must be '{2}'".format(item, var, t))
	except:
		if not isinstance(var, t):
			raise TypeError("Variable '{0}' must be '{1}'".format(var, t))

# Adder class
class _EntityAdder:
	def __init__(self, parent):
		self._me = parent.raw
		self._parent = parent

	@staticmethod
	def _fix_dict(kw: dict):
		# Remove all items with None value
		for k, v in kw.items():
			if v is None:
				kw.pop(k)

	def Face3D(self, p1: APoint, p2: APoint, p3: APoint, p4: APoint):
		"""
		Creates a 3DFace object given four vertices
		:param p1: APoint. The 3D WCS coordinates specifying a point on the 3DFace object
		:param p2: APoint. The 3D WCS coordinates specifying a point on the 3DFace object
		:param p3: APoint. The 3D WCS coordinates specifying a point on the 3DFace object
		:param p4: APoint. The 3D WCS coordinates specifying a point on the 3DFace object
		:return: Acad3DFace. The newly created 3DFace object
		"""
		kwargs = {
			"Point1": p1,
			"Point2": p2,
			"point3": p3,
			"Point4": p4
		}
		obj = self._me.Add3DFace(**kwargs)
		return self._add(obj)

	def Mesh3D(self, m: float, n: float, points_matrix: tuple[APoint]):
		"""
		Creates a free-form 3D mesh, given the number of points in the M and N directions and the coordinates of the points in the M and N directions
		:param m: float. Dimension of the point array. The size of the mesh on direction is limited to between 2 and 256
		:param n: float. Dimension of the point array. The size of the mesh on direction is limited to between 2 and 256
		:param points_matrix: list<APoint>. M x N matrix of 3D WCS coordinates. Defining vertices begins with vertex (0,0). Supplying the coordinate locations for each vertex in row M must be done before specifying vertices in row M + 1
		:return: AcadPolygonMesh. A PolygonMesh as the newly created 3DMesh object
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
		Creates a 3D polyline from the given array of coordinates
		:param points_array: tuple<APoint>. An array of 3D WCS coordinates. The polyline will be created according to the order of the coordinates in the array. The number of elements in the array must be a multiple of three. (Three elements define a single coordinate.)
		:return: Acad3DPolyline. The newly created 3DPolyline object
		"""
		_check(points_array, APoint)
		points = _cont(points_array)
		kwargs = {
			"PointsArray": points
		}
		obj = self._me.Add3DPoly(**kwargs)
		return self._add(obj)

	def Arc(self, center: APoint, radius: float, start_angle: float, end_angle: float):
		"""
		Creates an arc given the center, radius, start angle, and end angle of the arc
		:param center: APoint. The 3D WCS coordinates specifying the center point of the arc
		:param radius: float. The radius of the arc
		:param start_angle: float. The start angle in radians, defining the arc. A start angle greater than an end angle defines a counterclockwise arc.
		:param end_angle: float. The end angle in radians, defining the arc
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

	def Attribute(self, height: float, mode, prompt: str, insertion_point, tag: str, value: str):
		"""
		Creates an attribute definition at the given location with the specified properties
		:param height: float. The text height in the current drawing unit
		:param mode: AcAttributeMode enum
		:param prompt: str. This string appears when a block containing this attribute is inserted. The default for this string is the Tag string. Inputting acAttributeModeConstant for the Mode parameter disables the prompt
		:param insertion_point: APoint. The 3D WCS coordinates specifying the location for the attribute
		:param tag: str. This non-null string identifies each occurrence of the attribute. Enter any characters except spaces or exclamation points. AutoCAD changes lowercase letters to uppercase
		:param value: str. This non-null string is the default attribute value
		:return: AcadAttribute. The newly created Attribute object
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

	def Box(self, origin: APoint, length: float, width: float, height:float):
		"""
		Creates a 3D solid box with edges parallel to the axes of the WCS
		:param origin: APoint. The 3D WCS coordinates specifying the origin of the box. This coordinate represents the center of the bounding box for the object, not a corner.
		:param length: float. The length of the box. Must be a positive number
		:param width: float. The width of the box. Must be a positive number
		:param height: float. The height of the box. Must be a positive number
		:return: Acad3DSolid. A 3DSolid object as the newly created box
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

	def Circle(self, center: APoint, radius: float):
		"""
		Creates a circle given a center point and radius
		:param center: APoint. The 3D WCS coordinates specifying the circle's center
		:param radius: float. The radius of the circle. Must be a positive number
		:return: AcadCircle. The newly created Circle object
		"""
		kwargs = {
			"Center": center,
			"Radius": abs(radius)
		}
		obj = self._me.AddCircle(**kwargs)
		return self._add(obj)

	def Cone(self, center: APoint, base_radius: float, height: float):
		"""
		Creates a 3D solid cone with the base on the XY plane of the WCS
		:param center: APoint. The 3D WCS coordinates specifying the center of the bounding box
		:param base_radius: float. The radius of the cone base. Must be a positive number
		:param height: float. The height of the cone. Must be a positive number
		:return: Acad3DSolid. A 3DSolid object as the newly created cone
		"""
		kwargs = {
			"Center": center,
			"BaseRadius": abs(base_radius),
			"Height": abs(height)
		}
		obj = self._me.AddCone(**kwargs)
		return self._add(obj)

	def CustomObject(self, class_name: str):
		"""
		Creates a Custom object
		:param class_name: str. The rxClassName must be defined in an ObjectARX® application (ObjectARX DLL) or the method will fail
		:return: Object. The newly created Custom object
		"""
		kwargs = {
			"ClassName": class_name
		}
		obj = self._me.CustomObject(**kwargs)
		return self._add(obj)

	def Cylinder(self, center: APoint, radius: float, height: float):
		"""
		Creates a 3D solid cylinder whose base is on the XY plane of the WCS
		:param center: APoint. A 3D WCS coordinates specifying the center of the bounding box
		:param radius: float. The cylinder radius. Must be a positive number
		:param height: float. The cylinder height. Must be a positive number
		:return: Acad3DSolid. A 3DSolid object as the newly created cylinder.
		"""
		kwargs = {
			"Center": center,
			"Radius": abs(radius),
			"Height": abs(height)
		}
		obj = self._me.Cylinder(**kwargs)
		return self._add(obj)

	def Dim3PointAngular(self, angle_vertex: APoint, first_end_point: APoint, second_end_point: APoint, text_point: APoint):
		"""
		Creates an angular dimension for an arc, two lines, or a circle
		:param angle_vertex: APoint. The 3D WCS coordinates specifying the vertex of the angle to be measured
		:param first_end_point: APoint. he 3D WCS coordinates specifying the point through which the first extension line passes
		:param second_end_point: APoint. The 3D WCS coordinates specifying the point through which the second extension line passes
		:param text_point: APoint. The 3D WCS coordinates specifying the point at which the dimension text is to be displayed
		:return: AcadDim3PointAngular. The newly created angular dimension
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
		Creates an aligned dimension object
		:param ext_line_1_point: APoint. The 3D WCS coordinates specifying the first endpoint of the extension line
		:param ext_line_2_point: APoint. The 3D WCS coordinates specifying the second endpoint of the extension line
		:param text_position: APoint. The 3D WCS coordinates specifying the text position
		:return: AcadDimAligned. The newly created aligned dimension
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
		Creates an angular dimension for an arc, two lines, or a circle
		:param angle_vertex: APoint. The 3D WCS coordinates specifying the center of the circle or arc, or the common vertex between the two dimensioned lines
		:param first_end_point: APoint. The 3D WCS coordinates specifying the point through which the first extension line passes
		:param second_end_point: APoint. The 3D WCS coordinates specifying the point through which the second extension line passes
		:param text_point: APoint. The 3D WCS coordinates specifying the point at which the dimension text is to be displayed
		:return: AcadDimAngular. The newly created angular dimension
		"""
		kwargs = {
			"AngleVertex": angle_vertex,
			"FirstEndPoint": first_end_point,
			"SecondEndPoint": second_end_point,
			"TextPoint": text_point
		}
		obj = self._me.AddDimAngular(**kwargs)
		return self._add(obj)

	def DimArc(self, arc_center, first_end_point, second_end_point, arc_point):
		"""
		Creates an arc length dimension for an arc
		:param arc_center:
		:param first_end_point:
		:param second_end_point:
		:param arc_point:
		:return: AcadDimArcLength
		"""
		kwargs = {
			"ArcCenter": arc_center,
			"FirstEndPoint": first_end_point,
			"SecondEndPoint": second_end_point,
			"ArcPoint": arc_point
		}
		obj = self._me.AddDimArc(**kwargs)
		return self._add(obj)

	def DimDiametric(self, chord_point, far_chord_point, leader_length: float):
		"""
		Creates a diametric dimension for a circle or arc given the two points on the diameter and the length of the leader line
		:param chord_point:
		:param far_chord_point:
		:param leader_length:
		:return: AcadDimDiametric
		"""
		kwargs = {
			"ChordPoint": chord_point,
			"FarChordPoint": far_chord_point,
			"LeaderLength": leader_length
		}
		obj = self._me.AddDimDiametric(**kwargs)
		return self._add(obj)

	def DimOrdinate(self, definition_point, leader_end_point, use_xaxis: float):
		"""
		Creates an ordinate dimension given the definition point, and leader endpoint
		:param definition_point:
		:param leader_end_point:
		:param use_xaxis:
		:return: AcadDimOrdinate
		"""
		kwargs = {
			"DefinitionPoint": definition_point,
			"LeaderEndPoint": leader_end_point,
			"UseXAxis": use_xaxis
		}
		obj = self._me.AddDimOrdinate(**kwargs)
		return self._add(obj)

	def DimRadial(self, center, chord_point, leader_length: float):
		"""
		Creates a radial dimension for the selected object at the given location
		:param center:
		:param chord_point:
		:param leader_length:
		:return: AcadDimRadial
		"""
		kwargs = {
			"Center": center,
			"ChordPoint": chord_point,
			"LeaderLength": leader_length
		}
		obj = self._me.AddDimRadial(**kwargs)
		return self._add(obj)

	def DimRadialLarge(self, center, chord_point, override_center, jog_point, jog_angle: float):
		"""
		Creates a jogged radial dimension for an arc, circle, or polyline arc segment
		:param center:
		:param chord_point:
		:param override_center:
		:param jog_point:
		:param jog_angle:
		:return: AcadDimRadialLarge
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

	def DimRotated(self, ext_line_1_point, ext_line_2_point, dim_line_location, rotation_angle: float):
		"""
		Creates a rotated linear dimension
		:param ext_line_1_point:
		:param ext_line_2_point:
		:param dim_line_location:
		:param rotation_angle:
		:return: AcadDimRotated
		"""
		kwargs = {
			"ExtLine1Point": ext_line_1_point,
			"ExtLine2Point": ext_line_2_point,
			"DimLineLocation": dim_line_location,
			"RotationAngle": rotation_angle
		}
		obj = self._me.AddDimRotated(**kwargs)
		return self._add(obj)

	def Ellipse(self, center, major_axis, radius_ratio: float):
		"""
		Creates an ellipse in the XY plane of the WCS given the center point, a point on the major axis, and the radius ratio
		:param center: APoint
		:param major_axis: APoint
		:param radius_ratio: float
		:return: AcadEllipse
		"""
		kwargs = {
			"Center": center,
			"MajorAxis": major_axis,
			"RadiusRatio": radius_ratio
		}
		obj = self._me.AddEllipse(**kwargs)
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

