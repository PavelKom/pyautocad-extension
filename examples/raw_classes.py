

class AcadAcCmColor(POINTER(_dll.IAcadAcCmColor), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadAcCmColor
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadAcCmColor VBA-class wrapped as AcadAcCmColor python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadAcCmColor__com_Delete
	#	_IAcadAcCmColor__com_SetColorBookColor
	#	_IAcadAcCmColor__com_SetNames
	#	_IAcadAcCmColor__com_SetRGB
	#	_IAcadAcCmColor__com__get_Blue
	#	_IAcadAcCmColor__com__get_BookName
	#	_IAcadAcCmColor__com__get_ColorIndex
	#	_IAcadAcCmColor__com__get_ColorMethod
	#	_IAcadAcCmColor__com__get_ColorName
	#	_IAcadAcCmColor__com__get_EntityColor
	#	_IAcadAcCmColor__com__get_Green
	#	_IAcadAcCmColor__com__get_Red
	#	_IAcadAcCmColor__com__set_ColorIndex
	#	_IAcadAcCmColor__com__set_ColorMethod
	#	_IAcadAcCmColor__com__set_EntityColor
	# Methods
	def delete(self):
		"Deletes the true color."
		# VBA: object.Delete 
		self.com_parent.Delete()

	def setcolorbookcolor(self, BookName: str, ColorName: str):
		"Sets the color to a color from a color book."
		# ['in'] BookName:str
		# ['in'] ColorName:str
		# VBA: object.SetColorBookColor BookName, ColorName
		self.com_parent.SetColorBookColor(BookName, ColorName)

	def setnames(self, ColorName: str, BookName: str):
		"Specifies the color name and book name of the color."
		# ['in'] ColorName:str
		# ['in'] BookName:str
		# VBA: object.SetNames ColorName, BookName
		self.com_parent.SetNames(ColorName, BookName)

	def setrgb(self, Red: int, Green: int, Blue: int):
		"Specifies the RGB values of the true color."
		# ['in'] Red:int
		# ['in'] Green:int
		# ['in'] Blue:int
		# VBA: object.SetRGB Red, Green, Blue
		self.com_parent.SetRGB(Red, Green, Blue)

	# Properties
	@indexedproperty
	def blue(self) -> int:
		"Specifies the blue component of the true color."
		# TODO: Check arguments
		# ['out', 'retval'] Blue:int
		return self.com_parent.Blue

	@indexedproperty
	def bookname(self) -> str:
		"Specifies the book name (if any) of the color."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.BookName

	@indexedproperty
	def colorindex(self) -> int:
		"Specifies the color index."
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.ColorIndex
	@colorindex.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.ColorIndex = color

	@indexedproperty
	def colormethod(self) -> int:
		"Specifies the color method."
		# TODO: Check arguments
		# ['out', 'retval'] Flags:int
		return self.com_parent.ColorMethod
	@colormethod.setter
	def _(self, Flags:int):
		# ['in'] Flags:int
		self.com_parent.ColorMethod = Flags

	@indexedproperty
	def colorname(self) -> str:
		"Specifies the name (if any) of the color."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.ColorName

	@indexedproperty
	def entitycolor(self) -> int:
		"Specifies the AcCmEntityColor of the true color."
		# TODO: Check arguments
		# ['out', 'retval'] eColor:int
		return self.com_parent.EntityColor
	@entitycolor.setter
	def _(self, eColor:int):
		# ['in'] eColor:int
		self.com_parent.EntityColor = eColor

	@indexedproperty
	def green(self) -> int:
		"Specifies the green component of the true color."
		# TODO: Check arguments
		# ['out', 'retval'] Green:int
		return self.com_parent.Green

	@indexedproperty
	def red(self) -> int:
		"Specifies the red component of the true color."
		# TODO: Check arguments
		# ['out', 'retval'] Red:int
		return self.com_parent.Red


class AcadApplication(POINTER(_dll.IAcadApplication), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadApplication
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadApplication VBA-class wrapped as AcadApplication python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadApplication__com_Eval
	#	_IAcadApplication__com_GetAcadState
	#	_IAcadApplication__com_GetInterfaceObject
	#	_IAcadApplication__com_ListArx
	#	_IAcadApplication__com_LoadArx
	#	_IAcadApplication__com_LoadDVB
	#	_IAcadApplication__com_Quit
	#	_IAcadApplication__com_RunMacro
	#	_IAcadApplication__com_UnloadArx
	#	_IAcadApplication__com_UnloadDVB
	#	_IAcadApplication__com_Update
	#	_IAcadApplication__com_Zoom
	#	_IAcadApplication__com_ZoomAll
	#	_IAcadApplication__com_ZoomCenter
	#	_IAcadApplication__com_ZoomExtents
	#	_IAcadApplication__com_ZoomPickWindow
	#	_IAcadApplication__com_ZoomPrevious
	#	_IAcadApplication__com_ZoomScaled
	#	_IAcadApplication__com_ZoomWindow
	#	_IAcadApplication__com__get_ActiveDocument
	#	_IAcadApplication__com__get_Application
	#	_IAcadApplication__com__get_Caption
	#	_IAcadApplication__com__get_Documents
	#	_IAcadApplication__com__get_FullName
	#	_IAcadApplication__com__get_HWND
	#	_IAcadApplication__com__get_Height
	#	_IAcadApplication__com__get_LocaleId
	#	_IAcadApplication__com__get_MenuBar
	#	_IAcadApplication__com__get_MenuGroups
	#	_IAcadApplication__com__get_Name
	#	_IAcadApplication__com__get_Path
	#	_IAcadApplication__com__get_Preferences
	#	_IAcadApplication__com__get_StatusId
	#	_IAcadApplication__com__get_VBE
	#	_IAcadApplication__com__get_Version
	#	_IAcadApplication__com__get_Visible
	#	_IAcadApplication__com__get_Width
	#	_IAcadApplication__com__get_WindowLeft
	#	_IAcadApplication__com__get_WindowState
	#	_IAcadApplication__com__get_WindowTop
	#	_IAcadApplication__com__set_ActiveDocument
	#	_IAcadApplication__com__set_Height
	#	_IAcadApplication__com__set_Visible
	#	_IAcadApplication__com__set_Width
	#	_IAcadApplication__com__set_WindowLeft
	#	_IAcadApplication__com__set_WindowState
	#	_IAcadApplication__com__set_WindowTop
	# Methods
	def eval(self, Expression: str):
		"Evaluates an expression in VBA"
		# ['in'] Expression:str
		# VBA: object.Eval Expression
		self.com_parent.Eval(Expression)

	def getacadstate(self) -> AcadState:
		"Retrieves an AcadState object."
		# TODO: Check arguments
		# ['out', 'retval'] pVal:AcadState
		# VBA: pVal = object.GetAcadState ()
		return self.com_parent.GetAcadState()

	def getinterfaceobject(self, ProgID: str) -> POINTER(IDispatch):
		"Accepts a program ID and attempts to load it into AutoCAD as an in-process server"
		# TODO: Check arguments
		# ['in'] ProgID:str
		# ['out', 'retval'] pObj:POINTER(IDispatch)
		# VBA: pObj = object.GetInterfaceObject (ProgID)
		return self.com_parent.GetInterfaceObject(ProgID)

	def listarx(self) -> tagVARIANT:
		"Gets the currently loaded AutoCAD ARX applications"
		# TODO: Check arguments
		# ['out', 'retval'] pVarListArray:tagVARIANT
		# VBA: pVarListArray = object.ListArx ()
		return self.com_parent.ListArx()

	def loadarx(self, Name: str):
		"Loads the specified AutoCAD ARX application"
		# ['in'] Name:str
		# VBA: object.LoadArx Name
		self.com_parent.LoadArx(Name)

	def loaddvb(self, Name: str):
		"Loads the specified AutoCAD VBA project file"
		# ['in'] Name:str
		# VBA: object.LoadDVB Name
		self.com_parent.LoadDVB(Name)

	def quit(self):
		"Closes the drawing file and exits the AutoCAD application"
		# VBA: object.Quit 
		self.com_parent.Quit()

	def runmacro(self, MacroPath: str):
		"Runs a VBA macro from the Application object"
		# ['in'] MacroPath:str
		# VBA: object.RunMacro MacroPath
		self.com_parent.RunMacro(MacroPath)

	def unloadarx(self, Name: str):
		"Unloads the specified AutoCAD ARX application"
		# ['in'] Name:str
		# VBA: object.UnloadArx Name
		self.com_parent.UnloadArx(Name)

	def unloaddvb(self, Name: str):
		"Unloads the specified AutoCAD VBA project file"
		# ['in'] Name:str
		# VBA: object.UnloadDVB Name
		self.com_parent.UnloadDVB(Name)

	def update(self):
		"Updates the object to the drawing screen"
		# VBA: object.Update 
		self.com_parent.Update()

	def zoom(self, Type: int, vParams: tagVARIANT):
		"Zoom "
		# TODO: Check arguments
		# ['in'] Type:int
		# ['in'] vParams:tagVARIANT
		# VBA: object.Zoom Type, vParams
		self.com_parent.Zoom(Type, vParams)

	def zoomall(self):
		"Zooms the current viewport to display the entire drawing"
		# VBA: object.ZoomAll 
		self.com_parent.ZoomAll()

	def zoomcenter(self, Center: tagVARIANT, Magnify: float):
		"Zooms the current viewport to a specified center point and magnification"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Magnify:float
		# VBA: object.ZoomCenter Center, Magnify
		self.com_parent.ZoomCenter(Center, Magnify)

	def zoomextents(self):
		"Zooms the current viewport to the drawing extents"
		# VBA: object.ZoomExtents 
		self.com_parent.ZoomExtents()

	def zoompickwindow(self):
		"Zooms the current viewport to a window defined by points picked on the screen"
		# VBA: object.ZoomPickWindow 
		self.com_parent.ZoomPickWindow()

	def zoomprevious(self):
		"Zooms the current viewport to its previous extents"
		# VBA: object.ZoomPrevious 
		self.com_parent.ZoomPrevious()

	def zoomscaled(self, scale: float, ScaleType: int):
		"Zooms the current viewport to given scale factor"
		# ['in'] scale:float
		# ['in'] ScaleType:int
		# VBA: object.ZoomScaled scale, ScaleType
		self.com_parent.ZoomScaled(scale, ScaleType)

	def zoomwindow(self, LowerLeft: tagVARIANT, UpperRight: tagVARIANT):
		"Zooms the current viewport to the area specified by two opposite corners of a rectangle"
		# TODO: Check arguments
		# ['in'] LowerLeft:tagVARIANT
		# ['in'] UpperRight:tagVARIANT
		# VBA: object.ZoomWindow LowerLeft, UpperRight
		self.com_parent.ZoomWindow(LowerLeft, UpperRight)

	# Properties
	@indexedproperty
	def activedocument(self) -> AcadDocument:
		"Specifies the active document (drawing file)"
		# TODO: Check arguments
		# ['out', 'retval'] pActiveDoc:AcadDocument
		return self.com_parent.ActiveDocument
	@activedocument.setter
	def _(self, pActiveDoc:AcadDocument):
		# TODO: Check arguments
		# ['in'] pActiveDoc:AcadDocument
		self.com_parent.ActiveDocument = pActiveDoc

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def caption(self) -> str:
		"Gets the text that the user sees displayed for the application or a menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrCaption:str
		return self.com_parent.Caption

	@indexedproperty
	def documents(self) -> AcadDocuments:
		"Returns the documents collection."
		# TODO: Check arguments
		# ['out', 'retval'] pDocuments:AcadDocuments
		return self.com_parent.Documents

	@indexedproperty
	def fullname(self) -> str:
		"Gets the name of the application or document, including the path"
		# TODO: Check arguments
		# ['out', 'retval'] FullName:str
		return self.com_parent.FullName

	@indexedproperty
	def height(self) -> int:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Height:int
		return self.com_parent.Height
	@height.setter
	def _(self, Height:int):
		# ['in'] Height:int
		self.com_parent.Height = Height

	@indexedproperty
	def hwnd(self) -> int:
		"Gets the window handle of the application window frame"
		# TODO: Check arguments
		# ['out', 'retval'] HWND:int
		return self.com_parent.HWND

	@indexedproperty
	def localeid(self) -> int:
		"Gets the locale ID of the current AutoCAD session"
		# TODO: Check arguments
		# ['out', 'retval'] lcid:int
		return self.com_parent.LocaleId

	@indexedproperty
	def menubar(self) -> AcadMenuBar:
		"Gets the MenuBar object for the session"
		# TODO: Check arguments
		# ['out', 'retval'] pMenuBar:AcadMenuBar
		return self.com_parent.MenuBar

	@indexedproperty
	def menugroups(self) -> AcadMenuGroups:
		"Gets the MenuGroups collection for the session"
		# TODO: Check arguments
		# ['out', 'retval'] pMenuGroups:AcadMenuGroups
		return self.com_parent.MenuGroups

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppName:str
		return self.com_parent.Name

	@indexedproperty
	def path(self) -> str:
		"Gets the path of the document, application, or external reference"
		# TODO: Check arguments
		# ['out', 'retval'] bstrPath:str
		return self.com_parent.Path

	@indexedproperty
	def preferences(self) -> AcadPreferences:
		"Gets the Preferences object"
		# TODO: Check arguments
		# ['out', 'retval'] pPreferences:AcadPreferences
		return self.com_parent.Preferences

	@indexedproperty
	def statusid(self, VportObj:POINTER(IDispatch)) -> bool:
		"Gets the current active status of the viewport"
		# TODO: Check arguments
		# ['in'] VportObj:POINTER(IDispatch)
		# ['out', 'retval'] bStatus:bool
		return self.com_parent.StatusId[VportObj]

	@indexedproperty
	def vbe(self) -> POINTER(IDispatch):
		"Gets the VBAIDE extensibility object"
		# TODO: Check arguments
		# ['out', 'retval'] pDispVBE:POINTER(IDispatch)
		return self.com_parent.VBE

	@indexedproperty
	def version(self) -> str:
		"Gets the version of the AutoCAD application you are using"
		# TODO: Check arguments
		# ['out', 'retval'] bstrVer:str
		return self.com_parent.Version

	@indexedproperty
	def visible(self) -> bool:
		"Specifies the visibility of an object or the application"
		# TODO: Check arguments
		# ['out', 'retval'] Visible:bool
		return self.com_parent.Visible
	@visible.setter
	def _(self, Visible:bool):
		# ['in'] Visible:bool
		self.com_parent.Visible = Visible

	@indexedproperty
	def width(self) -> int:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Width:int
		return self.com_parent.Width
	@width.setter
	def _(self, Width:int):
		# ['in'] Width:int
		self.com_parent.Width = Width

	@indexedproperty
	def windowleft(self) -> int:
		"Specifies the left edge of the application window"
		# TODO: Check arguments
		# ['out', 'retval'] left:int
		return self.com_parent.WindowLeft
	@windowleft.setter
	def _(self, left:int):
		# ['in'] left:int
		self.com_parent.WindowLeft = left

	@indexedproperty
	def windowstate(self) -> int:
		"Specifies the state of the application or document window"
		# TODO: Check arguments
		# ['out', 'retval'] eWinState:int
		return self.com_parent.WindowState
	@windowstate.setter
	def _(self, eWinState:int):
		# ['in'] eWinState:int
		self.com_parent.WindowState = eWinState

	@indexedproperty
	def windowtop(self) -> int:
		"Specifies the top edge of the application window"
		# TODO: Check arguments
		# ['out', 'retval'] top:int
		return self.com_parent.WindowTop
	@windowtop.setter
	def _(self, top:int):
		# ['in'] top:int
		self.com_parent.WindowTop = top


class AcadBlock(POINTER(_dll.IAcadBlock), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadBlock
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadBlock VBA-class wrapped as AcadBlock python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadBlock__com_Add3DFace
	#	_IAcadBlock__com_Add3DMesh
	#	_IAcadBlock__com_Add3DPoly
	#	_IAcadBlock__com_AddArc
	#	_IAcadBlock__com_AddAttribute
	#	_IAcadBlock__com_AddBox
	#	_IAcadBlock__com_AddCircle
	#	_IAcadBlock__com_AddCone
	#	_IAcadBlock__com_AddCustomObject
	#	_IAcadBlock__com_AddCylinder
	#	_IAcadBlock__com_AddDim3PointAngular
	#	_IAcadBlock__com_AddDimAligned
	#	_IAcadBlock__com_AddDimAngular
	#	_IAcadBlock__com_AddDimArc
	#	_IAcadBlock__com_AddDimDiametric
	#	_IAcadBlock__com_AddDimOrdinate
	#	_IAcadBlock__com_AddDimRadial
	#	_IAcadBlock__com_AddDimRadialLarge
	#	_IAcadBlock__com_AddDimRotated
	#	_IAcadBlock__com_AddEllipse
	#	_IAcadBlock__com_AddEllipticalCone
	#	_IAcadBlock__com_AddEllipticalCylinder
	#	_IAcadBlock__com_AddExtrudedSolid
	#	_IAcadBlock__com_AddExtrudedSolidAlongPath
	#	_IAcadBlock__com_AddHatch
	#	_IAcadBlock__com_AddLeader
	#	_IAcadBlock__com_AddLightWeightPolyline
	#	_IAcadBlock__com_AddLine
	#	_IAcadBlock__com_AddMInsertBlock
	#	_IAcadBlock__com_AddMLeader
	#	_IAcadBlock__com_AddMLine
	#	_IAcadBlock__com_AddMText
	#	_IAcadBlock__com_AddPoint
	#	_IAcadBlock__com_AddPolyfaceMesh
	#	_IAcadBlock__com_AddPolyline
	#	_IAcadBlock__com_AddRaster
	#	_IAcadBlock__com_AddRay
	#	_IAcadBlock__com_AddRegion
	#	_IAcadBlock__com_AddRevolvedSolid
	#	_IAcadBlock__com_AddSection
	#	_IAcadBlock__com_AddShape
	#	_IAcadBlock__com_AddSolid
	#	_IAcadBlock__com_AddSphere
	#	_IAcadBlock__com_AddSpline
	#	_IAcadBlock__com_AddTable
	#	_IAcadBlock__com_AddText
	#	_IAcadBlock__com_AddTolerance
	#	_IAcadBlock__com_AddTorus
	#	_IAcadBlock__com_AddTrace
	#	_IAcadBlock__com_AddWedge
	#	_IAcadBlock__com_AddXline
	#	_IAcadBlock__com_AttachExternalReference
	#	_IAcadBlock__com_Bind
	#	_IAcadBlock__com_Detach
	#	_IAcadBlock__com_InsertBlock
	#	_IAcadBlock__com_Item
	#	_IAcadBlock__com_Reload
	#	_IAcadBlock__com_Unload
	#	_IAcadBlock__com__get_BlockScaling
	#	_IAcadBlock__com__get_Comments
	#	_IAcadBlock__com__get_Count
	#	_IAcadBlock__com__get_Explodable
	#	_IAcadBlock__com__get_IsDynamicBlock
	#	_IAcadBlock__com__get_IsLayout
	#	_IAcadBlock__com__get_IsXRef
	#	_IAcadBlock__com__get_Layout
	#	_IAcadBlock__com__get_Name
	#	_IAcadBlock__com__get_Origin
	#	_IAcadBlock__com__get_Path
	#	_IAcadBlock__com__get_Units
	#	_IAcadBlock__com__get_XRefDatabase
	#	_IAcadBlock__com__get__NewEnum
	#	_IAcadBlock__com__set_BlockScaling
	#	_IAcadBlock__com__set_Comments
	#	_IAcadBlock__com__set_Explodable
	#	_IAcadBlock__com__set_Name
	#	_IAcadBlock__com__set_Origin
	#	_IAcadBlock__com__set_Path
	#	_IAcadBlock__com__set_Units
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add3dface(self, Point1: tagVARIANT, Point2: tagVARIANT, point3: tagVARIANT, Point4: tagVARIANT) -> Acad3DFace:
		"Creates a 3DFace object given four vertices"
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['in'] point3:tagVARIANT
		# ['in'] Point4:tagVARIANT
		# ['out', 'retval'] pFace3d:Acad3DFace
		# VBA: pFace3d = object.Add3DFace (Point1, Point2, point3, Point4)
		return self.com_parent.Add3DFace(Point1, Point2, point3, Point4)

	def add3dmesh(self, M: int, N: int, PointsMatrix: tagVARIANT) -> AcadPolygonMesh:
		"Creates a free-form 3D mesh, given the number of points in the M and N directions and the coordinates of the points in the M and N directions"
		# TODO: Check arguments
		# ['in'] M:int
		# ['in'] N:int
		# ['in'] PointsMatrix:tagVARIANT
		# ['out', 'retval'] pMesh3d:AcadPolygonMesh
		# VBA: pMesh3d = object.Add3DMesh (M, N, PointsMatrix)
		return self.com_parent.Add3DMesh(M, N, PointsMatrix)

	def add3dpoly(self, PointsArray: tagVARIANT) -> Acad3DPolyline:
		"Creates a 3D polyline from the given array of coordinates"
		# TODO: Check arguments
		# ['in'] PointsArray:tagVARIANT
		# ['out', 'retval'] pPoly3d:Acad3DPolyline
		# VBA: pPoly3d = object.Add3DPoly (PointsArray)
		return self.com_parent.Add3DPoly(PointsArray)

	def addarc(self, Center: tagVARIANT, Radius: float, StartAngle: float, EndAngle: float) -> AcadArc:
		"Creates an arc given the center, radius, start angle, and end angle of the arc"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Radius:float
		# ['in'] StartAngle:float
		# ['in'] EndAngle:float
		# ['out', 'retval'] pArc:AcadArc
		# VBA: pArc = object.AddArc (Center, Radius, StartAngle, EndAngle)
		return self.com_parent.AddArc(Center, Radius, StartAngle, EndAngle)

	def addattribute(self, Height: float, Mode: int, Prompt: str, InsertionPoint: tagVARIANT, Tag: str, Value: str) -> AcadAttribute:
		"Creates an attribute definition at the given location with the specified properties"
		# TODO: Check arguments
		# ['in'] Height:float
		# ['in'] Mode:int
		# ['in'] Prompt:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Tag:str
		# ['in'] Value:str
		# ['out', 'retval'] pAttr:AcadAttribute
		# VBA: pAttr = object.AddAttribute (Height, Mode, Prompt, InsertionPoint, Tag, Value)
		return self.com_parent.AddAttribute(Height, Mode, Prompt, InsertionPoint, Tag, Value)

	def addbox(self, Origin: tagVARIANT, Length: float, Width: float, Height: float) -> Acad3DSolid:
		"Creates a 3D solid box with edges parallel to the axes of the WCS"
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT
		# ['in'] Length:float
		# ['in'] Width:float
		# ['in'] Height:float
		# ['out', 'retval'] pBox:Acad3DSolid
		# VBA: pBox = object.AddBox (Origin, Length, Width, Height)
		return self.com_parent.AddBox(Origin, Length, Width, Height)

	def addcircle(self, Center: tagVARIANT, Radius: float) -> AcadCircle:
		"Creates a circle given a center point and radius"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Radius:float
		# ['out', 'retval'] pCircle:AcadCircle
		# VBA: pCircle = object.AddCircle (Center, Radius)
		return self.com_parent.AddCircle(Center, Radius)

	def addcone(self, Center: tagVARIANT, BaseRadius: float, Height: float) -> Acad3DSolid:
		"Creates a 3D solid cone with the base on the XY plane of the WCS"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] BaseRadius:float
		# ['in'] Height:float
		# ['out', 'retval'] pCone:Acad3DSolid
		# VBA: pCone = object.AddCone (Center, BaseRadius, Height)
		return self.com_parent.AddCone(Center, BaseRadius, Height)

	def addcustomobject(self, ClassName: str) -> POINTER(IDispatch):
		"Creates a Custom object"
		# TODO: Check arguments
		# ['in'] ClassName:str
		# ['out', 'retval'] pObject:POINTER(IDispatch)
		# VBA: pObject = object.AddCustomObject (ClassName)
		return self.com_parent.AddCustomObject(ClassName)

	def addcylinder(self, Center: tagVARIANT, Radius: float, Height: float) -> Acad3DSolid:
		"Creates a 3D solid cylinder whose base is on the XY plane of the WCS"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Radius:float
		# ['in'] Height:float
		# ['out', 'retval'] pCyl:Acad3DSolid
		# VBA: pCyl = object.AddCylinder (Center, Radius, Height)
		return self.com_parent.AddCylinder(Center, Radius, Height)

	def adddim3pointangular(self, AngleVertex: tagVARIANT, FirstEndPoint: tagVARIANT, SecondEndPoint: tagVARIANT, TextPoint: tagVARIANT) -> AcadDim3PointAngular:
		"Creates an angular dimension for an arc, two lines, or a circle"
		# TODO: Check arguments
		# ['in'] AngleVertex:tagVARIANT
		# ['in'] FirstEndPoint:tagVARIANT
		# ['in'] SecondEndPoint:tagVARIANT
		# ['in'] TextPoint:tagVARIANT
		# ['out', 'retval'] pDim:AcadDim3PointAngular
		# VBA: pDim = object.AddDim3PointAngular (AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint)
		return self.com_parent.AddDim3PointAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint)

	def adddimaligned(self, ExtLine1Point: tagVARIANT, ExtLine2Point: tagVARIANT, TextPosition: tagVARIANT) -> AcadDimAligned:
		"Creates an aligned dimension object"
		# TODO: Check arguments
		# ['in'] ExtLine1Point:tagVARIANT
		# ['in'] ExtLine2Point:tagVARIANT
		# ['in'] TextPosition:tagVARIANT
		# ['out', 'retval'] pDim:AcadDimAligned
		# VBA: pDim = object.AddDimAligned (ExtLine1Point, ExtLine2Point, TextPosition)
		return self.com_parent.AddDimAligned(ExtLine1Point, ExtLine2Point, TextPosition)

	def adddimangular(self, AngleVertex: tagVARIANT, FirstEndPoint: tagVARIANT, SecondEndPoint: tagVARIANT, TextPoint: tagVARIANT) -> AcadDimAngular:
		"Creates an angular dimension for an arc, two lines, or a circle"
		# TODO: Check arguments
		# ['in'] AngleVertex:tagVARIANT
		# ['in'] FirstEndPoint:tagVARIANT
		# ['in'] SecondEndPoint:tagVARIANT
		# ['in'] TextPoint:tagVARIANT
		# ['out', 'retval'] pDim:AcadDimAngular
		# VBA: pDim = object.AddDimAngular (AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint)
		return self.com_parent.AddDimAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint)

	def adddimarc(self, ArcCenter: tagVARIANT, FirstEndPoint: tagVARIANT, SecondEndPoint: tagVARIANT, ArcPoint: tagVARIANT) -> AcadDimArcLength:
		"Creates an arc length dimension for an arc"
		# TODO: Check arguments
		# ['in'] ArcCenter:tagVARIANT
		# ['in'] FirstEndPoint:tagVARIANT
		# ['in'] SecondEndPoint:tagVARIANT
		# ['in'] ArcPoint:tagVARIANT
		# ['out', 'retval'] pDim:AcadDimArcLength
		# VBA: pDim = object.AddDimArc (ArcCenter, FirstEndPoint, SecondEndPoint, ArcPoint)
		return self.com_parent.AddDimArc(ArcCenter, FirstEndPoint, SecondEndPoint, ArcPoint)

	def adddimdiametric(self, ChordPoint: tagVARIANT, FarChordPoint: tagVARIANT, LeaderLength: float) -> AcadDimDiametric:
		"Creates a diametric dimension for a circle or arc given the two points on the diameter and the length of the leader line"
		# TODO: Check arguments
		# ['in'] ChordPoint:tagVARIANT
		# ['in'] FarChordPoint:tagVARIANT
		# ['in'] LeaderLength:float
		# ['out', 'retval'] pDim:AcadDimDiametric
		# VBA: pDim = object.AddDimDiametric (ChordPoint, FarChordPoint, LeaderLength)
		return self.com_parent.AddDimDiametric(ChordPoint, FarChordPoint, LeaderLength)

	def adddimordinate(self, DefinitionPoint: tagVARIANT, LeaderEndPoint: tagVARIANT, UseXAxis: int) -> AcadDimOrdinate:
		"Creates an ordinate dimension given the definition point, and leader endpoint"
		# TODO: Check arguments
		# ['in'] DefinitionPoint:tagVARIANT
		# ['in'] LeaderEndPoint:tagVARIANT
		# ['in'] UseXAxis:int
		# ['out', 'retval'] pDim:AcadDimOrdinate
		# VBA: pDim = object.AddDimOrdinate (DefinitionPoint, LeaderEndPoint, UseXAxis)
		return self.com_parent.AddDimOrdinate(DefinitionPoint, LeaderEndPoint, UseXAxis)

	def adddimradial(self, Center: tagVARIANT, ChordPoint: tagVARIANT, LeaderLength: float) -> AcadDimRadial:
		"Creates a radial dimension for the selected object at the given location"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] ChordPoint:tagVARIANT
		# ['in'] LeaderLength:float
		# ['out', 'retval'] pDim:AcadDimRadial
		# VBA: pDim = object.AddDimRadial (Center, ChordPoint, LeaderLength)
		return self.com_parent.AddDimRadial(Center, ChordPoint, LeaderLength)

	def adddimradiallarge(self, Center: tagVARIANT, ChordPoint: tagVARIANT, OverrideCenter: tagVARIANT, JogPoint: tagVARIANT, JogAngle: float) -> AcadDimRadialLarge:
		"Creates a jogged radial dimension for an arc, circle, or polyline arc segment"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] ChordPoint:tagVARIANT
		# ['in'] OverrideCenter:tagVARIANT
		# ['in'] JogPoint:tagVARIANT
		# ['in'] JogAngle:float
		# ['out', 'retval'] pDim:AcadDimRadialLarge
		# VBA: pDim = object.AddDimRadialLarge (Center, ChordPoint, OverrideCenter, JogPoint, JogAngle)
		return self.com_parent.AddDimRadialLarge(Center, ChordPoint, OverrideCenter, JogPoint, JogAngle)

	def adddimrotated(self, ExtLine1Point: tagVARIANT, ExtLine2Point: tagVARIANT, DimLineLocation: tagVARIANT, RotationAngle: float) -> AcadDimRotated:
		"Creates a rotated linear dimension"
		# TODO: Check arguments
		# ['in'] ExtLine1Point:tagVARIANT
		# ['in'] ExtLine2Point:tagVARIANT
		# ['in'] DimLineLocation:tagVARIANT
		# ['in'] RotationAngle:float
		# ['out', 'retval'] pDim:AcadDimRotated
		# VBA: pDim = object.AddDimRotated (ExtLine1Point, ExtLine2Point, DimLineLocation, RotationAngle)
		return self.com_parent.AddDimRotated(ExtLine1Point, ExtLine2Point, DimLineLocation, RotationAngle)

	def addellipse(self, Center: tagVARIANT, MajorAxis: tagVARIANT, RadiusRatio: float) -> AcadEllipse:
		"Creates an ellipse in the XY plane of the WCS given the center point, a point on the major axis, and the radius ratio"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] MajorAxis:tagVARIANT
		# ['in'] RadiusRatio:float
		# ['out', 'retval'] pEllipse:AcadEllipse
		# VBA: pEllipse = object.AddEllipse (Center, MajorAxis, RadiusRatio)
		return self.com_parent.AddEllipse(Center, MajorAxis, RadiusRatio)

	def addellipticalcone(self, Center: tagVARIANT, MajorRadius: float, MinorRadius: float, Height: float) -> Acad3DSolid:
		"Creates a 3D solid elliptical cone on the XY plane of the WCS given the Center, MajorRadius, MinorRadius, and Height"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] MajorRadius:float
		# ['in'] MinorRadius:float
		# ['in'] Height:float
		# ['out', 'retval'] pEllipCone:Acad3DSolid
		# VBA: pEllipCone = object.AddEllipticalCone (Center, MajorRadius, MinorRadius, Height)
		return self.com_parent.AddEllipticalCone(Center, MajorRadius, MinorRadius, Height)

	def addellipticalcylinder(self, Center: tagVARIANT, MajorRadius: float, MinorRadius: float, Height: float) -> Acad3DSolid:
		"Creates a 3D solid elliptical cylinder whose base is on the XY plane of the WCS, given the Center, MajorRadius, MinorRadius, and Height"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] MajorRadius:float
		# ['in'] MinorRadius:float
		# ['in'] Height:float
		# ['out', 'retval'] pEllipCyl:Acad3DSolid
		# VBA: pEllipCyl = object.AddEllipticalCylinder (Center, MajorRadius, MinorRadius, Height)
		return self.com_parent.AddEllipticalCylinder(Center, MajorRadius, MinorRadius, Height)

	def addextrudedsolid(self, Profile: AcadRegion, Height: float, TaperAngle: float) -> Acad3DSolid:
		"Creates an extruded solid given the Profile, Height, and TaperAngle"
		# TODO: Check arguments
		# ['in'] Profile:AcadRegion
		# ['in'] Height:float
		# ['in'] TaperAngle:float
		# ['out', 'retval'] pExtrSolid:Acad3DSolid
		# VBA: pExtrSolid = object.AddExtrudedSolid (Profile, Height, TaperAngle)
		return self.com_parent.AddExtrudedSolid(Profile, Height, TaperAngle)

	def addextrudedsolidalongpath(self, Profile: AcadRegion, Path: POINTER(IDispatch)) -> Acad3DSolid:
		"Creates an extruded solid given the profile and an extrusion path"
		# TODO: Check arguments
		# ['in'] Profile:AcadRegion
		# ['in'] Path:POINTER(IDispatch)
		# ['out', 'retval'] pExtrSolid:Acad3DSolid
		# VBA: pExtrSolid = object.AddExtrudedSolidAlongPath (Profile, Path)
		return self.com_parent.AddExtrudedSolidAlongPath(Profile, Path)

	def addhatch(self, PatternType: int, PatternName: str, Associativity: bool, HatchObjectType: tagVARIANT) -> AcadHatch:
		"Creates a Hatch object"
		# TODO: Check arguments
		# ['in'] PatternType:int
		# ['in'] PatternName:str
		# ['in'] Associativity:bool
		# ['in', '16'] HatchObjectType:tagVARIANT
		# ['out', 'retval'] pHatch:AcadHatch
		# VBA: pHatch = object.AddHatch (PatternType, PatternName, Associativity, HatchObjectType)
		return self.com_parent.AddHatch(PatternType, PatternName, Associativity, HatchObjectType)

	def addleader(self, PointsArray: tagVARIANT, Annotation: AcadEntity, Type: int) -> AcadLeader:
		"Creates a leader line, given the coordinates of the points"
		# TODO: Check arguments
		# ['in'] PointsArray:tagVARIANT
		# ['in'] Annotation:AcadEntity
		# ['in'] Type:int
		# ['out', 'retval'] pLeader:AcadLeader
		# VBA: pLeader = object.AddLeader (PointsArray, Annotation, Type)
		return self.com_parent.AddLeader(PointsArray, Annotation, Type)

	def addlightweightpolyline(self, VerticesList: tagVARIANT) -> AcadLWPolyline:
		"Creates a lightweight polyline from a list of vertices"
		# TODO: Check arguments
		# ['in'] VerticesList:tagVARIANT
		# ['out', 'retval'] pLWPolyline:AcadLWPolyline
		# VBA: pLWPolyline = object.AddLightWeightPolyline (VerticesList)
		return self.com_parent.AddLightWeightPolyline(VerticesList)

	def addline(self, StartPoint: tagVARIANT, EndPoint: tagVARIANT) -> AcadLine:
		"Creates a line passing through two points"
		# TODO: Check arguments
		# ['in'] StartPoint:tagVARIANT
		# ['in'] EndPoint:tagVARIANT
		# ['out', 'retval'] pLine:AcadLine
		# VBA: pLine = object.AddLine (StartPoint, EndPoint)
		return self.com_parent.AddLine(StartPoint, EndPoint)

	def addminsertblock(self, InsertionPoint: tagVARIANT, Name: str, Xscale: float, Yscale: float, Zscale: float, Rotation: float, NumRows: int, NumColumns: int, RowSpacing: int, ColumnSpacing: int, Password: tagVARIANT) -> AcadMInsertBlock:
		"Inserts an array of blocks"
		# TODO: Check arguments
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Name:str
		# ['in'] Xscale:float
		# ['in'] Yscale:float
		# ['in'] Zscale:float
		# ['in'] Rotation:float
		# ['in'] NumRows:int
		# ['in'] NumColumns:int
		# ['in'] RowSpacing:int
		# ['in'] ColumnSpacing:int
		# ['in', '16'] Password:tagVARIANT
		# ['out', 'retval'] pMInsertBlk:AcadMInsertBlock
		# VBA: pMInsertBlk = object.AddMInsertBlock (InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, NumRows, NumColumns, RowSpacing, ColumnSpacing, Password)
		return self.com_parent.AddMInsertBlock(InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, NumRows, NumColumns, RowSpacing, ColumnSpacing, Password)

	def addmleader(self, PointsArray: tagVARIANT):
		"Creates a multileader"
		# TODO: Check arguments
		# ['in'] PointsArray:tagVARIANT
		# ['out'] leaderLineIndex:int
		# ['out', 'retval'] pMLeader:AcadMLeader
		# VBA: pMLeader = object.AddMLeader (PointsArray, leaderLineIndex)
		return self.com_parent.AddMLeader(PointsArray)

	def addmline(self, VertexList: tagVARIANT) -> AcadMLine:
		"Creates a polyface mesh from a list of vertices"
		# TODO: Check arguments
		# ['in'] VertexList:tagVARIANT
		# ['out', 'retval'] pMLine:AcadMLine
		# VBA: pMLine = object.AddMLine (VertexList)
		return self.com_parent.AddMLine(VertexList)

	def addmtext(self, InsertionPoint: tagVARIANT, Width: float, Text: str) -> AcadMText:
		"Creates an MText entity in a rectangle defined by the insertion point and width of the bounding box"
		# TODO: Check arguments
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Width:float
		# ['in'] Text:str
		# ['out', 'retval'] pMtext:AcadMText
		# VBA: pMtext = object.AddMText (InsertionPoint, Width, Text)
		return self.com_parent.AddMText(InsertionPoint, Width, Text)

	def addpoint(self, Point: tagVARIANT) -> AcadPoint:
		"Creates a Point object at a given location"
		# TODO: Check arguments
		# ['in'] Point:tagVARIANT
		# ['out', 'retval'] pPoint:AcadPoint
		# VBA: pPoint = object.AddPoint (Point)
		return self.com_parent.AddPoint(Point)

	def addpolyfacemesh(self, VertexList: tagVARIANT, FaceList: tagVARIANT) -> AcadPolyfaceMesh:
		"Creates a polyface mesh from a list of vertices"
		# TODO: Check arguments
		# ['in'] VertexList:tagVARIANT
		# ['in'] FaceList:tagVARIANT
		# ['out', 'retval'] pPFMesh:AcadPolyfaceMesh
		# VBA: pPFMesh = object.AddPolyfaceMesh (VertexList, FaceList)
		return self.com_parent.AddPolyfaceMesh(VertexList, FaceList)

	def addpolyline(self, VerticesList: tagVARIANT) -> AcadPolyline:
		"Creates a polyline from a list of vertices"
		# TODO: Check arguments
		# ['in'] VerticesList:tagVARIANT
		# ['out', 'retval'] pPolyline:AcadPolyline
		# VBA: pPolyline = object.AddPolyline (VerticesList)
		return self.com_parent.AddPolyline(VerticesList)

	def addraster(self, imageFileName: str, InsertionPoint: tagVARIANT, ScaleFactor: float, RotationAngle: float) -> AcadRasterImage:
		"Creates a new raster image based on an existing image file"
		# TODO: Check arguments
		# ['in'] imageFileName:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] ScaleFactor:float
		# ['in'] RotationAngle:float
		# ['out', 'retval'] pRaster:AcadRasterImage
		# VBA: pRaster = object.AddRaster (imageFileName, InsertionPoint, ScaleFactor, RotationAngle)
		return self.com_parent.AddRaster(imageFileName, InsertionPoint, ScaleFactor, RotationAngle)

	def addray(self, Point1: tagVARIANT, Point2: tagVARIANT) -> AcadRay:
		"Creates a ray passing through two unique points"
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['out', 'retval'] pRay:AcadRay
		# VBA: pRay = object.AddRay (Point1, Point2)
		return self.com_parent.AddRay(Point1, Point2)

	def addregion(self, ObjectList: tagVARIANT) -> tagVARIANT:
		"Creates a region from a set of entities. The given entities must form a closed coplanar region"
		# TODO: Check arguments
		# ['in'] ObjectList:tagVARIANT
		# ['out', 'retval'] pRegions:tagVARIANT
		# VBA: pRegions = object.AddRegion (ObjectList)
		return self.com_parent.AddRegion(ObjectList)

	def addrevolvedsolid(self, Profile: AcadRegion, AxisPoint: tagVARIANT, AxisDir: tagVARIANT, Angle: float) -> Acad3DSolid:
		"Creates a revolved solid, given the region around an axis"
		# TODO: Check arguments
		# ['in'] Profile:AcadRegion
		# ['in'] AxisPoint:tagVARIANT
		# ['in'] AxisDir:tagVARIANT
		# ['in'] Angle:float
		# ['out', 'retval'] pRevolSolid:Acad3DSolid
		# VBA: pRevolSolid = object.AddRevolvedSolid (Profile, AxisPoint, AxisDir, Angle)
		return self.com_parent.AddRevolvedSolid(Profile, AxisPoint, AxisDir, Angle)

	def addsection(self, FromPoint: tagVARIANT, ToPoint: tagVARIANT, planeVector: tagVARIANT) -> AcadSection:
		"Creates a section plane"
		# TODO: Check arguments
		# ['in'] FromPoint:tagVARIANT
		# ['in'] ToPoint:tagVARIANT
		# ['in'] planeVector:tagVARIANT
		# ['out', 'retval'] ppSecPlane:AcadSection
		# VBA: ppSecPlane = object.AddSection (FromPoint, ToPoint, planeVector)
		return self.com_parent.AddSection(FromPoint, ToPoint, planeVector)

	def addshape(self, Name: str, InsertionPoint: tagVARIANT, ScaleFactor: float, RotationAngle: float) -> AcadShape:
		"Creates a Shape object based on a template identified by name, at the given insertion point, scale factor, and rotation"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] ScaleFactor:float
		# ['in'] RotationAngle:float
		# ['out', 'retval'] pShape:AcadShape
		# VBA: pShape = object.AddShape (Name, InsertionPoint, ScaleFactor, RotationAngle)
		return self.com_parent.AddShape(Name, InsertionPoint, ScaleFactor, RotationAngle)

	def addsolid(self, Point1: tagVARIANT, Point2: tagVARIANT, point3: tagVARIANT, Point4: tagVARIANT) -> AcadSolid:
		"Creates a 2D solid polygon"
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['in'] point3:tagVARIANT
		# ['in'] Point4:tagVARIANT
		# ['out', 'retval'] pSolid:AcadSolid
		# VBA: pSolid = object.AddSolid (Point1, Point2, point3, Point4)
		return self.com_parent.AddSolid(Point1, Point2, point3, Point4)

	def addsphere(self, Center: tagVARIANT, Radius: float) -> Acad3DSolid:
		"Creates a sphere given the center and radius"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Radius:float
		# ['out', 'retval'] pSphere:Acad3DSolid
		# VBA: pSphere = object.AddSphere (Center, Radius)
		return self.com_parent.AddSphere(Center, Radius)

	def addspline(self, PointsArray: tagVARIANT, StartTangent: tagVARIANT, EndTangent: tagVARIANT) -> AcadSpline:
		"Creates a quadratic or cubic NURBS (nonuniform rational B-spline) curve"
		# TODO: Check arguments
		# ['in'] PointsArray:tagVARIANT
		# ['in'] StartTangent:tagVARIANT
		# ['in'] EndTangent:tagVARIANT
		# ['out', 'retval'] pSpline:AcadSpline
		# VBA: pSpline = object.AddSpline (PointsArray, StartTangent, EndTangent)
		return self.com_parent.AddSpline(PointsArray, StartTangent, EndTangent)

	def addtable(self, InsertionPoint: tagVARIANT, NumRows: int, NumColumns: int, RowHeight: float, ColWidth: float) -> AcadTable:
		"Creates a table at the given insertion point, given the number of rows, number of columns, row height and column width"
		# TODO: Check arguments
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] NumRows:int
		# ['in'] NumColumns:int
		# ['in'] RowHeight:float
		# ['in'] ColWidth:float
		# ['out', 'retval'] pTable:AcadTable
		# VBA: pTable = object.AddTable (InsertionPoint, NumRows, NumColumns, RowHeight, ColWidth)
		return self.com_parent.AddTable(InsertionPoint, NumRows, NumColumns, RowHeight, ColWidth)

	def addtext(self, TextString: str, InsertionPoint: tagVARIANT, Height: float) -> AcadText:
		"Creates a single line of text"
		# TODO: Check arguments
		# ['in'] TextString:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Height:float
		# ['out', 'retval'] pText:AcadText
		# VBA: pText = object.AddText (TextString, InsertionPoint, Height)
		return self.com_parent.AddText(TextString, InsertionPoint, Height)

	def addtolerance(self, Text: str, InsertionPoint: tagVARIANT, Direction: tagVARIANT) -> AcadTolerance:
		"Creates a tolerance entity"
		# TODO: Check arguments
		# ['in'] Text:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Direction:tagVARIANT
		# ['out', 'retval'] pTolerance:AcadTolerance
		# VBA: pTolerance = object.AddTolerance (Text, InsertionPoint, Direction)
		return self.com_parent.AddTolerance(Text, InsertionPoint, Direction)

	def addtorus(self, Center: tagVARIANT, TorusRadius: float, TubeRadius: float) -> Acad3DSolid:
		"Creates a torus at the given location"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] TorusRadius:float
		# ['in'] TubeRadius:float
		# ['out', 'retval'] pTorus:Acad3DSolid
		# VBA: pTorus = object.AddTorus (Center, TorusRadius, TubeRadius)
		return self.com_parent.AddTorus(Center, TorusRadius, TubeRadius)

	def addtrace(self, PointsArray: tagVARIANT) -> AcadTrace:
		"Creates a Trace object from an array of points"
		# TODO: Check arguments
		# ['in'] PointsArray:tagVARIANT
		# ['out', 'retval'] pTrace:AcadTrace
		# VBA: pTrace = object.AddTrace (PointsArray)
		return self.com_parent.AddTrace(PointsArray)

	def addwedge(self, Center: tagVARIANT, Length: float, Width: float, Height: float) -> Acad3DSolid:
		"Creates a wedge with edges parallel to the axes given the length, width, and height"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Length:float
		# ['in'] Width:float
		# ['in'] Height:float
		# ['out', 'retval'] pWedge:Acad3DSolid
		# VBA: pWedge = object.AddWedge (Center, Length, Width, Height)
		return self.com_parent.AddWedge(Center, Length, Width, Height)

	def addxline(self, Point1: tagVARIANT, Point2: tagVARIANT) -> AcadXline:
		"Creates an xline (an infinite line) passing through two specified points"
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['out', 'retval'] pXline:AcadXline
		# VBA: pXline = object.AddXline (Point1, Point2)
		return self.com_parent.AddXline(Point1, Point2)

	def attachexternalreference(self, PathName: str, Name: str, InsertionPoint: tagVARIANT, Xscale: float, Yscale: float, Zscale: float, Rotation: float, bOverlay: bool, Password: tagVARIANT) -> AcadExternalReference:
		"Attaches an external reference (xref) to the drawing"
		# TODO: Check arguments
		# ['in'] PathName:str
		# ['in'] Name:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Xscale:float
		# ['in'] Yscale:float
		# ['in'] Zscale:float
		# ['in'] Rotation:float
		# ['in'] bOverlay:bool
		# ['in', '16'] Password:tagVARIANT
		# ['out', 'retval'] pXRef:AcadExternalReference
		# VBA: pXRef = object.AttachExternalReference (PathName, Name, InsertionPoint, Xscale, Yscale, Zscale, Rotation, bOverlay, Password)
		return self.com_parent.AttachExternalReference(PathName, Name, InsertionPoint, Xscale, Yscale, Zscale, Rotation, bOverlay, Password)

	def bind(self, bPrefixName: bool):
		"Binds an external reference (xref) to a drawing"
		# ['in'] bPrefixName:bool
		# VBA: object.Bind bPrefixName
		self.com_parent.Bind(bPrefixName)

	def detach(self):
		"Detachs an external reference (xref) from a drawing"
		# VBA: object.Detach 
		self.com_parent.Detach()

	def insertblock(self, InsertionPoint: tagVARIANT, Name: str, Xscale: float, Yscale: float, Zscale: float, Rotation: float, Password: tagVARIANT) -> AcadBlockReference:
		"Inserts a drawing file or a named block that has been defined in the current drawing"
		# TODO: Check arguments
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Name:str
		# ['in'] Xscale:float
		# ['in'] Yscale:float
		# ['in'] Zscale:float
		# ['in'] Rotation:float
		# ['in', '16'] Password:tagVARIANT
		# ['out', 'retval'] pBlkRef:AcadBlockReference
		# VBA: pBlkRef = object.InsertBlock (InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, Password)
		return self.com_parent.InsertBlock(InsertionPoint, Name, Xscale, Yscale, Zscale, Rotation, Password)

	def item(self, Index: tagVARIANT) -> AcadEntity:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadEntity
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def reload(self):
		"Reloads the external reference (xref)"
		# VBA: object.Reload 
		self.com_parent.Reload()

	def unload(self):
		"Unloads the menu group or external reference"
		# VBA: object.Unload 
		self.com_parent.Unload()

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def blockscaling(self) -> int:
		"Specifies the allowed scaling for the block"
		# TODO: Check arguments
		# ['out', 'retval'] pBS:int
		return self.com_parent.BlockScaling
	@blockscaling.setter
	def _(self, pBS:int):
		# ['in'] pBS:int
		self.com_parent.BlockScaling = pBS

	@indexedproperty
	def comments(self) -> str:
		"Specifies the comments for the block"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Comments
	@comments.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Comments = bstrName

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count

	@indexedproperty
	def explodable(self) -> bool:
		"Specifies whether the block can be exploded"
		# TODO: Check arguments
		# ['out', 'retval'] bExplodable:bool
		return self.com_parent.Explodable
	@explodable.setter
	def _(self, bExplodable:bool):
		# ['in'] bExplodable:bool
		self.com_parent.Explodable = bExplodable

	@indexedproperty
	def isdynamicblock(self) -> bool:
		"Specifies if this is a dynamic block"
		# TODO: Check arguments
		# ['out', 'retval'] pDynamicBlock:bool
		return self.com_parent.IsDynamicBlock

	@indexedproperty
	def islayout(self) -> bool:
		"Determines if the given block is a layout block"
		# TODO: Check arguments
		# ['out', 'retval'] bIsLayout:bool
		return self.com_parent.IsLayout

	@indexedproperty
	def isxref(self) -> bool:
		"Determines if the given block is an XRef block"
		# TODO: Check arguments
		# ['out', 'retval'] pIsXRref:bool
		return self.com_parent.IsXRef

	@indexedproperty
	def layout(self) -> AcadLayout:
		"Specifies the layout associated with the model space, paper space, or block object"
		# TODO: Check arguments
		# ['out', 'retval'] pLayout:AcadLayout
		return self.com_parent.Layout

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def origin(self) -> tagVARIANT:
		"Specifies the origin of the UCS, block, layout, or raster image in WCS coordinates"
		# TODO: Check arguments
		# ['out', 'retval'] Origin:tagVARIANT
		return self.com_parent.Origin
	@origin.setter
	def _(self, Origin:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT
		self.com_parent.Origin = Origin

	@indexedproperty
	def path(self) -> str:
		"Specifies the path of the external reference"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Path
	@path.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Path = bstrName

	@indexedproperty
	def units(self) -> int:
		"Specifies the native units of measure for the block"
		# TODO: Check arguments
		# ['out', 'retval'] pIU:int
		return self.com_parent.Units
	@units.setter
	def _(self, pIU:int):
		# ['in'] pIU:int
		self.com_parent.Units = pIU

	@indexedproperty
	def xrefdatabase(self) -> AcadDatabase:
		"Gets the Database object that defines the contents of the block"
		# TODO: Check arguments
		# ['out', 'retval'] pDatabase:AcadDatabase
		return self.com_parent.XRefDatabase


class AcadBlocks(POINTER(_dll.IAcadBlocks), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadBlocks
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadBlocks VBA-class wrapped as AcadBlocks python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadBlocks__com_Add
	#	_IAcadBlocks__com_Item
	#	_IAcadBlocks__com__get_Count
	#	_IAcadBlocks__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, InsertionPoint: tagVARIANT, Name: str) -> AcadBlock:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] Name:str
		# ['out', 'retval'] pBlock:AcadBlock
		# VBA: pBlock = object.Add (InsertionPoint, Name)
		return self.com_parent.Add(InsertionPoint, Name)

	def item(self, Index: tagVARIANT) -> AcadBlock:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadBlock
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count


class AcadDatabase(POINTER(_dll.IAcadDatabase), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDatabase
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadDatabase VBA-class wrapped as AcadDatabase python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDatabase__com_CopyObjects
	#	_IAcadDatabase__com_HandleToObject
	#	_IAcadDatabase__com_ObjectIdToObject
	#	_IAcadDatabase__com__get_Blocks
	#	_IAcadDatabase__com__get_Dictionaries
	#	_IAcadDatabase__com__get_DimStyles
	#	_IAcadDatabase__com__get_ElevationModelSpace
	#	_IAcadDatabase__com__get_ElevationPaperSpace
	#	_IAcadDatabase__com__get_Groups
	#	_IAcadDatabase__com__get_Layers
	#	_IAcadDatabase__com__get_Layouts
	#	_IAcadDatabase__com__get_Limits
	#	_IAcadDatabase__com__get_Linetypes
	#	_IAcadDatabase__com__get_Materials
	#	_IAcadDatabase__com__get_ModelSpace
	#	_IAcadDatabase__com__get_PaperSpace
	#	_IAcadDatabase__com__get_PlotConfigurations
	#	_IAcadDatabase__com__get_Preferences
	#	_IAcadDatabase__com__get_RegisteredApplications
	#	_IAcadDatabase__com__get_SectionManager
	#	_IAcadDatabase__com__get_SummaryInfo
	#	_IAcadDatabase__com__get_TextStyles
	#	_IAcadDatabase__com__get_UserCoordinateSystems
	#	_IAcadDatabase__com__get_Viewports
	#	_IAcadDatabase__com__get_Views
	#	_IAcadDatabase__com__set_ElevationModelSpace
	#	_IAcadDatabase__com__set_ElevationPaperSpace
	#	_IAcadDatabase__com__set_Limits
	# Methods
	def copyobjects(self, Objects: tagVARIANT, Owner: tagVARIANT, IdPairs: tagVARIANT):
		"Duplicates multiple objects (deep cloning)"
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# ['in', '16'] Owner:tagVARIANT
		# ['in', 'out', '16'] IdPairs:tagVARIANT
		# ['out', 'retval'] pNewObjects:tagVARIANT
		# VBA: pNewObjects = object.CopyObjects (Objects, Owner, IdPairs)
		return self.com_parent.CopyObjects(Objects, Owner, IdPairs)

	def handletoobject(self, Handle: str) -> POINTER(IDispatch):
		"Gets the object that corresponds to the given handle"
		# TODO: Check arguments
		# ['in'] Handle:str
		# ['out', 'retval'] pObj:POINTER(IDispatch)
		# VBA: pObj = object.HandleToObject (Handle)
		return self.com_parent.HandleToObject(Handle)

	def objectidtoobject(self, ObjectID: int) -> POINTER(IDispatch):
		"Gets the object that corresponds to the given object ID"
		# TODO: Check arguments
		# ['in'] ObjectID:int
		# ['out', 'retval'] pObj:POINTER(IDispatch)
		# VBA: pObj = object.ObjectIdToObject (ObjectID)
		return self.com_parent.ObjectIdToObject(ObjectID)

	# Properties
	@indexedproperty
	def blocks(self) -> AcadBlocks:
		"Gets the Blocks collection for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pBlocks:AcadBlocks
		return self.com_parent.Blocks

	@indexedproperty
	def dictionaries(self) -> AcadDictionaries:
		"Gets the Dictionaries collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pDictionaries:AcadDictionaries
		return self.com_parent.Dictionaries

	@indexedproperty
	def dimstyles(self) -> AcadDimStyles:
		"Gets the DimStyles collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pDimStyles:AcadDimStyles
		return self.com_parent.DimStyles

	@indexedproperty
	def elevationmodelspace(self) -> float:
		"Specifies the elevation setting in the model space"
		# TODO: Check arguments
		# ['out', 'retval'] Elevation:float
		return self.com_parent.ElevationModelSpace
	@elevationmodelspace.setter
	def _(self, Elevation:float):
		# ['in'] Elevation:float
		self.com_parent.ElevationModelSpace = Elevation

	@indexedproperty
	def elevationpaperspace(self) -> float:
		"Specifies the elevation setting in the paper space"
		# TODO: Check arguments
		# ['out', 'retval'] Elevation:float
		return self.com_parent.ElevationPaperSpace
	@elevationpaperspace.setter
	def _(self, Elevation:float):
		# ['in'] Elevation:float
		self.com_parent.ElevationPaperSpace = Elevation

	@indexedproperty
	def groups(self) -> AcadGroups:
		"Gets the Groups collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pGroups:AcadGroups
		return self.com_parent.Groups

	@indexedproperty
	def layers(self) -> AcadLayers:
		"Gets the Layers collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pLayers:AcadLayers
		return self.com_parent.Layers

	@indexedproperty
	def layouts(self) -> AcadLayouts:
		"Gets the Layouts collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pLayouts:AcadLayouts
		return self.com_parent.Layouts

	@indexedproperty
	def limits(self) -> tagVARIANT:
		"Specifies the drawing limits"
		# TODO: Check arguments
		# ['out', 'retval'] Limits:tagVARIANT
		return self.com_parent.Limits
	@limits.setter
	def _(self, Limits:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Limits:tagVARIANT
		self.com_parent.Limits = Limits

	@indexedproperty
	def linetypes(self) -> AcadLineTypes:
		"Gets the Linetypes collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pLinetypes:AcadLineTypes
		return self.com_parent.Linetypes

	@indexedproperty
	def materials(self) -> AcadMaterials:
		# TODO: Check arguments
		# ['out', 'retval'] pMaterials:AcadMaterials
		return self.com_parent.Materials

	@indexedproperty
	def modelspace(self) -> AcadModelSpace:
		"Gets the ModelSpace collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pMSpace:AcadModelSpace
		return self.com_parent.ModelSpace

	@indexedproperty
	def paperspace(self) -> AcadPaperSpace:
		"Gets the PaperSpace collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pPSpace:AcadPaperSpace
		return self.com_parent.PaperSpace

	@indexedproperty
	def plotconfigurations(self) -> AcadPlotConfigurations:
		"Gets the PlotConfigurations collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pPlotConfigs:AcadPlotConfigurations
		return self.com_parent.PlotConfigurations

	@indexedproperty
	def preferences(self) -> AcadDatabasePreferences:
		"Gets the Preferences object"
		# TODO: Check arguments
		# ['out', 'retval'] pPref:AcadDatabasePreferences
		return self.com_parent.Preferences

	@indexedproperty
	def registeredapplications(self) -> AcadRegisteredApplications:
		"The collection of all registered applications in the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pRegApps:AcadRegisteredApplications
		return self.com_parent.RegisteredApplications

	@indexedproperty
	def sectionmanager(self) -> AcadSectionManager:
		"Returns the section manager object."
		# TODO: Check arguments
		# ['out', 'retval'] pSecMgr:AcadSectionManager
		return self.com_parent.SectionManager

	@indexedproperty
	def summaryinfo(self) -> AcadSummaryInfo:
		"Returns the summary info object."
		# TODO: Check arguments
		# ['out', 'retval'] pSummaryInfo:AcadSummaryInfo
		return self.com_parent.SummaryInfo

	@indexedproperty
	def textstyles(self) -> AcadTextStyles:
		"Gets the TextStyles collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pTextStyles:AcadTextStyles
		return self.com_parent.TextStyles

	@indexedproperty
	def usercoordinatesystems(self) -> AcadUCSs:
		"Gets the UCSs collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pUCSs:AcadUCSs
		return self.com_parent.UserCoordinateSystems

	@indexedproperty
	def viewports(self) -> AcadViewports:
		"Gets the Viewports collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pViewports:AcadViewports
		return self.com_parent.Viewports

	@indexedproperty
	def views(self) -> AcadViews:
		"Gets the Views collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pViews:AcadViews
		return self.com_parent.Views


class AcadDatabasePreferences(POINTER(_dll.IAcadDatabasePreferences), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDatabasePreferences
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadDatabasePreferences VBA-class wrapped as AcadDatabasePreferences python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDatabasePreferences__com__get_AllowLongSymbolNames
	#	_IAcadDatabasePreferences__com__get_Application
	#	_IAcadDatabasePreferences__com__get_ContourLinesPerSurface
	#	_IAcadDatabasePreferences__com__get_DisplaySilhouette
	#	_IAcadDatabasePreferences__com__get_LineWeightDisplay
	#	_IAcadDatabasePreferences__com__get_Lineweight
	#	_IAcadDatabasePreferences__com__get_MaxActiveViewports
	#	_IAcadDatabasePreferences__com__get_OLELaunch
	#	_IAcadDatabasePreferences__com__get_ObjectSortByPSOutput
	#	_IAcadDatabasePreferences__com__get_ObjectSortByPlotting
	#	_IAcadDatabasePreferences__com__get_ObjectSortByRedraws
	#	_IAcadDatabasePreferences__com__get_ObjectSortByRegens
	#	_IAcadDatabasePreferences__com__get_ObjectSortBySelection
	#	_IAcadDatabasePreferences__com__get_ObjectSortBySnap
	#	_IAcadDatabasePreferences__com__get_RenderSmoothness
	#	_IAcadDatabasePreferences__com__get_SegmentPerPolyline
	#	_IAcadDatabasePreferences__com__get_SolidFill
	#	_IAcadDatabasePreferences__com__get_TextFrameDisplay
	#	_IAcadDatabasePreferences__com__get_XRefEdit
	#	_IAcadDatabasePreferences__com__get_XRefLayerVisibility
	#	_IAcadDatabasePreferences__com__set_AllowLongSymbolNames
	#	_IAcadDatabasePreferences__com__set_ContourLinesPerSurface
	#	_IAcadDatabasePreferences__com__set_DisplaySilhouette
	#	_IAcadDatabasePreferences__com__set_LineWeightDisplay
	#	_IAcadDatabasePreferences__com__set_Lineweight
	#	_IAcadDatabasePreferences__com__set_MaxActiveViewports
	#	_IAcadDatabasePreferences__com__set_OLELaunch
	#	_IAcadDatabasePreferences__com__set_ObjectSortByPSOutput
	#	_IAcadDatabasePreferences__com__set_ObjectSortByPlotting
	#	_IAcadDatabasePreferences__com__set_ObjectSortByRedraws
	#	_IAcadDatabasePreferences__com__set_ObjectSortByRegens
	#	_IAcadDatabasePreferences__com__set_ObjectSortBySelection
	#	_IAcadDatabasePreferences__com__set_ObjectSortBySnap
	#	_IAcadDatabasePreferences__com__set_RenderSmoothness
	#	_IAcadDatabasePreferences__com__set_SegmentPerPolyline
	#	_IAcadDatabasePreferences__com__set_SolidFill
	#	_IAcadDatabasePreferences__com__set_TextFrameDisplay
	#	_IAcadDatabasePreferences__com__set_XRefEdit
	#	_IAcadDatabasePreferences__com__set_XRefLayerVisibility
	# Properties
	@indexedproperty
	def allowlongsymbolnames(self) -> bool:
		"Determines if symbol names may include extended character sets, or more than 31 characters"
		# TODO: Check arguments
		# ['out', 'retval'] LongNames:bool
		return self.com_parent.AllowLongSymbolNames
	@allowlongsymbolnames.setter
	def _(self, LongNames:bool):
		# ['in'] LongNames:bool
		self.com_parent.AllowLongSymbolNames = LongNames

	@indexedproperty
	def application(self) -> POINTER(IDispatch):
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:POINTER(IDispatch)
		return self.com_parent.Application

	@indexedproperty
	def contourlinespersurface(self) -> int:
		"Specifies the number of contour lines (isolines) per surface on objects"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.ContourLinesPerSurface
	@contourlinespersurface.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.ContourLinesPerSurface = Path

	@indexedproperty
	def displaysilhouette(self) -> bool:
		"Controls if silhouette curves of solid objects are displayed in Wireframe mode"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplaySilhouette
	@displaysilhouette.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplaySilhouette = Path

	@indexedproperty
	def lineweight(self) -> int:
		"Specifies the lineweight of an individual entity or the default lineweight for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.Lineweight
	@lineweight.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.Lineweight = Path

	@indexedproperty
	def lineweightdisplay(self) -> bool:
		"Specifies whether lineweights are displayed in model space for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LineWeightDisplay
	@lineweightdisplay.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LineWeightDisplay = Path

	@indexedproperty
	def maxactiveviewports(self) -> int:
		"Specifies the maximum number of active viewports"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.MaxActiveViewports
	@maxactiveviewports.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.MaxActiveViewports = Path

	@indexedproperty
	def objectsortbyplotting(self) -> bool:
		"Toggles sorting of drawing objects by plotting order"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortByPlotting
	@objectsortbyplotting.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortByPlotting = Sort

	@indexedproperty
	def objectsortbypsoutput(self) -> bool:
		"Toggles sorting of drawing objects by PostScript output order"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortByPSOutput
	@objectsortbypsoutput.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortByPSOutput = Sort

	@indexedproperty
	def objectsortbyredraws(self) -> bool:
		"Toggles sorting of drawing objects by redraw order"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortByRedraws
	@objectsortbyredraws.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortByRedraws = Sort

	@indexedproperty
	def objectsortbyregens(self) -> bool:
		"Toggles sorting of drawing objects by regeneration order"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortByRegens
	@objectsortbyregens.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortByRegens = Sort

	@indexedproperty
	def objectsortbyselection(self) -> bool:
		"Toggles sorting of drawing objects by object selection"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortBySelection
	@objectsortbyselection.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortBySelection = Sort

	@indexedproperty
	def objectsortbysnap(self) -> bool:
		"Toggles sorting of drawing objects by object snap"
		# TODO: Check arguments
		# ['out', 'retval'] Sort:bool
		return self.com_parent.ObjectSortBySnap
	@objectsortbysnap.setter
	def _(self, Sort:bool):
		# ['in'] Sort:bool
		self.com_parent.ObjectSortBySnap = Sort

	@indexedproperty
	def olelaunch(self) -> bool:
		"Determines whether to launch the parent application when plotting OLE objects"
		# TODO: Check arguments
		# ['out', 'retval'] Launch:bool
		return self.com_parent.OLELaunch
	@olelaunch.setter
	def _(self, Launch:bool):
		# ['in'] Launch:bool
		self.com_parent.OLELaunch = Launch

	@indexedproperty
	def rendersmoothness(self) -> float:
		"Specifies the smoothness of shaded, rendered, and hidden line-removed objects"
		# TODO: Check arguments
		# ['out', 'retval'] Path:float
		return self.com_parent.RenderSmoothness
	@rendersmoothness.setter
	def _(self, Path:float):
		# ['in'] Path:float
		self.com_parent.RenderSmoothness = Path

	@indexedproperty
	def segmentperpolyline(self) -> int:
		"Specifies the number of line segments to be generated for each polyline curve"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.SegmentPerPolyline
	@segmentperpolyline.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.SegmentPerPolyline = Path

	@indexedproperty
	def solidfill(self) -> bool:
		"Specifies if multilines, traces, solids, all hatches (including solid-fill) and wide polylines are filled in"
		# TODO: Check arguments
		# ['out', 'retval'] Fill:bool
		return self.com_parent.SolidFill
	@solidfill.setter
	def _(self, Fill:bool):
		# ['in'] Fill:bool
		self.com_parent.SolidFill = Fill

	@indexedproperty
	def textframedisplay(self) -> bool:
		"Toggles the display of frames for text objects instead of displaying the text itself"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.TextFrameDisplay
	@textframedisplay.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.TextFrameDisplay = Path

	@indexedproperty
	def xrefedit(self) -> bool:
		"Determines if the current drawing can be edited in place when being referenced by another user"
		# TODO: Check arguments
		# ['out', 'retval'] Edit:bool
		return self.com_parent.XRefEdit
	@xrefedit.setter
	def _(self, Edit:bool):
		# ['in'] Edit:bool
		self.com_parent.XRefEdit = Edit

	@indexedproperty
	def xreflayervisibility(self) -> bool:
		"Determines the visibility of xref-dependent layers and specifies if nested xref path changes are saved"
		# TODO: Check arguments
		# ['out', 'retval'] XRefLayerVis:bool
		return self.com_parent.XRefLayerVisibility
	@xreflayervisibility.setter
	def _(self, XRefLayerVis:bool):
		# ['in'] XRefLayerVis:bool
		self.com_parent.XRefLayerVisibility = XRefLayerVis


class AcadDictionaries(POINTER(_dll.IAcadDictionaries), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDictionaries
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadDictionaries VBA-class wrapped as AcadDictionaries python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDictionaries__com_Add
	#	_IAcadDictionaries__com_Item
	#	_IAcadDictionaries__com__get_Count
	#	_IAcadDictionaries__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadDictionary:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pDimStyle:AcadDictionary
		# VBA: pDimStyle = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadObject:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadObject
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadDictionary(POINTER(_dll.IAcadDictionary), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDictionary
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadDictionary VBA-class wrapped as AcadDictionary python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDictionary__com_AddObject
	#	_IAcadDictionary__com_AddXRecord
	#	_IAcadDictionary__com_GetName
	#	_IAcadDictionary__com_GetObject
	#	_IAcadDictionary__com_Item
	#	_IAcadDictionary__com_Remove
	#	_IAcadDictionary__com_Rename
	#	_IAcadDictionary__com_Replace
	#	_IAcadDictionary__com__get_Count
	#	_IAcadDictionary__com__get_Name
	#	_IAcadDictionary__com__get__NewEnum
	#	_IAcadDictionary__com__set_Name
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def addobject(self, Keyword: str, ObjectName: str) -> AcadObject:
		"Adds an object to a named dictionary"
		# TODO: Check arguments
		# ['in'] Keyword:str
		# ['in'] ObjectName:str
		# ['out', 'retval'] pNewObj:AcadObject
		# VBA: pNewObj = object.AddObject (Keyword, ObjectName)
		return self.com_parent.AddObject(Keyword, ObjectName)

	def addxrecord(self, Keyword: str) -> AcadXRecord:
		"Creates an XRecord object in any dictionary"
		# TODO: Check arguments
		# ['in'] Keyword:str
		# ['out', 'retval'] pNewXRecord:AcadXRecord
		# VBA: pNewXRecord = object.AddXRecord (Keyword)
		return self.com_parent.AddXRecord(Keyword)

	def getname(self, Object: AcadObject) -> str:
		"Gets the name (keyword) of an object in a dictionary"
		# TODO: Check arguments
		# ['in'] Object:AcadObject
		# ['out', 'retval'] bstrName:str
		# VBA: bstrName = object.GetName (Object)
		return self.com_parent.GetName(Object)

	def getobject(self, Name: str) -> AcadObject:
		"Gets the object in a dictionary, given the name (keyword) of the object"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pObj:AcadObject
		# VBA: pObj = object.GetObject (Name)
		return self.com_parent.GetObject(Name)

	def item(self, Index: tagVARIANT) -> AcadObject:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadObject
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def remove(self, Name: str) -> AcadObject:
		"Removes a named object from the dictionary"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pObj:AcadObject
		# VBA: pObj = object.Remove (Name)
		return self.com_parent.Remove(Name)

	def rename(self, OldName: str, NewName: str):
		"Renames an item in the dictionary"
		# ['in'] OldName:str
		# ['in'] NewName:str
		# VBA: object.Rename OldName, NewName
		self.com_parent.Rename(OldName, NewName)

	def replace(self, OldName: str, pObj: AcadObject):
		"Replaces an item in the dictionary by a given item"
		# TODO: Check arguments
		# ['in'] OldName:str
		# ['in'] pObj:AcadObject
		# VBA: object.Replace OldName, pObj
		self.com_parent.Replace(OldName, pObj)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:str
		return self.com_parent.Name
	@name.setter
	def _(self, pVal:str):
		# ['in'] pVal:str
		self.com_parent.Name = pVal


class AcadDimStyle(POINTER(_dll.IAcadDimStyle), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDimStyle
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadDimStyle VBA-class wrapped as AcadDimStyle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDimStyle__com_CopyFrom
	#	_IAcadDimStyle__com__get_Name
	#	_IAcadDimStyle__com__set_Name
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def copyfrom(self, StyleSource: POINTER(IDispatch)):
		"Copies the dimension style data from a source object"
		# TODO: Check arguments
		# ['in'] StyleSource:POINTER(IDispatch)
		# VBA: object.CopyFrom StyleSource
		self.com_parent.CopyFrom(StyleSource)

	# Properties
	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName


class AcadDimStyles(POINTER(_dll.IAcadDimStyles), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDimStyles
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadDimStyles VBA-class wrapped as AcadDimStyles python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDimStyles__com_Add
	#	_IAcadDimStyles__com_Item
	#	_IAcadDimStyles__com__get_Count
	#	_IAcadDimStyles__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadDimStyle:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pDimStyle:AcadDimStyle
		# VBA: pDimStyle = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadDimStyle:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadDimStyle
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadDocument(POINTER(_dll.IAcadDocument), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDocument
	#	IAcadDatabase
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadDocument VBA-class wrapped as AcadDocument python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDatabase__com_CopyObjects
	#	_IAcadDatabase__com_HandleToObject
	#	_IAcadDatabase__com_ObjectIdToObject
	#	_IAcadDatabase__com__get_Blocks
	#	_IAcadDatabase__com__get_Dictionaries
	#	_IAcadDatabase__com__get_DimStyles
	#	_IAcadDatabase__com__get_ElevationModelSpace
	#	_IAcadDatabase__com__get_ElevationPaperSpace
	#	_IAcadDatabase__com__get_Groups
	#	_IAcadDatabase__com__get_Layers
	#	_IAcadDatabase__com__get_Layouts
	#	_IAcadDatabase__com__get_Limits
	#	_IAcadDatabase__com__get_Linetypes
	#	_IAcadDatabase__com__get_Materials
	#	_IAcadDatabase__com__get_ModelSpace
	#	_IAcadDatabase__com__get_PaperSpace
	#	_IAcadDatabase__com__get_PlotConfigurations
	#	_IAcadDatabase__com__get_Preferences
	#	_IAcadDatabase__com__get_RegisteredApplications
	#	_IAcadDatabase__com__get_SectionManager
	#	_IAcadDatabase__com__get_SummaryInfo
	#	_IAcadDatabase__com__get_TextStyles
	#	_IAcadDatabase__com__get_UserCoordinateSystems
	#	_IAcadDatabase__com__get_Viewports
	#	_IAcadDatabase__com__get_Views
	#	_IAcadDatabase__com__set_ElevationModelSpace
	#	_IAcadDatabase__com__set_ElevationPaperSpace
	#	_IAcadDatabase__com__set_Limits
	#	_IAcadDocument__com_Activate
	#	_IAcadDocument__com_AuditInfo
	#	_IAcadDocument__com_Close
	#	_IAcadDocument__com_EndUndoMark
	#	_IAcadDocument__com_Export
	#	_IAcadDocument__com_GetVariable
	#	_IAcadDocument__com_Import
	#	_IAcadDocument__com_LoadShapeFile
	#	_IAcadDocument__com_New
	#	_IAcadDocument__com_Open
	#	_IAcadDocument__com_PostCommand
	#	_IAcadDocument__com_PurgeAll
	#	_IAcadDocument__com_Regen
	#	_IAcadDocument__com_Save
	#	_IAcadDocument__com_SaveAs
	#	_IAcadDocument__com_SendCommand
	#	_IAcadDocument__com_SetVariable
	#	_IAcadDocument__com_StartUndoMark
	#	_IAcadDocument__com_Wblock
	#	_IAcadDocument__com__get_Active
	#	_IAcadDocument__com__get_ActiveDimStyle
	#	_IAcadDocument__com__get_ActiveLayer
	#	_IAcadDocument__com__get_ActiveLayout
	#	_IAcadDocument__com__get_ActiveLinetype
	#	_IAcadDocument__com__get_ActiveMaterial
	#	_IAcadDocument__com__get_ActivePViewport
	#	_IAcadDocument__com__get_ActiveSelectionSet
	#	_IAcadDocument__com__get_ActiveSpace
	#	_IAcadDocument__com__get_ActiveTextStyle
	#	_IAcadDocument__com__get_ActiveUCS
	#	_IAcadDocument__com__get_ActiveViewport
	#	_IAcadDocument__com__get_Application
	#	_IAcadDocument__com__get_Database
	#	_IAcadDocument__com__get_FullName
	#	_IAcadDocument__com__get_HWND
	#	_IAcadDocument__com__get_Height
	#	_IAcadDocument__com__get_MSpace
	#	_IAcadDocument__com__get_Name
	#	_IAcadDocument__com__get_ObjectSnapMode
	#	_IAcadDocument__com__get_Path
	#	_IAcadDocument__com__get_PickfirstSelectionSet
	#	_IAcadDocument__com__get_Plot
	#	_IAcadDocument__com__get_ReadOnly
	#	_IAcadDocument__com__get_Saved
	#	_IAcadDocument__com__get_SelectionSets
	#	_IAcadDocument__com__get_Utility
	#	_IAcadDocument__com__get_Width
	#	_IAcadDocument__com__get_WindowState
	#	_IAcadDocument__com__get_WindowTitle
	#	_IAcadDocument__com__set_ActiveDimStyle
	#	_IAcadDocument__com__set_ActiveLayer
	#	_IAcadDocument__com__set_ActiveLayout
	#	_IAcadDocument__com__set_ActiveLinetype
	#	_IAcadDocument__com__set_ActiveMaterial
	#	_IAcadDocument__com__set_ActivePViewport
	#	_IAcadDocument__com__set_ActiveSpace
	#	_IAcadDocument__com__set_ActiveTextStyle
	#	_IAcadDocument__com__set_ActiveUCS
	#	_IAcadDocument__com__set_ActiveViewport
	#	_IAcadDocument__com__set_Height
	#	_IAcadDocument__com__set_MSpace
	#	_IAcadDocument__com__set_ObjectSnapMode
	#	_IAcadDocument__com__set_Width
	#	_IAcadDocument__com__set_WindowState
	# Methods
	def activate(self):
		"Makes the specified drawing active"
		# VBA: object.Activate 
		self.com_parent.Activate()

	def auditinfo(self, FixErr: bool):
		"Evaluates the integrity of the drawing"
		# ['in'] FixErr:bool
		# VBA: object.AuditInfo FixErr
		self.com_parent.AuditInfo(FixErr)

	def close(self, SaveChanges: tagVARIANT, FileName: tagVARIANT):
		"Closes the specified drawing, or all open drawings"
		# TODO: Check arguments
		# ['in', '16'] SaveChanges:tagVARIANT
		# ['in', '16'] FileName:tagVARIANT
		# VBA: object.Close SaveChanges, FileName
		self.com_parent.Close(SaveChanges, FileName)

	def endundomark(self):
		"Marks the end of a block of operations"
		# VBA: object.EndUndoMark 
		self.com_parent.EndUndoMark()

	def export(self, FileName: str, Extension: str, SelectionSet: AcadSelectionSet):
		"Exports the AutoCAD drawing to a WMF, SAT, EPS, DXF, or BMP format"
		# TODO: Check arguments
		# ['in'] FileName:str
		# ['in'] Extension:str
		# ['in'] SelectionSet:AcadSelectionSet
		# VBA: object.Export FileName, Extension, SelectionSet
		self.com_parent.Export(FileName, Extension, SelectionSet)

	def getvariable(self, Name: str) -> tagVARIANT:
		"Gets the current setting of an AutoCAD system variable"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] Value:tagVARIANT
		# VBA: Value = object.GetVariable (Name)
		return self.com_parent.GetVariable(Name)

	def import(self, FileName: str, InsertionPoint: tagVARIANT, ScaleFactor: float) -> POINTER(IDispatch):
		"Imports a drawing file in SAT, EPS, DXF, or WMF format"
		# TODO: Check arguments
		# ['in'] FileName:str
		# ['in'] InsertionPoint:tagVARIANT
		# ['in'] ScaleFactor:float
		# ['out', 'retval'] pObj:POINTER(IDispatch)
		# VBA: pObj = object.Import (FileName, InsertionPoint, ScaleFactor)
		return self.com_parent.Import(FileName, InsertionPoint, ScaleFactor)

	def loadshapefile(self, FullName: str):
		"Loads a shape file (SHX)"
		# ['in'] FullName:str
		# VBA: object.LoadShapeFile FullName
		self.com_parent.LoadShapeFile(FullName)

	def new(self, TemplateFileName: str) -> AcadDocument:
		"Creates a new document in SDI mode"
		# TODO: Check arguments
		# ['in'] TemplateFileName:str
		# ['out', 'retval'] pDocObj:AcadDocument
		# VBA: pDocObj = object.New (TemplateFileName)
		return self.com_parent.New(TemplateFileName)

	def open(self, FullName: str, Password: tagVARIANT) -> AcadDocument:
		"Opens an existing drawing file (DWG) and makes it the active document"
		# TODO: Check arguments
		# ['in'] FullName:str
		# ['in', '16'] Password:tagVARIANT
		# ['out', 'retval'] pDocObj:AcadDocument
		# VBA: pDocObj = object.Open (FullName, Password)
		return self.com_parent.Open(FullName, Password)

	def postcommand(self, Command: str):
		"Posts a command string from a VB or VBA application to the document for processing"
		# ['in'] Command:str
		# VBA: object.PostCommand Command
		self.com_parent.PostCommand(Command)

	def purgeall(self):
		"Removes unused named references such as unused blocks or layers from the document"
		# VBA: object.PurgeAll 
		self.com_parent.PurgeAll()

	def regen(self, WhichViewports: int):
		"Regenerates the entire drawing and recomputes the screen coordinates and view resolution for all objects"
		# ['in'] WhichViewports:int
		# VBA: object.Regen WhichViewports
		self.com_parent.Regen(WhichViewports)

	def save(self):
		"Saves the document or menu group"
		# VBA: object.Save 
		self.com_parent.Save()

	def saveas(self, FullFileName: str, SaveAsType: tagVARIANT, vSecurityParams: tagVARIANT):
		"Saves the document or menu group to a specified file"
		# TODO: Check arguments
		# ['in'] FullFileName:str
		# ['in', '16'] SaveAsType:tagVARIANT
		# ['in', '16'] vSecurityParams:tagVARIANT
		# VBA: object.SaveAs FullFileName, SaveAsType, vSecurityParams
		self.com_parent.SaveAs(FullFileName, SaveAsType, vSecurityParams)

	def sendcommand(self, Command: str):
		"Sends a command string from a VB or VBA application to the document for processing"
		# ['in'] Command:str
		# VBA: object.SendCommand Command
		self.com_parent.SendCommand(Command)

	def setvariable(self, Name: str, Value: tagVARIANT):
		"Sets the value of an AutoCAD system variable"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['in'] Value:tagVARIANT
		# VBA: object.SetVariable Name, Value
		self.com_parent.SetVariable(Name, Value)

	def startundomark(self):
		"Marks the beginning of a block of operations"
		# VBA: object.StartUndoMark 
		self.com_parent.StartUndoMark()

	def wblock(self, FileName: str, SelectionSet: AcadSelectionSet):
		"Writes out the given selection set as a new drawing file"
		# TODO: Check arguments
		# ['in'] FileName:str
		# ['in'] SelectionSet:AcadSelectionSet
		# VBA: object.Wblock FileName, SelectionSet
		self.com_parent.Wblock(FileName, SelectionSet)

	# Properties
	@indexedproperty
	def active(self) -> bool:
		"Determines if the document is the active document for the session"
		# TODO: Check arguments
		# ['out', 'retval'] pvbActive:bool
		return self.com_parent.Active

	@indexedproperty
	def activedimstyle(self) -> AcadDimStyle:
		"Specifies the active dimension style"
		# TODO: Check arguments
		# ['out', 'retval'] pActDimStyle:AcadDimStyle
		return self.com_parent.ActiveDimStyle
	@activedimstyle.setter
	def _(self, pActDimStyle:AcadDimStyle):
		# TODO: Check arguments
		# ['in'] pActDimStyle:AcadDimStyle
		self.com_parent.ActiveDimStyle = pActDimStyle

	@indexedproperty
	def activelayer(self) -> AcadLayer:
		"Specifies the active layer"
		# TODO: Check arguments
		# ['out', 'retval'] pActLayer:AcadLayer
		return self.com_parent.ActiveLayer
	@activelayer.setter
	def _(self, pActLayer:AcadLayer):
		# TODO: Check arguments
		# ['in'] pActLayer:AcadLayer
		self.com_parent.ActiveLayer = pActLayer

	@indexedproperty
	def activelayout(self) -> AcadLayout:
		"Specifies the active layout"
		# TODO: Check arguments
		# ['out', 'retval'] pLayout:AcadLayout
		return self.com_parent.ActiveLayout
	@activelayout.setter
	def _(self, pLayout:AcadLayout):
		# TODO: Check arguments
		# ['in'] pLayout:AcadLayout
		self.com_parent.ActiveLayout = pLayout

	@indexedproperty
	def activelinetype(self) -> AcadLineType:
		"Specifies the active linetype for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pActLinetype:AcadLineType
		return self.com_parent.ActiveLinetype
	@activelinetype.setter
	def _(self, pActLinetype:AcadLineType):
		# TODO: Check arguments
		# ['in'] pActLinetype:AcadLineType
		self.com_parent.ActiveLinetype = pActLinetype

	@indexedproperty
	def activematerial(self) -> AcadMaterial:
		# TODO: Check arguments
		# ['out', 'retval'] pActMaterial:AcadMaterial
		return self.com_parent.ActiveMaterial
	@activematerial.setter
	def _(self, pActMaterial:AcadMaterial):
		# TODO: Check arguments
		# ['in'] pActMaterial:AcadMaterial
		self.com_parent.ActiveMaterial = pActMaterial

	@indexedproperty
	def activepviewport(self) -> AcadPViewport:
		"Specifies the active paper space viewport for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pActView:AcadPViewport
		return self.com_parent.ActivePViewport
	@activepviewport.setter
	def _(self, pActView:AcadPViewport):
		# TODO: Check arguments
		# ['in'] pActView:AcadPViewport
		self.com_parent.ActivePViewport = pActView

	@indexedproperty
	def activeselectionset(self) -> AcadSelectionSet:
		"Gets the active selection set for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pSelSet:AcadSelectionSet
		return self.com_parent.ActiveSelectionSet

	@indexedproperty
	def activespace(self) -> int:
		"Toggles the active space between paper space and model space"
		# TODO: Check arguments
		# ['out', 'retval'] ActSpace:int
		return self.com_parent.ActiveSpace
	@activespace.setter
	def _(self, ActSpace:int):
		# ['in'] ActSpace:int
		self.com_parent.ActiveSpace = ActSpace

	@indexedproperty
	def activetextstyle(self) -> AcadTextStyle:
		"Specifies the active text style for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pActTextStyle:AcadTextStyle
		return self.com_parent.ActiveTextStyle
	@activetextstyle.setter
	def _(self, pActTextStyle:AcadTextStyle):
		# TODO: Check arguments
		# ['in'] pActTextStyle:AcadTextStyle
		self.com_parent.ActiveTextStyle = pActTextStyle

	@indexedproperty
	def activeucs(self) -> AcadUCS:
		"Specifies the active UCS for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pActUCS:AcadUCS
		return self.com_parent.ActiveUCS
	@activeucs.setter
	def _(self, pActUCS:AcadUCS):
		# TODO: Check arguments
		# ['in'] pActUCS:AcadUCS
		self.com_parent.ActiveUCS = pActUCS

	@indexedproperty
	def activeviewport(self) -> AcadViewport:
		"Specifies the active viewport for the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] pActView:AcadViewport
		return self.com_parent.ActiveViewport
	@activeviewport.setter
	def _(self, pActView:AcadViewport):
		# TODO: Check arguments
		# ['in'] pActView:AcadViewport
		self.com_parent.ActiveViewport = pActView

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def database(self) -> AcadDatabase:
		"Gets the database in which the object belongs"
		# TODO: Check arguments
		# ['out', 'retval'] pDatabase:AcadDatabase
		return self.com_parent.Database

	@indexedproperty
	def fullname(self) -> str:
		"Gets the name of the application or document, including the path"
		# TODO: Check arguments
		# ['out', 'retval'] FullName:str
		return self.com_parent.FullName

	@indexedproperty
	def height(self) -> int:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] pHeight:int
		return self.com_parent.Height
	@height.setter
	def _(self, pHeight:int):
		# ['in'] pHeight:int
		self.com_parent.Height = pHeight

	@indexedproperty
	def hwnd(self) -> int:
		"Gets the window handle of the document window frame"
		# TODO: Check arguments
		# ['out', 'retval'] HWND:int
		return self.com_parent.HWND

	@indexedproperty
	def mspace(self) -> bool:
		"Allows editing of the model from floating paper space viewports"
		# TODO: Check arguments
		# ['out', 'retval'] Mode:bool
		return self.com_parent.MSpace
	@mspace.setter
	def _(self, Mode:bool):
		# ['in'] Mode:bool
		self.com_parent.MSpace = Mode

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.Name

	@indexedproperty
	def objectsnapmode(self) -> bool:
		"Specifies the setting of the object snap mode"
		# TODO: Check arguments
		# ['out', 'retval'] fSnapMode:bool
		return self.com_parent.ObjectSnapMode
	@objectsnapmode.setter
	def _(self, fSnapMode:bool):
		# ['in'] fSnapMode:bool
		self.com_parent.ObjectSnapMode = fSnapMode

	@indexedproperty
	def path(self) -> str:
		"Gets the path of the document, application, or external reference"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.Path

	@indexedproperty
	def pickfirstselectionset(self) -> AcadSelectionSet:
		"Gets the pickfirst selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pSelSet:AcadSelectionSet
		return self.com_parent.PickfirstSelectionSet

	@indexedproperty
	def plot(self) -> AcadPlot:
		"Gets the Plot object for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pPlot:AcadPlot
		return self.com_parent.Plot

	@indexedproperty
	def readonly(self) -> bool:
		"Specifies if the document is read-only or read-write"
		# TODO: Check arguments
		# ['out', 'retval'] bReadOnly:bool
		return self.com_parent.ReadOnly

	@indexedproperty
	def saved(self) -> bool:
		"Specifies if the document has any unsaved changes"
		# TODO: Check arguments
		# ['out', 'retval'] bSaved:bool
		return self.com_parent.Saved

	@indexedproperty
	def selectionsets(self) -> AcadSelectionSets:
		"Gets the SelectionSets collection for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pSelSets:AcadSelectionSets
		return self.com_parent.SelectionSets

	@indexedproperty
	def utility(self) -> AcadUtility:
		"Gets the Utility object for the document"
		# TODO: Check arguments
		# ['out', 'retval'] pUtil:AcadUtility
		return self.com_parent.Utility

	@indexedproperty
	def width(self) -> int:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] pWidth:int
		return self.com_parent.Width
	@width.setter
	def _(self, pWidth:int):
		# ['in'] pWidth:int
		self.com_parent.Width = pWidth

	@indexedproperty
	def windowstate(self) -> int:
		"Specifies the state of the application or document window"
		# TODO: Check arguments
		# ['out', 'retval'] pWinState:int
		return self.com_parent.WindowState
	@windowstate.setter
	def _(self, pWinState:int):
		# ['in'] pWinState:int
		self.com_parent.WindowState = pWinState

	@indexedproperty
	def windowtitle(self) -> str:
		"Gets the title of the document window"
		# TODO: Check arguments
		# ['out', 'retval'] Title:str
		return self.com_parent.WindowTitle


class AcadDocuments(POINTER(_dll.IAcadDocuments), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDocuments
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadDocuments VBA-class wrapped as AcadDocuments python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDocuments__com_Add
	#	_IAcadDocuments__com_Close
	#	_IAcadDocuments__com_Item
	#	_IAcadDocuments__com_Open
	#	_IAcadDocuments__com__get_Application
	#	_IAcadDocuments__com__get_Count
	#	_IAcadDocuments__com__get__NewEnum
	# Methods
	def add(self, TemplateName: tagVARIANT) -> AcadDocument:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in', '16'] TemplateName:tagVARIANT
		# ['out', 'retval'] pDispDoc:AcadDocument
		# VBA: pDispDoc = object.Add (TemplateName)
		return self.com_parent.Add(TemplateName)

	def close(self):
		"Closes the specified drawing, or all open drawings"
		# VBA: object.Close 
		self.com_parent.Close()

	def item(self, Index: tagVARIANT) -> AcadDocument:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadDocument
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def open(self, Name: str, ReadOnly: tagVARIANT, Password: tagVARIANT) -> AcadDocument:
		"Opens an existing drawing file (DWG) and makes it the active document"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['in', '16'] ReadOnly:tagVARIANT
		# ['in', '16'] Password:tagVARIANT
		# ['out', 'retval'] pDispDoc:AcadDocument
		# VBA: pDispDoc = object.Open (Name, ReadOnly, Password)
		return self.com_parent.Open(Name, ReadOnly, Password)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count


class AcadDynamicBlockReferenceProperty(POINTER(_dll.IAcadDynamicBlockReferenceProperty), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadDynamicBlockReferenceProperty
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadDynamicBlockReferenceProperty VBA-class wrapped as AcadDynamicBlockReferenceProperty python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadDynamicBlockReferenceProperty__com__get_AllowedValues
	#	_IAcadDynamicBlockReferenceProperty__com__get_Description
	#	_IAcadDynamicBlockReferenceProperty__com__get_PropertyName
	#	_IAcadDynamicBlockReferenceProperty__com__get_ReadOnly
	#	_IAcadDynamicBlockReferenceProperty__com__get_UnitsType
	#	_IAcadDynamicBlockReferenceProperty__com__get_Value
	#	_IAcadDynamicBlockReferenceProperty__com__get_show
	#	_IAcadDynamicBlockReferenceProperty__com__set_Value
	# Properties
	@indexedproperty
	def allowedvalues(self) -> tagVARIANT:
		"Specifies the allowed values for the property."
		# TODO: Check arguments
		# ['out', 'retval'] AllowedValues:tagVARIANT
		return self.com_parent.AllowedValues

	@indexedproperty
	def description(self) -> str:
		"Specifies the description for the property."
		# TODO: Check arguments
		# ['out', 'retval'] Description:str
		return self.com_parent.Description

	@indexedproperty
	def propertyname(self) -> str:
		"Specifies the name for the property."
		# TODO: Check arguments
		# ['out', 'retval'] PropertyName:str
		return self.com_parent.PropertyName

	@indexedproperty
	def readonly(self) -> bool:
		"Specifies whether the property is read-only."
		# TODO: Check arguments
		# ['out', 'retval'] ReadOnly:bool
		return self.com_parent.ReadOnly

	@indexedproperty
	def show(self) -> bool:
		"Specifies whether the property is showin in the user interface."
		# TODO: Check arguments
		# ['out', 'retval'] show:bool
		return self.com_parent.show

	@indexedproperty
	def unitstype(self) -> int:
		"Specifies the current display units type for the property."
		# TODO: Check arguments
		# ['out', 'retval'] Units:int
		return self.com_parent.UnitsType

	@indexedproperty
	def value(self) -> tagVARIANT:
		"Specifies the current value for the property."
		# TODO: Check arguments
		# ['out', 'retval'] Value:tagVARIANT
		return self.com_parent.Value
	@value.setter
	def _(self, Value:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Value:tagVARIANT
		self.com_parent.Value = Value


class AcadEntity(POINTER(_dll.IAcadEntity), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadEntity
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadEntity VBA-class wrapped as AcadEntity python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadEntity__com_ArrayPolar
	#	_IAcadEntity__com_ArrayRectangular
	#	_IAcadEntity__com_Copy
	#	_IAcadEntity__com_GetBoundingBox
	#	_IAcadEntity__com_Highlight
	#	_IAcadEntity__com_IntersectWith
	#	_IAcadEntity__com_Mirror
	#	_IAcadEntity__com_Mirror3D
	#	_IAcadEntity__com_Move
	#	_IAcadEntity__com_Rotate
	#	_IAcadEntity__com_Rotate3D
	#	_IAcadEntity__com_ScaleEntity
	#	_IAcadEntity__com_TransformBy
	#	_IAcadEntity__com_Update
	#	_IAcadEntity__com__get_EntityName
	#	_IAcadEntity__com__get_EntityTransparency
	#	_IAcadEntity__com__get_EntityType
	#	_IAcadEntity__com__get_Hyperlinks
	#	_IAcadEntity__com__get_Layer
	#	_IAcadEntity__com__get_Linetype
	#	_IAcadEntity__com__get_LinetypeScale
	#	_IAcadEntity__com__get_Lineweight
	#	_IAcadEntity__com__get_Material
	#	_IAcadEntity__com__get_PlotStyleName
	#	_IAcadEntity__com__get_TrueColor
	#	_IAcadEntity__com__get_Visible
	#	_IAcadEntity__com__get_color
	#	_IAcadEntity__com__set_EntityTransparency
	#	_IAcadEntity__com__set_Layer
	#	_IAcadEntity__com__set_Linetype
	#	_IAcadEntity__com__set_LinetypeScale
	#	_IAcadEntity__com__set_Lineweight
	#	_IAcadEntity__com__set_Material
	#	_IAcadEntity__com__set_PlotStyleName
	#	_IAcadEntity__com__set_TrueColor
	#	_IAcadEntity__com__set_Visible
	#	_IAcadEntity__com__set_color
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def arraypolar(self, NumberOfObjects: int, AngleToFill: float, CenterPoint: tagVARIANT) -> tagVARIANT:
		"Creates an array of selected objects in a polar pattern."
		# TODO: Check arguments
		# ['in'] NumberOfObjects:int
		# ['in'] AngleToFill:float
		# ['in'] CenterPoint:tagVARIANT
		# ['out', 'retval'] pArrayObjs:tagVARIANT
		# VBA: pArrayObjs = object.ArrayPolar (NumberOfObjects, AngleToFill, CenterPoint)
		return self.com_parent.ArrayPolar(NumberOfObjects, AngleToFill, CenterPoint)

	def arrayrectangular(self, NumberOfRows: int, NumberOfColumns: int, NumberOfLevels: int, DistBetweenRows: float, DistBetweenCols: float, DistBetweenLevels: float) -> tagVARIANT:
		"Creates an array of selected objects in a rectangular pattern."
		# TODO: Check arguments
		# ['in'] NumberOfRows:int
		# ['in'] NumberOfColumns:int
		# ['in'] NumberOfLevels:int
		# ['in'] DistBetweenRows:float
		# ['in'] DistBetweenCols:float
		# ['in'] DistBetweenLevels:float
		# ['out', 'retval'] pArrayObjs:tagVARIANT
		# VBA: pArrayObjs = object.ArrayRectangular (NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenCols, DistBetweenLevels)
		return self.com_parent.ArrayRectangular(NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenCols, DistBetweenLevels)

	def copy(self) -> POINTER(IDispatch):
		"Copies the entity object."
		# TODO: Check arguments
		# ['out', 'retval'] pCopyObj:POINTER(IDispatch)
		# VBA: pCopyObj = object.Copy ()
		return self.com_parent.Copy()

	def getboundingbox(self):
		"Returns the min and max point of the bounding box of the entity object."
		# TODO: Check arguments
		# ['out'] MinPoint:tagVARIANT
		# ['out'] MaxPoint:tagVARIANT
		# VBA: object.GetBoundingBox MinPoint, MaxPoint
		return self.com_parent.GetBoundingBox()

	def highlight(self, HighlightFlag: bool):
		"Highlights the entity object."
		# ['in'] HighlightFlag:bool
		# VBA: object.Highlight HighlightFlag
		self.com_parent.Highlight(HighlightFlag)

	def intersectwith(self, IntersectObject: POINTER(IDispatch), option: int) -> tagVARIANT:
		"Intersects with the input entity object."
		# TODO: Check arguments
		# ['in'] IntersectObject:POINTER(IDispatch)
		# ['in'] option:int
		# ['out', 'retval'] intPoints:tagVARIANT
		# VBA: intPoints = object.IntersectWith (IntersectObject, option)
		return self.com_parent.IntersectWith(IntersectObject, option)

	def mirror(self, Point1: tagVARIANT, Point2: tagVARIANT) -> POINTER(IDispatch):
		"Mirrors selected objects about a line."
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['out', 'retval'] pMirrorObj:POINTER(IDispatch)
		# VBA: pMirrorObj = object.Mirror (Point1, Point2)
		return self.com_parent.Mirror(Point1, Point2)

	def mirror3d(self, Point1: tagVARIANT, Point2: tagVARIANT, point3: tagVARIANT) -> POINTER(IDispatch):
		"Mirrors selected objects about a plane defined by three points."
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['in'] point3:tagVARIANT
		# ['out', 'retval'] pMirrorObj:POINTER(IDispatch)
		# VBA: pMirrorObj = object.Mirror3D (Point1, Point2, point3)
		return self.com_parent.Mirror3D(Point1, Point2, point3)

	def move(self, FromPoint: tagVARIANT, ToPoint: tagVARIANT):
		"Moves the entity object from source to destination."
		# TODO: Check arguments
		# ['in'] FromPoint:tagVARIANT
		# ['in'] ToPoint:tagVARIANT
		# VBA: object.Move FromPoint, ToPoint
		self.com_parent.Move(FromPoint, ToPoint)

	def rotate(self, BasePoint: tagVARIANT, RotationAngle: float):
		"Rotates the entity object about a point."
		# TODO: Check arguments
		# ['in'] BasePoint:tagVARIANT
		# ['in'] RotationAngle:float
		# VBA: object.Rotate BasePoint, RotationAngle
		self.com_parent.Rotate(BasePoint, RotationAngle)

	def rotate3d(self, Point1: tagVARIANT, Point2: tagVARIANT, RotationAngle: float):
		"Rotates the entity object about a 3D line."
		# TODO: Check arguments
		# ['in'] Point1:tagVARIANT
		# ['in'] Point2:tagVARIANT
		# ['in'] RotationAngle:float
		# VBA: object.Rotate3D Point1, Point2, RotationAngle
		self.com_parent.Rotate3D(Point1, Point2, RotationAngle)

	def scaleentity(self, BasePoint: tagVARIANT, ScaleFactor: float):
		"Scale the entity object with respect to the base point and the scale factor."
		# TODO: Check arguments
		# ['in'] BasePoint:tagVARIANT
		# ['in'] ScaleFactor:float
		# VBA: object.ScaleEntity BasePoint, ScaleFactor
		self.com_parent.ScaleEntity(BasePoint, ScaleFactor)

	def transformby(self, TransformationMatrix: tagVARIANT):
		"Performs the specified transformation on the entity object."
		# TODO: Check arguments
		# ['in'] TransformationMatrix:tagVARIANT
		# VBA: object.TransformBy TransformationMatrix
		self.com_parent.TransformBy(TransformationMatrix)

	def update(self):
		"Updates the graphics of the entity object."
		# VBA: object.Update 
		self.com_parent.Update()

	# Properties
	@indexedproperty
	def color(self) -> int:
		"Specifies the color for objects"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.color
	@color.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.color = color

	@indexedproperty
	def entityname(self) -> str:
		"Returns the class name of the object."
		# TODO: Check arguments
		# ['out', 'retval'] EntityName:str
		return self.com_parent.EntityName

	@indexedproperty
	def entitytransparency(self) -> str:
		"Specifies the transparency of the object"
		# TODO: Check arguments
		# ['out', 'retval'] transparency:str
		return self.com_parent.EntityTransparency
	@entitytransparency.setter
	def _(self, transparency:str):
		# ['in'] transparency:str
		self.com_parent.EntityTransparency = transparency

	@indexedproperty
	def entitytype(self) -> int:
		"Returns the entity type of the object as an integer."
		# TODO: Check arguments
		# ['out', 'retval'] entType:int
		return self.com_parent.EntityType

	@indexedproperty
	def hyperlinks(self) -> AcadHyperlinks:
		"Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)"
		# TODO: Check arguments
		# ['out', 'retval'] Hyperlinks:AcadHyperlinks
		return self.com_parent.Hyperlinks

	@indexedproperty
	def layer(self) -> str:
		"Specifies the current layer of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.Layer
	@layer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.Layer = Layer

	@indexedproperty
	def linetype(self) -> str:
		"Specifies the current linetype of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.Linetype
	@linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.Linetype = Linetype

	@indexedproperty
	def linetypescale(self) -> float:
		"Specifies the linetype scale factor of the object"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.LinetypeScale
	@linetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.LinetypeScale = ltScale

	@indexedproperty
	def lineweight(self) -> int:
		"Specifies the lineweight for the object"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.Lineweight
	@lineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.Lineweight = Lineweight

	@indexedproperty
	def material(self) -> str:
		"Specifies the material"
		# TODO: Check arguments
		# ['out', 'retval'] Material:str
		return self.com_parent.Material
	@material.setter
	def _(self, Material:str):
		# ['in'] Material:str
		self.com_parent.Material = Material

	@indexedproperty
	def plotstylename(self) -> str:
		"Specifies the plotstyle name for the object"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.PlotStyleName
	@plotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.PlotStyleName = plotStyle

	@indexedproperty
	def truecolor(self) -> AcadAcCmColor:
		"Returns the true color of the object."
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.TrueColor
	@truecolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.TrueColor = pColor

	@indexedproperty
	def visible(self) -> bool:
		"Specifies the visibility of an object or the application"
		# TODO: Check arguments
		# ['out', 'retval'] bVisible:bool
		return self.com_parent.Visible
	@visible.setter
	def _(self, bVisible:bool):
		# ['in'] bVisible:bool
		self.com_parent.Visible = bVisible


class AcadGroup(POINTER(_dll.IAcadGroup), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadGroup
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadGroup VBA-class wrapped as AcadGroup python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadGroup__com_AppendItems
	#	_IAcadGroup__com_Highlight
	#	_IAcadGroup__com_Item
	#	_IAcadGroup__com_RemoveItems
	#	_IAcadGroup__com_Update
	#	_IAcadGroup__com__get_Count
	#	_IAcadGroup__com__get_Name
	#	_IAcadGroup__com__get__NewEnum
	#	_IAcadGroup__com__set_Layer
	#	_IAcadGroup__com__set_Linetype
	#	_IAcadGroup__com__set_LinetypeScale
	#	_IAcadGroup__com__set_Lineweight
	#	_IAcadGroup__com__set_Material
	#	_IAcadGroup__com__set_Name
	#	_IAcadGroup__com__set_PlotStyleName
	#	_IAcadGroup__com__set_TrueColor
	#	_IAcadGroup__com__set_Visible
	#	_IAcadGroup__com__set_color
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def appenditems(self, Objects: tagVARIANT):
		"Appends one or more entities to the specified group"
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.AppendItems Objects
		self.com_parent.AppendItems(Objects)

	def highlight(self, HighlightFlag: bool):
		"Sets the highlight status for the given object, or for all objects in a given selection set"
		# ['in'] HighlightFlag:bool
		# VBA: object.Highlight HighlightFlag
		self.com_parent.Highlight(HighlightFlag)

	def item(self, Index: tagVARIANT) -> AcadEntity:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] ppEntity:AcadEntity
		# VBA: ppEntity = object.Item (Index)
		return self.com_parent.Item(Index)

	def removeitems(self, Objects: tagVARIANT):
		"Removes specified items from the group or selection set"
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.RemoveItems Objects
		self.com_parent.RemoveItems(Objects)

	def update(self):
		"Updates the object to the drawing screen"
		# VBA: object.Update 
		self.com_parent.Update()

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@property
	def color(self):
		"Specifies the color of an entity or layer"
	Exception("Can't GET color value") @color.setter
	def _(self, rhs:int):
		# ['in'] rhs:int
		self.com_parent.color = rhs

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count

	@property
	def layer(self):
		"Specifies the layer for an entity"
	Exception("Can't GET Layer value") @layer.setter
	def _(self, rhs:str):
		# ['in'] rhs:str
		self.com_parent.Layer = rhs

	@property
	def linetype(self):
		"Specifies the linetype of an entity"
	Exception("Can't GET Linetype value") @linetype.setter
	def _(self, rhs:str):
		# ['in'] rhs:str
		self.com_parent.Linetype = rhs

	@property
	def linetypescale(self):
		"Specifies the linetype scale of an entity"
	Exception("Can't GET LinetypeScale value") @linetypescale.setter
	def _(self, rhs:float):
		# ['in'] rhs:float
		self.com_parent.LinetypeScale = rhs

	@property
	def lineweight(self):
		"Specifies the lineweight of an individual entity or the default lineweight for the drawing"
	Exception("Can't GET Lineweight value") @lineweight.setter
	def _(self, rhs:int):
		# ['in'] rhs:int
		self.com_parent.Lineweight = rhs

	@property
	def material(self):
		"Specifies the material"
	Exception("Can't GET Material value") @material.setter
	def _(self, rhs:str):
		# ['in'] rhs:str
		self.com_parent.Material = rhs

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:str
		return self.com_parent.Name
	@name.setter
	def _(self, pVal:str):
		# ['in'] pVal:str
		self.com_parent.Name = pVal

	@property
	def plotstylename(self):
		"Specifies the plot style name for an entity"
	Exception("Can't GET PlotStyleName value") @plotstylename.setter
	def _(self, rhs:str):
		# ['in'] rhs:str
		self.com_parent.PlotStyleName = rhs

	@property
	def truecolor(self):
		"Sets the true color for entities in the group."
	Exception("Can't GET TrueColor value") @truecolor.setter
	def _(self, rhs:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] rhs:AcadAcCmColor
		self.com_parent.TrueColor = rhs

	@property
	def visible(self):
		"Specifies the visibility of an object or the application"
	Exception("Can't GET Visible value") @visible.setter
	def _(self, rhs:bool):
		# ['in'] rhs:bool
		self.com_parent.Visible = rhs


class AcadGroups(POINTER(_dll.IAcadGroups), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadGroups
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadGroups VBA-class wrapped as AcadGroups python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadGroups__com_Add
	#	_IAcadGroups__com_Item
	#	_IAcadGroups__com__get_Count
	#	_IAcadGroups__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadGroup:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pDimStyle:AcadGroup
		# VBA: pDimStyle = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadGroup:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadGroup
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadHyperlink(POINTER(_dll.IAcadHyperlink), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadHyperlink
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadHyperlink VBA-class wrapped as AcadHyperlink python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadHyperlink__com_Delete
	#	_IAcadHyperlink__com__get_Application
	#	_IAcadHyperlink__com__get_URL
	#	_IAcadHyperlink__com__get_URLDescription
	#	_IAcadHyperlink__com__get_URLNamedLocation
	#	_IAcadHyperlink__com__set_URL
	#	_IAcadHyperlink__com__set_URLDescription
	#	_IAcadHyperlink__com__set_URLNamedLocation
	# Methods
	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	# Properties
	@indexedproperty
	def application(self) -> POINTER(IDispatch):
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] ApplicationObject:POINTER(IDispatch)
		return self.com_parent.Application

	@indexedproperty
	def url(self) -> str:
		"Specifies the URL for the Hyperlink object"
		# TODO: Check arguments
		# ['out', 'retval'] URLPath:str
		return self.com_parent.URL
	@url.setter
	def _(self, URLPath:str):
		# ['in'] URLPath:str
		self.com_parent.URL = URLPath

	@indexedproperty
	def urldescription(self) -> str:
		"Specifies the URL description for the Hyperlink object"
		# TODO: Check arguments
		# ['out', 'retval'] Description:str
		return self.com_parent.URLDescription
	@urldescription.setter
	def _(self, Description:str):
		# ['in'] Description:str
		self.com_parent.URLDescription = Description

	@indexedproperty
	def urlnamedlocation(self) -> str:
		"Specifies the named location for the Hyperlink object"
		# TODO: Check arguments
		# ['out', 'retval'] Location:str
		return self.com_parent.URLNamedLocation
	@urlnamedlocation.setter
	def _(self, Location:str):
		# ['in'] Location:str
		self.com_parent.URLNamedLocation = Location


class AcadHyperlinks(POINTER(_dll.IAcadHyperlinks), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadHyperlinks
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadHyperlinks VBA-class wrapped as AcadHyperlinks python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadHyperlinks__com_Add
	#	_IAcadHyperlinks__com_Item
	#	_IAcadHyperlinks__com__get_Application
	#	_IAcadHyperlinks__com__get_Count
	#	_IAcadHyperlinks__com__get__NewEnum
	# Methods
	def add(self, Name: str, Description: tagVARIANT, NamedLocation: tagVARIANT) -> AcadHyperlink:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['in', '16'] Description:tagVARIANT
		# ['in', '16'] NamedLocation:tagVARIANT
		# ['out', 'retval'] pHyperlink:AcadHyperlink
		# VBA: pHyperlink = object.Add (Name, Description, NamedLocation)
		return self.com_parent.Add(Name, Description, NamedLocation)

	def item(self, Index: int) -> AcadHyperlink:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out', 'retval'] pItem:AcadHyperlink
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> POINTER(IDispatch):
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] ApplicationObject:POINTER(IDispatch)
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count


class AcadIdPair(POINTER(_dll.IAcadIdPair), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadIdPair
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadIdPair VBA-class wrapped as AcadIdPair python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadIdPair__com__get_Application
	#	_IAcadIdPair__com__get_IsCloned
	#	_IAcadIdPair__com__get_IsOwnerXlated
	#	_IAcadIdPair__com__get_IsPrimary
	#	_IAcadIdPair__com__get_Value
	#	_IAcadIdPair__com__get_key
	# Properties
	@indexedproperty
	def application(self) -> POINTER(IDispatch):
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] ApplicationObject:POINTER(IDispatch)
		return self.com_parent.Application

	@indexedproperty
	def iscloned(self) -> bool:
		"Determines if the source object in a CopyObjects operation has been cloned"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IsCloned

	@indexedproperty
	def isownerxlated(self) -> bool:
		"Determines if the owning object in a CopyObjects operation has been translated"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IsOwnerXlated

	@indexedproperty
	def isprimary(self) -> bool:
		"Determines if the source object in a CopyObjects operation was part of the primary set of objects being copied, or if it was simply owned by a member in the primary set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IsPrimary

	@indexedproperty
	def key(self) -> int:
		"The object ID of the source object in the CopyObjects operation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.key

	@indexedproperty
	def value(self) -> int:
		"The object ID of the newly created cloned object in the CopyObjects operation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Value


class AcadLayer(POINTER(_dll.IAcadLayer), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLayer
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadLayer VBA-class wrapped as AcadLayer python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLayer__com__get_Description
	#	_IAcadLayer__com__get_Freeze
	#	_IAcadLayer__com__get_LayerOn
	#	_IAcadLayer__com__get_Linetype
	#	_IAcadLayer__com__get_Lineweight
	#	_IAcadLayer__com__get_Lock
	#	_IAcadLayer__com__get_Material
	#	_IAcadLayer__com__get_Name
	#	_IAcadLayer__com__get_PlotStyleName
	#	_IAcadLayer__com__get_Plottable
	#	_IAcadLayer__com__get_TrueColor
	#	_IAcadLayer__com__get_Used
	#	_IAcadLayer__com__get_ViewportDefault
	#	_IAcadLayer__com__get_color
	#	_IAcadLayer__com__set_Description
	#	_IAcadLayer__com__set_Freeze
	#	_IAcadLayer__com__set_LayerOn
	#	_IAcadLayer__com__set_Linetype
	#	_IAcadLayer__com__set_Lineweight
	#	_IAcadLayer__com__set_Lock
	#	_IAcadLayer__com__set_Material
	#	_IAcadLayer__com__set_Name
	#	_IAcadLayer__com__set_PlotStyleName
	#	_IAcadLayer__com__set_Plottable
	#	_IAcadLayer__com__set_TrueColor
	#	_IAcadLayer__com__set_ViewportDefault
	#	_IAcadLayer__com__set_color
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Properties
	@indexedproperty
	def color(self) -> int:
		"Specifies the color of an entity or layer"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.color
	@color.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.color = color

	@indexedproperty
	def description(self) -> str:
		"Returns and sets the description of the layer."
		# TODO: Check arguments
		# ['out', 'retval'] Description:str
		return self.com_parent.Description
	@description.setter
	def _(self, Description:str):
		# ['in'] Description:str
		self.com_parent.Description = Description

	@indexedproperty
	def freeze(self) -> bool:
		"Specifies the freeze status of a layer"
		# TODO: Check arguments
		# ['out', 'retval'] bFreeze:bool
		return self.com_parent.Freeze
	@freeze.setter
	def _(self, bFreeze:bool):
		# ['in'] bFreeze:bool
		self.com_parent.Freeze = bFreeze

	@indexedproperty
	def layeron(self) -> bool:
		"Specifies the state of a layer"
		# TODO: Check arguments
		# ['out', 'retval'] bOn:bool
		return self.com_parent.LayerOn
	@layeron.setter
	def _(self, bOn:bool):
		# ['in'] bOn:bool
		self.com_parent.LayerOn = bOn

	@indexedproperty
	def linetype(self) -> str:
		"Specifies the linetype of an entity"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.Linetype
	@linetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.Linetype = Linetype

	@indexedproperty
	def lineweight(self) -> int:
		"Specifies the lineweight for the object"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.Lineweight
	@lineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.Lineweight = Lineweight

	@indexedproperty
	def lock(self) -> bool:
		"Locks or unlocks a layer"
		# TODO: Check arguments
		# ['out', 'retval'] Block:bool
		return self.com_parent.Lock
	@lock.setter
	def _(self, Block:bool):
		# ['in'] Block:bool
		self.com_parent.Lock = Block

	@indexedproperty
	def material(self) -> str:
		"Specifies the material"
		# TODO: Check arguments
		# ['out', 'retval'] Material:str
		return self.com_parent.Material
	@material.setter
	def _(self, Material:str):
		# ['in'] Material:str
		self.com_parent.Material = Material

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def plotstylename(self) -> str:
		"Specifies the plotstyle name for the object"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.PlotStyleName
	@plotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.PlotStyleName = plotStyle

	@indexedproperty
	def plottable(self) -> bool:
		"Specifies wether the layer is plottable."
		# TODO: Check arguments
		# ['out', 'retval'] bPlottable:bool
		return self.com_parent.Plottable
	@plottable.setter
	def _(self, bPlottable:bool):
		# ['in'] bPlottable:bool
		self.com_parent.Plottable = bPlottable

	@indexedproperty
	def truecolor(self) -> AcadAcCmColor:
		"Specifies the color of an entity or layer"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.TrueColor
	@truecolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.TrueColor = pColor

	@indexedproperty
	def used(self) -> bool:
		"returns whether the layer is in use. See GenerateUsageData."
		# TODO: Check arguments
		# ['out', 'retval'] bUsed:bool
		return self.com_parent.Used

	@indexedproperty
	def viewportdefault(self) -> bool:
		"Specifies if the layer is to be frozen in new viewports"
		# TODO: Check arguments
		# ['out', 'retval'] bDefault:bool
		return self.com_parent.ViewportDefault
	@viewportdefault.setter
	def _(self, bDefault:bool):
		# ['in'] bDefault:bool
		self.com_parent.ViewportDefault = bDefault


class AcadLayerStateManager(POINTER(_dll.IAcadLayerStateManager), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLayerStateManager
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadLayerStateManager VBA-class wrapped as AcadLayerStateManager python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLayerStateManager__com_Delete
	#	_IAcadLayerStateManager__com_Export
	#	_IAcadLayerStateManager__com_Import
	#	_IAcadLayerStateManager__com_Rename
	#	_IAcadLayerStateManager__com_Restore
	#	_IAcadLayerStateManager__com_Save
	#	_IAcadLayerStateManager__com_SetDatabase
	#	_IAcadLayerStateManager__com__get_Mask
	#	_IAcadLayerStateManager__com__set_Mask
	# Methods
	def delete(self, bsName: str):
		"Deletes the specified layers state."
		# ['in'] bsName:str
		# VBA: object.Delete bsName
		self.com_parent.Delete(bsName)

	def export(self, bsName: str, bsFilename: str):
		"Exports the specified layer state to the specified file."
		# ['in'] bsName:str
		# ['in'] bsFilename:str
		# VBA: object.Export bsName, bsFilename
		self.com_parent.Export(bsName, bsFilename)

	def import(self, bsFilename: str):
		"Imports all layer states from the specified file."
		# ['in'] bsFilename:str
		# VBA: object.Import bsFilename
		self.com_parent.Import(bsFilename)

	def rename(self, bsName: str, bsNewName: str):
		"Renames the specified layers state."
		# ['in'] bsName:str
		# ['in'] bsNewName:str
		# VBA: object.Rename bsName, bsNewName
		self.com_parent.Rename(bsName, bsNewName)

	def restore(self, bsName: str):
		"Restores the layers to the specified state as per the layer state mask."
		# ['in'] bsName:str
		# VBA: object.Restore bsName
		self.com_parent.Restore(bsName)

	def save(self, bsName: str, eMask: int):
		"Saves the attribute mask and the state of all layers into the specified layer state."
		# ['in'] bsName:str
		# ['in'] eMask:int
		# VBA: object.Save bsName, eMask
		self.com_parent.Save(bsName, eMask)

	def setdatabase(self, iHostDb: AcadDatabase):
		"Sets the working database for the layer state manager."
		# TODO: Check arguments
		# ['in'] iHostDb:AcadDatabase
		# VBA: object.SetDatabase iHostDb
		self.com_parent.SetDatabase(iHostDb)

	# Properties
	@indexedproperty
	def mask(self, bsName:str) -> int:
		"Sets the mask used for restoring the specified layer state."
		# TODO: Check arguments
		# ['in'] bsName:str
		# ['out', 'retval'] eMask:int
		return self.com_parent.Mask[bsName]
	@mask.setter
	def _(self, bsName:str, eMask:int):
		# ['in'] bsName:str
		# ['in'] eMask:int
		self.com_parent.Mask[bsName] = eMask


class AcadLayers(POINTER(_dll.IAcadLayers), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLayers
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadLayers VBA-class wrapped as AcadLayers python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLayers__com_Add
	#	_IAcadLayers__com_GenerateUsageData
	#	_IAcadLayers__com_Item
	#	_IAcadLayers__com__get_Count
	#	_IAcadLayers__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadLayer:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pLayer:AcadLayer
		# VBA: pLayer = object.Add (Name)
		return self.com_parent.Add(Name)

	def generateusagedata(self):
		"Generates layer usage data. See also Used property of Layer."
		# VBA: object.GenerateUsageData 
		self.com_parent.GenerateUsageData()

	def item(self, Index: tagVARIANT) -> AcadLayer:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadLayer
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadLayout(POINTER(_dll.IAcadLayout), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLayout
	#	IAcadPlotConfiguration
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadLayout VBA-class wrapped as AcadLayout python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLayout__com__get_Block
	#	_IAcadLayout__com__get_TabOrder
	#	_IAcadLayout__com__set_TabOrder
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadPlotConfiguration__com_CopyFrom
	#	_IAcadPlotConfiguration__com_GetCanonicalMediaNames
	#	_IAcadPlotConfiguration__com_GetCustomScale
	#	_IAcadPlotConfiguration__com_GetLocaleMediaName
	#	_IAcadPlotConfiguration__com_GetPaperMargins
	#	_IAcadPlotConfiguration__com_GetPaperSize
	#	_IAcadPlotConfiguration__com_GetPlotDeviceNames
	#	_IAcadPlotConfiguration__com_GetPlotStyleTableNames
	#	_IAcadPlotConfiguration__com_GetWindowToPlot
	#	_IAcadPlotConfiguration__com_RefreshPlotDeviceInfo
	#	_IAcadPlotConfiguration__com_SetCustomScale
	#	_IAcadPlotConfiguration__com_SetWindowToPlot
	#	_IAcadPlotConfiguration__com__get_CanonicalMediaName
	#	_IAcadPlotConfiguration__com__get_CenterPlot
	#	_IAcadPlotConfiguration__com__get_ConfigName
	#	_IAcadPlotConfiguration__com__get_ModelType
	#	_IAcadPlotConfiguration__com__get_Name
	#	_IAcadPlotConfiguration__com__get_PaperUnits
	#	_IAcadPlotConfiguration__com__get_PlotHidden
	#	_IAcadPlotConfiguration__com__get_PlotOrigin
	#	_IAcadPlotConfiguration__com__get_PlotRotation
	#	_IAcadPlotConfiguration__com__get_PlotType
	#	_IAcadPlotConfiguration__com__get_PlotViewportBorders
	#	_IAcadPlotConfiguration__com__get_PlotViewportsFirst
	#	_IAcadPlotConfiguration__com__get_PlotWithLineweights
	#	_IAcadPlotConfiguration__com__get_PlotWithPlotStyles
	#	_IAcadPlotConfiguration__com__get_ScaleLineweights
	#	_IAcadPlotConfiguration__com__get_ShowPlotStyles
	#	_IAcadPlotConfiguration__com__get_StandardScale
	#	_IAcadPlotConfiguration__com__get_StyleSheet
	#	_IAcadPlotConfiguration__com__get_UseStandardScale
	#	_IAcadPlotConfiguration__com__get_ViewToPlot
	#	_IAcadPlotConfiguration__com__set_CanonicalMediaName
	#	_IAcadPlotConfiguration__com__set_CenterPlot
	#	_IAcadPlotConfiguration__com__set_ConfigName
	#	_IAcadPlotConfiguration__com__set_Name
	#	_IAcadPlotConfiguration__com__set_PaperUnits
	#	_IAcadPlotConfiguration__com__set_PlotHidden
	#	_IAcadPlotConfiguration__com__set_PlotOrigin
	#	_IAcadPlotConfiguration__com__set_PlotRotation
	#	_IAcadPlotConfiguration__com__set_PlotType
	#	_IAcadPlotConfiguration__com__set_PlotViewportBorders
	#	_IAcadPlotConfiguration__com__set_PlotViewportsFirst
	#	_IAcadPlotConfiguration__com__set_PlotWithLineweights
	#	_IAcadPlotConfiguration__com__set_PlotWithPlotStyles
	#	_IAcadPlotConfiguration__com__set_ScaleLineweights
	#	_IAcadPlotConfiguration__com__set_ShowPlotStyles
	#	_IAcadPlotConfiguration__com__set_StandardScale
	#	_IAcadPlotConfiguration__com__set_StyleSheet
	#	_IAcadPlotConfiguration__com__set_UseStandardScale
	#	_IAcadPlotConfiguration__com__set_ViewToPlot
	# Properties
	@indexedproperty
	def block(self) -> AcadBlock:
		"Gets the block associated with the layout"
		# TODO: Check arguments
		# ['out', 'retval'] pBlock:AcadBlock
		return self.com_parent.Block

	@indexedproperty
	def taborder(self) -> int:
		"Specifies the tab order of a layout"
		# TODO: Check arguments
		# ['out', 'retval'] pOrder:int
		return self.com_parent.TabOrder
	@taborder.setter
	def _(self, pOrder:int):
		# ['in'] pOrder:int
		self.com_parent.TabOrder = pOrder


class AcadLayouts(POINTER(_dll.IAcadLayouts), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLayouts
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadLayouts VBA-class wrapped as AcadLayouts python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLayouts__com_Add
	#	_IAcadLayouts__com_Item
	#	_IAcadLayouts__com__get_Count
	#	_IAcadLayouts__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadLayout:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pLayout:AcadLayout
		# VBA: pLayout = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadLayout:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadLayout
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadLineType(POINTER(_dll.IAcadLineType), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLineType
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadLineType VBA-class wrapped as AcadLineType python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLineType__com__get_Description
	#	_IAcadLineType__com__get_Name
	#	_IAcadLineType__com__set_Description
	#	_IAcadLineType__com__set_Name
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Properties
	@indexedproperty
	def description(self) -> str:
		"Specifies the linetype description"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDes:str
		return self.com_parent.Description
	@description.setter
	def _(self, bstrDes:str):
		# ['in'] bstrDes:str
		self.com_parent.Description = bstrDes

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName


class AcadLineTypes(POINTER(_dll.IAcadLineTypes), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadLineTypes
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadLineTypes VBA-class wrapped as AcadLineTypes python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadLineTypes__com_Add
	#	_IAcadLineTypes__com_Item
	#	_IAcadLineTypes__com_Load
	#	_IAcadLineTypes__com__get_Count
	#	_IAcadLineTypes__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadLineType:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pLinetype:AcadLineType
		# VBA: pLinetype = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadLineType:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadLineType
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def load(self, Name: str, FileName: str):
		"Loads a menu group from a menu file or the definition of a linetype from a library (LIN) file"
		# ['in'] Name:str
		# ['in'] FileName:str
		# VBA: object.Load Name, FileName
		self.com_parent.Load(Name, FileName)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadMLeaderLeader(POINTER(_dll.IAcadMLeaderLeader), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMLeaderLeader
	#	IAcadSubEntity
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadMLeaderLeader VBA-class wrapped as AcadMLeaderLeader python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMLeaderLeader__com__get_ArrowheadBlock
	#	_IAcadMLeaderLeader__com__get_ArrowheadSize
	#	_IAcadMLeaderLeader__com__get_ArrowheadType
	#	_IAcadMLeaderLeader__com__get_LeaderLineColor
	#	_IAcadMLeaderLeader__com__get_LeaderLineWeight
	#	_IAcadMLeaderLeader__com__get_LeaderLinetype
	#	_IAcadMLeaderLeader__com__get_LeaderType
	#	_IAcadMLeaderLeader__com__set_ArrowheadBlock
	#	_IAcadMLeaderLeader__com__set_ArrowheadSize
	#	_IAcadMLeaderLeader__com__set_ArrowheadType
	#	_IAcadMLeaderLeader__com__set_LeaderLineColor
	#	_IAcadMLeaderLeader__com__set_LeaderLineWeight
	#	_IAcadMLeaderLeader__com__set_LeaderLinetype
	#	_IAcadMLeaderLeader__com__set_LeaderType
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Properties
	@indexedproperty
	def arrowheadblock(self) -> str:
		"Specifies the block to use as the custom arrowhead for leader lines of multileader"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:str
		return self.com_parent.ArrowheadBlock
	@arrowheadblock.setter
	def _(self, BlockName:str):
		# ['in'] BlockName:str
		self.com_parent.ArrowheadBlock = BlockName

	@indexedproperty
	def arrowheadsize(self) -> float:
		"Specifies the size of leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowheadSize
	@arrowheadsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowheadSize = size

	@indexedproperty
	def arrowheadtype(self) -> int:
		"Specifies the type of leader arrowhead"
		# TODO: Check arguments
		# ['out', 'retval'] BlockName:int
		return self.com_parent.ArrowheadType
	@arrowheadtype.setter
	def _(self, BlockName:int):
		# ['in'] BlockName:int
		self.com_parent.ArrowheadType = BlockName

	@indexedproperty
	def leaderlinecolor(self) -> AcadAcCmColor:
		"Specifies the color of the leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Type:AcadAcCmColor
		return self.com_parent.LeaderLineColor
	@leaderlinecolor.setter
	def _(self, Type:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] Type:AcadAcCmColor
		self.com_parent.LeaderLineColor = Type

	@indexedproperty
	def leaderlinetype(self) -> str:
		"Specifies the linetype of leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.LeaderLinetype
	@leaderlinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.LeaderLinetype = Linetype

	@indexedproperty
	def leaderlineweight(self) -> int:
		"Specifies the line weight of leader lines"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.LeaderLineWeight
	@leaderlineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.LeaderLineWeight = Lineweight

	@indexedproperty
	def leadertype(self) -> int:
		"Specifies the leader type"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.LeaderType
	@leadertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.LeaderType = Type


class AcadMLeaderStyle(POINTER(_dll.IAcadMLeaderStyle), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMLeaderStyle
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadMLeaderStyle VBA-class wrapped as AcadMLeaderStyle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMLeaderStyle__com__get_AlignSpace
	#	_IAcadMLeaderStyle__com__get_Annotative
	#	_IAcadMLeaderStyle__com__get_ArrowSize
	#	_IAcadMLeaderStyle__com__get_ArrowSymbol
	#	_IAcadMLeaderStyle__com__get_BitFlags
	#	_IAcadMLeaderStyle__com__get_Block
	#	_IAcadMLeaderStyle__com__get_BlockColor
	#	_IAcadMLeaderStyle__com__get_BlockConnectionType
	#	_IAcadMLeaderStyle__com__get_BlockRotation
	#	_IAcadMLeaderStyle__com__get_BlockScale
	#	_IAcadMLeaderStyle__com__get_BreakSize
	#	_IAcadMLeaderStyle__com__get_ContentType
	#	_IAcadMLeaderStyle__com__get_Description
	#	_IAcadMLeaderStyle__com__get_DoglegLength
	#	_IAcadMLeaderStyle__com__get_DrawLeaderOrderType
	#	_IAcadMLeaderStyle__com__get_DrawMLeaderOrderType
	#	_IAcadMLeaderStyle__com__get_EnableBlockRotation
	#	_IAcadMLeaderStyle__com__get_EnableBlockScale
	#	_IAcadMLeaderStyle__com__get_EnableDogleg
	#	_IAcadMLeaderStyle__com__get_EnableFrameText
	#	_IAcadMLeaderStyle__com__get_EnableLanding
	#	_IAcadMLeaderStyle__com__get_FirstSegmentAngleConstraint
	#	_IAcadMLeaderStyle__com__get_LandingGap
	#	_IAcadMLeaderStyle__com__get_LeaderLineColor
	#	_IAcadMLeaderStyle__com__get_LeaderLineTypeId
	#	_IAcadMLeaderStyle__com__get_LeaderLineWeight
	#	_IAcadMLeaderStyle__com__get_LeaderLinetype
	#	_IAcadMLeaderStyle__com__get_MaxLeaderSegmentsPoints
	#	_IAcadMLeaderStyle__com__get_Name
	#	_IAcadMLeaderStyle__com__get_OverwritePropChanged
	#	_IAcadMLeaderStyle__com__get_ScaleFactor
	#	_IAcadMLeaderStyle__com__get_SecondSegmentAngleConstraint
	#	_IAcadMLeaderStyle__com__get_TextAlignmentType
	#	_IAcadMLeaderStyle__com__get_TextAngleType
	#	_IAcadMLeaderStyle__com__get_TextAttachmentDirection
	#	_IAcadMLeaderStyle__com__get_TextBottomAttachmentType
	#	_IAcadMLeaderStyle__com__get_TextColor
	#	_IAcadMLeaderStyle__com__get_TextHeight
	#	_IAcadMLeaderStyle__com__get_TextLeftAttachmentType
	#	_IAcadMLeaderStyle__com__get_TextRightAttachmentType
	#	_IAcadMLeaderStyle__com__get_TextString
	#	_IAcadMLeaderStyle__com__get_TextStyle
	#	_IAcadMLeaderStyle__com__get_TextTopAttachmentType
	#	_IAcadMLeaderStyle__com__set_AlignSpace
	#	_IAcadMLeaderStyle__com__set_Annotative
	#	_IAcadMLeaderStyle__com__set_ArrowSize
	#	_IAcadMLeaderStyle__com__set_ArrowSymbol
	#	_IAcadMLeaderStyle__com__set_BitFlags
	#	_IAcadMLeaderStyle__com__set_Block
	#	_IAcadMLeaderStyle__com__set_BlockColor
	#	_IAcadMLeaderStyle__com__set_BlockConnectionType
	#	_IAcadMLeaderStyle__com__set_BlockRotation
	#	_IAcadMLeaderStyle__com__set_BlockScale
	#	_IAcadMLeaderStyle__com__set_BreakSize
	#	_IAcadMLeaderStyle__com__set_ContentType
	#	_IAcadMLeaderStyle__com__set_Description
	#	_IAcadMLeaderStyle__com__set_DoglegLength
	#	_IAcadMLeaderStyle__com__set_DrawLeaderOrderType
	#	_IAcadMLeaderStyle__com__set_DrawMLeaderOrderType
	#	_IAcadMLeaderStyle__com__set_EnableBlockRotation
	#	_IAcadMLeaderStyle__com__set_EnableBlockScale
	#	_IAcadMLeaderStyle__com__set_EnableDogleg
	#	_IAcadMLeaderStyle__com__set_EnableFrameText
	#	_IAcadMLeaderStyle__com__set_EnableLanding
	#	_IAcadMLeaderStyle__com__set_FirstSegmentAngleConstraint
	#	_IAcadMLeaderStyle__com__set_LandingGap
	#	_IAcadMLeaderStyle__com__set_LeaderLineColor
	#	_IAcadMLeaderStyle__com__set_LeaderLineTypeId
	#	_IAcadMLeaderStyle__com__set_LeaderLineWeight
	#	_IAcadMLeaderStyle__com__set_LeaderLinetype
	#	_IAcadMLeaderStyle__com__set_MaxLeaderSegmentsPoints
	#	_IAcadMLeaderStyle__com__set_Name
	#	_IAcadMLeaderStyle__com__set_ScaleFactor
	#	_IAcadMLeaderStyle__com__set_SecondSegmentAngleConstraint
	#	_IAcadMLeaderStyle__com__set_TextAlignmentType
	#	_IAcadMLeaderStyle__com__set_TextAngleType
	#	_IAcadMLeaderStyle__com__set_TextAttachmentDirection
	#	_IAcadMLeaderStyle__com__set_TextBottomAttachmentType
	#	_IAcadMLeaderStyle__com__set_TextColor
	#	_IAcadMLeaderStyle__com__set_TextHeight
	#	_IAcadMLeaderStyle__com__set_TextLeftAttachmentType
	#	_IAcadMLeaderStyle__com__set_TextRightAttachmentType
	#	_IAcadMLeaderStyle__com__set_TextString
	#	_IAcadMLeaderStyle__com__set_TextStyle
	#	_IAcadMLeaderStyle__com__set_TextTopAttachmentType
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Properties
	@indexedproperty
	def alignspace(self) -> float:
		"Returns the alignment space value for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] AlignSpace:float
		return self.com_parent.AlignSpace
	@alignspace.setter
	def _(self, AlignSpace:float):
		# ['in'] AlignSpace:float
		self.com_parent.AlignSpace = AlignSpace

	@indexedproperty
	def annotative(self) -> bool:
		"Returns the annotative status for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Annotative:bool
		return self.com_parent.Annotative
	@annotative.setter
	def _(self, Annotative:bool):
		# ['in'] Annotative:bool
		self.com_parent.Annotative = Annotative

	@indexedproperty
	def arrowsize(self) -> float:
		"Returns the arrow size for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.ArrowSize
	@arrowsize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.ArrowSize = size

	@indexedproperty
	def arrowsymbol(self) -> str:
		"Returns the arrow symbol for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.ArrowSymbol
	@arrowsymbol.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.ArrowSymbol = Name

	@indexedproperty
	def bitflags(self) -> int:
		"Returns the operation bit set for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] bitFlag:int
		return self.com_parent.BitFlags
	@bitflags.setter
	def _(self, bitFlag:int):
		# ['in'] bitFlag:int
		self.com_parent.BitFlags = bitFlag

	@indexedproperty
	def block(self) -> str:
		"Returns the block content for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.Block
	@block.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.Block = Name

	@indexedproperty
	def blockcolor(self) -> AcadAcCmColor:
		"Returns the block color in block content for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] color:AcadAcCmColor
		return self.com_parent.BlockColor
	@blockcolor.setter
	def _(self, color:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] color:AcadAcCmColor
		self.com_parent.BlockColor = color

	@indexedproperty
	def blockconnectiontype(self) -> int:
		"Returns the block connection type for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.BlockConnectionType
	@blockconnectiontype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.BlockConnectionType = Type

	@indexedproperty
	def blockrotation(self) -> float:
		"Returns the rotation of the block referenced by multileader for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Rotation:float
		return self.com_parent.BlockRotation
	@blockrotation.setter
	def _(self, Rotation:float):
		# ['in'] Rotation:float
		self.com_parent.BlockRotation = Rotation

	@indexedproperty
	def blockscale(self) -> float:
		"Returns the scale of the block referenced by multileader for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] ScaleFactor:float
		return self.com_parent.BlockScale
	@blockscale.setter
	def _(self, ScaleFactor:float):
		# ['in'] ScaleFactor:float
		self.com_parent.BlockScale = ScaleFactor

	@indexedproperty
	def breaksize(self) -> float:
		"Returns the break size used for breaking leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] size:float
		return self.com_parent.BreakSize
	@breaksize.setter
	def _(self, size:float):
		# ['in'] size:float
		self.com_parent.BreakSize = size

	@indexedproperty
	def contenttype(self) -> int:
		"Returns the content type for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.ContentType
	@contenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.ContentType = Type

	@indexedproperty
	def description(self) -> str:
		"Returns the description for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Description:str
		return self.com_parent.Description
	@description.setter
	def _(self, Description:str):
		# ['in'] Description:str
		self.com_parent.Description = Description

	@indexedproperty
	def dogleglength(self) -> float:
		"Returns the length of dog-leg leader line for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] DoglegLength:float
		return self.com_parent.DoglegLength
	@dogleglength.setter
	def _(self, DoglegLength:float):
		# ['in'] DoglegLength:float
		self.com_parent.DoglegLength = DoglegLength

	@indexedproperty
	def drawleaderordertype(self) -> int:
		"Returns the order of leader line creation when creating a multileader for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.DrawLeaderOrderType
	@drawleaderordertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DrawLeaderOrderType = Type

	@indexedproperty
	def drawmleaderordertype(self) -> int:
		"Returns the order of multileader creation for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.DrawMLeaderOrderType
	@drawmleaderordertype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.DrawMLeaderOrderType = Type

	@indexedproperty
	def enableblockrotation(self) -> bool:
		"Indicate whether the block rotation value works for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] enabled:bool
		return self.com_parent.EnableBlockRotation
	@enableblockrotation.setter
	def _(self, enabled:bool):
		# ['in'] enabled:bool
		self.com_parent.EnableBlockRotation = enabled

	@indexedproperty
	def enableblockscale(self) -> bool:
		"Indicate whether the block scale value works for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] enabled:bool
		return self.com_parent.EnableBlockScale
	@enableblockscale.setter
	def _(self, enabled:bool):
		# ['in'] enabled:bool
		self.com_parent.EnableBlockScale = enabled

	@indexedproperty
	def enabledogleg(self) -> bool:
		"Indicate whether dog-leg leader lines are enabled for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] enabled:bool
		return self.com_parent.EnableDogleg
	@enabledogleg.setter
	def _(self, enabled:bool):
		# ['in'] enabled:bool
		self.com_parent.EnableDogleg = enabled

	@indexedproperty
	def enableframetext(self) -> bool:
		"Indicate whether or not the text frame is displayed around the MText for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] enabled:bool
		return self.com_parent.EnableFrameText
	@enableframetext.setter
	def _(self, enabled:bool):
		# ['in'] enabled:bool
		self.com_parent.EnableFrameText = enabled

	@indexedproperty
	def enablelanding(self) -> bool:
		"Indicate whether landing of leader line is enabled for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] enabled:bool
		return self.com_parent.EnableLanding
	@enablelanding.setter
	def _(self, enabled:bool):
		# ['in'] enabled:bool
		self.com_parent.EnableLanding = enabled

	@indexedproperty
	def firstsegmentangleconstraint(self) -> int:
		"Returns the first segment angle constraint when creating a multileader for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] constraint:int
		return self.com_parent.FirstSegmentAngleConstraint
	@firstsegmentangleconstraint.setter
	def _(self, constraint:int):
		# ['in'] constraint:int
		self.com_parent.FirstSegmentAngleConstraint = constraint

	@indexedproperty
	def landinggap(self) -> float:
		"Returns the gap between MText and the tail of leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] LandingGap:float
		return self.com_parent.LandingGap
	@landinggap.setter
	def _(self, LandingGap:float):
		# ['in'] LandingGap:float
		self.com_parent.LandingGap = LandingGap

	@indexedproperty
	def leaderlinecolor(self) -> AcadAcCmColor:
		"Returns the color of leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] color:AcadAcCmColor
		return self.com_parent.LeaderLineColor
	@leaderlinecolor.setter
	def _(self, color:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] color:AcadAcCmColor
		self.com_parent.LeaderLineColor = color

	@indexedproperty
	def leaderlinetype(self) -> int:
		"Returns the leader line type for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.LeaderLinetype
	@leaderlinetype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.LeaderLinetype = Type

	@indexedproperty
	def leaderlinetypeid(self) -> str:
		"Returns the linetype of leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:str
		return self.com_parent.LeaderLineTypeId
	@leaderlinetypeid.setter
	def _(self, Type:str):
		# ['in'] Type:str
		self.com_parent.LeaderLineTypeId = Type

	@indexedproperty
	def leaderlineweight(self) -> int:
		"Returns the line weight of leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] weight:int
		return self.com_parent.LeaderLineWeight
	@leaderlineweight.setter
	def _(self, weight:int):
		# ['in'] weight:int
		self.com_parent.LeaderLineWeight = weight

	@indexedproperty
	def maxleadersegmentspoints(self) -> int:
		"Returns the max number of segment points in leader lines for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] number:int
		return self.com_parent.MaxLeaderSegmentsPoints
	@maxleadersegmentspoints.setter
	def _(self, number:int):
		# ['in'] number:int
		self.com_parent.MaxLeaderSegmentsPoints = number

	@indexedproperty
	def name(self) -> str:
		"Returns the name for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.Name
	@name.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.Name = Name

	@indexedproperty
	def overwritepropchanged(self) -> bool:
		"Indicate whether properties were changed for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] changed:bool
		return self.com_parent.OverwritePropChanged

	@indexedproperty
	def scalefactor(self) -> float:
		"Returns the scale of multileader created for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] scale:float
		return self.com_parent.ScaleFactor
	@scalefactor.setter
	def _(self, scale:float):
		# ['in'] scale:float
		self.com_parent.ScaleFactor = scale

	@indexedproperty
	def secondsegmentangleconstraint(self) -> int:
		"Returns the second segment angle constraint when creating a multileader for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] constraint:int
		return self.com_parent.SecondSegmentAngleConstraint
	@secondsegmentangleconstraint.setter
	def _(self, constraint:int):
		# ['in'] constraint:int
		self.com_parent.SecondSegmentAngleConstraint = constraint

	@indexedproperty
	def textalignmenttype(self) -> int:
		"Returns the text alignment type for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextAlignmentType
	@textalignmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextAlignmentType = Type

	@indexedproperty
	def textangletype(self) -> int:
		"Returns the angle type of text with respect to the last leader line segment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextAngleType
	@textangletype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextAngleType = Type

	@indexedproperty
	def textattachmentdirection(self) -> int:
		"Returns the type of text attachment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] dir:int
		return self.com_parent.TextAttachmentDirection
	@textattachmentdirection.setter
	def _(self, dir:int):
		# ['in'] dir:int
		self.com_parent.TextAttachmentDirection = dir

	@indexedproperty
	def textbottomattachmenttype(self) -> int:
		"Returns the type of text attachment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextBottomAttachmentType
	@textbottomattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextBottomAttachmentType = Type

	@indexedproperty
	def textcolor(self) -> AcadAcCmColor:
		"Returns the text color of MText for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] color:AcadAcCmColor
		return self.com_parent.TextColor
	@textcolor.setter
	def _(self, color:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] color:AcadAcCmColor
		self.com_parent.TextColor = color

	@indexedproperty
	def textheight(self) -> float:
		"Returns the text height of MText for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.TextHeight
	@textheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.TextHeight = Height

	@indexedproperty
	def textleftattachmenttype(self) -> int:
		"Returns the type of text attachment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextLeftAttachmentType
	@textleftattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextLeftAttachmentType = Type

	@indexedproperty
	def textrightattachmenttype(self) -> int:
		"Returns the type of text attachment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextRightAttachmentType
	@textrightattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextRightAttachmentType = Type

	@indexedproperty
	def textstring(self) -> str:
		"Returns the text string of the Mtext for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Text:str
		return self.com_parent.TextString
	@textstring.setter
	def _(self, Text:str):
		# ['in'] Text:str
		self.com_parent.TextString = Text

	@indexedproperty
	def textstyle(self) -> str:
		"Returns the text style for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.TextStyle
	@textstyle.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.TextStyle = Name

	@indexedproperty
	def texttopattachmenttype(self) -> int:
		"Returns the type of text attachment for the specified mleaderstyle."
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.TextTopAttachmentType
	@texttopattachmenttype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.TextTopAttachmentType = Type


class AcadMaterial(POINTER(_dll.IAcadMaterial), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMaterial
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadMaterial VBA-class wrapped as AcadMaterial python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMaterial__com__get_Description
	#	_IAcadMaterial__com__get_Name
	#	_IAcadMaterial__com__set_Description
	#	_IAcadMaterial__com__set_Name
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Properties
	@indexedproperty
	def description(self) -> str:
		"Specifies the material description"
		# TODO: Check arguments
		# ['out', 'retval'] bstrDes:str
		return self.com_parent.Description
	@description.setter
	def _(self, bstrDes:str):
		# ['in'] bstrDes:str
		self.com_parent.Description = bstrDes

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName


class AcadMaterials(POINTER(_dll.IAcadMaterials), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMaterials
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadMaterials VBA-class wrapped as AcadMaterials python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMaterials__com_Add
	#	_IAcadMaterials__com_Item
	#	_IAcadMaterials__com__get_Count
	#	_IAcadMaterials__com__get__NewEnum
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def add(self, Name: str) -> AcadMaterial:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pDimStyle:AcadMaterial
		# VBA: pDimStyle = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadMaterial:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadMaterial
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadMenuBar(POINTER(_dll.IAcadMenuBar), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMenuBar
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadMenuBar VBA-class wrapped as AcadMenuBar python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMenuBar__com_Item
	#	_IAcadMenuBar__com__get_Application
	#	_IAcadMenuBar__com__get_Count
	#	_IAcadMenuBar__com__get_Parent
	#	_IAcadMenuBar__com__get__NewEnum
	# Methods
	def item(self, Index: tagVARIANT) -> AcadPopupMenu:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadPopupMenu
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def parent(self) -> AcadApplication:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadApplication
		return self.com_parent.Parent


class AcadMenuGroup(POINTER(_dll.IAcadMenuGroup), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMenuGroup
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadMenuGroup VBA-class wrapped as AcadMenuGroup python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMenuGroup__com_Save
	#	_IAcadMenuGroup__com_SaveAs
	#	_IAcadMenuGroup__com_Unload
	#	_IAcadMenuGroup__com__get_Application
	#	_IAcadMenuGroup__com__get_MenuFileName
	#	_IAcadMenuGroup__com__get_Menus
	#	_IAcadMenuGroup__com__get_Name
	#	_IAcadMenuGroup__com__get_Parent
	#	_IAcadMenuGroup__com__get_Toolbars
	#	_IAcadMenuGroup__com__get_Type
	# Methods
	def save(self, MenuFileType: int):
		"Saves the document or menu group"
		# ['in'] MenuFileType:int
		# VBA: object.Save MenuFileType
		self.com_parent.Save(MenuFileType)

	def saveas(self, MenuFileName: str, MenuFileType: int):
		"Saves the document or menu group to a specified file"
		# ['in'] MenuFileName:str
		# ['in'] MenuFileType:int
		# VBA: object.SaveAs MenuFileName, MenuFileType
		self.com_parent.SaveAs(MenuFileName, MenuFileType)

	def unload(self):
		"Unloads the menu group or external reference"
		# VBA: object.Unload 
		self.com_parent.Unload()

	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def menufilename(self) -> str:
		"Gets the menu file name where the menu group is located"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.MenuFileName

	@indexedproperty
	def menus(self) -> AcadPopupMenus:
		"Gets the PopupMenus collection"
		# TODO: Check arguments
		# ['out', 'retval'] pMenus:AcadPopupMenus
		return self.com_parent.Menus

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.Name

	@indexedproperty
	def parent(self) -> AcadMenuGroups:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadMenuGroups
		return self.com_parent.Parent

	@indexedproperty
	def toolbars(self) -> AcadToolbars:
		"Gets the Toolbars collection"
		# TODO: Check arguments
		# ['out', 'retval'] pToolbars:AcadToolbars
		return self.com_parent.Toolbars

	@indexedproperty
	def type(self) -> int:
		"Specifies type of a Leader, MenuGroup, PopupMenuItem, ToolbarItem, Polyline, or PolygonMesh object"
		# TODO: Check arguments
		# ['out', 'retval'] menuType:int
		return self.com_parent.Type


class AcadMenuGroups(POINTER(_dll.IAcadMenuGroups), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadMenuGroups
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadMenuGroups VBA-class wrapped as AcadMenuGroups python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadMenuGroups__com_Item
	#	_IAcadMenuGroups__com_Load
	#	_IAcadMenuGroups__com__get_Application
	#	_IAcadMenuGroups__com__get_Count
	#	_IAcadMenuGroups__com__get_Parent
	#	_IAcadMenuGroups__com__get__NewEnum
	# Methods
	def item(self, Index: tagVARIANT) -> AcadMenuGroup:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadMenuGroup
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def load(self, MenuFileName: str, BaseMenu: tagVARIANT) -> AcadMenuGroup:
		"Loads a menu group from a menu file or the definition of a linetype from a library (LIN) file"
		# TODO: Check arguments
		# ['in'] MenuFileName:str
		# ['in', '16'] BaseMenu:tagVARIANT
		# ['out', 'retval'] pMenuGroup:AcadMenuGroup
		# VBA: pMenuGroup = object.Load (MenuFileName, BaseMenu)
		return self.com_parent.Load(MenuFileName, BaseMenu)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def parent(self) -> AcadApplication:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadApplication
		return self.com_parent.Parent


class AcadObject(POINTER(_dll.IAcadObject), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadObject
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadObject VBA-class wrapped as AcadObject python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	# Methods
	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	def erase(self):
		"Erases all the objects in a selection set"
		# VBA: object.Erase 
		self.com_parent.Erase()

	def getextensiondictionary(self) -> AcadDictionary:
		"Gets the extension dictionary associated with an object"
		# TODO: Check arguments
		# ['out', 'retval'] pExtDictionary:AcadDictionary
		# VBA: pExtDictionary = object.GetExtensionDictionary ()
		return self.com_parent.GetExtensionDictionary()

	def getxdata(self, AppName: str):
		"Gets the extended data (XData) associated with an object"
		# TODO: Check arguments
		# ['in'] AppName:str
		# ['out'] XDataType:tagVARIANT
		# ['out'] XDataValue:tagVARIANT
		# VBA: object.GetXData AppName, XDataType, XDataValue
		return self.com_parent.GetXData(AppName)

	def setxdata(self, XDataType: tagVARIANT, XDataValue: tagVARIANT):
		"Sets the extended data (XData) associated with an object"
		# TODO: Check arguments
		# ['in'] XDataType:tagVARIANT
		# ['in'] XDataValue:tagVARIANT
		# VBA: object.SetXData XDataType, XDataValue
		self.com_parent.SetXData(XDataType, XDataValue)

	# Properties
	@indexedproperty
	def application(self) -> POINTER(IDispatch):
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] ApplicationObject:POINTER(IDispatch)
		return self.com_parent.Application

	@indexedproperty
	def database(self) -> AcadDatabase:
		"Gets the database in which the object belongs"
		# TODO: Check arguments
		# ['out', 'retval'] pDatabase:AcadDatabase
		return self.com_parent.Database

	@indexedproperty
	def document(self) -> POINTER(IDispatch):
		"Gets the document (drawing) in which the object belongs"
		# TODO: Check arguments
		# ['out', 'retval'] pDocument:POINTER(IDispatch)
		return self.com_parent.Document

	@indexedproperty
	def handle(self) -> str:
		"Gets the handle of an object"
		# TODO: Check arguments
		# ['out', 'retval'] Handle:str
		return self.com_parent.Handle

	@indexedproperty
	def hasextensiondictionary(self) -> bool:
		"Determines if the object has an extension dictionary associated with it"
		# TODO: Check arguments
		# ['out', 'retval'] bHasDictionary:bool
		return self.com_parent.HasExtensionDictionary

	@indexedproperty
	def objectid(self) -> int:
		"Gets the object ID of the object"
		# TODO: Check arguments
		# ['out', 'retval'] ObjectID:int
		return self.com_parent.ObjectID

	@indexedproperty
	def objectname(self) -> str:
		"Gets the AutoCAD class name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] ObjectName:str
		return self.com_parent.ObjectName

	@indexedproperty
	def ownerid(self) -> int:
		"Gets the object ID of the owner (parent) object"
		# TODO: Check arguments
		# ['out', 'retval'] OwnerID:int
		return self.com_parent.OwnerID


class AcadObjectEvents(POINTER(_dll.IAcadObjectEvents), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadObjectEvents
	#	IUnknown
	#		object
	# Prototype for IAcadObjectEvents VBA-class wrapped as AcadObjectEvents python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObjectEvents__com_Modified
	# Methods
	def modified(self, pObject: AcadObject):
		"Triggered when an object or collection in the drawing has been modified"
		# TODO: Check arguments
		# ['in'] pObject:AcadObject
		# VBA: object.Modified pObject
		self.com_parent.Modified(pObject)


class AcadPaperSpace(POINTER(_dll.IAcadPaperSpace), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPaperSpace
	#	IAcadBlock
	#		IAcadObject
	#			IDispatch
	#				IUnknown
	#					object
	# Prototype for IAcadPaperSpace VBA-class wrapped as AcadPaperSpace python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadBlock__com_Add3DFace
	#	_IAcadBlock__com_Add3DMesh
	#	_IAcadBlock__com_Add3DPoly
	#	_IAcadBlock__com_AddArc
	#	_IAcadBlock__com_AddAttribute
	#	_IAcadBlock__com_AddBox
	#	_IAcadBlock__com_AddCircle
	#	_IAcadBlock__com_AddCone
	#	_IAcadBlock__com_AddCustomObject
	#	_IAcadBlock__com_AddCylinder
	#	_IAcadBlock__com_AddDim3PointAngular
	#	_IAcadBlock__com_AddDimAligned
	#	_IAcadBlock__com_AddDimAngular
	#	_IAcadBlock__com_AddDimArc
	#	_IAcadBlock__com_AddDimDiametric
	#	_IAcadBlock__com_AddDimOrdinate
	#	_IAcadBlock__com_AddDimRadial
	#	_IAcadBlock__com_AddDimRadialLarge
	#	_IAcadBlock__com_AddDimRotated
	#	_IAcadBlock__com_AddEllipse
	#	_IAcadBlock__com_AddEllipticalCone
	#	_IAcadBlock__com_AddEllipticalCylinder
	#	_IAcadBlock__com_AddExtrudedSolid
	#	_IAcadBlock__com_AddExtrudedSolidAlongPath
	#	_IAcadBlock__com_AddHatch
	#	_IAcadBlock__com_AddLeader
	#	_IAcadBlock__com_AddLightWeightPolyline
	#	_IAcadBlock__com_AddLine
	#	_IAcadBlock__com_AddMInsertBlock
	#	_IAcadBlock__com_AddMLeader
	#	_IAcadBlock__com_AddMLine
	#	_IAcadBlock__com_AddMText
	#	_IAcadBlock__com_AddPoint
	#	_IAcadBlock__com_AddPolyfaceMesh
	#	_IAcadBlock__com_AddPolyline
	#	_IAcadBlock__com_AddRaster
	#	_IAcadBlock__com_AddRay
	#	_IAcadBlock__com_AddRegion
	#	_IAcadBlock__com_AddRevolvedSolid
	#	_IAcadBlock__com_AddSection
	#	_IAcadBlock__com_AddShape
	#	_IAcadBlock__com_AddSolid
	#	_IAcadBlock__com_AddSphere
	#	_IAcadBlock__com_AddSpline
	#	_IAcadBlock__com_AddTable
	#	_IAcadBlock__com_AddText
	#	_IAcadBlock__com_AddTolerance
	#	_IAcadBlock__com_AddTorus
	#	_IAcadBlock__com_AddTrace
	#	_IAcadBlock__com_AddWedge
	#	_IAcadBlock__com_AddXline
	#	_IAcadBlock__com_AttachExternalReference
	#	_IAcadBlock__com_Bind
	#	_IAcadBlock__com_Detach
	#	_IAcadBlock__com_InsertBlock
	#	_IAcadBlock__com_Item
	#	_IAcadBlock__com_Reload
	#	_IAcadBlock__com_Unload
	#	_IAcadBlock__com__get_BlockScaling
	#	_IAcadBlock__com__get_Comments
	#	_IAcadBlock__com__get_Count
	#	_IAcadBlock__com__get_Explodable
	#	_IAcadBlock__com__get_IsDynamicBlock
	#	_IAcadBlock__com__get_IsLayout
	#	_IAcadBlock__com__get_IsXRef
	#	_IAcadBlock__com__get_Layout
	#	_IAcadBlock__com__get_Name
	#	_IAcadBlock__com__get_Origin
	#	_IAcadBlock__com__get_Path
	#	_IAcadBlock__com__get_Units
	#	_IAcadBlock__com__get_XRefDatabase
	#	_IAcadBlock__com__get__NewEnum
	#	_IAcadBlock__com__set_BlockScaling
	#	_IAcadBlock__com__set_Comments
	#	_IAcadBlock__com__set_Explodable
	#	_IAcadBlock__com__set_Name
	#	_IAcadBlock__com__set_Origin
	#	_IAcadBlock__com__set_Path
	#	_IAcadBlock__com__set_Units
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadPaperSpace__com_AddPViewport
	# Methods
	def addpviewport(self, Center: tagVARIANT, Width: float, Height: float) -> AcadPViewport:
		"Adds a paper space viewport, given the center, height, and width"
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		# ['in'] Width:float
		# ['in'] Height:float
		# ['out', 'retval'] pPViewport:AcadPViewport
		# VBA: pPViewport = object.AddPViewport (Center, Width, Height)
		return self.com_parent.AddPViewport(Center, Width, Height)


class AcadPlot(POINTER(_dll.IAcadPlot), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPlot
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPlot VBA-class wrapped as AcadPlot python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPlot__com_DisplayPlotPreview
	#	_IAcadPlot__com_PlotToDevice
	#	_IAcadPlot__com_PlotToFile
	#	_IAcadPlot__com_SetLayoutsToPlot
	#	_IAcadPlot__com_StartBatchMode
	#	_IAcadPlot__com__get_Application
	#	_IAcadPlot__com__get_BatchPlotProgress
	#	_IAcadPlot__com__get_NumberOfCopies
	#	_IAcadPlot__com__get_QuietErrorMode
	#	_IAcadPlot__com__set_BatchPlotProgress
	#	_IAcadPlot__com__set_NumberOfCopies
	#	_IAcadPlot__com__set_QuietErrorMode
	# Methods
	def displayplotpreview(self, Preview: int):
		"Displays the Plot Preview dialog box with the specified partial or full view preview"
		# ['in'] Preview:int
		# VBA: object.DisplayPlotPreview Preview
		self.com_parent.DisplayPlotPreview(Preview)

	def plottodevice(self, plotConfig: tagVARIANT) -> bool:
		"Plots a layout to a device"
		# TODO: Check arguments
		# ['in', '16'] plotConfig:tagVARIANT
		# ['out', 'retval'] success:bool
		# VBA: success = object.PlotToDevice (plotConfig)
		return self.com_parent.PlotToDevice(plotConfig)

	def plottofile(self, plotFile: str, plotConfig: tagVARIANT) -> bool:
		"Plots a layout to the specified file"
		# TODO: Check arguments
		# ['in'] plotFile:str
		# ['in', '16'] plotConfig:tagVARIANT
		# ['out', 'retval'] success:bool
		# VBA: success = object.PlotToFile (plotFile, plotConfig)
		return self.com_parent.PlotToFile(plotFile, plotConfig)

	def setlayoutstoplot(self, layoutList: tagVARIANT):
		"Specifies the layout or layouts to plot"
		# TODO: Check arguments
		# ['in'] layoutList:tagVARIANT
		# VBA: object.SetLayoutsToPlot layoutList
		self.com_parent.SetLayoutsToPlot(layoutList)

	def startbatchmode(self, entryCount: int):
		"Invokes batchmode printing"
		# ['in'] entryCount:int
		# VBA: object.StartBatchMode entryCount
		self.com_parent.StartBatchMode(entryCount)

	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def batchplotprogress(self) -> bool:
		"Gets the current status of the batch plot, or terminates the batch plot"
		# TODO: Check arguments
		# ['out', 'retval'] bProgressStatus:bool
		return self.com_parent.BatchPlotProgress
	@batchplotprogress.setter
	def _(self, bProgressStatus:bool):
		# ['in'] bProgressStatus:bool
		self.com_parent.BatchPlotProgress = bProgressStatus

	@indexedproperty
	def numberofcopies(self) -> int:
		"Specifies the number of copies to plot"
		# TODO: Check arguments
		# ['out', 'retval'] numCopies:int
		return self.com_parent.NumberOfCopies
	@numberofcopies.setter
	def _(self, numCopies:int):
		# ['in'] numCopies:int
		self.com_parent.NumberOfCopies = numCopies

	@indexedproperty
	def quieterrormode(self) -> bool:
		"Toggles the quiet error mode for plot error reporting"
		# TODO: Check arguments
		# ['out', 'retval'] bErrorMode:bool
		return self.com_parent.QuietErrorMode
	@quieterrormode.setter
	def _(self, bErrorMode:bool):
		# ['in'] bErrorMode:bool
		self.com_parent.QuietErrorMode = bErrorMode


class AcadPlotConfiguration(POINTER(_dll.IAcadPlotConfiguration), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPlotConfiguration
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadPlotConfiguration VBA-class wrapped as AcadPlotConfiguration python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadPlotConfiguration__com_CopyFrom
	#	_IAcadPlotConfiguration__com_GetCanonicalMediaNames
	#	_IAcadPlotConfiguration__com_GetCustomScale
	#	_IAcadPlotConfiguration__com_GetLocaleMediaName
	#	_IAcadPlotConfiguration__com_GetPaperMargins
	#	_IAcadPlotConfiguration__com_GetPaperSize
	#	_IAcadPlotConfiguration__com_GetPlotDeviceNames
	#	_IAcadPlotConfiguration__com_GetPlotStyleTableNames
	#	_IAcadPlotConfiguration__com_GetWindowToPlot
	#	_IAcadPlotConfiguration__com_RefreshPlotDeviceInfo
	#	_IAcadPlotConfiguration__com_SetCustomScale
	#	_IAcadPlotConfiguration__com_SetWindowToPlot
	#	_IAcadPlotConfiguration__com__get_CanonicalMediaName
	#	_IAcadPlotConfiguration__com__get_CenterPlot
	#	_IAcadPlotConfiguration__com__get_ConfigName
	#	_IAcadPlotConfiguration__com__get_ModelType
	#	_IAcadPlotConfiguration__com__get_Name
	#	_IAcadPlotConfiguration__com__get_PaperUnits
	#	_IAcadPlotConfiguration__com__get_PlotHidden
	#	_IAcadPlotConfiguration__com__get_PlotOrigin
	#	_IAcadPlotConfiguration__com__get_PlotRotation
	#	_IAcadPlotConfiguration__com__get_PlotType
	#	_IAcadPlotConfiguration__com__get_PlotViewportBorders
	#	_IAcadPlotConfiguration__com__get_PlotViewportsFirst
	#	_IAcadPlotConfiguration__com__get_PlotWithLineweights
	#	_IAcadPlotConfiguration__com__get_PlotWithPlotStyles
	#	_IAcadPlotConfiguration__com__get_ScaleLineweights
	#	_IAcadPlotConfiguration__com__get_ShowPlotStyles
	#	_IAcadPlotConfiguration__com__get_StandardScale
	#	_IAcadPlotConfiguration__com__get_StyleSheet
	#	_IAcadPlotConfiguration__com__get_UseStandardScale
	#	_IAcadPlotConfiguration__com__get_ViewToPlot
	#	_IAcadPlotConfiguration__com__set_CanonicalMediaName
	#	_IAcadPlotConfiguration__com__set_CenterPlot
	#	_IAcadPlotConfiguration__com__set_ConfigName
	#	_IAcadPlotConfiguration__com__set_Name
	#	_IAcadPlotConfiguration__com__set_PaperUnits
	#	_IAcadPlotConfiguration__com__set_PlotHidden
	#	_IAcadPlotConfiguration__com__set_PlotOrigin
	#	_IAcadPlotConfiguration__com__set_PlotRotation
	#	_IAcadPlotConfiguration__com__set_PlotType
	#	_IAcadPlotConfiguration__com__set_PlotViewportBorders
	#	_IAcadPlotConfiguration__com__set_PlotViewportsFirst
	#	_IAcadPlotConfiguration__com__set_PlotWithLineweights
	#	_IAcadPlotConfiguration__com__set_PlotWithPlotStyles
	#	_IAcadPlotConfiguration__com__set_ScaleLineweights
	#	_IAcadPlotConfiguration__com__set_ShowPlotStyles
	#	_IAcadPlotConfiguration__com__set_StandardScale
	#	_IAcadPlotConfiguration__com__set_StyleSheet
	#	_IAcadPlotConfiguration__com__set_UseStandardScale
	#	_IAcadPlotConfiguration__com__set_ViewToPlot
	# Methods
	def copyfrom(self, pPlotConfig: AcadPlotConfiguration):
		"Copies the settings from the given plotconfiguration"
		# TODO: Check arguments
		# ['in'] pPlotConfig:AcadPlotConfiguration
		# VBA: object.CopyFrom pPlotConfig
		self.com_parent.CopyFrom(pPlotConfig)

	def getcanonicalmedianames(self) -> tagVARIANT:
		"Gets all available canonical media names for the specified plot device."
		# TODO: Check arguments
		# ['out', 'retval'] pNames:tagVARIANT
		# VBA: pNames = object.GetCanonicalMediaNames ()
		return self.com_parent.GetCanonicalMediaNames()

	def getcustomscale(self):
		"Gets the custom scale for a layout or plot configuration"
		# TODO: Check arguments
		# ['out'] Numerator:float
		# ['out'] Denominator:float
		# VBA: object.GetCustomScale Numerator, Denominator
		return self.com_parent.GetCustomScale()

	def getlocalemedianame(self, Name: str) -> str:
		"Gets the localized version of the canonical media name."
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pLocalName:str
		# VBA: pLocalName = object.GetLocaleMediaName (Name)
		return self.com_parent.GetLocaleMediaName(Name)

	def getpapermargins(self):
		"Gets the margins for the layout or plot configuration"
		# TODO: Check arguments
		# ['out'] LowerLeft:tagVARIANT
		# ['out'] UpperRight:tagVARIANT
		# VBA: object.GetPaperMargins LowerLeft, UpperRight
		return self.com_parent.GetPaperMargins()

	def getpapersize(self):
		"Gets the width and height of the configured paper"
		# TODO: Check arguments
		# ['out'] Width:float
		# ['out'] Height:float
		# VBA: object.GetPaperSize Width, Height
		return self.com_parent.GetPaperSize()

	def getplotdevicenames(self) -> tagVARIANT:
		"Gets all available plot device names."
		# TODO: Check arguments
		# ['out', 'retval'] pNames:tagVARIANT
		# VBA: pNames = object.GetPlotDeviceNames ()
		return self.com_parent.GetPlotDeviceNames()

	def getplotstyletablenames(self) -> tagVARIANT:
		"Gets all available plot style table names."
		# TODO: Check arguments
		# ['out', 'retval'] pNames:tagVARIANT
		# VBA: pNames = object.GetPlotStyleTableNames ()
		return self.com_parent.GetPlotStyleTableNames()

	def getwindowtoplot(self):
		"Gets the coordinates that define the portion of the layout to plot"
		# TODO: Check arguments
		# ['out'] LowerLeft:tagVARIANT
		# ['out'] UpperRight:tagVARIANT
		# VBA: object.GetWindowToPlot LowerLeft, UpperRight
		return self.com_parent.GetWindowToPlot()

	def refreshplotdeviceinfo(self):
		"Updates the plot, canonical media, and plot style table information to reflect the current system state."
		# VBA: object.RefreshPlotDeviceInfo 
		self.com_parent.RefreshPlotDeviceInfo()

	def setcustomscale(self, Numerator: float, Denominator: float):
		"Sets the custom scale for a layout or plot configuration"
		# ['in'] Numerator:float
		# ['in'] Denominator:float
		# VBA: object.SetCustomScale Numerator, Denominator
		self.com_parent.SetCustomScale(Numerator, Denominator)

	def setwindowtoplot(self, LowerLeft: tagVARIANT, UpperRight: tagVARIANT):
		"Sets the coordinates that define the portion of the layout to plot"
		# TODO: Check arguments
		# ['in'] LowerLeft:tagVARIANT
		# ['in'] UpperRight:tagVARIANT
		# VBA: object.SetWindowToPlot LowerLeft, UpperRight
		self.com_parent.SetWindowToPlot(LowerLeft, UpperRight)

	# Properties
	@indexedproperty
	def canonicalmedianame(self) -> str:
		"Specifies the paper size by name"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.CanonicalMediaName
	@canonicalmedianame.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.CanonicalMediaName = pName

	@indexedproperty
	def centerplot(self) -> bool:
		"Specifies the centering of the plot on the media"
		# TODO: Check arguments
		# ['out', 'retval'] pCentered:bool
		return self.com_parent.CenterPlot
	@centerplot.setter
	def _(self, pCentered:bool):
		# ['in'] pCentered:bool
		self.com_parent.CenterPlot = pCentered

	@indexedproperty
	def configname(self) -> str:
		"Specifies the plotter configuration name"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.ConfigName
	@configname.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.ConfigName = pName

	@indexedproperty
	def modeltype(self) -> bool:
		"Specifies if the plot configuration applies only to model space or to all layouts"
		# TODO: Check arguments
		# ['out', 'retval'] pType:bool
		return self.com_parent.ModelType

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.Name
	@name.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.Name = pName

	@indexedproperty
	def paperunits(self) -> int:
		"Specifies the units for the display of layout or plot configuration properties"
		# TODO: Check arguments
		# ['out', 'retval'] pPaperUnits:int
		return self.com_parent.PaperUnits
	@paperunits.setter
	def _(self, pPaperUnits:int):
		# ['in'] pPaperUnits:int
		self.com_parent.PaperUnits = pPaperUnits

	@indexedproperty
	def plothidden(self) -> bool:
		"Specifies if objects are to be hidden during a plot"
		# TODO: Check arguments
		# ['out', 'retval'] pHidden:bool
		return self.com_parent.PlotHidden
	@plothidden.setter
	def _(self, pHidden:bool):
		# ['in'] pHidden:bool
		self.com_parent.PlotHidden = pHidden

	@indexedproperty
	def plotorigin(self) -> tagVARIANT:
		"Specifies the origin of the UCS, block, layout, or raster image in WCS coordinates"
		# TODO: Check arguments
		# ['out', 'retval'] pOrigin:tagVARIANT
		return self.com_parent.PlotOrigin
	@plotorigin.setter
	def _(self, pOrigin:tagVARIANT):
		# TODO: Check arguments
		# ['in'] pOrigin:tagVARIANT
		self.com_parent.PlotOrigin = pOrigin

	@indexedproperty
	def plotrotation(self) -> int:
		"Specifies the rotation angle for the layout or plot configuration"
		# TODO: Check arguments
		# ['out', 'retval'] pRotation:int
		return self.com_parent.PlotRotation
	@plotrotation.setter
	def _(self, pRotation:int):
		# ['in'] pRotation:int
		self.com_parent.PlotRotation = pRotation

	@indexedproperty
	def plottype(self) -> int:
		"Specifies the type of layout or plot configuration"
		# TODO: Check arguments
		# ['out', 'retval'] pType:int
		return self.com_parent.PlotType
	@plottype.setter
	def _(self, pType:int):
		# ['in'] pType:int
		self.com_parent.PlotType = pType

	@indexedproperty
	def plotviewportborders(self) -> bool:
		"Specifies if the viewport borders are to be plotted"
		# TODO: Check arguments
		# ['out', 'retval'] pViewportBorders:bool
		return self.com_parent.PlotViewportBorders
	@plotviewportborders.setter
	def _(self, pViewportBorders:bool):
		# ['in'] pViewportBorders:bool
		self.com_parent.PlotViewportBorders = pViewportBorders

	@indexedproperty
	def plotviewportsfirst(self) -> bool:
		"Specifies if all geometry in paper space viewports is plotted first"
		# TODO: Check arguments
		# ['out', 'retval'] pViewportsFirst:bool
		return self.com_parent.PlotViewportsFirst
	@plotviewportsfirst.setter
	def _(self, pViewportsFirst:bool):
		# ['in'] pViewportsFirst:bool
		self.com_parent.PlotViewportsFirst = pViewportsFirst

	@indexedproperty
	def plotwithlineweights(self) -> bool:
		"Specifies if objects plot with the lineweights they're assigned in the plot file, or with the lineweights in the drawing file"
		# TODO: Check arguments
		# ['out', 'retval'] pPlot:bool
		return self.com_parent.PlotWithLineweights
	@plotwithlineweights.setter
	def _(self, pPlot:bool):
		# ['in'] pPlot:bool
		self.com_parent.PlotWithLineweights = pPlot

	@indexedproperty
	def plotwithplotstyles(self) -> bool:
		"Specifies if objects plot with the configuration they're assigned in the plot file, or with the configuration in the drawing file"
		# TODO: Check arguments
		# ['out', 'retval'] pStyles:bool
		return self.com_parent.PlotWithPlotStyles
	@plotwithplotstyles.setter
	def _(self, pStyles:bool):
		# ['in'] pStyles:bool
		self.com_parent.PlotWithPlotStyles = pStyles

	@indexedproperty
	def scalelineweights(self) -> bool:
		"Specifies if the lineweight is scaled with the rest of the geometry when a layout is printed"
		# TODO: Check arguments
		# ['out', 'retval'] pScale:bool
		return self.com_parent.ScaleLineweights
	@scalelineweights.setter
	def _(self, pScale:bool):
		# ['in'] pScale:bool
		self.com_parent.ScaleLineweights = pScale

	@indexedproperty
	def showplotstyles(self) -> bool:
		"Specifies if plot styles are to be used in the plot"
		# TODO: Check arguments
		# ['out', 'retval'] pStyles:bool
		return self.com_parent.ShowPlotStyles
	@showplotstyles.setter
	def _(self, pStyles:bool):
		# ['in'] pStyles:bool
		self.com_parent.ShowPlotStyles = pStyles

	@indexedproperty
	def standardscale(self) -> int:
		"Specifies the standard scale for the layout, viewport, or plot configuration"
		# TODO: Check arguments
		# ['out', 'retval'] pStdScale:int
		return self.com_parent.StandardScale
	@standardscale.setter
	def _(self, pStdScale:int):
		# ['in'] pStdScale:int
		self.com_parent.StandardScale = pStdScale

	@indexedproperty
	def stylesheet(self) -> str:
		"Specifies the style sheet for the layout or plot configuration"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.StyleSheet
	@stylesheet.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.StyleSheet = pName

	@indexedproperty
	def usestandardscale(self) -> bool:
		"Specifies if the plot is to use a standard or custom scale"
		# TODO: Check arguments
		# ['out', 'retval'] pUseStdScale:bool
		return self.com_parent.UseStandardScale
	@usestandardscale.setter
	def _(self, pUseStdScale:bool):
		# ['in'] pUseStdScale:bool
		self.com_parent.UseStandardScale = pUseStdScale

	@indexedproperty
	def viewtoplot(self) -> str:
		"Specifies the name of the view to plot"
		# TODO: Check arguments
		# ['out', 'retval'] pName:str
		return self.com_parent.ViewToPlot
	@viewtoplot.setter
	def _(self, pName:str):
		# ['in'] pName:str
		self.com_parent.ViewToPlot = pName


class AcadPlotConfigurations(POINTER(_dll.IAcadPlotConfigurations), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPlotConfigurations
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadPlotConfigurations VBA-class wrapped as AcadPlotConfigurations python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadPlotConfigurations__com_Add
	#	_IAcadPlotConfigurations__com_Item
	#	_IAcadPlotConfigurations__com__get_Count
	#	_IAcadPlotConfigurations__com__get__NewEnum
	# Methods
	def add(self, Name: str, ModelType: tagVARIANT) -> AcadPlotConfiguration:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['in', '16'] ModelType:tagVARIANT
		# ['out', 'retval'] pPlotConfig:AcadPlotConfiguration
		# VBA: pPlotConfig = object.Add (Name, ModelType)
		return self.com_parent.Add(Name, ModelType)

	def item(self, Index: tagVARIANT) -> AcadPlotConfiguration:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadPlotConfiguration
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadPopupMenu(POINTER(_dll.IAcadPopupMenu), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPopupMenu
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPopupMenu VBA-class wrapped as AcadPopupMenu python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPopupMenu__com_AddMenuItem
	#	_IAcadPopupMenu__com_AddSeparator
	#	_IAcadPopupMenu__com_AddSubMenu
	#	_IAcadPopupMenu__com_InsertInMenuBar
	#	_IAcadPopupMenu__com_Item
	#	_IAcadPopupMenu__com_RemoveFromMenuBar
	#	_IAcadPopupMenu__com__get_Application
	#	_IAcadPopupMenu__com__get_Count
	#	_IAcadPopupMenu__com__get_Name
	#	_IAcadPopupMenu__com__get_NameNoMnemonic
	#	_IAcadPopupMenu__com__get_OnMenuBar
	#	_IAcadPopupMenu__com__get_Parent
	#	_IAcadPopupMenu__com__get_ShortcutMenu
	#	_IAcadPopupMenu__com__get_TagString
	#	_IAcadPopupMenu__com__get__NewEnum
	#	_IAcadPopupMenu__com__set_Name
	# Methods
	def addmenuitem(self, Index: tagVARIANT, Label: str, Macro: str) -> AcadPopupMenuItem:
		"Adds a popup menu item to a popup menu"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['in'] Label:str
		# ['in'] Macro:str
		# ['out', 'retval'] pItem:AcadPopupMenuItem
		# VBA: pItem = object.AddMenuItem (Index, Label, Macro)
		return self.com_parent.AddMenuItem(Index, Label, Macro)

	def addseparator(self, Index: tagVARIANT) -> AcadPopupMenuItem:
		"Adds a separator to an existing menu or toolbar"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadPopupMenuItem
		# VBA: pItem = object.AddSeparator (Index)
		return self.com_parent.AddSeparator(Index)

	def addsubmenu(self, Index: tagVARIANT, Label: str) -> AcadPopupMenu:
		"Adds a submenu to an existing menu"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['in'] Label:str
		# ['out', 'retval'] pMenu:AcadPopupMenu
		# VBA: pMenu = object.AddSubMenu (Index, Label)
		return self.com_parent.AddSubMenu(Index, Label)

	def insertinmenubar(self, Index: tagVARIANT):
		"Inserts the popup menu into the AutoCAD menu bar at a specified location"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# VBA: object.InsertInMenuBar Index
		self.com_parent.InsertInMenuBar(Index)

	def item(self, Index: tagVARIANT) -> AcadPopupMenuItem:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadPopupMenuItem
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def removefrommenubar(self):
		"Removes the popup menu from the AutoCAD menu bar"
		# VBA: object.RemoveFromMenuBar 
		self.com_parent.RemoveFromMenuBar()

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def namenomnemonic(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.NameNoMnemonic

	@indexedproperty
	def onmenubar(self) -> bool:
		"Determines if the specified popup menu is on the menu bar"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.OnMenuBar

	@indexedproperty
	def parent(self) -> POINTER(IDispatch):
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:POINTER(IDispatch)
		return self.com_parent.Parent

	@indexedproperty
	def shortcutmenu(self) -> bool:
		"Determines if the specified popup menu is the shortcut menu"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.ShortcutMenu

	@indexedproperty
	def tagstring(self) -> str:
		"Specifies the tag string of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrTag:str
		return self.com_parent.TagString


class AcadPopupMenuItem(POINTER(_dll.IAcadPopupMenuItem), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPopupMenuItem
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPopupMenuItem VBA-class wrapped as AcadPopupMenuItem python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPopupMenuItem__com_Delete
	#	_IAcadPopupMenuItem__com__get_Application
	#	_IAcadPopupMenuItem__com__get_Caption
	#	_IAcadPopupMenuItem__com__get_Check
	#	_IAcadPopupMenuItem__com__get_Enable
	#	_IAcadPopupMenuItem__com__get_EndSubMenuLevel
	#	_IAcadPopupMenuItem__com__get_HelpString
	#	_IAcadPopupMenuItem__com__get_Index
	#	_IAcadPopupMenuItem__com__get_Label
	#	_IAcadPopupMenuItem__com__get_Macro
	#	_IAcadPopupMenuItem__com__get_Parent
	#	_IAcadPopupMenuItem__com__get_SubMenu
	#	_IAcadPopupMenuItem__com__get_TagString
	#	_IAcadPopupMenuItem__com__get_Type
	#	_IAcadPopupMenuItem__com__set_Check
	#	_IAcadPopupMenuItem__com__set_Enable
	#	_IAcadPopupMenuItem__com__set_EndSubMenuLevel
	#	_IAcadPopupMenuItem__com__set_HelpString
	#	_IAcadPopupMenuItem__com__set_Label
	#	_IAcadPopupMenuItem__com__set_Macro
	#	_IAcadPopupMenuItem__com__set_TagString
	# Methods
	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def caption(self) -> str:
		"Gets the text that the user sees displayed for the application or a menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrCaption:str
		return self.com_parent.Caption

	@indexedproperty
	def check(self) -> bool:
		"Specifies the check status for the popup menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.Check
	@check.setter
	def _(self, bFlag:bool):
		# ['in'] bFlag:bool
		self.com_parent.Check = bFlag

	@indexedproperty
	def enable(self) -> bool:
		"Enables the popup menu or toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.Enable
	@enable.setter
	def _(self, bFlag:bool):
		# ['in'] bFlag:bool
		self.com_parent.Enable = bFlag

	@indexedproperty
	def endsubmenulevel(self) -> int:
		"Specifies the submenu level for the menu item"
		# TODO: Check arguments
		# ['out', 'retval'] level:int
		return self.com_parent.EndSubMenuLevel
	@endsubmenulevel.setter
	def _(self, level:int):
		# ['in'] level:int
		self.com_parent.EndSubMenuLevel = level

	@indexedproperty
	def helpstring(self) -> str:
		"Specifies the help string for the toolbar, toolbar item, or menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrHelp:str
		return self.com_parent.HelpString
	@helpstring.setter
	def _(self, bstrHelp:str):
		# ['in'] bstrHelp:str
		self.com_parent.HelpString = bstrHelp

	@indexedproperty
	def index(self) -> int:
		"Specifies the index of the menu or toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] nIndex:int
		return self.com_parent.Index

	@indexedproperty
	def label(self) -> str:
		"Specifies the content and formatting of menu items as they appear to the user"
		# TODO: Check arguments
		# ['out', 'retval'] bstrLabel:str
		return self.com_parent.Label
	@label.setter
	def _(self, bstrLabel:str):
		# ['in'] bstrLabel:str
		self.com_parent.Label = bstrLabel

	@indexedproperty
	def macro(self) -> str:
		"Specifies the macro for the menu or toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrMacro:str
		return self.com_parent.Macro
	@macro.setter
	def _(self, bstrMacro:str):
		# ['in'] bstrMacro:str
		self.com_parent.Macro = bstrMacro

	@indexedproperty
	def parent(self) -> AcadPopupMenu:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadPopupMenu
		return self.com_parent.Parent

	@indexedproperty
	def submenu(self) -> AcadPopupMenu:
		"Gets the popup menu associated with a sub menu"
		# TODO: Check arguments
		# ['out', 'retval'] pMenu:AcadPopupMenu
		return self.com_parent.SubMenu

	@indexedproperty
	def tagstring(self) -> str:
		"Specifies the tag string of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrTag:str
		return self.com_parent.TagString
	@tagstring.setter
	def _(self, bstrTag:str):
		# ['in'] bstrTag:str
		self.com_parent.TagString = bstrTag

	@indexedproperty
	def type(self) -> int:
		"Specifies type of a Leader, MenuGroup, PopupMenuItem, ToolbarItem, Polyline, or PolygonMesh object"
		# TODO: Check arguments
		# ['out', 'retval'] itemType:int
		return self.com_parent.Type


class AcadPopupMenus(POINTER(_dll.IAcadPopupMenus), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPopupMenus
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPopupMenus VBA-class wrapped as AcadPopupMenus python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPopupMenus__com_Add
	#	_IAcadPopupMenus__com_InsertMenuInMenuBar
	#	_IAcadPopupMenus__com_Item
	#	_IAcadPopupMenus__com_RemoveMenuFromMenuBar
	#	_IAcadPopupMenus__com__get_Application
	#	_IAcadPopupMenus__com__get_Count
	#	_IAcadPopupMenus__com__get_Parent
	#	_IAcadPopupMenus__com__get__NewEnum
	# Methods
	def add(self, MenuName: str) -> AcadPopupMenu:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] MenuName:str
		# ['out', 'retval'] pMenu:AcadPopupMenu
		# VBA: pMenu = object.Add (MenuName)
		return self.com_parent.Add(MenuName)

	def insertmenuinmenubar(self, MenuName: str, Index: tagVARIANT):
		"Inserts a menu into the AutoCAD menu bar"
		# TODO: Check arguments
		# ['in'] MenuName:str
		# ['in'] Index:tagVARIANT
		# VBA: object.InsertMenuInMenuBar MenuName, Index
		self.com_parent.InsertMenuInMenuBar(MenuName, Index)

	def item(self, Index: tagVARIANT) -> AcadPopupMenu:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadPopupMenu
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	def removemenufrommenubar(self, Index: tagVARIANT):
		"Removes the popup menu, as specified from the collection, from the AutoCAD menu bar"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# VBA: object.RemoveMenuFromMenuBar Index
		self.com_parent.RemoveMenuFromMenuBar(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def parent(self) -> AcadMenuGroup:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadMenuGroup
		return self.com_parent.Parent


class AcadPreferences(POINTER(_dll.IAcadPreferences), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferences
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferences VBA-class wrapped as AcadPreferences python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferences__com__get_Application
	#	_IAcadPreferences__com__get_Display
	#	_IAcadPreferences__com__get_Drafting
	#	_IAcadPreferences__com__get_Files
	#	_IAcadPreferences__com__get_OpenSave
	#	_IAcadPreferences__com__get_Output
	#	_IAcadPreferences__com__get_Profiles
	#	_IAcadPreferences__com__get_Selection
	#	_IAcadPreferences__com__get_System
	#	_IAcadPreferences__com__get_User
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def display(self) -> AcadPreferencesDisplay:
		"Gets the PreferencesDisplay object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesDisplay
		return self.com_parent.Display

	@indexedproperty
	def drafting(self) -> AcadPreferencesDrafting:
		"Gets the PreferencesDrafting object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesDrafting
		return self.com_parent.Drafting

	@indexedproperty
	def files(self) -> AcadPreferencesFiles:
		"Gets the PreferencesFiles object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesFiles
		return self.com_parent.Files

	@indexedproperty
	def opensave(self) -> AcadPreferencesOpenSave:
		"Gets the PreferencesOpenSave object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesOpenSave
		return self.com_parent.OpenSave

	@indexedproperty
	def output(self) -> AcadPreferencesOutput:
		"Gets the PreferencesOutput object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesOutput
		return self.com_parent.Output

	@indexedproperty
	def profiles(self) -> AcadPreferencesProfiles:
		"Gets the PreferencesProfiles object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesProfiles
		return self.com_parent.Profiles

	@indexedproperty
	def selection(self) -> AcadPreferencesSelection:
		"Gets the PreferencesSelection object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesSelection
		return self.com_parent.Selection

	@indexedproperty
	def system(self) -> AcadPreferencesSystem:
		"Gets the PreferencesSystem object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesSystem
		return self.com_parent.System

	@indexedproperty
	def user(self) -> AcadPreferencesUser:
		"Gets the PreferencesUser object"
		# TODO: Check arguments
		# ['out', 'retval'] pObj:AcadPreferencesUser
		return self.com_parent.User


class AcadPreferencesDisplay(POINTER(_dll.IAcadPreferencesDisplay), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesDisplay
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesDisplay VBA-class wrapped as AcadPreferencesDisplay python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesDisplay__com__get_Application
	#	_IAcadPreferencesDisplay__com__get_AutoTrackingVecColor
	#	_IAcadPreferencesDisplay__com__get_CursorSize
	#	_IAcadPreferencesDisplay__com__get_DisplayLayoutTabs
	#	_IAcadPreferencesDisplay__com__get_DisplayScreenMenu
	#	_IAcadPreferencesDisplay__com__get_DisplayScrollBars
	#	_IAcadPreferencesDisplay__com__get_DockedVisibleLines
	#	_IAcadPreferencesDisplay__com__get_GraphicsWinLayoutBackgrndColor
	#	_IAcadPreferencesDisplay__com__get_GraphicsWinModelBackgrndColor
	#	_IAcadPreferencesDisplay__com__get_HistoryLines
	#	_IAcadPreferencesDisplay__com__get_ImageFrameHighlight
	#	_IAcadPreferencesDisplay__com__get_LayoutCreateViewport
	#	_IAcadPreferencesDisplay__com__get_LayoutCrosshairColor
	#	_IAcadPreferencesDisplay__com__get_LayoutDisplayMargins
	#	_IAcadPreferencesDisplay__com__get_LayoutDisplayPaper
	#	_IAcadPreferencesDisplay__com__get_LayoutDisplayPaperShadow
	#	_IAcadPreferencesDisplay__com__get_LayoutShowPlotSetup
	#	_IAcadPreferencesDisplay__com__get_MaxAutoCADWindow
	#	_IAcadPreferencesDisplay__com__get_ModelCrosshairColor
	#	_IAcadPreferencesDisplay__com__get_ShowRasterImage
	#	_IAcadPreferencesDisplay__com__get_TextFont
	#	_IAcadPreferencesDisplay__com__get_TextFontSize
	#	_IAcadPreferencesDisplay__com__get_TextFontStyle
	#	_IAcadPreferencesDisplay__com__get_TextWinBackgrndColor
	#	_IAcadPreferencesDisplay__com__get_TextWinTextColor
	#	_IAcadPreferencesDisplay__com__get_TrueColorImages
	#	_IAcadPreferencesDisplay__com__get_XRefFadeIntensity
	#	_IAcadPreferencesDisplay__com__set_AutoTrackingVecColor
	#	_IAcadPreferencesDisplay__com__set_CursorSize
	#	_IAcadPreferencesDisplay__com__set_DisplayLayoutTabs
	#	_IAcadPreferencesDisplay__com__set_DisplayScreenMenu
	#	_IAcadPreferencesDisplay__com__set_DisplayScrollBars
	#	_IAcadPreferencesDisplay__com__set_DockedVisibleLines
	#	_IAcadPreferencesDisplay__com__set_GraphicsWinLayoutBackgrndColor
	#	_IAcadPreferencesDisplay__com__set_GraphicsWinModelBackgrndColor
	#	_IAcadPreferencesDisplay__com__set_HistoryLines
	#	_IAcadPreferencesDisplay__com__set_ImageFrameHighlight
	#	_IAcadPreferencesDisplay__com__set_LayoutCreateViewport
	#	_IAcadPreferencesDisplay__com__set_LayoutCrosshairColor
	#	_IAcadPreferencesDisplay__com__set_LayoutDisplayMargins
	#	_IAcadPreferencesDisplay__com__set_LayoutDisplayPaper
	#	_IAcadPreferencesDisplay__com__set_LayoutDisplayPaperShadow
	#	_IAcadPreferencesDisplay__com__set_LayoutShowPlotSetup
	#	_IAcadPreferencesDisplay__com__set_MaxAutoCADWindow
	#	_IAcadPreferencesDisplay__com__set_ModelCrosshairColor
	#	_IAcadPreferencesDisplay__com__set_ShowRasterImage
	#	_IAcadPreferencesDisplay__com__set_TextFont
	#	_IAcadPreferencesDisplay__com__set_TextFontSize
	#	_IAcadPreferencesDisplay__com__set_TextFontStyle
	#	_IAcadPreferencesDisplay__com__set_TextWinBackgrndColor
	#	_IAcadPreferencesDisplay__com__set_TextWinTextColor
	#	_IAcadPreferencesDisplay__com__set_TrueColorImages
	#	_IAcadPreferencesDisplay__com__set_XRefFadeIntensity
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def autotrackingveccolor(self) -> int:
		"Specifies the color of the auto tracking vector"
		# TODO: Check arguments
		# ['out', 'retval'] AutoTrackingVecColor:int
		return self.com_parent.AutoTrackingVecColor
	@autotrackingveccolor.setter
	def _(self, AutoTrackingVecColor:int):
		# ['in'] AutoTrackingVecColor:int
		self.com_parent.AutoTrackingVecColor = AutoTrackingVecColor

	@indexedproperty
	def cursorsize(self) -> int:
		"Specifies the crosshairs size as a percentage of the screen size"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.CursorSize
	@cursorsize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.CursorSize = Path

	@indexedproperty
	def displaylayouttabs(self) -> bool:
		"Specifies whether to display the Model and Layout tabs in the drawing editor"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayLayoutTabs
	@displaylayouttabs.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayLayoutTabs = Path

	@indexedproperty
	def displayscreenmenu(self) -> bool:
		"Specifies whether to display the screen menu on the right side of the drawing window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayScreenMenu
	@displayscreenmenu.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayScreenMenu = Path

	@indexedproperty
	def displayscrollbars(self) -> bool:
		"Specifies whether to display scroll bars at the bottom and right sides of the drawing window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayScrollBars
	@displayscrollbars.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayScrollBars = Path

	@indexedproperty
	def dockedvisiblelines(self) -> int:
		"Specifies the number of lines of text to display in the command window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.DockedVisibleLines
	@dockedvisiblelines.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.DockedVisibleLines = Path

	@indexedproperty
	def graphicswinlayoutbackgrndcolor(self) -> int:
		"Specifies the background color for the paper space layouts"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.GraphicsWinLayoutBackgrndColor
	@graphicswinlayoutbackgrndcolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.GraphicsWinLayoutBackgrndColor = color

	@indexedproperty
	def graphicswinmodelbackgrndcolor(self) -> int:
		"Specifies the background color for the model space window"
		# TODO: Check arguments
		# ['out', 'retval'] color:int
		return self.com_parent.GraphicsWinModelBackgrndColor
	@graphicswinmodelbackgrndcolor.setter
	def _(self, color:int):
		# ['in'] color:int
		self.com_parent.GraphicsWinModelBackgrndColor = color

	@indexedproperty
	def historylines(self) -> int:
		"Specifies the number of lines of text in the text window to keep in memory"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.HistoryLines
	@historylines.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.HistoryLines = Path

	@indexedproperty
	def imageframehighlight(self) -> bool:
		"Controls the display of raster images during selection"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.ImageFrameHighlight
	@imageframehighlight.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.ImageFrameHighlight = Path

	@indexedproperty
	def layoutcreateviewport(self) -> bool:
		"Toggles the automatic creation of a viewport for new layouts"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LayoutCreateViewport
	@layoutcreateviewport.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LayoutCreateViewport = Path

	@indexedproperty
	def layoutcrosshaircolor(self) -> int:
		"Specifies the color of the crosshairs and text for paper space layouts"
		# TODO: Check arguments
		# ['out', 'retval'] crossHairColor:int
		return self.com_parent.LayoutCrosshairColor
	@layoutcrosshaircolor.setter
	def _(self, crossHairColor:int):
		# ['in'] crossHairColor:int
		self.com_parent.LayoutCrosshairColor = crossHairColor

	@indexedproperty
	def layoutdisplaymargins(self) -> bool:
		"Toggles the display of margins in layouts"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LayoutDisplayMargins
	@layoutdisplaymargins.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LayoutDisplayMargins = Path

	@indexedproperty
	def layoutdisplaypaper(self) -> bool:
		"Toggles the display of the paper background in layouts"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LayoutDisplayPaper
	@layoutdisplaypaper.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LayoutDisplayPaper = Path

	@indexedproperty
	def layoutdisplaypapershadow(self) -> bool:
		"Toggles the display of the paper background shadow in layouts"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LayoutDisplayPaperShadow
	@layoutdisplaypapershadow.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LayoutDisplayPaperShadow = Path

	@indexedproperty
	def layoutshowplotsetup(self) -> bool:
		"Toggles the display of the Plot Setup dialog when a new layout is created"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LayoutShowPlotSetup
	@layoutshowplotsetup.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LayoutShowPlotSetup = Path

	@indexedproperty
	def maxautocadwindow(self) -> bool:
		"Specifies if AutoCAD should fill the entire screen area when you start"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.MaxAutoCADWindow
	@maxautocadwindow.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.MaxAutoCADWindow = Path

	@indexedproperty
	def modelcrosshaircolor(self) -> int:
		"Specifies the color of the crosshairs and text for model space"
		# TODO: Check arguments
		# ['out', 'retval'] crossHairColor:int
		return self.com_parent.ModelCrosshairColor
	@modelcrosshaircolor.setter
	def _(self, crossHairColor:int):
		# ['in'] crossHairColor:int
		self.com_parent.ModelCrosshairColor = crossHairColor

	@indexedproperty
	def showrasterimage(self) -> bool:
		"Controls the display of raster images during real time pan and zooms"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.ShowRasterImage
	@showrasterimage.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.ShowRasterImage = Path

	@indexedproperty
	def textfont(self) -> str:
		"Specifies the font for new text"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TextFont
	@textfont.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TextFont = Path

	@indexedproperty
	def textfontsize(self) -> int:
		"Specifies the font size for new text"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.TextFontSize
	@textfontsize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.TextFontSize = Path

	@indexedproperty
	def textfontstyle(self) -> int:
		"Specifies the font style for new text"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.TextFontStyle
	@textfontstyle.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.TextFontStyle = Path

	@indexedproperty
	def textwinbackgrndcolor(self) -> int:
		"Specifies the background color for the text window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.TextWinBackgrndColor
	@textwinbackgrndcolor.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.TextWinBackgrndColor = Path

	@indexedproperty
	def textwintextcolor(self) -> int:
		"Specifies the text color for the text window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.TextWinTextColor
	@textwintextcolor.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.TextWinTextColor = Path

	@indexedproperty
	def truecolorimages(self) -> bool:
		"Determines if raster and render images are displayed at true color or palletized color"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.TrueColorImages
	@truecolorimages.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.TrueColorImages = Path

	@indexedproperty
	def xreffadeintensity(self) -> int:
		"Controls the dimming intensity for XRefs"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.XRefFadeIntensity
	@xreffadeintensity.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.XRefFadeIntensity = Path


class AcadPreferencesDrafting(POINTER(_dll.IAcadPreferencesDrafting), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesDrafting
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesDrafting VBA-class wrapped as AcadPreferencesDrafting python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesDrafting__com__get_AlignmentPointAcquisition
	#	_IAcadPreferencesDrafting__com__get_Application
	#	_IAcadPreferencesDrafting__com__get_AutoSnapAperture
	#	_IAcadPreferencesDrafting__com__get_AutoSnapApertureSize
	#	_IAcadPreferencesDrafting__com__get_AutoSnapMagnet
	#	_IAcadPreferencesDrafting__com__get_AutoSnapMarker
	#	_IAcadPreferencesDrafting__com__get_AutoSnapMarkerColor
	#	_IAcadPreferencesDrafting__com__get_AutoSnapMarkerSize
	#	_IAcadPreferencesDrafting__com__get_AutoSnapTooltip
	#	_IAcadPreferencesDrafting__com__get_AutoTrackTooltip
	#	_IAcadPreferencesDrafting__com__get_FullScreenTrackingVector
	#	_IAcadPreferencesDrafting__com__get_PolarTrackingVector
	#	_IAcadPreferencesDrafting__com__set_AlignmentPointAcquisition
	#	_IAcadPreferencesDrafting__com__set_AutoSnapAperture
	#	_IAcadPreferencesDrafting__com__set_AutoSnapApertureSize
	#	_IAcadPreferencesDrafting__com__set_AutoSnapMagnet
	#	_IAcadPreferencesDrafting__com__set_AutoSnapMarker
	#	_IAcadPreferencesDrafting__com__set_AutoSnapMarkerColor
	#	_IAcadPreferencesDrafting__com__set_AutoSnapMarkerSize
	#	_IAcadPreferencesDrafting__com__set_AutoSnapTooltip
	#	_IAcadPreferencesDrafting__com__set_AutoTrackTooltip
	#	_IAcadPreferencesDrafting__com__set_FullScreenTrackingVector
	#	_IAcadPreferencesDrafting__com__set_PolarTrackingVector
	# Properties
	@indexedproperty
	def alignmentpointacquisition(self) -> int:
		"Specifies how AutoAlignment points are acquired"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.AlignmentPointAcquisition
	@alignmentpointacquisition.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.AlignmentPointAcquisition = Path

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def autosnapaperture(self) -> bool:
		"Toggles the display of the AutoSnap aperture"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutoSnapAperture
	@autosnapaperture.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutoSnapAperture = Path

	@indexedproperty
	def autosnapaperturesize(self) -> int:
		"Specifies the size of the AutoSnap aperture"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.AutoSnapApertureSize
	@autosnapaperturesize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.AutoSnapApertureSize = Path

	@indexedproperty
	def autosnapmagnet(self) -> bool:
		"Toggles the AutoSnap magnet"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutoSnapMagnet
	@autosnapmagnet.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutoSnapMagnet = Path

	@indexedproperty
	def autosnapmarker(self) -> bool:
		"Toggles the AutoSnap marker"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutoSnapMarker
	@autosnapmarker.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutoSnapMarker = Path

	@indexedproperty
	def autosnapmarkercolor(self) -> int:
		"Specifies the color of the AutoSnap marker"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.AutoSnapMarkerColor
	@autosnapmarkercolor.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.AutoSnapMarkerColor = Path

	@indexedproperty
	def autosnapmarkersize(self) -> int:
		"Specifies the size of the AutoSnap marker"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.AutoSnapMarkerSize
	@autosnapmarkersize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.AutoSnapMarkerSize = Path

	@indexedproperty
	def autosnaptooltip(self) -> bool:
		"Toggles the AutoSnap tooltips"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutoSnapTooltip
	@autosnaptooltip.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutoSnapTooltip = Path

	@indexedproperty
	def autotracktooltip(self) -> bool:
		"Toggles the display of the AutoTrack tooltips"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutoTrackTooltip
	@autotracktooltip.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutoTrackTooltip = Path

	@indexedproperty
	def fullscreentrackingvector(self) -> bool:
		"Toggles the display of full screen tracking vectors"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.FullScreenTrackingVector
	@fullscreentrackingvector.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.FullScreenTrackingVector = Path

	@indexedproperty
	def polartrackingvector(self) -> bool:
		"Toggles the display of polar tracking vectors"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PolarTrackingVector
	@polartrackingvector.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PolarTrackingVector = Path


class AcadPreferencesFiles(POINTER(_dll.IAcadPreferencesFiles), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesFiles
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesFiles VBA-class wrapped as AcadPreferencesFiles python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesFiles__com_GetProjectFilePath
	#	_IAcadPreferencesFiles__com_SetProjectFilePath
	#	_IAcadPreferencesFiles__com__get_ActiveInvProject
	#	_IAcadPreferencesFiles__com__get_AltFontFile
	#	_IAcadPreferencesFiles__com__get_AltTabletMenuFile
	#	_IAcadPreferencesFiles__com__get_Application
	#	_IAcadPreferencesFiles__com__get_AutoSavePath
	#	_IAcadPreferencesFiles__com__get_ColorBookPath
	#	_IAcadPreferencesFiles__com__get_ConfigFile
	#	_IAcadPreferencesFiles__com__get_CustomDictionary
	#	_IAcadPreferencesFiles__com__get_CustomIconPath
	#	_IAcadPreferencesFiles__com__get_DefaultInternetURL
	#	_IAcadPreferencesFiles__com__get_DriversPath
	#	_IAcadPreferencesFiles__com__get_EnterpriseMenuFile
	#	_IAcadPreferencesFiles__com__get_FontFileMap
	#	_IAcadPreferencesFiles__com__get_HelpFilePath
	#	_IAcadPreferencesFiles__com__get_LicenseServer
	#	_IAcadPreferencesFiles__com__get_LogFilePath
	#	_IAcadPreferencesFiles__com__get_MainDictionary
	#	_IAcadPreferencesFiles__com__get_MenuFile
	#	_IAcadPreferencesFiles__com__get_ObjectARXPath
	#	_IAcadPreferencesFiles__com__get_PageSetupOverridesTemplateFile
	#	_IAcadPreferencesFiles__com__get_PlotLogFilePath
	#	_IAcadPreferencesFiles__com__get_PostScriptPrologFile
	#	_IAcadPreferencesFiles__com__get_PrintFile
	#	_IAcadPreferencesFiles__com__get_PrintSpoolExecutable
	#	_IAcadPreferencesFiles__com__get_PrintSpoolerPath
	#	_IAcadPreferencesFiles__com__get_PrinterConfigPath
	#	_IAcadPreferencesFiles__com__get_PrinterDescPath
	#	_IAcadPreferencesFiles__com__get_PrinterStyleSheetPath
	#	_IAcadPreferencesFiles__com__get_QNewTemplateFile
	#	_IAcadPreferencesFiles__com__get_SupportPath
	#	_IAcadPreferencesFiles__com__get_TempFilePath
	#	_IAcadPreferencesFiles__com__get_TempXrefPath
	#	_IAcadPreferencesFiles__com__get_TemplateDwgPath
	#	_IAcadPreferencesFiles__com__get_TextEditor
	#	_IAcadPreferencesFiles__com__get_TextureMapPath
	#	_IAcadPreferencesFiles__com__get_ToolPalettePath
	#	_IAcadPreferencesFiles__com__get_WorkspacePath
	#	_IAcadPreferencesFiles__com__set_ActiveInvProject
	#	_IAcadPreferencesFiles__com__set_AltFontFile
	#	_IAcadPreferencesFiles__com__set_AltTabletMenuFile
	#	_IAcadPreferencesFiles__com__set_AutoSavePath
	#	_IAcadPreferencesFiles__com__set_ColorBookPath
	#	_IAcadPreferencesFiles__com__set_CustomDictionary
	#	_IAcadPreferencesFiles__com__set_CustomIconPath
	#	_IAcadPreferencesFiles__com__set_DefaultInternetURL
	#	_IAcadPreferencesFiles__com__set_DriversPath
	#	_IAcadPreferencesFiles__com__set_EnterpriseMenuFile
	#	_IAcadPreferencesFiles__com__set_FontFileMap
	#	_IAcadPreferencesFiles__com__set_HelpFilePath
	#	_IAcadPreferencesFiles__com__set_LogFilePath
	#	_IAcadPreferencesFiles__com__set_MainDictionary
	#	_IAcadPreferencesFiles__com__set_MenuFile
	#	_IAcadPreferencesFiles__com__set_ObjectARXPath
	#	_IAcadPreferencesFiles__com__set_PageSetupOverridesTemplateFile
	#	_IAcadPreferencesFiles__com__set_PlotLogFilePath
	#	_IAcadPreferencesFiles__com__set_PostScriptPrologFile
	#	_IAcadPreferencesFiles__com__set_PrintFile
	#	_IAcadPreferencesFiles__com__set_PrintSpoolExecutable
	#	_IAcadPreferencesFiles__com__set_PrintSpoolerPath
	#	_IAcadPreferencesFiles__com__set_PrinterConfigPath
	#	_IAcadPreferencesFiles__com__set_PrinterDescPath
	#	_IAcadPreferencesFiles__com__set_PrinterStyleSheetPath
	#	_IAcadPreferencesFiles__com__set_QNewTemplateFile
	#	_IAcadPreferencesFiles__com__set_SupportPath
	#	_IAcadPreferencesFiles__com__set_TempFilePath
	#	_IAcadPreferencesFiles__com__set_TempXrefPath
	#	_IAcadPreferencesFiles__com__set_TemplateDwgPath
	#	_IAcadPreferencesFiles__com__set_TextEditor
	#	_IAcadPreferencesFiles__com__set_TextureMapPath
	#	_IAcadPreferencesFiles__com__set_ToolPalettePath
	#	_IAcadPreferencesFiles__com__set_WorkspacePath
	# Methods
	def getprojectfilepath(self, ProjectName: str) -> str:
		"Gets the directory in which AutoCAD looks for external reference files"
		# TODO: Check arguments
		# ['in'] ProjectName:str
		# ['out', 'retval'] Path:str
		# VBA: Path = object.GetProjectFilePath (ProjectName)
		return self.com_parent.GetProjectFilePath(ProjectName)

	def setprojectfilepath(self, ProjectName: str, ProjectFilePath: str):
		"Sets the directory in which AutoCAD looks for external reference files"
		# ['in'] ProjectName:str
		# ['in'] ProjectFilePath:str
		# VBA: object.SetProjectFilePath ProjectName, ProjectFilePath
		self.com_parent.SetProjectFilePath(ProjectName, ProjectFilePath)

	# Properties
	@indexedproperty
	def activeinvproject(self) -> str:
		"Sets the active Inventor project file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.ActiveInvProject
	@activeinvproject.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.ActiveInvProject = Path

	@indexedproperty
	def altfontfile(self) -> str:
		"Specifies the location of the font file to use if AutoCAD can't locate the original font and an alternate font is not specified in the font mapping file"
		# TODO: Check arguments
		# ['out', 'retval'] fontFile:str
		return self.com_parent.AltFontFile
	@altfontfile.setter
	def _(self, fontFile:str):
		# ['in'] fontFile:str
		self.com_parent.AltFontFile = fontFile

	@indexedproperty
	def alttabletmenufile(self) -> str:
		"Specifies the path for an alternate menu to swap with the standard AutoCAD tablet menu"
		# TODO: Check arguments
		# ['out', 'retval'] MenuFile:str
		return self.com_parent.AltTabletMenuFile
	@alttabletmenufile.setter
	def _(self, MenuFile:str):
		# ['in'] MenuFile:str
		self.com_parent.AltTabletMenuFile = MenuFile

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def autosavepath(self) -> str:
		"Specifies the path for the file that is created if you enable automatic save using the AutoSaveInterval property"
		# TODO: Check arguments
		# ['out', 'retval'] AutoSavePath:str
		return self.com_parent.AutoSavePath
	@autosavepath.setter
	def _(self, AutoSavePath:str):
		# ['in'] AutoSavePath:str
		self.com_parent.AutoSavePath = AutoSavePath

	@indexedproperty
	def colorbookpath(self) -> str:
		"Sets the Colorbook path."
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.ColorBookPath
	@colorbookpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.ColorBookPath = Path

	@indexedproperty
	def configfile(self) -> str:
		"Gets the location of the configuration file used to store hardware device driver information"
		# TODO: Check arguments
		# ['out', 'retval'] ConfigFile:str
		return self.com_parent.ConfigFile

	@indexedproperty
	def customdictionary(self) -> str:
		"Specifies a custom dictionary to use if you have one"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.CustomDictionary
	@customdictionary.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.CustomDictionary = Path

	@indexedproperty
	def customiconpath(self) -> str:
		"Specifies the search path for custom icons"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.CustomIconPath
	@customiconpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.CustomIconPath = Path

	@indexedproperty
	def defaultinterneturl(self) -> str:
		"Specifies the default Internet address"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultInternetURL
	@defaultinterneturl.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultInternetURL = Path

	@indexedproperty
	def driverspath(self) -> str:
		"Specifies the directory in which AutoCAD looks for ADI device drivers for the video display, pointing devices, printers, and plotters"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DriversPath
	@driverspath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DriversPath = Path

	@indexedproperty
	def enterprisemenufile(self) -> str:
		"Specifies the location of the enterprise menu file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.EnterpriseMenuFile
	@enterprisemenufile.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.EnterpriseMenuFile = Path

	@indexedproperty
	def fontfilemap(self) -> str:
		"Specifies the location of the file that defines how AutoCAD should convert fonts it can't locate"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.FontFileMap
	@fontfilemap.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.FontFileMap = Path

	@indexedproperty
	def helpfilepath(self) -> str:
		"Specifies the location of the AutoCAD Help file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.HelpFilePath
	@helpfilepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.HelpFilePath = Path

	@indexedproperty
	def licenseserver(self) -> str:
		"Provides network administrators a current list of client license servers available to the network license manager program"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.LicenseServer

	@indexedproperty
	def logfilepath(self) -> str:
		"Specifies the location for the log file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.LogFilePath
	@logfilepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.LogFilePath = Path

	@indexedproperty
	def maindictionary(self) -> str:
		"Specifies the current dictionary to use for spell checking"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.MainDictionary
	@maindictionary.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.MainDictionary = Path

	@indexedproperty
	def menufile(self) -> str:
		"Specifies the location of the AutoCAD menu file for the session"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.MenuFile
	@menufile.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.MenuFile = Path

	@indexedproperty
	def objectarxpath(self) -> str:
		"Specifies the location for ObjectARX applications"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.ObjectARXPath
	@objectarxpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.ObjectARXPath = Path

	@indexedproperty
	def pagesetupoverridestemplatefile(self) -> str:
		"Sets the default template for Page Setup overrides."
		# TODO: Check arguments
		# ['out', 'retval'] templateFile:str
		return self.com_parent.PageSetupOverridesTemplateFile
	@pagesetupoverridestemplatefile.setter
	def _(self, templateFile:str):
		# ['in'] templateFile:str
		self.com_parent.PageSetupOverridesTemplateFile = templateFile

	@indexedproperty
	def plotlogfilepath(self) -> str:
		"Sets the plot log file path."
		# TODO: Check arguments
		# ['out', 'retval'] templateFile:str
		return self.com_parent.PlotLogFilePath
	@plotlogfilepath.setter
	def _(self, templateFile:str):
		# ['in'] templateFile:str
		self.com_parent.PlotLogFilePath = templateFile

	@indexedproperty
	def postscriptprologfile(self) -> str:
		"Specifies a name for a customized prolog section in the acad.psf file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PostScriptPrologFile
	@postscriptprologfile.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PostScriptPrologFile = Path

	@indexedproperty
	def printerconfigpath(self) -> str:
		"Specifies the location for printer configuration files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrinterConfigPath
	@printerconfigpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrinterConfigPath = Path

	@indexedproperty
	def printerdescpath(self) -> str:
		"Specifies the location for printer description files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrinterDescPath
	@printerdescpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrinterDescPath = Path

	@indexedproperty
	def printerstylesheetpath(self) -> str:
		"Specifies the location for printer style sheet files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrinterStyleSheetPath
	@printerstylesheetpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrinterStyleSheetPath = Path

	@indexedproperty
	def printfile(self) -> str:
		"Specifies an alternate name to use for the temporary plot file name"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrintFile
	@printfile.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrintFile = Path

	@indexedproperty
	def printspoolerpath(self) -> str:
		"Specifies the directory for the print spool files. AutoCAD writes the plot to this location"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrintSpoolerPath
	@printspoolerpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrintSpoolerPath = Path

	@indexedproperty
	def printspoolexecutable(self) -> str:
		"Specifies the application to use for print spooling"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.PrintSpoolExecutable
	@printspoolexecutable.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.PrintSpoolExecutable = Path

	@indexedproperty
	def qnewtemplatefile(self) -> str:
		"Sets the default template for the QNEW command."
		# TODO: Check arguments
		# ['out', 'retval'] templateFile:str
		return self.com_parent.QNewTemplateFile
	@qnewtemplatefile.setter
	def _(self, templateFile:str):
		# ['in'] templateFile:str
		self.com_parent.QNewTemplateFile = templateFile

	@indexedproperty
	def supportpath(self) -> str:
		"Specifies the directories where AutoCAD searches for support files"
		# TODO: Check arguments
		# ['out', 'retval'] orient:str
		return self.com_parent.SupportPath
	@supportpath.setter
	def _(self, orient:str):
		# ['in'] orient:str
		self.com_parent.SupportPath = orient

	@indexedproperty
	def tempfilepath(self) -> str:
		"Specifies the directory AutoCAD uses to store temporary files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TempFilePath
	@tempfilepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TempFilePath = Path

	@indexedproperty
	def templatedwgpath(self) -> str:
		"Specifies the path for the template files used by the start-up wizards"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TemplateDwgPath
	@templatedwgpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TemplateDwgPath = Path

	@indexedproperty
	def tempxrefpath(self) -> str:
		"Specifies the location of external reference files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TempXrefPath
	@tempxrefpath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TempXrefPath = Path

	@indexedproperty
	def texteditor(self) -> str:
		"Specifies the name of the text editor for the MTEXT command"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TextEditor
	@texteditor.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TextEditor = Path

	@indexedproperty
	def texturemappath(self) -> str:
		"Specifies the directory in which AutoCAD searches for rendering texture maps"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TextureMapPath
	@texturemappath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TextureMapPath = Path

	@indexedproperty
	def toolpalettepath(self) -> str:
		"Sets the ToolPalette path."
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.ToolPalettePath
	@toolpalettepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.ToolPalettePath = Path

	@indexedproperty
	def workspacepath(self) -> str:
		"Specifies the path for the database workspace file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.WorkspacePath
	@workspacepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.WorkspacePath = Path


class AcadPreferencesOpenSave(POINTER(_dll.IAcadPreferencesOpenSave), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesOpenSave
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesOpenSave VBA-class wrapped as AcadPreferencesOpenSave python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesOpenSave__com__get_Application
	#	_IAcadPreferencesOpenSave__com__get_AutoAudit
	#	_IAcadPreferencesOpenSave__com__get_AutoSaveInterval
	#	_IAcadPreferencesOpenSave__com__get_CreateBackup
	#	_IAcadPreferencesOpenSave__com__get_DemandLoadARXApp
	#	_IAcadPreferencesOpenSave__com__get_FullCRCValidation
	#	_IAcadPreferencesOpenSave__com__get_IncrementalSavePercent
	#	_IAcadPreferencesOpenSave__com__get_LogFileOn
	#	_IAcadPreferencesOpenSave__com__get_MRUNumber
	#	_IAcadPreferencesOpenSave__com__get_ProxyImage
	#	_IAcadPreferencesOpenSave__com__get_SaveAsType
	#	_IAcadPreferencesOpenSave__com__get_SavePreviewThumbnail
	#	_IAcadPreferencesOpenSave__com__get_ShowProxyDialogBox
	#	_IAcadPreferencesOpenSave__com__get_TempFileExtension
	#	_IAcadPreferencesOpenSave__com__get_XrefDemandLoad
	#	_IAcadPreferencesOpenSave__com__set_AutoAudit
	#	_IAcadPreferencesOpenSave__com__set_AutoSaveInterval
	#	_IAcadPreferencesOpenSave__com__set_CreateBackup
	#	_IAcadPreferencesOpenSave__com__set_DemandLoadARXApp
	#	_IAcadPreferencesOpenSave__com__set_FullCRCValidation
	#	_IAcadPreferencesOpenSave__com__set_IncrementalSavePercent
	#	_IAcadPreferencesOpenSave__com__set_LogFileOn
	#	_IAcadPreferencesOpenSave__com__set_ProxyImage
	#	_IAcadPreferencesOpenSave__com__set_SaveAsType
	#	_IAcadPreferencesOpenSave__com__set_SavePreviewThumbnail
	#	_IAcadPreferencesOpenSave__com__set_ShowProxyDialogBox
	#	_IAcadPreferencesOpenSave__com__set_TempFileExtension
	#	_IAcadPreferencesOpenSave__com__set_XrefDemandLoad
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def autoaudit(self) -> bool:
		"Specifies if AutoCAD should perform an audit after you render a DXFIN or DXBIN interchange command"
		# TODO: Check arguments
		# ['out', 'retval'] bAudit:bool
		return self.com_parent.AutoAudit
	@autoaudit.setter
	def _(self, bAudit:bool):
		# ['in'] bAudit:bool
		self.com_parent.AutoAudit = bAudit

	@indexedproperty
	def autosaveinterval(self) -> int:
		"Specifies an automatic save interval in minutes"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.AutoSaveInterval
	@autosaveinterval.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.AutoSaveInterval = Path

	@indexedproperty
	def createbackup(self) -> bool:
		"Specifies the use of a backup file"
		# TODO: Check arguments
		# ['out', 'retval'] CreateBackup:bool
		return self.com_parent.CreateBackup
	@createbackup.setter
	def _(self, CreateBackup:bool):
		# ['in'] CreateBackup:bool
		self.com_parent.CreateBackup = CreateBackup

	@indexedproperty
	def demandloadarxapp(self) -> int:
		"Specifies if and when AutoCAD demand loads a third-party application if a drawing contains custom objects created in that application"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.DemandLoadARXApp
	@demandloadarxapp.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.DemandLoadARXApp = Path

	@indexedproperty
	def fullcrcvalidation(self) -> bool:
		"Specifies if a cyclic redundancy check (CRC) should be performed each time an object is read into the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.FullCRCValidation
	@fullcrcvalidation.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.FullCRCValidation = Path

	@indexedproperty
	def incrementalsavepercent(self) -> int:
		"Specifies the percentage of wasted space allowed in a drawing file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.IncrementalSavePercent
	@incrementalsavepercent.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.IncrementalSavePercent = Path

	@indexedproperty
	def logfileon(self) -> bool:
		"Specifies if the contents of the text window are written to a log file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.LogFileOn
	@logfileon.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.LogFileOn = Path

	@indexedproperty
	def mrunumber(self) -> int:
		"Specifies the number of most recently used files that appear in the File menu"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.MRUNumber

	@indexedproperty
	def proxyimage(self) -> int:
		"Controls the display of objects in a drawing that were created in a third-party application"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.ProxyImage
	@proxyimage.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.ProxyImage = Path

	@indexedproperty
	def saveastype(self) -> int:
		"Specifies the drawing type to save the drawing as"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.SaveAsType
	@saveastype.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.SaveAsType = Path

	@indexedproperty
	def savepreviewthumbnail(self) -> bool:
		"Specifies if BMP preview images are saved with the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.SavePreviewThumbnail
	@savepreviewthumbnail.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.SavePreviewThumbnail = Path

	@indexedproperty
	def showproxydialogbox(self) -> bool:
		"Specifies if AutoCAD displays a warning message when you open a drawing that contains custom objects"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.ShowProxyDialogBox
	@showproxydialogbox.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.ShowProxyDialogBox = Path

	@indexedproperty
	def tempfileextension(self) -> str:
		"Specifies the extension for temporary files"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.TempFileExtension
	@tempfileextension.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.TempFileExtension = Path

	@indexedproperty
	def xrefdemandload(self) -> int:
		"Specifies demand loading of external references"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.XrefDemandLoad
	@xrefdemandload.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.XrefDemandLoad = Path


class AcadPreferencesOutput(POINTER(_dll.IAcadPreferencesOutput), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesOutput
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesOutput VBA-class wrapped as AcadPreferencesOutput python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesOutput__com__get_Application
	#	_IAcadPreferencesOutput__com__get_AutomaticPlotLog
	#	_IAcadPreferencesOutput__com__get_ContinuousPlotLog
	#	_IAcadPreferencesOutput__com__get_DefaultOutputDevice
	#	_IAcadPreferencesOutput__com__get_DefaultPlotStyleForLayer
	#	_IAcadPreferencesOutput__com__get_DefaultPlotStyleForObjects
	#	_IAcadPreferencesOutput__com__get_DefaultPlotStyleTable
	#	_IAcadPreferencesOutput__com__get_DefaultPlotToFilePath
	#	_IAcadPreferencesOutput__com__get_OLEQuality
	#	_IAcadPreferencesOutput__com__get_PlotLegacy
	#	_IAcadPreferencesOutput__com__get_PlotPolicy
	#	_IAcadPreferencesOutput__com__get_PrinterPaperSizeAlert
	#	_IAcadPreferencesOutput__com__get_PrinterSpoolAlert
	#	_IAcadPreferencesOutput__com__get_UseLastPlotSettings
	#	_IAcadPreferencesOutput__com__set_AutomaticPlotLog
	#	_IAcadPreferencesOutput__com__set_ContinuousPlotLog
	#	_IAcadPreferencesOutput__com__set_DefaultOutputDevice
	#	_IAcadPreferencesOutput__com__set_DefaultPlotStyleForLayer
	#	_IAcadPreferencesOutput__com__set_DefaultPlotStyleForObjects
	#	_IAcadPreferencesOutput__com__set_DefaultPlotStyleTable
	#	_IAcadPreferencesOutput__com__set_DefaultPlotToFilePath
	#	_IAcadPreferencesOutput__com__set_OLEQuality
	#	_IAcadPreferencesOutput__com__set_PlotLegacy
	#	_IAcadPreferencesOutput__com__set_PlotPolicy
	#	_IAcadPreferencesOutput__com__set_PrinterPaperSizeAlert
	#	_IAcadPreferencesOutput__com__set_PrinterSpoolAlert
	#	_IAcadPreferencesOutput__com__set_UseLastPlotSettings
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def automaticplotlog(self) -> bool:
		"Determines whether to automatically save plot and publish log."
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.AutomaticPlotLog
	@automaticplotlog.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.AutomaticPlotLog = Path

	@indexedproperty
	def continuousplotlog(self) -> bool:
		"Determines whether to save a continuous plot log."
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.ContinuousPlotLog
	@continuousplotlog.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.ContinuousPlotLog = Path

	@indexedproperty
	def defaultoutputdevice(self) -> str:
		"Specifies the default output device for new layouts and model space"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultOutputDevice
	@defaultoutputdevice.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultOutputDevice = Path

	@indexedproperty
	def defaultplotstyleforlayer(self) -> str:
		"Specifies the default plot style for Layer 0 for new drawings or drawings created with earlier releases of AutoCAD never been saved in AutoCAD 2000 format"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultPlotStyleForLayer
	@defaultplotstyleforlayer.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultPlotStyleForLayer = Path

	@indexedproperty
	def defaultplotstyleforobjects(self) -> str:
		"Specifies the default plot style table to attach to new drawings"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultPlotStyleForObjects
	@defaultplotstyleforobjects.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultPlotStyleForObjects = Path

	@indexedproperty
	def defaultplotstyletable(self) -> str:
		"DefaultPlotStyleTable."
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultPlotStyleTable
	@defaultplotstyletable.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultPlotStyleTable = Path

	@indexedproperty
	def defaultplottofilepath(self) -> str:
		"Sets the default location for plot to file operations."
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.DefaultPlotToFilePath
	@defaultplottofilepath.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.DefaultPlotToFilePath = Path

	@indexedproperty
	def olequality(self) -> int:
		"Specifies the plot quality of OLE objects"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.OLEQuality
	@olequality.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.OLEQuality = Path

	@indexedproperty
	def plotlegacy(self) -> bool:
		"Toggles if legacy plot scripts are allowed to run"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PlotLegacy
	@plotlegacy.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PlotLegacy = Path

	@indexedproperty
	def plotpolicy(self) -> int:
		"Determines whether an object's color property is associated with its plot style name when creating a new drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.PlotPolicy
	@plotpolicy.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.PlotPolicy = Path

	@indexedproperty
	def printerpapersizealert(self) -> bool:
		"Specifies whether to alert the user when a layout is configured with a paper size that is different than the default setting for the PC3 file"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PrinterPaperSizeAlert
	@printerpapersizealert.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PrinterPaperSizeAlert = Path

	@indexedproperty
	def printerspoolalert(self) -> int:
		"Specifies whether to alert the user when the output to a device must be spooled through a system printer due to a conflict with the I/O port"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.PrinterSpoolAlert
	@printerspoolalert.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.PrinterSpoolAlert = Path

	@indexedproperty
	def uselastplotsettings(self) -> bool:
		"Applies the plotting settings of the last successful plot"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.UseLastPlotSettings
	@uselastplotsettings.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.UseLastPlotSettings = Path


class AcadPreferencesProfiles(POINTER(_dll.IAcadPreferencesProfiles), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesProfiles
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesProfiles VBA-class wrapped as AcadPreferencesProfiles python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesProfiles__com_CopyProfile
	#	_IAcadPreferencesProfiles__com_DeleteProfile
	#	_IAcadPreferencesProfiles__com_ExportProfile
	#	_IAcadPreferencesProfiles__com_GetAllProfileNames
	#	_IAcadPreferencesProfiles__com_ImportProfile
	#	_IAcadPreferencesProfiles__com_RenameProfile
	#	_IAcadPreferencesProfiles__com_ResetProfile
	#	_IAcadPreferencesProfiles__com__get_ActiveProfile
	#	_IAcadPreferencesProfiles__com__get_Application
	#	_IAcadPreferencesProfiles__com__set_ActiveProfile
	# Methods
	def copyprofile(self, oldProfileName: str, newProfileName: str):
		"Copies the specified profile"
		# ['in'] oldProfileName:str
		# ['in'] newProfileName:str
		# VBA: object.CopyProfile oldProfileName, newProfileName
		self.com_parent.CopyProfile(oldProfileName, newProfileName)

	def deleteprofile(self, ProfileName: str):
		"Deletes the specified profile"
		# ['in'] ProfileName:str
		# VBA: object.DeleteProfile ProfileName
		self.com_parent.DeleteProfile(ProfileName)

	def exportprofile(self, ProfileName: str, RegFile: str):
		"Exports the active profile so it can be shared with other users"
		# ['in'] ProfileName:str
		# ['in'] RegFile:str
		# VBA: object.ExportProfile ProfileName, RegFile
		self.com_parent.ExportProfile(ProfileName, RegFile)

	def getallprofilenames(self) -> tagVARIANT:
		"Gets all available profiles for the system"
		# TODO: Check arguments
		# ['out'] pNames:tagVARIANT
		# VBA: object.GetAllProfileNames pNames
		return self.com_parent.GetAllProfileNames()

	def importprofile(self, ProfileName: str, RegFile: str, IncludePathInfo: bool):
		"Imports a profile created by another user"
		# ['in'] ProfileName:str
		# ['in'] RegFile:str
		# ['in'] IncludePathInfo:bool
		# VBA: object.ImportProfile ProfileName, RegFile, IncludePathInfo
		self.com_parent.ImportProfile(ProfileName, RegFile, IncludePathInfo)

	def renameprofile(self, origProfileName: str, newProfileName: str):
		"Renames the specified profile"
		# ['in'] origProfileName:str
		# ['in'] newProfileName:str
		# VBA: object.RenameProfile origProfileName, newProfileName
		self.com_parent.RenameProfile(origProfileName, newProfileName)

	def resetprofile(self, Profile: str):
		"Resets the value in the specified profile to its default values"
		# ['in'] Profile:str
		# VBA: object.ResetProfile Profile
		self.com_parent.ResetProfile(Profile)

	# Properties
	@indexedproperty
	def activeprofile(self) -> str:
		"Specifies the active profile for the AutoCAD session"
		# TODO: Check arguments
		# ['out', 'retval'] Path:str
		return self.com_parent.ActiveProfile
	@activeprofile.setter
	def _(self, Path:str):
		# ['in'] Path:str
		self.com_parent.ActiveProfile = Path

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application


class AcadPreferencesSelection(POINTER(_dll.IAcadPreferencesSelection), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesSelection
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesSelection VBA-class wrapped as AcadPreferencesSelection python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesSelection__com__get_Application
	#	_IAcadPreferencesSelection__com__get_DisplayGrips
	#	_IAcadPreferencesSelection__com__get_DisplayGripsWithinBlocks
	#	_IAcadPreferencesSelection__com__get_GripColorSelected
	#	_IAcadPreferencesSelection__com__get_GripColorUnselected
	#	_IAcadPreferencesSelection__com__get_GripSize
	#	_IAcadPreferencesSelection__com__get_PickAdd
	#	_IAcadPreferencesSelection__com__get_PickAuto
	#	_IAcadPreferencesSelection__com__get_PickBoxSize
	#	_IAcadPreferencesSelection__com__get_PickDrag
	#	_IAcadPreferencesSelection__com__get_PickFirst
	#	_IAcadPreferencesSelection__com__get_PickGroup
	#	_IAcadPreferencesSelection__com__set_DisplayGrips
	#	_IAcadPreferencesSelection__com__set_DisplayGripsWithinBlocks
	#	_IAcadPreferencesSelection__com__set_GripColorSelected
	#	_IAcadPreferencesSelection__com__set_GripColorUnselected
	#	_IAcadPreferencesSelection__com__set_GripSize
	#	_IAcadPreferencesSelection__com__set_PickAdd
	#	_IAcadPreferencesSelection__com__set_PickAuto
	#	_IAcadPreferencesSelection__com__set_PickBoxSize
	#	_IAcadPreferencesSelection__com__set_PickDrag
	#	_IAcadPreferencesSelection__com__set_PickFirst
	#	_IAcadPreferencesSelection__com__set_PickGroup
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def displaygrips(self) -> bool:
		"Controls the display of selection set grips for the Stretch, Move, Rotate, Scale, and Mirror grip modes"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayGrips
	@displaygrips.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayGrips = Path

	@indexedproperty
	def displaygripswithinblocks(self) -> bool:
		"Controls the assignment of grips within blocks"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayGripsWithinBlocks
	@displaygripswithinblocks.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayGripsWithinBlocks = Path

	@indexedproperty
	def gripcolorselected(self) -> int:
		"Specifies the color of selected grips"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.GripColorSelected
	@gripcolorselected.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.GripColorSelected = Path

	@indexedproperty
	def gripcolorunselected(self) -> int:
		"Specifies the color of unselected grips"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.GripColorUnselected
	@gripcolorunselected.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.GripColorUnselected = Path

	@indexedproperty
	def gripsize(self) -> int:
		"Specifies the size of grips"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.GripSize
	@gripsize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.GripSize = Path

	@indexedproperty
	def pickadd(self) -> bool:
		"Determines if objects are added to the selection set using the Shift key"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PickAdd
	@pickadd.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PickAdd = Path

	@indexedproperty
	def pickauto(self) -> bool:
		"Controls automatic windowing at the Select Objects prompt"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PickAuto
	@pickauto.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PickAuto = Path

	@indexedproperty
	def pickboxsize(self) -> int:
		"Specifies the size of the object selection target"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.PickBoxSize
	@pickboxsize.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.PickBoxSize = Path

	@indexedproperty
	def pickdrag(self) -> bool:
		"Controls the method of drawing a selection window"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PickDrag
	@pickdrag.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PickDrag = Path

	@indexedproperty
	def pickfirst(self) -> bool:
		"Determines if you select objects before (noun-verb selection) or after you issue a command"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.PickFirst
	@pickfirst.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.PickFirst = Path

	@indexedproperty
	def pickgroup(self) -> bool:
		"Determines if picking a single object in a group selects the entire group"
		# TODO: Check arguments
		# ['out', 'retval'] pick:bool
		return self.com_parent.PickGroup
	@pickgroup.setter
	def _(self, pick:bool):
		# ['in'] pick:bool
		self.com_parent.PickGroup = pick


class AcadPreferencesSystem(POINTER(_dll.IAcadPreferencesSystem), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesSystem
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesSystem VBA-class wrapped as AcadPreferencesSystem python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesSystem__com__get_Application
	#	_IAcadPreferencesSystem__com__get_BeepOnError
	#	_IAcadPreferencesSystem__com__get_DisplayOLEScale
	#	_IAcadPreferencesSystem__com__get_EnableStartupDialog
	#	_IAcadPreferencesSystem__com__get_LoadAcadLspInAllDocuments
	#	_IAcadPreferencesSystem__com__get_ShowWarningMessages
	#	_IAcadPreferencesSystem__com__get_SingleDocumentMode
	#	_IAcadPreferencesSystem__com__get_StoreSQLIndex
	#	_IAcadPreferencesSystem__com__get_TablesReadOnly
	#	_IAcadPreferencesSystem__com__set_BeepOnError
	#	_IAcadPreferencesSystem__com__set_DisplayOLEScale
	#	_IAcadPreferencesSystem__com__set_EnableStartupDialog
	#	_IAcadPreferencesSystem__com__set_LoadAcadLspInAllDocuments
	#	_IAcadPreferencesSystem__com__set_ShowWarningMessages
	#	_IAcadPreferencesSystem__com__set_SingleDocumentMode
	#	_IAcadPreferencesSystem__com__set_StoreSQLIndex
	#	_IAcadPreferencesSystem__com__set_TablesReadOnly
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def beeponerror(self) -> bool:
		"Specifies if AutoCAD should sound an alarm beep when it detects an invalid entry"
		# TODO: Check arguments
		# ['out', 'retval'] BeepOnError:bool
		return self.com_parent.BeepOnError
	@beeponerror.setter
	def _(self, BeepOnError:bool):
		# ['in'] BeepOnError:bool
		self.com_parent.BeepOnError = BeepOnError

	@indexedproperty
	def displayolescale(self) -> bool:
		"Determines if the OLE scaling dialog is displayed when OLE objects are inserted into a drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.DisplayOLEScale
	@displayolescale.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.DisplayOLEScale = Path

	@indexedproperty
	def enablestartupdialog(self) -> bool:
		"Specifies if the Start-up dialog box is displayed when AutoCAD is launched"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.EnableStartupDialog
	@enablestartupdialog.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.EnableStartupDialog = Path

	@indexedproperty
	def loadacadlspinalldocuments(self) -> bool:
		"LoadAcadLspInAllDocuments."
		# TODO: Check arguments
		# ['out', 'retval'] pALID:bool
		return self.com_parent.LoadAcadLspInAllDocuments
	@loadacadlspinalldocuments.setter
	def _(self, pALID:bool):
		# ['in'] pALID:bool
		self.com_parent.LoadAcadLspInAllDocuments = pALID

	@indexedproperty
	def showwarningmessages(self) -> bool:
		"Resets all dialog boxes that have the "Don't Display This Warning Again" check box so they display again"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.ShowWarningMessages
	@showwarningmessages.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.ShowWarningMessages = Path

	@indexedproperty
	def singledocumentmode(self) -> bool:
		"Determines if AutoCAD runs in single- or multiple-document mode"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.SingleDocumentMode
	@singledocumentmode.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.SingleDocumentMode = Path

	@indexedproperty
	def storesqlindex(self) -> bool:
		"Determines if the SQL index is stored in the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.StoreSQLIndex
	@storesqlindex.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.StoreSQLIndex = Path

	@indexedproperty
	def tablesreadonly(self) -> bool:
		"Determines whether to open database tables in read-only mode"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.TablesReadOnly
	@tablesreadonly.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.TablesReadOnly = Path


class AcadPreferencesUser(POINTER(_dll.IAcadPreferencesUser), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadPreferencesUser
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadPreferencesUser VBA-class wrapped as AcadPreferencesUser python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadPreferencesUser__com__get_ADCInsertUnitsDefaultSource
	#	_IAcadPreferencesUser__com__get_ADCInsertUnitsDefaultTarget
	#	_IAcadPreferencesUser__com__get_Application
	#	_IAcadPreferencesUser__com__get_HyperlinkDisplayCursor
	#	_IAcadPreferencesUser__com__get_KeyboardAccelerator
	#	_IAcadPreferencesUser__com__get_KeyboardPriority
	#	_IAcadPreferencesUser__com__get_SCMCommandMode
	#	_IAcadPreferencesUser__com__get_SCMDefaultMode
	#	_IAcadPreferencesUser__com__get_SCMEditMode
	#	_IAcadPreferencesUser__com__get_SCMTimeMode
	#	_IAcadPreferencesUser__com__get_SCMTimeValue
	#	_IAcadPreferencesUser__com__get_ShortCutMenuDisplay
	#	_IAcadPreferencesUser__com__set_ADCInsertUnitsDefaultSource
	#	_IAcadPreferencesUser__com__set_ADCInsertUnitsDefaultTarget
	#	_IAcadPreferencesUser__com__set_HyperlinkDisplayCursor
	#	_IAcadPreferencesUser__com__set_KeyboardAccelerator
	#	_IAcadPreferencesUser__com__set_KeyboardPriority
	#	_IAcadPreferencesUser__com__set_SCMCommandMode
	#	_IAcadPreferencesUser__com__set_SCMDefaultMode
	#	_IAcadPreferencesUser__com__set_SCMEditMode
	#	_IAcadPreferencesUser__com__set_SCMTimeMode
	#	_IAcadPreferencesUser__com__set_SCMTimeValue
	#	_IAcadPreferencesUser__com__set_ShortCutMenuDisplay
	# Properties
	@indexedproperty
	def adcinsertunitsdefaultsource(self) -> int:
		"Determines the units to automatically use for objects in the AutoCAD DesignCenter for a source drawing that does not have assigned insert units"
		# TODO: Check arguments
		# ['out', 'retval'] pIU:int
		return self.com_parent.ADCInsertUnitsDefaultSource
	@adcinsertunitsdefaultsource.setter
	def _(self, pIU:int):
		# ['in'] pIU:int
		self.com_parent.ADCInsertUnitsDefaultSource = pIU

	@indexedproperty
	def adcinsertunitsdefaulttarget(self) -> int:
		"Determines the units to automatically use for objects in the AutoCAD DesignCenter for a target drawing that does not have assigned insert units"
		# TODO: Check arguments
		# ['out', 'retval'] pSUunits:int
		return self.com_parent.ADCInsertUnitsDefaultTarget
	@adcinsertunitsdefaulttarget.setter
	def _(self, pSUunits:int):
		# ['in'] pSUunits:int
		self.com_parent.ADCInsertUnitsDefaultTarget = pSUunits

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def hyperlinkdisplaycursor(self) -> bool:
		"Toggles the display of the hyperlink cursor and shortcut menu"
		# TODO: Check arguments
		# ['out', 'retval'] Path:bool
		return self.com_parent.HyperlinkDisplayCursor
	@hyperlinkdisplaycursor.setter
	def _(self, Path:bool):
		# ['in'] Path:bool
		self.com_parent.HyperlinkDisplayCursor = Path

	@indexedproperty
	def keyboardaccelerator(self) -> int:
		"Specifies the Windows standard or AutoCAD classic keyboard"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.KeyboardAccelerator
	@keyboardaccelerator.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.KeyboardAccelerator = Path

	@indexedproperty
	def keyboardpriority(self) -> int:
		"Controls how AutoCAD responds to the input of coordinate data"
		# TODO: Check arguments
		# ['out', 'retval'] Path:int
		return self.com_parent.KeyboardPriority
	@keyboardpriority.setter
	def _(self, Path:int):
		# ['in'] Path:int
		self.com_parent.KeyboardPriority = Path

	@indexedproperty
	def scmcommandmode(self) -> int:
		"Determines right-click functionality in the drawing area while in Command mode, which means that a command is currently in progress"
		# TODO: Check arguments
		# ['out', 'retval'] pSCM:int
		return self.com_parent.SCMCommandMode
	@scmcommandmode.setter
	def _(self, pSCM:int):
		# ['in'] pSCM:int
		self.com_parent.SCMCommandMode = pSCM

	@indexedproperty
	def scmdefaultmode(self) -> int:
		"Determines right-click functionality in the drawing area while in Default mode, which means that no objects are selected and no commands are in progress"
		# TODO: Check arguments
		# ['out', 'retval'] pSCM:int
		return self.com_parent.SCMDefaultMode
	@scmdefaultmode.setter
	def _(self, pSCM:int):
		# ['in'] pSCM:int
		self.com_parent.SCMDefaultMode = pSCM

	@indexedproperty
	def scmeditmode(self) -> int:
		"Determines right-click functionality in the drawing area while in Edit mode, which means that one or more objects are selected and no commands are in progress"
		# TODO: Check arguments
		# ['out', 'retval'] pSCM:int
		return self.com_parent.SCMEditMode
	@scmeditmode.setter
	def _(self, pSCM:int):
		# ['in'] pSCM:int
		self.com_parent.SCMEditMode = pSCM

	@indexedproperty
	def scmtimemode(self) -> bool:
		"Determines whether time sensitive right-click functionality is on."
		# TODO: Check arguments
		# ['out', 'retval'] time:bool
		return self.com_parent.SCMTimeMode
	@scmtimemode.setter
	def _(self, time:bool):
		# ['in'] time:bool
		self.com_parent.SCMTimeMode = time

	@indexedproperty
	def scmtimevalue(self) -> int:
		"Determines time sensitive right-click functionality longer click duration in milliseconds."
		# TODO: Check arguments
		# ['out', 'retval'] time:int
		return self.com_parent.SCMTimeValue
	@scmtimevalue.setter
	def _(self, time:int):
		# ['in'] time:int
		self.com_parent.SCMTimeValue = time

	@indexedproperty
	def shortcutmenudisplay(self) -> bool:
		"ShortCutMenuDisplay."
		# TODO: Check arguments
		# ['out', 'retval'] pSCM:bool
		return self.com_parent.ShortCutMenuDisplay
	@shortcutmenudisplay.setter
	def _(self, pSCM:bool):
		# ['in'] pSCM:bool
		self.com_parent.ShortCutMenuDisplay = pSCM


class AcadRegisteredApplication(POINTER(_dll.IAcadRegisteredApplication), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadRegisteredApplication
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadRegisteredApplication VBA-class wrapped as AcadRegisteredApplication python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadRegisteredApplication__com__get_Name
	#	_IAcadRegisteredApplication__com__set_Name
	# Properties
	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName


class AcadRegisteredApplications(POINTER(_dll.IAcadRegisteredApplications), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadRegisteredApplications
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadRegisteredApplications VBA-class wrapped as AcadRegisteredApplications python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadRegisteredApplications__com_Add
	#	_IAcadRegisteredApplications__com_Item
	#	_IAcadRegisteredApplications__com__get_Count
	#	_IAcadRegisteredApplications__com__get__NewEnum
	# Methods
	def add(self, Name: str) -> AcadRegisteredApplication:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pRegApp:AcadRegisteredApplication
		# VBA: pRegApp = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadRegisteredApplication:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadRegisteredApplication
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadSectionManager(POINTER(_dll.IAcadSectionManager), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSectionManager
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSectionManager VBA-class wrapped as AcadSectionManager python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadSectionManager__com_GetLiveSection
	#	_IAcadSectionManager__com_GetUniqueSectionName
	#	_IAcadSectionManager__com_Item
	#	_IAcadSectionManager__com__get_Count
	#	_IAcadSectionManager__com__get__NewEnum
	# Methods
	def getlivesection(self) -> AcadSection:
		"Gets the section whose live section is currently active"
		# TODO: Check arguments
		# ['out', 'retval'] pSection:AcadSection
		# VBA: pSection = object.GetLiveSection ()
		return self.com_parent.GetLiveSection()

	def getuniquesectionname(self, pBaseName: str) -> str:
		"Finds an unique name for secion"
		# TODO: Check arguments
		# ['in'] pBaseName:str
		# ['out', 'retval'] ppUniqueName:str
		# VBA: ppUniqueName = object.GetUniqueSectionName (pBaseName)
		return self.com_parent.GetUniqueSectionName(pBaseName)

	def item(self, Index: tagVARIANT) -> AcadSection:
		"Returns an item in the collection."
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pSection:AcadSection
		# VBA: pSection = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of sections in the database"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count


class AcadSectionSettings(POINTER(_dll.IAcadSectionSettings), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSectionSettings
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSectionSettings VBA-class wrapped as AcadSectionSettings python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadSectionSettings__com_GetSectionTypeSettings
	#	_IAcadSectionSettings__com__get_CurrentSectionType
	#	_IAcadSectionSettings__com__set_CurrentSectionType
	# Methods
	def getsectiontypesettings(self, secType: int) -> AcadSectionTypeSettings:
		"Gets the section type settings object"
		# TODO: Check arguments
		# ['in'] secType:int
		# ['out', 'retval'] pUnk:AcadSectionTypeSettings
		# VBA: pUnk = object.GetSectionTypeSettings (secType)
		return self.com_parent.GetSectionTypeSettings(secType)

	# Properties
	@indexedproperty
	def currentsectiontype(self) -> int:
		"Specifies the current section type"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.CurrentSectionType
	@currentsectiontype.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.CurrentSectionType = pVal


class AcadSectionTypeSettings(POINTER(_dll.IAcadSectionTypeSettings), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSectionTypeSettings
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSectionTypeSettings VBA-class wrapped as AcadSectionTypeSettings python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesColor
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLayer
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesVisible
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesColor
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLayer
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesVisible
	#	_IAcadSectionTypeSettings__com__get_DestinationBlock
	#	_IAcadSectionTypeSettings__com__get_DestinationFile
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesColor
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesEdgeTransparency
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesFaceTransparency
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLayer
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesVisible
	#	_IAcadSectionTypeSettings__com__get_GenerationOptions
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryColor
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryDivisionLines
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLayer
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLinetype
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLineweight
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillColor
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillFaceTransparency
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchAngle
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchPatternName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchPatternType
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchSpacing
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLayer
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLinetype
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLineweight
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillVisible
	#	_IAcadSectionTypeSettings__com__get_SourceObjects
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesColor
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLayer
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesVisible
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesColor
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLayer
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesVisible
	#	_IAcadSectionTypeSettings__com__set_DestinationBlock
	#	_IAcadSectionTypeSettings__com__set_DestinationFile
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesColor
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesEdgeTransparency
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesFaceTransparency
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLayer
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesVisible
	#	_IAcadSectionTypeSettings__com__set_GenerationOptions
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryColor
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryDivisionLines
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLayer
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLinetype
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLineweight
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillColor
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillFaceTransparency
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchAngle
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchPatternName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchPatternType
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchSpacing
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLayer
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLinetype
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLineweight
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillVisible
	#	_IAcadSectionTypeSettings__com__set_SourceObjects
	# Properties
	@indexedproperty
	def backgroundlinescolor(self) -> AcadAcCmColor:
		"Specifies the color of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.BackgroundLinesColor
	@backgroundlinescolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.BackgroundLinesColor = pColor

	@indexedproperty
	def backgroundlineshiddenline(self) -> bool:
		"Specifies the hidden line visibility of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.BackgroundLinesHiddenLine
	@backgroundlineshiddenline.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.BackgroundLinesHiddenLine = pVal

	@indexedproperty
	def backgroundlineslayer(self) -> str:
		"Specifies the layer of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.BackgroundLinesLayer
	@backgroundlineslayer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.BackgroundLinesLayer = Layer

	@indexedproperty
	def backgroundlineslinetype(self) -> str:
		"Specifies the linetype of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.BackgroundLinesLinetype
	@backgroundlineslinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.BackgroundLinesLinetype = Linetype

	@indexedproperty
	def backgroundlineslinetypescale(self) -> float:
		"Specifies the linetype scale of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.BackgroundLinesLinetypeScale
	@backgroundlineslinetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.BackgroundLinesLinetypeScale = ltScale

	@indexedproperty
	def backgroundlineslineweight(self) -> int:
		"Specifies the line weight of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.BackgroundLinesLineweight
	@backgroundlineslineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.BackgroundLinesLineweight = Lineweight

	@indexedproperty
	def backgroundlinesplotstylename(self) -> str:
		"Specifies the plot style name of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.BackgroundLinesPlotStyleName
	@backgroundlinesplotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.BackgroundLinesPlotStyleName = plotStyle

	@indexedproperty
	def backgroundlinesvisible(self) -> bool:
		"Specifies the visibility of background lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.BackgroundLinesVisible
	@backgroundlinesvisible.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.BackgroundLinesVisible = pVal

	@indexedproperty
	def curvetangencylinescolor(self) -> AcadAcCmColor:
		"Specifies the color of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.CurveTangencyLinesColor
	@curvetangencylinescolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.CurveTangencyLinesColor = pColor

	@indexedproperty
	def curvetangencylineslayer(self) -> str:
		"Specifies the layer of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.CurveTangencyLinesLayer
	@curvetangencylineslayer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.CurveTangencyLinesLayer = Layer

	@indexedproperty
	def curvetangencylineslinetype(self) -> str:
		"Specifies the linetype of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.CurveTangencyLinesLinetype
	@curvetangencylineslinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.CurveTangencyLinesLinetype = Linetype

	@indexedproperty
	def curvetangencylineslinetypescale(self) -> float:
		"Specifies the linetype scale of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.CurveTangencyLinesLinetypeScale
	@curvetangencylineslinetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.CurveTangencyLinesLinetypeScale = ltScale

	@indexedproperty
	def curvetangencylineslineweight(self) -> int:
		"Specifies the line weight of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.CurveTangencyLinesLineweight
	@curvetangencylineslineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.CurveTangencyLinesLineweight = Lineweight

	@indexedproperty
	def curvetangencylinesplotstylename(self) -> str:
		"Specifies the plot style name of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.CurveTangencyLinesPlotStyleName
	@curvetangencylinesplotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.CurveTangencyLinesPlotStyleName = plotStyle

	@indexedproperty
	def curvetangencylinesvisible(self) -> bool:
		"Specifies the visibility of curve tangency lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.CurveTangencyLinesVisible
	@curvetangencylinesvisible.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.CurveTangencyLinesVisible = pVal

	@indexedproperty
	def destinationblock(self) -> tagVARIANT:
		"Specifies the destination block for section generation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT
		return self.com_parent.DestinationBlock
	@destinationblock.setter
	def _(self, pVal:tagVARIANT):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT
		self.com_parent.DestinationBlock = pVal

	@indexedproperty
	def destinationfile(self) -> str:
		"Specifies the destination file for section generation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:str
		return self.com_parent.DestinationFile
	@destinationfile.setter
	def _(self, pVal:str):
		# ['in'] pVal:str
		self.com_parent.DestinationFile = pVal

	@indexedproperty
	def foregroundlinescolor(self) -> AcadAcCmColor:
		"Specifies the color of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.ForegroundLinesColor
	@foregroundlinescolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.ForegroundLinesColor = pColor

	@indexedproperty
	def foregroundlinesedgetransparency(self) -> int:
		"Specifies the edge transparency of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.ForegroundLinesEdgeTransparency
	@foregroundlinesedgetransparency.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.ForegroundLinesEdgeTransparency = pVal

	@indexedproperty
	def foregroundlinesfacetransparency(self) -> int:
		"Specifies the face transparency of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.ForegroundLinesFaceTransparency
	@foregroundlinesfacetransparency.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.ForegroundLinesFaceTransparency = pVal

	@indexedproperty
	def foregroundlineshiddenline(self) -> bool:
		"Specifies the hidden line visibility of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.ForegroundLinesHiddenLine
	@foregroundlineshiddenline.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.ForegroundLinesHiddenLine = pVal

	@indexedproperty
	def foregroundlineslayer(self) -> str:
		"Specifies the layer of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.ForegroundLinesLayer
	@foregroundlineslayer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.ForegroundLinesLayer = Layer

	@indexedproperty
	def foregroundlineslinetype(self) -> str:
		"Specifies the linetype of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.ForegroundLinesLinetype
	@foregroundlineslinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.ForegroundLinesLinetype = Linetype

	@indexedproperty
	def foregroundlineslinetypescale(self) -> float:
		"Specifies the linetype scale of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.ForegroundLinesLinetypeScale
	@foregroundlineslinetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.ForegroundLinesLinetypeScale = ltScale

	@indexedproperty
	def foregroundlineslineweight(self) -> int:
		"Specifies the line weight of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.ForegroundLinesLineweight
	@foregroundlineslineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.ForegroundLinesLineweight = Lineweight

	@indexedproperty
	def foregroundlinesplotstylename(self) -> str:
		"Specifies the plot style name of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.ForegroundLinesPlotStyleName
	@foregroundlinesplotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.ForegroundLinesPlotStyleName = plotStyle

	@indexedproperty
	def foregroundlinesvisible(self) -> bool:
		"Specifies the visibility of foreground lines"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.ForegroundLinesVisible
	@foregroundlinesvisible.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.ForegroundLinesVisible = pVal

	@indexedproperty
	def generationoptions(self) -> int:
		"Specifies the section generation options"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.GenerationOptions
	@generationoptions.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.GenerationOptions = pVal

	@indexedproperty
	def intersectionboundarycolor(self) -> AcadAcCmColor:
		"Specifies the color of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.IntersectionBoundaryColor
	@intersectionboundarycolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.IntersectionBoundaryColor = pColor

	@indexedproperty
	def intersectionboundarydivisionlines(self) -> bool:
		"Specifies whether division lines are shown in intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IntersectionBoundaryDivisionLines
	@intersectionboundarydivisionlines.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.IntersectionBoundaryDivisionLines = pVal

	@indexedproperty
	def intersectionboundarylayer(self) -> str:
		"Specifies the layer of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.IntersectionBoundaryLayer
	@intersectionboundarylayer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.IntersectionBoundaryLayer = Layer

	@indexedproperty
	def intersectionboundarylinetype(self) -> str:
		"Specifies the linetype of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.IntersectionBoundaryLinetype
	@intersectionboundarylinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.IntersectionBoundaryLinetype = Linetype

	@indexedproperty
	def intersectionboundarylinetypescale(self) -> float:
		"Specifies the linetype scale of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.IntersectionBoundaryLinetypeScale
	@intersectionboundarylinetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.IntersectionBoundaryLinetypeScale = ltScale

	@indexedproperty
	def intersectionboundarylineweight(self) -> int:
		"Specifies the line weight of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.IntersectionBoundaryLineweight
	@intersectionboundarylineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.IntersectionBoundaryLineweight = Lineweight

	@indexedproperty
	def intersectionboundaryplotstylename(self) -> str:
		"Specifies the plot style name of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.IntersectionBoundaryPlotStyleName
	@intersectionboundaryplotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.IntersectionBoundaryPlotStyleName = plotStyle

	@indexedproperty
	def intersectionfillcolor(self) -> AcadAcCmColor:
		"Specifies the color of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.IntersectionFillColor
	@intersectionfillcolor.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.IntersectionFillColor = pColor

	@indexedproperty
	def intersectionfillfacetransparency(self) -> int:
		"Specifies the face transparency of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.IntersectionFillFaceTransparency
	@intersectionfillfacetransparency.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.IntersectionFillFaceTransparency = pVal

	@indexedproperty
	def intersectionfillhatchangle(self) -> float:
		"Specifies the hatch angle for intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.IntersectionFillHatchAngle
	@intersectionfillhatchangle.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.IntersectionFillHatchAngle = pVal

	@indexedproperty
	def intersectionfillhatchpatternname(self) -> str:
		"Specifies the hatch pattern name for intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:str
		return self.com_parent.IntersectionFillHatchPatternName
	@intersectionfillhatchpatternname.setter
	def _(self, pVal:str):
		# ['in'] pVal:str
		self.com_parent.IntersectionFillHatchPatternName = pVal

	@indexedproperty
	def intersectionfillhatchpatterntype(self) -> int:
		"Specifies the hatch pattern type for intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.IntersectionFillHatchPatternType
	@intersectionfillhatchpatterntype.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.IntersectionFillHatchPatternType = pVal

	@indexedproperty
	def intersectionfillhatchscale(self) -> float:
		"Specifies the hatch scale for intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.IntersectionFillHatchScale
	@intersectionfillhatchscale.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.IntersectionFillHatchScale = pVal

	@indexedproperty
	def intersectionfillhatchspacing(self) -> float:
		"Specifies the hatch spacing for intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:float
		return self.com_parent.IntersectionFillHatchSpacing
	@intersectionfillhatchspacing.setter
	def _(self, pVal:float):
		# ['in'] pVal:float
		self.com_parent.IntersectionFillHatchSpacing = pVal

	@indexedproperty
	def intersectionfilllayer(self) -> str:
		"Specifies the layer of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.IntersectionFillLayer
	@intersectionfilllayer.setter
	def _(self, Layer:str):
		# ['in'] Layer:str
		self.com_parent.IntersectionFillLayer = Layer

	@indexedproperty
	def intersectionfilllinetype(self) -> str:
		"Specifies the linetype of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.IntersectionFillLinetype
	@intersectionfilllinetype.setter
	def _(self, Linetype:str):
		# ['in'] Linetype:str
		self.com_parent.IntersectionFillLinetype = Linetype

	@indexedproperty
	def intersectionfilllinetypescale(self) -> float:
		"Specifies the linetype scale of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.IntersectionFillLinetypeScale
	@intersectionfilllinetypescale.setter
	def _(self, ltScale:float):
		# ['in'] ltScale:float
		self.com_parent.IntersectionFillLinetypeScale = ltScale

	@indexedproperty
	def intersectionfilllineweight(self) -> int:
		"Specifies the line weight of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.IntersectionFillLineweight
	@intersectionfilllineweight.setter
	def _(self, Lineweight:int):
		# ['in'] Lineweight:int
		self.com_parent.IntersectionFillLineweight = Lineweight

	@indexedproperty
	def intersectionfillplotstylename(self) -> str:
		"Specifies the plot style name of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.IntersectionFillPlotStyleName
	@intersectionfillplotstylename.setter
	def _(self, plotStyle:str):
		# ['in'] plotStyle:str
		self.com_parent.IntersectionFillPlotStyleName = plotStyle

	@indexedproperty
	def intersectionfillvisible(self) -> bool:
		"Specifies the visibility of intersection fill"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IntersectionFillVisible
	@intersectionfillvisible.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.IntersectionFillVisible = pVal

	@indexedproperty
	def sourceobjects(self) -> tagVARIANT:
		"Specifies the source objects for section generation"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:tagVARIANT
		return self.com_parent.SourceObjects
	@sourceobjects.setter
	def _(self, pVal:tagVARIANT):
		# TODO: Check arguments
		# ['in'] pVal:tagVARIANT
		self.com_parent.SourceObjects = pVal


class AcadSectionTypeSettings2(POINTER(_dll.IAcadSectionTypeSettings2), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSectionTypeSettings2
	#	IAcadSectionTypeSettings
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSectionTypeSettings2 VBA-class wrapped as AcadSectionTypeSettings2 python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSectionTypeSettings2__com__get_IntersectionBoundaryVisible
	#	_IAcadSectionTypeSettings2__com__set_IntersectionBoundaryVisible
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesColor
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLayer
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_BackgroundLinesVisible
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesColor
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLayer
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_CurveTangencyLinesVisible
	#	_IAcadSectionTypeSettings__com__get_DestinationBlock
	#	_IAcadSectionTypeSettings__com__get_DestinationFile
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesColor
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesEdgeTransparency
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesFaceTransparency
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLayer
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_ForegroundLinesVisible
	#	_IAcadSectionTypeSettings__com__get_GenerationOptions
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryColor
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryDivisionLines
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLayer
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLinetype
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryLineweight
	#	_IAcadSectionTypeSettings__com__get_IntersectionBoundaryPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillColor
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillFaceTransparency
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchAngle
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchPatternName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchPatternType
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillHatchSpacing
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLayer
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLinetype
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLinetypeScale
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillLineweight
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillPlotStyleName
	#	_IAcadSectionTypeSettings__com__get_IntersectionFillVisible
	#	_IAcadSectionTypeSettings__com__get_SourceObjects
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesColor
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLayer
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_BackgroundLinesVisible
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesColor
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLayer
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_CurveTangencyLinesVisible
	#	_IAcadSectionTypeSettings__com__set_DestinationBlock
	#	_IAcadSectionTypeSettings__com__set_DestinationFile
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesColor
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesEdgeTransparency
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesFaceTransparency
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesHiddenLine
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLayer
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLinetype
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesLineweight
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_ForegroundLinesVisible
	#	_IAcadSectionTypeSettings__com__set_GenerationOptions
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryColor
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryDivisionLines
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLayer
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLinetype
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryLineweight
	#	_IAcadSectionTypeSettings__com__set_IntersectionBoundaryPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillColor
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillFaceTransparency
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchAngle
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchPatternName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchPatternType
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillHatchSpacing
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLayer
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLinetype
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLinetypeScale
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillLineweight
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillPlotStyleName
	#	_IAcadSectionTypeSettings__com__set_IntersectionFillVisible
	#	_IAcadSectionTypeSettings__com__set_SourceObjects
	# Properties
	@indexedproperty
	def intersectionboundaryvisible(self) -> bool:
		"Specifies the visibility of intersection boundary"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IntersectionBoundaryVisible
	@intersectionboundaryvisible.setter
	def _(self, pVal:bool):
		# ['in'] pVal:bool
		self.com_parent.IntersectionBoundaryVisible = pVal


class AcadSecurityParams(POINTER(_dll.IAcadSecurityParams), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSecurityParams
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSecurityParams VBA-class wrapped as AcadSecurityParams python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSecurityParams__com__get_Action
	#	_IAcadSecurityParams__com__get_Algorithm
	#	_IAcadSecurityParams__com__get_Comment
	#	_IAcadSecurityParams__com__get_Issuer
	#	_IAcadSecurityParams__com__get_KeyLength
	#	_IAcadSecurityParams__com__get_Password
	#	_IAcadSecurityParams__com__get_ProviderName
	#	_IAcadSecurityParams__com__get_ProviderType
	#	_IAcadSecurityParams__com__get_SerialNumber
	#	_IAcadSecurityParams__com__get_Subject
	#	_IAcadSecurityParams__com__get_TimeServer
	#	_IAcadSecurityParams__com__set_Action
	#	_IAcadSecurityParams__com__set_Algorithm
	#	_IAcadSecurityParams__com__set_Comment
	#	_IAcadSecurityParams__com__set_Issuer
	#	_IAcadSecurityParams__com__set_KeyLength
	#	_IAcadSecurityParams__com__set_Password
	#	_IAcadSecurityParams__com__set_ProviderName
	#	_IAcadSecurityParams__com__set_ProviderType
	#	_IAcadSecurityParams__com__set_SerialNumber
	#	_IAcadSecurityParams__com__set_Subject
	#	_IAcadSecurityParams__com__set_TimeServer
	# Properties
	@indexedproperty
	def action(self) -> int:
		"Specifies the security-related operations to be performed."
		# TODO: Check arguments
		# ['out', 'retval'] pOperations:int
		return self.com_parent.Action
	@action.setter
	def _(self, pOperations:int):
		# ['in'] pOperations:int
		self.com_parent.Action = pOperations

	@indexedproperty
	def algorithm(self) -> int:
		"Specifies the encryption algorithm identifier."
		# TODO: Check arguments
		# ['out', 'retval'] pAlgId:int
		return self.com_parent.Algorithm
	@algorithm.setter
	def _(self, pAlgId:int):
		# ['in'] pAlgId:int
		self.com_parent.Algorithm = pAlgId

	@indexedproperty
	def comment(self) -> str:
		"Specifies the comment to be included with the digital signature."
		# TODO: Check arguments
		# ['out', 'retval'] pText:str
		return self.com_parent.Comment
	@comment.setter
	def _(self, pText:str):
		# ['in'] pText:str
		self.com_parent.Comment = pText

	@indexedproperty
	def issuer(self) -> str:
		"Specifies the issuer name of the digital certificate."
		# TODO: Check arguments
		# ['out', 'retval'] pCertIssuer:str
		return self.com_parent.Issuer
	@issuer.setter
	def _(self, pCertIssuer:str):
		# ['in'] pCertIssuer:str
		self.com_parent.Issuer = pCertIssuer

	@indexedproperty
	def keylength(self) -> int:
		"Specifies the length of the encryption key."
		# TODO: Check arguments
		# ['out', 'retval'] pKeyLen:int
		return self.com_parent.KeyLength
	@keylength.setter
	def _(self, pKeyLen:int):
		# ['in'] pKeyLen:int
		self.com_parent.KeyLength = pKeyLen

	@indexedproperty
	def password(self) -> str:
		"Specifies the encryption password."
		# TODO: Check arguments
		# ['out', 'retval'] pSecret:str
		return self.com_parent.Password
	@password.setter
	def _(self, pSecret:str):
		# ['in'] pSecret:str
		self.com_parent.Password = pSecret

	@indexedproperty
	def providername(self) -> str:
		"Specifies the encryption provider name."
		# TODO: Check arguments
		# ['out', 'retval'] pProvName:str
		return self.com_parent.ProviderName
	@providername.setter
	def _(self, pProvName:str):
		# ['in'] pProvName:str
		self.com_parent.ProviderName = pProvName

	@indexedproperty
	def providertype(self) -> int:
		"Specifies the encryption provider type."
		# TODO: Check arguments
		# ['out', 'retval'] pProvType:int
		return self.com_parent.ProviderType
	@providertype.setter
	def _(self, pProvType:int):
		# ['in'] pProvType:int
		self.com_parent.ProviderType = pProvType

	@indexedproperty
	def serialnumber(self) -> str:
		"Specifies the serial number of the digital certificate."
		# TODO: Check arguments
		# ['out', 'retval'] pSerialNum:str
		return self.com_parent.SerialNumber
	@serialnumber.setter
	def _(self, pSerialNum:str):
		# ['in'] pSerialNum:str
		self.com_parent.SerialNumber = pSerialNum

	@indexedproperty
	def subject(self) -> str:
		"Specifies the subject name of the digital certificate"
		# TODO: Check arguments
		# ['out', 'retval'] pCertSubject:str
		return self.com_parent.Subject
	@subject.setter
	def _(self, pCertSubject:str):
		# ['in'] pCertSubject:str
		self.com_parent.Subject = pCertSubject

	@indexedproperty
	def timeserver(self) -> str:
		"Specifies the name of the time server to be used for the digital signature."
		# TODO: Check arguments
		# ['out', 'retval'] pTimeServerName:str
		return self.com_parent.TimeServer
	@timeserver.setter
	def _(self, pTimeServerName:str):
		# ['in'] pTimeServerName:str
		self.com_parent.TimeServer = pTimeServerName


class AcadSelectionSet(POINTER(_dll.IAcadSelectionSet), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSelectionSet
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSelectionSet VBA-class wrapped as AcadSelectionSet python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSelectionSet__com_AddItems
	#	_IAcadSelectionSet__com_Clear
	#	_IAcadSelectionSet__com_Delete
	#	_IAcadSelectionSet__com_Erase
	#	_IAcadSelectionSet__com_Highlight
	#	_IAcadSelectionSet__com_Item
	#	_IAcadSelectionSet__com_RemoveItems
	#	_IAcadSelectionSet__com_Select
	#	_IAcadSelectionSet__com_SelectAtPoint
	#	_IAcadSelectionSet__com_SelectByPolygon
	#	_IAcadSelectionSet__com_SelectOnScreen
	#	_IAcadSelectionSet__com_Update
	#	_IAcadSelectionSet__com__get_Application
	#	_IAcadSelectionSet__com__get_Count
	#	_IAcadSelectionSet__com__get_Name
	#	_IAcadSelectionSet__com__get__NewEnum
	# Methods
	def additems(self, pSelSet: tagVARIANT):
		"Adds one or more objects to the specified selection set"
		# TODO: Check arguments
		# ['in'] pSelSet:tagVARIANT
		# VBA: object.AddItems pSelSet
		self.com_parent.AddItems(pSelSet)

	def clear(self):
		"Clears the specified selection set of all items"
		# VBA: object.Clear 
		self.com_parent.Clear()

	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	def erase(self):
		"Erases all the objects in a selection set"
		# VBA: object.Erase 
		self.com_parent.Erase()

	def highlight(self, bFlag: bool):
		"Sets the highlight status for the given object, or for all objects in a given selection set"
		# ['in'] bFlag:bool
		# VBA: object.Highlight bFlag
		self.com_parent.Highlight(bFlag)

	def item(self, Index: tagVARIANT) -> AcadEntity:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pEntity:AcadEntity
		# VBA: pEntity = object.Item (Index)
		return self.com_parent.Item(Index)

	def removeitems(self, Objects: tagVARIANT):
		"Removes specified items from the group or selection set"
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.RemoveItems Objects
		self.com_parent.RemoveItems(Objects)

	def select(self, Mode: int, Point1: tagVARIANT, Point2: tagVARIANT, FilterType: tagVARIANT, FilterData: tagVARIANT):
		"Selects objects and places them into a selection set"
		# TODO: Check arguments
		# ['in'] Mode:int
		# ['in', '16'] Point1:tagVARIANT
		# ['in', '16'] Point2:tagVARIANT
		# ['in', '16'] FilterType:tagVARIANT
		# ['in', '16'] FilterData:tagVARIANT
		# VBA: object.Select Mode, Point1, Point2, FilterType, FilterData
		self.com_parent.Select(Mode, Point1, Point2, FilterType, FilterData)

	def selectatpoint(self, Point: tagVARIANT, FilterType: tagVARIANT, FilterData: tagVARIANT):
		"Selects an object passing through a given point and places it into a selection set"
		# TODO: Check arguments
		# ['in'] Point:tagVARIANT
		# ['in', '16'] FilterType:tagVARIANT
		# ['in', '16'] FilterData:tagVARIANT
		# VBA: object.SelectAtPoint Point, FilterType, FilterData
		self.com_parent.SelectAtPoint(Point, FilterType, FilterData)

	def selectbypolygon(self, Mode: int, PointsList: tagVARIANT, FilterType: tagVARIANT, FilterData: tagVARIANT):
		"Selects entities within a fence and adds them to the selection set"
		# TODO: Check arguments
		# ['in'] Mode:int
		# ['in'] PointsList:tagVARIANT
		# ['in', '16'] FilterType:tagVARIANT
		# ['in', '16'] FilterData:tagVARIANT
		# VBA: object.SelectByPolygon Mode, PointsList, FilterType, FilterData
		self.com_parent.SelectByPolygon(Mode, PointsList, FilterType, FilterData)

	def selectonscreen(self, FilterType: tagVARIANT, FilterData: tagVARIANT):
		"Prompts the user to pick an object from the screen"
		# TODO: Check arguments
		# ['in', '16'] FilterType:tagVARIANT
		# ['in', '16'] FilterData:tagVARIANT
		# VBA: object.SelectOnScreen FilterType, FilterData
		self.com_parent.SelectOnScreen(FilterType, FilterData)

	def update(self):
		"Updates the object to the drawing screen"
		# VBA: object.Update 
		self.com_parent.Update()

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name


class AcadSelectionSets(POINTER(_dll.IAcadSelectionSets), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSelectionSets
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSelectionSets VBA-class wrapped as AcadSelectionSets python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSelectionSets__com_Add
	#	_IAcadSelectionSets__com_Item
	#	_IAcadSelectionSets__com__get_Application
	#	_IAcadSelectionSets__com__get_Count
	#	_IAcadSelectionSets__com__get__NewEnum
	# Methods
	def add(self, Name: str) -> AcadSelectionSet:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pSet:AcadSelectionSet
		# VBA: pSet = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadSelectionSet:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadSelectionSet
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.Count


class AcadShadowDisplay(POINTER(_dll.IAcadShadowDisplay), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadShadowDisplay
	#	IUnknown
	#		object
	# Prototype for IAcadShadowDisplay VBA-class wrapped as AcadShadowDisplay python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadShadowDisplay__com__get_EnableShadowDisplay
	#	_IAcadShadowDisplay__com__get_ShadowDisplay
	#	_IAcadShadowDisplay__com__set_ShadowDisplay
	# Properties
	@indexedproperty
	def enableshadowdisplay(self) -> int:
		"Specifies whether the shadow display property is enabled for the object."
		# TODO: Check arguments
		# ['out', 'retval'] ShadowDisplay:int
		return self.com_parent.EnableShadowDisplay

	@indexedproperty
	def shadowdisplay(self) -> int:
		"Specifies the shadow display property of the object."
		# TODO: Check arguments
		# ['out', 'retval'] ShadowDisplay:int
		return self.com_parent.ShadowDisplay
	@shadowdisplay.setter
	def _(self, ShadowDisplay:int):
		# ['in'] ShadowDisplay:int
		self.com_parent.ShadowDisplay = ShadowDisplay


class AcadSortentsTable(POINTER(_dll.IAcadSortentsTable), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSortentsTable
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSortentsTable VBA-class wrapped as AcadSortentsTable python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadSortentsTable__com_Block
	#	_IAcadSortentsTable__com_GetFullDrawOrder
	#	_IAcadSortentsTable__com_GetRelativeDrawOrder
	#	_IAcadSortentsTable__com_MoveAbove
	#	_IAcadSortentsTable__com_MoveBelow
	#	_IAcadSortentsTable__com_MoveToBottom
	#	_IAcadSortentsTable__com_MoveToTop
	#	_IAcadSortentsTable__com_SetRelativeDrawOrder
	#	_IAcadSortentsTable__com_SwapOrder
	# Methods
	def block(self) -> AcadBlock:
		"Returns the Block this Sortents Table belongs to."
		# TODO: Check arguments
		# ['out', 'retval'] pBlock:AcadBlock
		# VBA: pBlock = object.Block ()
		return self.com_parent.Block()

	def getfulldraworder(self, honorSortentsSysvar: bool) -> tagVARIANT:
		"Returns all objects in the block, sorted by draw order, bottommost first."
		# TODO: Check arguments
		# ['out'] Objects:tagVARIANT
		# ['in'] honorSortentsSysvar:bool
		# VBA: object.GetFullDrawOrder Objects, honorSortentsSysvar
		return self.com_parent.GetFullDrawOrder(honorSortentsSysvar)

	def getrelativedraworder(self, honorSortentsSysvar: bool) -> tagVARIANT:
		"Returns specified objects, sorted by draw order, bottommost first."
		# TODO: Check arguments
		# ['out'] Objects:tagVARIANT
		# ['in'] honorSortentsSysvar:bool
		# VBA: object.GetRelativeDrawOrder Objects, honorSortentsSysvar
		return self.com_parent.GetRelativeDrawOrder(honorSortentsSysvar)

	def moveabove(self, Objects: tagVARIANT, Target: AcadEntity):
		"Moves objects above target in draw order."
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# ['in'] Target:AcadEntity
		# VBA: object.MoveAbove Objects, Target
		self.com_parent.MoveAbove(Objects, Target)

	def movebelow(self, Objects: tagVARIANT, Target: AcadEntity):
		"Moves objects below target in draw order."
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# ['in'] Target:AcadEntity
		# VBA: object.MoveBelow Objects, Target
		self.com_parent.MoveBelow(Objects, Target)

	def movetobottom(self, Objects: tagVARIANT):
		"Moves objects to bottom of draw order."
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.MoveToBottom Objects
		self.com_parent.MoveToBottom(Objects)

	def movetotop(self, Objects: tagVARIANT):
		"Moves objects to top of draw order."
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.MoveToTop Objects
		self.com_parent.MoveToTop(Objects)

	def setrelativedraworder(self, Objects: tagVARIANT):
		"Sets the relative draw order of the objects to the order specifed, bottommost first."
		# TODO: Check arguments
		# ['in'] Objects:tagVARIANT
		# VBA: object.SetRelativeDrawOrder Objects
		self.com_parent.SetRelativeDrawOrder(Objects)

	def swaporder(self, Object1: AcadEntity, Object2: AcadEntity):
		"Swaps draw order position for two objects."
		# TODO: Check arguments
		# ['in'] Object1:AcadEntity
		# ['in'] Object2:AcadEntity
		# VBA: object.SwapOrder Object1, Object2
		self.com_parent.SwapOrder(Object1, Object2)


class AcadState(POINTER(_dll.IAcadState), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadState
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadState VBA-class wrapped as AcadState python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadState__com__get_Application
	#	_IAcadState__com__get_IsQuiescent
	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def isquiescent(self) -> bool:
		"Specifies if AutoCAD is idle and accepting out of process Automation requests."
		# TODO: Check arguments
		# ['out', 'retval'] pVal:bool
		return self.com_parent.IsQuiescent


class AcadSubDMeshEdge(POINTER(_dll.IAcadSubDMeshEdge), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSubDMeshEdge
	#	IAcadSubEntity
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSubDMeshEdge VBA-class wrapped as AcadSubDMeshEdge python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSubDMeshEdge__com__get_CreaseLevel
	#	_IAcadSubDMeshEdge__com__get_CreaseType
	#	_IAcadSubDMeshEdge__com__set_CreaseLevel
	#	_IAcadSubDMeshEdge__com__set_CreaseType
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Properties
	@indexedproperty
	def creaselevel(self) -> float:
		"Specifies crease level at which the crease starts losing its effect"
		# TODO: Check arguments
		# ['out', 'retval'] level:float
		return self.com_parent.CreaseLevel
	@creaselevel.setter
	def _(self, level:float):
		# ['in'] level:float
		self.com_parent.CreaseLevel = level

	@indexedproperty
	def creasetype(self) -> int:
		"Specifies if a crease is applied"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.CreaseType
	@creasetype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CreaseType = Type


class AcadSubDMeshFace(POINTER(_dll.IAcadSubDMeshFace), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSubDMeshFace
	#	IAcadSubEntity
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSubDMeshFace VBA-class wrapped as AcadSubDMeshFace python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSubDMeshFace__com__get_CreaseLevel
	#	_IAcadSubDMeshFace__com__get_CreaseType
	#	_IAcadSubDMeshFace__com__get_Material
	#	_IAcadSubDMeshFace__com__set_CreaseLevel
	#	_IAcadSubDMeshFace__com__set_CreaseType
	#	_IAcadSubDMeshFace__com__set_Material
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Properties
	@indexedproperty
	def creaselevel(self) -> float:
		"Specifies crease level at which the crease starts losing its effect"
		# TODO: Check arguments
		# ['out', 'retval'] level:float
		return self.com_parent.CreaseLevel
	@creaselevel.setter
	def _(self, level:float):
		# ['in'] level:float
		self.com_parent.CreaseLevel = level

	@indexedproperty
	def creasetype(self) -> int:
		"Specifies if a crease is applied"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.CreaseType
	@creasetype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CreaseType = Type

	@indexedproperty
	def material(self) -> str:
		"Specifies the material style of the selected object"
		# TODO: Check arguments
		# ['out', 'retval'] Material:str
		return self.com_parent.Material
	@material.setter
	def _(self, Material:str):
		# ['in'] Material:str
		self.com_parent.Material = Material


class AcadSubDMeshVertex(POINTER(_dll.IAcadSubDMeshVertex), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSubDMeshVertex
	#	IAcadSubEntity
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSubDMeshVertex VBA-class wrapped as AcadSubDMeshVertex python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSubDMeshVertex__com__get_Coordinates
	#	_IAcadSubDMeshVertex__com__get_CreaseLevel
	#	_IAcadSubDMeshVertex__com__get_CreaseType
	#	_IAcadSubDMeshVertex__com__set_Coordinates
	#	_IAcadSubDMeshVertex__com__set_CreaseLevel
	#	_IAcadSubDMeshVertex__com__set_CreaseType
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Properties
	@indexedproperty
	def coordinates(self) -> tagVARIANT:
		"Specifies the coordinate"
		# TODO: Check arguments
		# ['out', 'retval'] coord:tagVARIANT
		return self.com_parent.Coordinates
	@coordinates.setter
	def _(self, coord:tagVARIANT):
		# TODO: Check arguments
		# ['in'] coord:tagVARIANT
		self.com_parent.Coordinates = coord

	@indexedproperty
	def creaselevel(self) -> float:
		"Specifies crease level at which the crease starts losing its effect"
		# TODO: Check arguments
		# ['out', 'retval'] level:float
		return self.com_parent.CreaseLevel
	@creaselevel.setter
	def _(self, level:float):
		# ['in'] level:float
		self.com_parent.CreaseLevel = level

	@indexedproperty
	def creasetype(self) -> int:
		"Specifies if a crease is applied"
		# TODO: Check arguments
		# ['out', 'retval'] Type:int
		return self.com_parent.CreaseType
	@creasetype.setter
	def _(self, Type:int):
		# ['in'] Type:int
		self.com_parent.CreaseType = Type


class AcadSubEntSolidFace(POINTER(_dll.IAcadSubEntSolidFace), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSubEntSolidFace
	#	IAcadSubEntity
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadSubEntSolidFace VBA-class wrapped as AcadSubEntSolidFace python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSubEntSolidFace__com__get_Material
	#	_IAcadSubEntSolidFace__com__set_Material
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Properties
	@indexedproperty
	def material(self) -> str:
		"Specifies the material"
		# TODO: Check arguments
		# ['out', 'retval'] Material:str
		return self.com_parent.Material
	@material.setter
	def _(self, Material:str):
		# ['in'] Material:str
		self.com_parent.Material = Material


class AcadSubEntity(POINTER(_dll.IAcadSubEntity), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSubEntity
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSubEntity VBA-class wrapped as AcadSubEntity python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSubEntity__com_OnModified
	#	_IAcadSubEntity__com__get_Hyperlinks
	#	_IAcadSubEntity__com__get_Layer
	#	_IAcadSubEntity__com__get_Linetype
	#	_IAcadSubEntity__com__get_LinetypeScale
	#	_IAcadSubEntity__com__get_Lineweight
	#	_IAcadSubEntity__com__get_ObjectName
	#	_IAcadSubEntity__com__get_PlotStyleName
	#	_IAcadSubEntity__com__get_color
	#	_IAcadSubEntity__com__set_color
	# Methods
	def onmodified(self):
		"None"
		# VBA: object.OnModified 
		self.com_parent.OnModified()

	# Properties
	@indexedproperty
	def color(self) -> AcadAcCmColor:
		"Returns the true color of the object."
		# TODO: Check arguments
		# ['out', 'retval'] pColor:AcadAcCmColor
		return self.com_parent.color
	@color.setter
	def _(self, pColor:AcadAcCmColor):
		# TODO: Check arguments
		# ['in'] pColor:AcadAcCmColor
		self.com_parent.color = pColor

	@indexedproperty
	def hyperlinks(self) -> AcadHyperlinks:
		"Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)"
		# TODO: Check arguments
		# ['out', 'retval'] Hyperlinks:AcadHyperlinks
		return self.com_parent.Hyperlinks

	@indexedproperty
	def layer(self) -> str:
		"Specifies the current layer of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Layer:str
		return self.com_parent.Layer

	@indexedproperty
	def linetype(self) -> str:
		"Specifies the current linetype of the object"
		# TODO: Check arguments
		# ['out', 'retval'] Linetype:str
		return self.com_parent.Linetype

	@indexedproperty
	def linetypescale(self) -> float:
		"Specifies the linetype scale factor of the object"
		# TODO: Check arguments
		# ['out', 'retval'] ltScale:float
		return self.com_parent.LinetypeScale

	@indexedproperty
	def lineweight(self) -> int:
		"Specifies the lineweight for the object"
		# TODO: Check arguments
		# ['out', 'retval'] Lineweight:int
		return self.com_parent.Lineweight

	@indexedproperty
	def objectname(self) -> str:
		"Gets the AutoCAD class name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] ObjectName:str
		return self.com_parent.ObjectName

	@indexedproperty
	def plotstylename(self) -> str:
		"Specifies the plotstyle name for the object"
		# TODO: Check arguments
		# ['out', 'retval'] plotStyle:str
		return self.com_parent.PlotStyleName


class AcadSummaryInfo(POINTER(_dll.IAcadSummaryInfo), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadSummaryInfo
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadSummaryInfo VBA-class wrapped as AcadSummaryInfo python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadSummaryInfo__com_AddCustomInfo
	#	_IAcadSummaryInfo__com_GetCustomByIndex
	#	_IAcadSummaryInfo__com_GetCustomByKey
	#	_IAcadSummaryInfo__com_NumCustomInfo
	#	_IAcadSummaryInfo__com_RemoveCustomByIndex
	#	_IAcadSummaryInfo__com_RemoveCustomByKey
	#	_IAcadSummaryInfo__com_SetCustomByIndex
	#	_IAcadSummaryInfo__com_SetCustomByKey
	#	_IAcadSummaryInfo__com__get_Author
	#	_IAcadSummaryInfo__com__get_Comments
	#	_IAcadSummaryInfo__com__get_HyperlinkBase
	#	_IAcadSummaryInfo__com__get_Keywords
	#	_IAcadSummaryInfo__com__get_LastSavedBy
	#	_IAcadSummaryInfo__com__get_RevisionNumber
	#	_IAcadSummaryInfo__com__get_Subject
	#	_IAcadSummaryInfo__com__get_Title
	#	_IAcadSummaryInfo__com__set_Author
	#	_IAcadSummaryInfo__com__set_Comments
	#	_IAcadSummaryInfo__com__set_HyperlinkBase
	#	_IAcadSummaryInfo__com__set_Keywords
	#	_IAcadSummaryInfo__com__set_LastSavedBy
	#	_IAcadSummaryInfo__com__set_RevisionNumber
	#	_IAcadSummaryInfo__com__set_Subject
	#	_IAcadSummaryInfo__com__set_Title
	# Methods
	def addcustominfo(self, key: str, Value: str):
		"Adds a new custom field at the end of the existing list of custom fields."
		# ['in'] key:str
		# ['in'] Value:str
		# VBA: object.AddCustomInfo key, Value
		self.com_parent.AddCustomInfo(key, Value)

	def getcustombyindex(self, Index: int):
		"Gets the key and value of the custom field specified its index."
		# TODO: Check arguments
		# ['in'] Index:int
		# ['out'] pKey:str
		# ['out'] pValue:str
		# VBA: object.GetCustomByIndex Index, pKey, pValue
		return self.com_parent.GetCustomByIndex(Index)

	def getcustombykey(self, key: str) -> str:
		"Returns the number of custom information fields that have been set."
		# TODO: Check arguments
		# ['in'] key:str
		# ['out'] pValue:str
		# VBA: object.GetCustomByKey key, pValue
		return self.com_parent.GetCustomByKey(key)

	def numcustominfo(self) -> int:
		"Returns the number of custom information fields that have been set."
		# TODO: Check arguments
		# ['out', 'retval'] Index:int
		# VBA: Index = object.NumCustomInfo ()
		return self.com_parent.NumCustomInfo()

	def removecustombyindex(self, Index: int):
		"Removes a custom field (key and value) indicated by the index. Note, index range is from one to the number of custom fields."
		# ['in'] Index:int
		# VBA: object.RemoveCustomByIndex Index
		self.com_parent.RemoveCustomByIndex(Index)

	def removecustombykey(self, key: str):
		"Removes a custom field (key and value) indicated by the key."
		# ['in'] key:str
		# VBA: object.RemoveCustomByKey key
		self.com_parent.RemoveCustomByKey(key)

	def setcustombyindex(self, Index: int, key: str, Value: str):
		"Sets set the key and value of the custom field specified by the index. Note, index range is from one to the number of custom fields."
		# ['in'] Index:int
		# ['in'] key:str
		# ['in'] Value:str
		# VBA: object.SetCustomByIndex Index, key, Value
		self.com_parent.SetCustomByIndex(Index, key, Value)

	def setcustombykey(self, key: str, Value: str):
		"Sets set the value of the custom field specified by the key."
		# ['in'] key:str
		# ['in'] Value:str
		# VBA: object.SetCustomByKey key, Value
		self.com_parent.SetCustomByKey(key, Value)

	# Properties
	@indexedproperty
	def author(self) -> str:
		"Returns the value of the author field."
		# TODO: Check arguments
		# ['out', 'retval'] pAuthor:str
		return self.com_parent.Author
	@author.setter
	def _(self, pAuthor:str):
		# ['in'] pAuthor:str
		self.com_parent.Author = pAuthor

	@indexedproperty
	def comments(self) -> str:
		"Returns the value of the comments field."
		# TODO: Check arguments
		# ['out', 'retval'] pComments:str
		return self.com_parent.Comments
	@comments.setter
	def _(self, pComments:str):
		# ['in'] pComments:str
		self.com_parent.Comments = pComments

	@indexedproperty
	def hyperlinkbase(self) -> str:
		"Returns the value of the hyperlink base path field."
		# TODO: Check arguments
		# ['out', 'retval'] pHyperlinkBase:str
		return self.com_parent.HyperlinkBase
	@hyperlinkbase.setter
	def _(self, pHyperlinkBase:str):
		# ['in'] pHyperlinkBase:str
		self.com_parent.HyperlinkBase = pHyperlinkBase

	@indexedproperty
	def keywords(self) -> str:
		"Returns the value of the keywords field."
		# TODO: Check arguments
		# ['out', 'retval'] pKeywords:str
		return self.com_parent.Keywords
	@keywords.setter
	def _(self, pKeywords:str):
		# ['in'] pKeywords:str
		self.com_parent.Keywords = pKeywords

	@indexedproperty
	def lastsavedby(self) -> str:
		"Returns the login name of the user to last save this database by using the LOGINNAME sysvar, or NULL if it has not been set."
		# TODO: Check arguments
		# ['out', 'retval'] pLastSavedBy:str
		return self.com_parent.LastSavedBy
	@lastsavedby.setter
	def _(self, pLastSavedBy:str):
		# ['in'] pLastSavedBy:str
		self.com_parent.LastSavedBy = pLastSavedBy

	@indexedproperty
	def revisionnumber(self) -> str:
		"Returns the value of the revision number field, which is a string."
		# TODO: Check arguments
		# ['out', 'retval'] pRevisionNumber:str
		return self.com_parent.RevisionNumber
	@revisionnumber.setter
	def _(self, pRevisionNumber:str):
		# ['in'] pRevisionNumber:str
		self.com_parent.RevisionNumber = pRevisionNumber

	@indexedproperty
	def subject(self) -> str:
		"Returns the value of the subject field."
		# TODO: Check arguments
		# ['out', 'retval'] pSubject:str
		return self.com_parent.Subject
	@subject.setter
	def _(self, pSubject:str):
		# ['in'] pSubject:str
		self.com_parent.Subject = pSubject

	@indexedproperty
	def title(self) -> str:
		"Returns the value of the title field."
		# TODO: Check arguments
		# ['out', 'retval'] pTitle:str
		return self.com_parent.Title
	@title.setter
	def _(self, pTitle:str):
		# ['in'] pTitle:str
		self.com_parent.Title = pTitle


class AcadTableStyle(POINTER(_dll.IAcadTableStyle), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadTableStyle
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadTableStyle VBA-class wrapped as AcadTableStyle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadTableStyle__com_CreateCellStyle
	#	_IAcadTableStyle__com_CreateCellStyleFromStyle
	#	_IAcadTableStyle__com_DeleteCellStyle
	#	_IAcadTableStyle__com_EnableMergeAll
	#	_IAcadTableStyle__com_GetAlignment
	#	_IAcadTableStyle__com_GetAlignment2
	#	_IAcadTableStyle__com_GetBackgroundColor
	#	_IAcadTableStyle__com_GetBackgroundColor2
	#	_IAcadTableStyle__com_GetBackgroundColorNone
	#	_IAcadTableStyle__com_GetCellClass
	#	_IAcadTableStyle__com_GetCellStyles
	#	_IAcadTableStyle__com_GetColor
	#	_IAcadTableStyle__com_GetColor2
	#	_IAcadTableStyle__com_GetDataType
	#	_IAcadTableStyle__com_GetDataType2
	#	_IAcadTableStyle__com_GetFormat
	#	_IAcadTableStyle__com_GetFormat2
	#	_IAcadTableStyle__com_GetGridColor
	#	_IAcadTableStyle__com_GetGridColor2
	#	_IAcadTableStyle__com_GetGridLineWeight
	#	_IAcadTableStyle__com_GetGridLineWeight2
	#	_IAcadTableStyle__com_GetGridVisibility
	#	_IAcadTableStyle__com_GetGridVisibility2
	#	_IAcadTableStyle__com_GetIsCellStyleInUse
	#	_IAcadTableStyle__com_GetIsMergeAllEnabled
	#	_IAcadTableStyle__com_GetRotation
	#	_IAcadTableStyle__com_GetTextHeight
	#	_IAcadTableStyle__com_GetTextHeight2
	#	_IAcadTableStyle__com_GetTextStyle
	#	_IAcadTableStyle__com_GetTextStyleId
	#	_IAcadTableStyle__com_GetUniqueCellStyleName
	#	_IAcadTableStyle__com_RenameCellStyle
	#	_IAcadTableStyle__com_SetAlignment
	#	_IAcadTableStyle__com_SetAlignment2
	#	_IAcadTableStyle__com_SetBackgroundColor
	#	_IAcadTableStyle__com_SetBackgroundColor2
	#	_IAcadTableStyle__com_SetBackgroundColorNone
	#	_IAcadTableStyle__com_SetCellClass
	#	_IAcadTableStyle__com_SetColor
	#	_IAcadTableStyle__com_SetColor2
	#	_IAcadTableStyle__com_SetDataType
	#	_IAcadTableStyle__com_SetDataType2
	#	_IAcadTableStyle__com_SetFormat
	#	_IAcadTableStyle__com_SetFormat2
	#	_IAcadTableStyle__com_SetGridColor
	#	_IAcadTableStyle__com_SetGridColor2
	#	_IAcadTableStyle__com_SetGridLineWeight
	#	_IAcadTableStyle__com_SetGridLineWeight2
	#	_IAcadTableStyle__com_SetGridVisibility
	#	_IAcadTableStyle__com_SetGridVisibility2
	#	_IAcadTableStyle__com_SetRotation
	#	_IAcadTableStyle__com_SetTemplateId
	#	_IAcadTableStyle__com_SetTextHeight
	#	_IAcadTableStyle__com_SetTextHeight2
	#	_IAcadTableStyle__com_SetTextStyle
	#	_IAcadTableStyle__com_SetTextStyleId
	#	_IAcadTableStyle__com__get_BitFlags
	#	_IAcadTableStyle__com__get_Description
	#	_IAcadTableStyle__com__get_FlowDirection
	#	_IAcadTableStyle__com__get_HeaderSuppressed
	#	_IAcadTableStyle__com__get_HorzCellMargin
	#	_IAcadTableStyle__com__get_Name
	#	_IAcadTableStyle__com__get_NumCellStyles
	#	_IAcadTableStyle__com__get_TemplateId
	#	_IAcadTableStyle__com__get_TitleSuppressed
	#	_IAcadTableStyle__com__get_VertCellMargin
	#	_IAcadTableStyle__com__set_BitFlags
	#	_IAcadTableStyle__com__set_Description
	#	_IAcadTableStyle__com__set_FlowDirection
	#	_IAcadTableStyle__com__set_HeaderSuppressed
	#	_IAcadTableStyle__com__set_HorzCellMargin
	#	_IAcadTableStyle__com__set_Name
	#	_IAcadTableStyle__com__set_TemplateId
	#	_IAcadTableStyle__com__set_TitleSuppressed
	#	_IAcadTableStyle__com__set_VertCellMargin
	# Methods
	def createcellstyle(self, bstrCellStyle: str):
		"None"
		# ['in'] bstrCellStyle:str
		# VBA: object.CreateCellStyle bstrCellStyle
		self.com_parent.CreateCellStyle(bstrCellStyle)

	def createcellstylefromstyle(self, bstrCellStyle: str, bstrSourceCellStyle: str):
		"None"
		# ['in'] bstrCellStyle:str
		# ['in'] bstrSourceCellStyle:str
		# VBA: object.CreateCellStyleFromStyle bstrCellStyle, bstrSourceCellStyle
		self.com_parent.CreateCellStyleFromStyle(bstrCellStyle, bstrSourceCellStyle)

	def deletecellstyle(self, bstrCellStyle: str):
		"None"
		# ['in'] bstrCellStyle:str
		# VBA: object.DeleteCellStyle bstrCellStyle
		self.com_parent.DeleteCellStyle(bstrCellStyle)

	def enablemergeall(self, bstrCellStyle: str, bEnable: bool):
		"None"
		# ['in'] bstrCellStyle:str
		# ['in'] bEnable:bool
		# VBA: object.EnableMergeAll bstrCellStyle, bEnable
		self.com_parent.EnableMergeAll(bstrCellStyle, bEnable)

	def getalignment(self, rowType: int) -> int:
		"Returns the cell alignment for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pCellAlignment:int
		# VBA: pCellAlignment = object.GetAlignment (rowType)
		return self.com_parent.GetAlignment(rowType)

	def getalignment2(self, bstrCellStyle: str) -> int:
		"Returns the cell alignment for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] pCellAlignment:int
		# VBA: pCellAlignment = object.GetAlignment2 (bstrCellStyle)
		return self.com_parent.GetAlignment2(bstrCellStyle)

	def getbackgroundcolor(self, rowType: int) -> AcadAcCmColor:
		"Returns the background true color value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetBackgroundColor (rowType)
		return self.com_parent.GetBackgroundColor(rowType)

	def getbackgroundcolor2(self, bstrCellStyle: str) -> AcadAcCmColor:
		"Returns the background true color value for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] color:AcadAcCmColor
		# VBA: color = object.GetBackgroundColor2 (bstrCellStyle)
		return self.com_parent.GetBackgroundColor2(bstrCellStyle)

	def getbackgroundcolornone(self, rowType: int) -> bool:
		"Returns the backgroundColorNone flag value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetBackgroundColorNone (rowType)
		return self.com_parent.GetBackgroundColorNone(rowType)

	def getcellclass(self, bstrCellStyle: str) -> int:
		"None"
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] cellClass:int
		# VBA: cellClass = object.GetCellClass (bstrCellStyle)
		return self.com_parent.GetCellClass(bstrCellStyle)

	def getcellstyles(self, cellStylesArray: tagVARIANT):
		"None"
		# TODO: Check arguments
		# ['in'] cellStylesArray:tagVARIANT
		# VBA: object.GetCellStyles cellStylesArray
		self.com_parent.GetCellStyles(cellStylesArray)

	def getcolor(self, rowType: int) -> AcadAcCmColor:
		"Returns the true color value for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetColor (rowType)
		return self.com_parent.GetColor(rowType)

	def getcolor2(self, bstrCellStyle: str) -> AcadAcCmColor:
		"Returns the true color value for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] color:AcadAcCmColor
		# VBA: color = object.GetColor2 (bstrCellStyle)
		return self.com_parent.GetColor2(bstrCellStyle)

	def getdatatype(self, rowType: int):
		"Returns the data type and unit type for the specifed row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out'] pDataType:int
		# ['out'] pUnitType:int
		# VBA: object.GetDataType rowType, pDataType, pUnitType
		return self.com_parent.GetDataType(rowType)

	def getdatatype2(self, bstrCellStyle: str):
		"Returns the data type and unit type for the specifed cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out'] pDataType:int
		# ['out'] pUnitType:int
		# VBA: object.GetDataType2 bstrCellStyle, pDataType, pUnitType
		return self.com_parent.GetDataType2(bstrCellStyle)

	def getformat(self, rowType: int) -> str:
		"Returns the format for the specifed row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pVal:str
		# VBA: pVal = object.GetFormat (rowType)
		return self.com_parent.GetFormat(rowType)

	def getformat2(self, bstrCellStyle: str) -> str:
		"Returns the format for the specifed cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out'] pbstrFormat:str
		# VBA: object.GetFormat2 bstrCellStyle, pbstrFormat
		return self.com_parent.GetFormat2(bstrCellStyle)

	def getgridcolor(self, gridLineType: int, rowType: int) -> AcadAcCmColor:
		"Returns the gridColor value for the specifed gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int
		# ['in'] rowType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetGridColor (gridLineType, rowType)
		return self.com_parent.GetGridColor(gridLineType, rowType)

	def getgridcolor2(self, bstrCellStyle: str, gridLineType: int) -> AcadAcCmColor:
		"Returns the gridColor value for the specified gridLineType and cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineType:int
		# ['out', 'retval'] pColor:AcadAcCmColor
		# VBA: pColor = object.GetGridColor2 (bstrCellStyle, gridLineType)
		return self.com_parent.GetGridColor2(bstrCellStyle, gridLineType)

	def getgridlineweight(self, gridLineType: int, rowType: int) -> int:
		"Returns the gridLineWeight value for the specifed gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int
		# ['in'] rowType:int
		# ['out', 'retval'] Lineweight:int
		# VBA: Lineweight = object.GetGridLineWeight (gridLineType, rowType)
		return self.com_parent.GetGridLineWeight(gridLineType, rowType)

	def getgridlineweight2(self, bstrCellStyle: str, gridLineType: int) -> int:
		"Gets the gridLineWeight value for the specified gridLineType(s) and cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineType:int
		# ['out', 'retval'] Lineweight:int
		# VBA: Lineweight = object.GetGridLineWeight2 (bstrCellStyle, gridLineType)
		return self.com_parent.GetGridLineWeight2(bstrCellStyle, gridLineType)

	def getgridvisibility(self, gridLineType: int, rowType: int) -> bool:
		"Returns the gridVisibility value for the specifed gridLineType and row type."
		# TODO: Check arguments
		# ['in'] gridLineType:int
		# ['in'] rowType:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetGridVisibility (gridLineType, rowType)
		return self.com_parent.GetGridVisibility(gridLineType, rowType)

	def getgridvisibility2(self, bstrCellStyle: str, gridLineType: int) -> bool:
		"Returns the gridVisibility value for the specified gridLineType and cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineType:int
		# ['out', 'retval'] bValue:bool
		# VBA: bValue = object.GetGridVisibility2 (bstrCellStyle, gridLineType)
		return self.com_parent.GetGridVisibility2(bstrCellStyle, gridLineType)

	def getiscellstyleinuse(self, pszCellStyle: str) -> bool:
		"None"
		# TODO: Check arguments
		# ['in'] pszCellStyle:str
		# ['out', 'retval'] pVal:bool
		# VBA: pVal = object.GetIsCellStyleInUse (pszCellStyle)
		return self.com_parent.GetIsCellStyleInUse(pszCellStyle)

	def getismergeallenabled(self, bstrCellStyle: str) -> bool:
		"None"
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] bEnable:bool
		# VBA: bEnable = object.GetIsMergeAllEnabled (bstrCellStyle)
		return self.com_parent.GetIsMergeAllEnabled(bstrCellStyle)

	def getrotation(self, bstrCellStyle: str) -> float:
		"None"
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] Rotation:float
		# VBA: Rotation = object.GetRotation (bstrCellStyle)
		return self.com_parent.GetRotation(bstrCellStyle)

	def gettextheight(self, rowType: int) -> float:
		"Returns the text height for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] pTextHeight:float
		# VBA: pTextHeight = object.GetTextHeight (rowType)
		return self.com_parent.GetTextHeight(rowType)

	def gettextheight2(self, bstrCellStyle: str) -> float:
		"Returns the text height for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] pHeight:float
		# VBA: pHeight = object.GetTextHeight2 (bstrCellStyle)
		return self.com_parent.GetTextHeight2(bstrCellStyle)

	def gettextstyle(self, rowType: int) -> str:
		"Returns the text style name for the specified row type."
		# TODO: Check arguments
		# ['in'] rowType:int
		# ['out', 'retval'] bstrName:str
		# VBA: bstrName = object.GetTextStyle (rowType)
		return self.com_parent.GetTextStyle(rowType)

	def gettextstyleid(self, bstrCellStyle: str) -> int:
		"Returns the text style name for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['out', 'retval'] pVal:int
		# VBA: pVal = object.GetTextStyleId (bstrCellStyle)
		return self.com_parent.GetTextStyleId(bstrCellStyle)

	def getuniquecellstylename(self, pszBaseName: str) -> str:
		"None"
		# TODO: Check arguments
		# ['in'] pszBaseName:str
		# ['out', 'retval'] pbstrUniqueName:str
		# VBA: pbstrUniqueName = object.GetUniqueCellStyleName (pszBaseName)
		return self.com_parent.GetUniqueCellStyleName(pszBaseName)

	def renamecellstyle(self, bstrOldName: str, bstrNewName: str):
		"None"
		# ['in'] bstrOldName:str
		# ['in'] bstrNewName:str
		# VBA: object.RenameCellStyle bstrOldName, bstrNewName
		self.com_parent.RenameCellStyle(bstrOldName, bstrNewName)

	def setalignment(self, rowTypes: int, cellAlignment: int):
		"Sets the cell alignment for the specified row types."
		# ['in'] rowTypes:int
		# ['in'] cellAlignment:int
		# VBA: object.SetAlignment rowTypes, cellAlignment
		self.com_parent.SetAlignment(rowTypes, cellAlignment)

	def setalignment2(self, bstrCellStyle: str, cellAlignment: int):
		"Sets the cell alignment for the specified cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] cellAlignment:int
		# VBA: object.SetAlignment2 bstrCellStyle, cellAlignment
		self.com_parent.SetAlignment2(bstrCellStyle, cellAlignment)

	def setbackgroundcolor(self, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the background true color value for the specifed row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetBackgroundColor rowTypes, pColor
		self.com_parent.SetBackgroundColor(rowTypes, pColor)

	def setbackgroundcolor2(self, bstrCellStyle: str, color: AcadAcCmColor):
		"Sets the background true color value for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] color:AcadAcCmColor
		# VBA: object.SetBackgroundColor2 bstrCellStyle, color
		self.com_parent.SetBackgroundColor2(bstrCellStyle, color)

	def setbackgroundcolornone(self, rowTypes: int, bValue: bool):
		"Sets the backgroundColorNone flag value for the specified row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int
		# ['in'] bValue:bool
		# VBA: object.SetBackgroundColorNone rowTypes, bValue
		self.com_parent.SetBackgroundColorNone(rowTypes, bValue)

	def setcellclass(self, bstrCellStyle: str, cellClass: int):
		"None"
		# ['in'] bstrCellStyle:str
		# ['in'] cellClass:int
		# VBA: object.SetCellClass bstrCellStyle, cellClass
		self.com_parent.SetCellClass(bstrCellStyle, cellClass)

	def setcolor(self, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the true color value for the specifed row types."
		# TODO: Check arguments
		# ['in'] rowTypes:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetColor rowTypes, pColor
		self.com_parent.SetColor(rowTypes, pColor)

	def setcolor2(self, bstrCellStyle: str, color: AcadAcCmColor):
		"Sets the true color value for the specified cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] color:AcadAcCmColor
		# VBA: object.SetColor2 bstrCellStyle, color
		self.com_parent.SetColor2(bstrCellStyle, color)

	def setdatatype(self, rowTypes: int, nDataType: int, nUnitType: int):
		"Sets the data type and unit type for the specifed row type."
		# ['in'] rowTypes:int
		# ['in'] nDataType:int
		# ['in'] nUnitType:int
		# VBA: object.SetDataType rowTypes, nDataType, nUnitType
		self.com_parent.SetDataType(rowTypes, nDataType, nUnitType)

	def setdatatype2(self, bstrCellStyle: str, nDataType: int, nUnitType: int):
		"Sets the data type and unit type for the specifed cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] nDataType:int
		# ['in'] nUnitType:int
		# VBA: object.SetDataType2 bstrCellStyle, nDataType, nUnitType
		self.com_parent.SetDataType2(bstrCellStyle, nDataType, nUnitType)

	def setformat(self, rowTypes: int, val: str):
		"Sets the format for the specifed row type."
		# ['in'] rowTypes:int
		# ['in'] val:str
		# VBA: object.SetFormat rowTypes, val
		self.com_parent.SetFormat(rowTypes, val)

	def setformat2(self, bstrCellStyle: str, bstrFormat: str):
		"Sets the format for the specifed cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] bstrFormat:str
		# VBA: object.SetFormat2 bstrCellStyle, bstrFormat
		self.com_parent.SetFormat2(bstrCellStyle, bstrFormat)

	def setgridcolor(self, gridLineTypes: int, rowTypes: int, pColor: AcadAcCmColor):
		"Sets the gridColor value for the specifed gridLineTypes and row types."
		# TODO: Check arguments
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetGridColor gridLineTypes, rowTypes, pColor
		self.com_parent.SetGridColor(gridLineTypes, rowTypes, pColor)

	def setgridcolor2(self, bstrCellStyle: str, gridLineTypes: int, pColor: AcadAcCmColor):
		"Sets the gridColor value for the specified gridLineType and cellStyle."
		# TODO: Check arguments
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineTypes:int
		# ['in'] pColor:AcadAcCmColor
		# VBA: object.SetGridColor2 bstrCellStyle, gridLineTypes, pColor
		self.com_parent.SetGridColor2(bstrCellStyle, gridLineTypes, pColor)

	def setgridlineweight(self, gridLineTypes: int, rowTypes: int, Lineweight: int):
		"Sets the gridLineWeight value for the specifed gridLineTypes and row types."
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] Lineweight:int
		# VBA: object.SetGridLineWeight gridLineTypes, rowTypes, Lineweight
		self.com_parent.SetGridLineWeight(gridLineTypes, rowTypes, Lineweight)

	def setgridlineweight2(self, bstrCellStyle: str, gridLineTypes: int, Lineweight: int):
		"Sets the gridLineWeight value for the specified gridLineType(s) and cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineTypes:int
		# ['in'] Lineweight:int
		# VBA: object.SetGridLineWeight2 bstrCellStyle, gridLineTypes, Lineweight
		self.com_parent.SetGridLineWeight2(bstrCellStyle, gridLineTypes, Lineweight)

	def setgridvisibility(self, gridLineTypes: int, rowTypes: int, bValue: bool):
		"Sets the gridVisibility value for the specifed gridLineTypes and row types."
		# ['in'] gridLineTypes:int
		# ['in'] rowTypes:int
		# ['in'] bValue:bool
		# VBA: object.SetGridVisibility gridLineTypes, rowTypes, bValue
		self.com_parent.SetGridVisibility(gridLineTypes, rowTypes, bValue)

	def setgridvisibility2(self, bstrCellStyle: str, gridLineTypes: int, bValue: bool):
		"Sets the gridVisibility value for the specified gridLineType and cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] gridLineTypes:int
		# ['in'] bValue:bool
		# VBA: object.SetGridVisibility2 bstrCellStyle, gridLineTypes, bValue
		self.com_parent.SetGridVisibility2(bstrCellStyle, gridLineTypes, bValue)

	def setrotation(self, bstrCellStyle: str, Rotation: float):
		"None"
		# ['in'] bstrCellStyle:str
		# ['in'] Rotation:float
		# VBA: object.SetRotation bstrCellStyle, Rotation
		self.com_parent.SetRotation(bstrCellStyle, Rotation)

	def settemplateid(self, val: int):
		"None"
		# ['in'] val:int
		# [] option:int
		# VBA: object.SetTemplateId val, option
		self.com_parent.SetTemplateId(val)

	def settextheight(self, rowTypes: int, TextHeight: float):
		"Sets the text height for the specified row types."
		# ['in'] rowTypes:int
		# ['in'] TextHeight:float
		# VBA: object.SetTextHeight rowTypes, TextHeight
		self.com_parent.SetTextHeight(rowTypes, TextHeight)

	def settextheight2(self, bstrCellStyle: str, Height: float):
		"Sets the text height for the specified cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] Height:float
		# VBA: object.SetTextHeight2 bstrCellStyle, Height
		self.com_parent.SetTextHeight2(bstrCellStyle, Height)

	def settextstyle(self, rowTypes: int, bstrName: str):
		"Sets the text style name for the specified row types."
		# ['in'] rowTypes:int
		# ['in'] bstrName:str
		# VBA: object.SetTextStyle rowTypes, bstrName
		self.com_parent.SetTextStyle(rowTypes, bstrName)

	def settextstyleid(self, bstrCellStyle: str, val: int):
		"Sets the text style name for the specified cellStyle."
		# ['in'] bstrCellStyle:str
		# ['in'] val:int
		# VBA: object.SetTextStyleId bstrCellStyle, val
		self.com_parent.SetTextStyleId(bstrCellStyle, val)

	# Properties
	@indexedproperty
	def bitflags(self) -> int:
		"Returns and sets the bit flag values."
		# TODO: Check arguments
		# ['out', 'retval'] bitFlag:int
		return self.com_parent.BitFlags
	@bitflags.setter
	def _(self, bitFlag:int):
		# ['in'] bitFlag:int
		self.com_parent.BitFlags = bitFlag

	@indexedproperty
	def description(self) -> str:
		"Returns and sets the description of the tablestyle."
		# TODO: Check arguments
		# ['out', 'retval'] bstr:str
		return self.com_parent.Description
	@description.setter
	def _(self, bstr:str):
		# ['in'] bstr:str
		self.com_parent.Description = bstr

	@indexedproperty
	def flowdirection(self) -> int:
		"Returns and sets the table flow direction value."
		# TODO: Check arguments
		# ['out', 'retval'] pFlow:int
		return self.com_parent.FlowDirection
	@flowdirection.setter
	def _(self, pFlow:int):
		# ['in'] pFlow:int
		self.com_parent.FlowDirection = pFlow

	@indexedproperty
	def headersuppressed(self) -> bool:
		"Returns and sets the header suppressed flag value."
		# TODO: Check arguments
		# ['out', 'retval'] bValue:bool
		return self.com_parent.HeaderSuppressed
	@headersuppressed.setter
	def _(self, bValue:bool):
		# ['in'] bValue:bool
		self.com_parent.HeaderSuppressed = bValue

	@indexedproperty
	def horzcellmargin(self) -> float:
		"Returns and sets the horizontal cell margin value."
		# TODO: Check arguments
		# ['out', 'retval'] dHorzCellMargin:float
		return self.com_parent.HorzCellMargin
	@horzcellmargin.setter
	def _(self, dHorzCellMargin:float):
		# ['in'] dHorzCellMargin:float
		self.com_parent.HorzCellMargin = dHorzCellMargin

	@indexedproperty
	def name(self) -> str:
		"Returns and sets the name of the tablestyle."
		# TODO: Check arguments
		# ['out', 'retval'] bstrValue:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrValue:str):
		# ['in'] bstrValue:str
		self.com_parent.Name = bstrValue

	@indexedproperty
	def numcellstyles(self) -> int:
		# TODO: Check arguments
		# ['out', 'retval'] NumCellStyles:int
		return self.com_parent.NumCellStyles

	@indexedproperty
	def templateid(self) -> int:
		# TODO: Check arguments
		# ['out', 'retval'] pVal:int
		return self.com_parent.TemplateId
	@templateid.setter
	def _(self, pVal:int):
		# ['in'] pVal:int
		self.com_parent.TemplateId = pVal

	@indexedproperty
	def titlesuppressed(self) -> bool:
		"Returns and sets the title suppressed flag value."
		# TODO: Check arguments
		# ['out', 'retval'] bValue:bool
		return self.com_parent.TitleSuppressed
	@titlesuppressed.setter
	def _(self, bValue:bool):
		# ['in'] bValue:bool
		self.com_parent.TitleSuppressed = bValue

	@indexedproperty
	def vertcellmargin(self) -> float:
		"Returns and sets the vertical cell margin value."
		# TODO: Check arguments
		# ['out', 'retval'] dVertCellMargin:float
		return self.com_parent.VertCellMargin
	@vertcellmargin.setter
	def _(self, dVertCellMargin:float):
		# ['in'] dVertCellMargin:float
		self.com_parent.VertCellMargin = dVertCellMargin


class AcadTextStyle(POINTER(_dll.IAcadTextStyle), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadTextStyle
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadTextStyle VBA-class wrapped as AcadTextStyle python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadTextStyle__com_GetFont
	#	_IAcadTextStyle__com_SetFont
	#	_IAcadTextStyle__com__get_BigFontFile
	#	_IAcadTextStyle__com__get_Height
	#	_IAcadTextStyle__com__get_LastHeight
	#	_IAcadTextStyle__com__get_Name
	#	_IAcadTextStyle__com__get_ObliqueAngle
	#	_IAcadTextStyle__com__get_TextGenerationFlag
	#	_IAcadTextStyle__com__get_Width
	#	_IAcadTextStyle__com__get_fontFile
	#	_IAcadTextStyle__com__set_BigFontFile
	#	_IAcadTextStyle__com__set_Height
	#	_IAcadTextStyle__com__set_LastHeight
	#	_IAcadTextStyle__com__set_ObliqueAngle
	#	_IAcadTextStyle__com__set_TextGenerationFlag
	#	_IAcadTextStyle__com__set_Width
	#	_IAcadTextStyle__com__set_fontFile
	# Methods
	def getfont(self):
		"Gets the definition data of the font for the TextStyle"
		# TODO: Check arguments
		# ['out'] TypeFace:str
		# ['out'] Bold:bool
		# ['out'] Italic:bool
		# ['out'] Charset:int
		# ['out'] PitchAndFamily:int
		# VBA: object.GetFont TypeFace, Bold, Italic, Charset, PitchAndFamily
		return self.com_parent.GetFont()

	def setfont(self, TypeFace: str, Bold: bool, Italic: bool, Charset: int, PitchAndFamily: int):
		"Sets the definition data of the font for the TextStyle"
		# ['in'] TypeFace:str
		# ['in'] Bold:bool
		# ['in'] Italic:bool
		# ['in'] Charset:int
		# ['in'] PitchAndFamily:int
		# VBA: object.SetFont TypeFace, Bold, Italic, Charset, PitchAndFamily
		self.com_parent.SetFont(TypeFace, Bold, Italic, Charset, PitchAndFamily)

	# Properties
	@indexedproperty
	def bigfontfile(self) -> str:
		"Specifies the name of the big font file associated with the text or attribute"
		# TODO: Check arguments
		# ['out', 'retval'] fontFile:str
		return self.com_parent.BigFontFile
	@bigfontfile.setter
	def _(self, fontFile:str):
		# ['in'] fontFile:str
		self.com_parent.BigFontFile = fontFile

	@indexedproperty
	def fontfile(self) -> str:
		"Specifies the primary font file path and name"
		# TODO: Check arguments
		# ['out', 'retval'] fontFile:str
		return self.com_parent.fontFile
	@fontfile.setter
	def _(self, fontFile:str):
		# ['in'] fontFile:str
		self.com_parent.fontFile = fontFile

	@indexedproperty
	def height(self) -> float:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@indexedproperty
	def lastheight(self) -> float:
		"Specifies the last text height used"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.LastHeight
	@lastheight.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.LastHeight = Height

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name

	@indexedproperty
	def obliqueangle(self) -> float:
		"Specifies the oblique angle of the object"
		# TODO: Check arguments
		# ['out', 'retval'] obliAngle:float
		return self.com_parent.ObliqueAngle
	@obliqueangle.setter
	def _(self, obliAngle:float):
		# ['in'] obliAngle:float
		self.com_parent.ObliqueAngle = obliAngle

	@indexedproperty
	def textgenerationflag(self) -> int:
		"Specifies the attribute text generation flag"
		# TODO: Check arguments
		# ['out', 'retval'] textGenFlag:int
		return self.com_parent.TextGenerationFlag
	@textgenerationflag.setter
	def _(self, textGenFlag:int):
		# ['in'] textGenFlag:int
		self.com_parent.TextGenerationFlag = textGenFlag

	@indexedproperty
	def width(self) -> float:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadTextStyles(POINTER(_dll.IAcadTextStyles), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadTextStyles
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadTextStyles VBA-class wrapped as AcadTextStyles python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadTextStyles__com_Add
	#	_IAcadTextStyles__com_Item
	#	_IAcadTextStyles__com__get_Count
	#	_IAcadTextStyles__com__get__NewEnum
	# Methods
	def add(self, Name: str) -> AcadTextStyle:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pTextStyle:AcadTextStyle
		# VBA: pTextStyle = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadTextStyle:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadTextStyle
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadToolbar(POINTER(_dll.IAcadToolbar), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadToolbar
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadToolbar VBA-class wrapped as AcadToolbar python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadToolbar__com_AddSeparator
	#	_IAcadToolbar__com_AddToolbarButton
	#	_IAcadToolbar__com_Delete
	#	_IAcadToolbar__com_Dock
	#	_IAcadToolbar__com_Float
	#	_IAcadToolbar__com_Item
	#	_IAcadToolbar__com__get_Application
	#	_IAcadToolbar__com__get_Count
	#	_IAcadToolbar__com__get_DockStatus
	#	_IAcadToolbar__com__get_FloatingRows
	#	_IAcadToolbar__com__get_Height
	#	_IAcadToolbar__com__get_HelpString
	#	_IAcadToolbar__com__get_LargeButtons
	#	_IAcadToolbar__com__get_Name
	#	_IAcadToolbar__com__get_Parent
	#	_IAcadToolbar__com__get_TagString
	#	_IAcadToolbar__com__get_Visible
	#	_IAcadToolbar__com__get_Width
	#	_IAcadToolbar__com__get__NewEnum
	#	_IAcadToolbar__com__get_left
	#	_IAcadToolbar__com__get_top
	#	_IAcadToolbar__com__set_FloatingRows
	#	_IAcadToolbar__com__set_HelpString
	#	_IAcadToolbar__com__set_Name
	#	_IAcadToolbar__com__set_Visible
	#	_IAcadToolbar__com__set_left
	#	_IAcadToolbar__com__set_top
	# Methods
	def addseparator(self, Index: tagVARIANT) -> AcadToolbarItem:
		"Adds a separator to an existing menu or toolbar"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadToolbarItem
		# VBA: pItem = object.AddSeparator (Index)
		return self.com_parent.AddSeparator(Index)

	def addtoolbarbutton(self, Index: tagVARIANT, Name: str, HelpString: str, Macro: str, FlyoutButton: tagVARIANT) -> AcadToolbarItem:
		"Adds a toolbar item to a toolbar at a specified position"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['in'] Name:str
		# ['in'] HelpString:str
		# ['in'] Macro:str
		# ['in', '16'] FlyoutButton:tagVARIANT
		# ['out', 'retval'] pItem:AcadToolbarItem
		# VBA: pItem = object.AddToolbarButton (Index, Name, HelpString, Macro, FlyoutButton)
		return self.com_parent.AddToolbarButton(Index, Name, HelpString, Macro, FlyoutButton)

	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	def dock(self, Side: int):
		"Docks the toolbar to the owning frame window"
		# ['in'] Side:int
		# VBA: object.Dock Side
		self.com_parent.Dock(Side)

	def float(self, top: int, left: int, NumberFloatRows: int):
		"Floats the toolbar"
		# ['in'] top:int
		# ['in'] left:int
		# ['in'] NumberFloatRows:int
		# VBA: object.Float top, left, NumberFloatRows
		self.com_parent.Float(top, left, NumberFloatRows)

	def item(self, Index: tagVARIANT) -> AcadToolbarItem:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadToolbarItem
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def dockstatus(self) -> int:
		"Specifies if the toolbar is docked or floating"
		# TODO: Check arguments
		# ['out', 'retval'] nStatus:int
		return self.com_parent.DockStatus

	@indexedproperty
	def floatingrows(self) -> int:
		"Specifies the number of rows for a floating toolbar"
		# TODO: Check arguments
		# ['out', 'retval'] nRows:int
		return self.com_parent.FloatingRows
	@floatingrows.setter
	def _(self, nRows:int):
		# ['in'] nRows:int
		self.com_parent.FloatingRows = nRows

	@indexedproperty
	def height(self) -> int:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] nHeight:int
		return self.com_parent.Height

	@indexedproperty
	def helpstring(self) -> str:
		"Specifies the help string for the toolbar, toolbar item, or menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrHelp:str
		return self.com_parent.HelpString
	@helpstring.setter
	def _(self, bstrHelp:str):
		# ['in'] bstrHelp:str
		self.com_parent.HelpString = bstrHelp

	@indexedproperty
	def largebuttons(self) -> bool:
		"Specifies if the toolbar button is large or small"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.LargeButtons

	@indexedproperty
	def left(self) -> int:
		"Specifies the left edge of a toolbar"
		# TODO: Check arguments
		# ['out', 'retval'] nLeft:int
		return self.com_parent.left
	@left.setter
	def _(self, nLeft:int):
		# ['in'] nLeft:int
		self.com_parent.left = nLeft

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def parent(self) -> POINTER(IDispatch):
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:POINTER(IDispatch)
		return self.com_parent.Parent

	@indexedproperty
	def tagstring(self) -> str:
		"Specifies the tag string of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrTag:str
		return self.com_parent.TagString

	@indexedproperty
	def top(self) -> int:
		"Specifies the top edge of a toolbar"
		# TODO: Check arguments
		# ['out', 'retval'] nTop:int
		return self.com_parent.top
	@top.setter
	def _(self, nTop:int):
		# ['in'] nTop:int
		self.com_parent.top = nTop

	@indexedproperty
	def visible(self) -> bool:
		"Specifies the visibility of an object or the application"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.Visible
	@visible.setter
	def _(self, bFlag:bool):
		# ['in'] bFlag:bool
		self.com_parent.Visible = bFlag

	@indexedproperty
	def width(self) -> int:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] nWidth:int
		return self.com_parent.Width


class AcadToolbarItem(POINTER(_dll.IAcadToolbarItem), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadToolbarItem
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadToolbarItem VBA-class wrapped as AcadToolbarItem python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadToolbarItem__com_AttachToolbarToFlyout
	#	_IAcadToolbarItem__com_Delete
	#	_IAcadToolbarItem__com_GetBitmaps
	#	_IAcadToolbarItem__com_SetBitmaps
	#	_IAcadToolbarItem__com__get_Application
	#	_IAcadToolbarItem__com__get_CommandDisplayName
	#	_IAcadToolbarItem__com__get_Flyout
	#	_IAcadToolbarItem__com__get_HelpString
	#	_IAcadToolbarItem__com__get_Index
	#	_IAcadToolbarItem__com__get_Macro
	#	_IAcadToolbarItem__com__get_Name
	#	_IAcadToolbarItem__com__get_Parent
	#	_IAcadToolbarItem__com__get_TagString
	#	_IAcadToolbarItem__com__get_Type
	#	_IAcadToolbarItem__com__set_CommandDisplayName
	#	_IAcadToolbarItem__com__set_HelpString
	#	_IAcadToolbarItem__com__set_Macro
	#	_IAcadToolbarItem__com__set_Name
	#	_IAcadToolbarItem__com__set_TagString
	# Methods
	def attachtoolbartoflyout(self, MenuGroupName: str, ToolbarName: str):
		"Attaches a toolbar to a toolbar button defined as a flyout"
		# ['in'] MenuGroupName:str
		# ['in'] ToolbarName:str
		# VBA: object.AttachToolbarToFlyout MenuGroupName, ToolbarName
		self.com_parent.AttachToolbarToFlyout(MenuGroupName, ToolbarName)

	def delete(self):
		"Deletes a specified object"
		# VBA: object.Delete 
		self.com_parent.Delete()

	def getbitmaps(self):
		"Gets the large and small bitmaps used as icons for the toolbar item"
		# TODO: Check arguments
		# ['out'] SmallIconName:str
		# ['out'] LargeIconName:str
		# VBA: object.GetBitmaps SmallIconName, LargeIconName
		return self.com_parent.GetBitmaps()

	def setbitmaps(self, SmallIconName: str, LargeIconName: str):
		"Sets the large and small bitmaps used as icons for the toolbar item"
		# ['in'] SmallIconName:str
		# ['in'] LargeIconName:str
		# VBA: object.SetBitmaps SmallIconName, LargeIconName
		self.com_parent.SetBitmaps(SmallIconName, LargeIconName)

	# Properties
	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def commanddisplayname(self) -> str:
		# TODO: Check arguments
		# ['out', 'retval'] Name:str
		return self.com_parent.CommandDisplayName
	@commanddisplayname.setter
	def _(self, Name:str):
		# ['in'] Name:str
		self.com_parent.CommandDisplayName = Name

	@indexedproperty
	def flyout(self) -> AcadToolbar:
		"Gets the toolbar associated with a flyout toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] pTlbar:AcadToolbar
		return self.com_parent.Flyout

	@indexedproperty
	def helpstring(self) -> str:
		"Specifies the help string for the toolbar, toolbar item, or menu item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrHelp:str
		return self.com_parent.HelpString
	@helpstring.setter
	def _(self, bstrHelp:str):
		# ['in'] bstrHelp:str
		self.com_parent.HelpString = bstrHelp

	@indexedproperty
	def index(self) -> int:
		"Specifies the index of the menu or toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] nIndex:int
		return self.com_parent.Index

	@indexedproperty
	def macro(self) -> str:
		"Specifies the macro for the menu or toolbar item"
		# TODO: Check arguments
		# ['out', 'retval'] bstrMacro:str
		return self.com_parent.Macro
	@macro.setter
	def _(self, bstrMacro:str):
		# ['in'] bstrMacro:str
		self.com_parent.Macro = bstrMacro

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def parent(self) -> AcadToolbar:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadToolbar
		return self.com_parent.Parent

	@indexedproperty
	def tagstring(self) -> str:
		"Specifies the tag string of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrTag:str
		return self.com_parent.TagString
	@tagstring.setter
	def _(self, bstrTag:str):
		# ['in'] bstrTag:str
		self.com_parent.TagString = bstrTag

	@indexedproperty
	def type(self) -> int:
		"Specifies type of a Leader, MenuGroup, PopupMenuItem, ToolbarItem, Polyline, or PolygonMesh object"
		# TODO: Check arguments
		# ['out', 'retval'] itemType:int
		return self.com_parent.Type


class AcadToolbars(POINTER(_dll.IAcadToolbars), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadToolbars
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadToolbars VBA-class wrapped as AcadToolbars python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadToolbars__com_Add
	#	_IAcadToolbars__com_Item
	#	_IAcadToolbars__com__get_Application
	#	_IAcadToolbars__com__get_Count
	#	_IAcadToolbars__com__get_LargeButtons
	#	_IAcadToolbars__com__get_Parent
	#	_IAcadToolbars__com__get__NewEnum
	#	_IAcadToolbars__com__set_LargeButtons
	# Methods
	def add(self, ToolbarName: str) -> AcadToolbar:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] ToolbarName:str
		# ['out', 'retval'] pTlbar:AcadToolbar
		# VBA: pTlbar = object.Add (ToolbarName)
		return self.com_parent.Add(ToolbarName)

	def item(self, Index: tagVARIANT) -> AcadToolbar:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadToolbar
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pEnumVariant:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def application(self) -> AcadApplication:
		"Gets the Application object"
		# TODO: Check arguments
		# ['out', 'retval'] pAppObj:AcadApplication
		return self.com_parent.Application

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] Count:int
		return self.com_parent.Count

	@indexedproperty
	def largebuttons(self) -> bool:
		"Specifies if the toolbar button is large or small"
		# TODO: Check arguments
		# ['out', 'retval'] bFlag:bool
		return self.com_parent.LargeButtons
	@largebuttons.setter
	def _(self, bFlag:bool):
		# ['in'] bFlag:bool
		self.com_parent.LargeButtons = bFlag

	@indexedproperty
	def parent(self) -> AcadMenuGroup:
		"Gets the parent of the object"
		# TODO: Check arguments
		# ['out', 'retval'] pParent:AcadMenuGroup
		return self.com_parent.Parent


class AcadUCS(POINTER(_dll.IAcadUCS), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadUCS
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadUCS VBA-class wrapped as AcadUCS python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadUCS__com_GetUCSMatrix
	#	_IAcadUCS__com__get_Name
	#	_IAcadUCS__com__get_Origin
	#	_IAcadUCS__com__get_XVector
	#	_IAcadUCS__com__get_YVector
	#	_IAcadUCS__com__set_Name
	#	_IAcadUCS__com__set_Origin
	#	_IAcadUCS__com__set_XVector
	#	_IAcadUCS__com__set_YVector
	# Methods
	def getucsmatrix(self) -> tagVARIANT:
		"Gets the transformation matrix consisting of UCS coordinate system data"
		# TODO: Check arguments
		# ['out', 'retval'] transMatrix:tagVARIANT
		# VBA: transMatrix = object.GetUCSMatrix ()
		return self.com_parent.GetUCSMatrix()

	# Properties
	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def origin(self) -> tagVARIANT:
		"Specifies the origin of the UCS, block, layout, or raster image in WCS coordinates"
		# TODO: Check arguments
		# ['out', 'retval'] Origin:tagVARIANT
		return self.com_parent.Origin
	@origin.setter
	def _(self, Origin:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT
		self.com_parent.Origin = Origin

	@indexedproperty
	def xvector(self) -> tagVARIANT:
		"Specifies the X direction of the given UCS"
		# TODO: Check arguments
		# ['out', 'retval'] XVector:tagVARIANT
		return self.com_parent.XVector
	@xvector.setter
	def _(self, XVector:tagVARIANT):
		# TODO: Check arguments
		# ['in'] XVector:tagVARIANT
		self.com_parent.XVector = XVector

	@indexedproperty
	def yvector(self) -> tagVARIANT:
		"Specifies the Y direction of the given UCS"
		# TODO: Check arguments
		# ['out', 'retval'] YVector:tagVARIANT
		return self.com_parent.YVector
	@yvector.setter
	def _(self, YVector:tagVARIANT):
		# TODO: Check arguments
		# ['in'] YVector:tagVARIANT
		self.com_parent.YVector = YVector


class AcadUCSs(POINTER(_dll.IAcadUCSs), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadUCSs
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadUCSs VBA-class wrapped as AcadUCSs python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadUCSs__com_Add
	#	_IAcadUCSs__com_Item
	#	_IAcadUCSs__com__get_Count
	#	_IAcadUCSs__com__get__NewEnum
	# Methods
	def add(self, Origin: tagVARIANT, XAxisPoint: tagVARIANT, YAxisPoint: tagVARIANT, Name: str) -> AcadUCS:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Origin:tagVARIANT
		# ['in'] XAxisPoint:tagVARIANT
		# ['in'] YAxisPoint:tagVARIANT
		# ['in'] Name:str
		# ['out', 'retval'] pUCS:AcadUCS
		# VBA: pUCS = object.Add (Origin, XAxisPoint, YAxisPoint, Name)
		return self.com_parent.Add(Origin, XAxisPoint, YAxisPoint, Name)

	def item(self, Index: tagVARIANT) -> AcadUCS:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadUCS
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadUtility(POINTER(_dll.IAcadUtility), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadUtility
	#	IDispatch
	#		IUnknown
	#			object
	# Prototype for IAcadUtility VBA-class wrapped as AcadUtility python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadUtility__com_AngleFromXAxis
	#	_IAcadUtility__com_AngleToReal
	#	_IAcadUtility__com_AngleToString
	#	_IAcadUtility__com_CreateTypedArray
	#	_IAcadUtility__com_DistanceToReal
	#	_IAcadUtility__com_GetAngle
	#	_IAcadUtility__com_GetCorner
	#	_IAcadUtility__com_GetDistance
	#	_IAcadUtility__com_GetEntity
	#	_IAcadUtility__com_GetInput
	#	_IAcadUtility__com_GetInteger
	#	_IAcadUtility__com_GetKeyword
	#	_IAcadUtility__com_GetObjectIdString
	#	_IAcadUtility__com_GetOrientation
	#	_IAcadUtility__com_GetPoint
	#	_IAcadUtility__com_GetReal
	#	_IAcadUtility__com_GetRemoteFile
	#	_IAcadUtility__com_GetString
	#	_IAcadUtility__com_GetSubEntity
	#	_IAcadUtility__com_InitializeUserInput
	#	_IAcadUtility__com_IsRemoteFile
	#	_IAcadUtility__com_IsURL
	#	_IAcadUtility__com_LaunchBrowserDialog
	#	_IAcadUtility__com_PolarPoint
	#	_IAcadUtility__com_Prompt
	#	_IAcadUtility__com_PutRemoteFile
	#	_IAcadUtility__com_RealToString
	#	_IAcadUtility__com_SendModelessOperationEnded
	#	_IAcadUtility__com_SendModelessOperationStart
	#	_IAcadUtility__com_TranslateCoordinates
	# Methods
	def anglefromxaxis(self, StartPoint: tagVARIANT, EndPoint: tagVARIANT) -> float:
		"Gets the angle of a line from the X axis"
		# TODO: Check arguments
		# ['in'] StartPoint:tagVARIANT
		# ['in'] EndPoint:tagVARIANT
		# ['out', 'retval'] Angle:float
		# VBA: Angle = object.AngleFromXAxis (StartPoint, EndPoint)
		return self.com_parent.AngleFromXAxis(StartPoint, EndPoint)

	def angletoreal(self, Angle: str, Unit: int) -> float:
		"Converts an angle as a string to a real (double) value"
		# TODO: Check arguments
		# ['in'] Angle:str
		# ['in'] Unit:int
		# ['out', 'retval'] Value:float
		# VBA: Value = object.AngleToReal (Angle, Unit)
		return self.com_parent.AngleToReal(Angle, Unit)

	def angletostring(self, Angle: float, Unit: int, precision: int) -> str:
		"Converts an angle from a real (double) value to a string"
		# TODO: Check arguments
		# ['in'] Angle:float
		# ['in'] Unit:int
		# ['in'] precision:int
		# ['out', 'retval'] bstrValue:str
		# VBA: bstrValue = object.AngleToString (Angle, Unit, precision)
		return self.com_parent.AngleToString(Angle, Unit, precision)

	def createtypedarray(self, Type: int, inArgs: SAFEARRAY_tagVARIANT) -> tagVARIANT:
		"Creates a variant that contains an array of typed arguments"
		# TODO: Check arguments
		# ['out'] varArr:tagVARIANT
		# ['in'] Type:int
		# ['in'] inArgs:SAFEARRAY_tagVARIANT
		# VBA: object.CreateTypedArray varArr, Type, inArgs
		return self.com_parent.CreateTypedArray(Type, inArgs)

	def distancetoreal(self, Distance: str, Unit: int) -> float:
		"Converts a distance from a string to a real (double) value"
		# TODO: Check arguments
		# ['in'] Distance:str
		# ['in'] Unit:int
		# ['out', 'retval'] Value:float
		# VBA: Value = object.DistanceToReal (Distance, Unit)
		return self.com_parent.DistanceToReal(Distance, Unit)

	def getangle(self, Point: tagVARIANT, Prompt: tagVARIANT) -> float:
		"Gets the angle specified. Considers the setting of the ANGBASE system variable"
		# TODO: Check arguments
		# ['in', '16'] Point:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] Angle:float
		# VBA: Angle = object.GetAngle (Point, Prompt)
		return self.com_parent.GetAngle(Point, Prompt)

	def getcorner(self, Point: tagVARIANT, Prompt: tagVARIANT) -> tagVARIANT:
		"Gets a corner of a rectangle"
		# TODO: Check arguments
		# ['in'] Point:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] corner:tagVARIANT
		# VBA: corner = object.GetCorner (Point, Prompt)
		return self.com_parent.GetCorner(Point, Prompt)

	def getdistance(self, Point: tagVARIANT, Prompt: tagVARIANT) -> float:
		"Gets the distance from the prompt line or a selected set of points on the screen"
		# TODO: Check arguments
		# ['in', '16'] Point:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] dist:float
		# VBA: dist = object.GetDistance (Point, Prompt)
		return self.com_parent.GetDistance(Point, Prompt)

	def getentity(self, Prompt: tagVARIANT):
		"Gets an object interactively"
		# TODO: Check arguments
		# ['out'] Object:POINTER(IDispatch)
		# ['out'] PickedPoint:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# VBA: object.GetEntity Object, PickedPoint, Prompt
		return self.com_parent.GetEntity(Prompt)

	def getinput(self) -> str:
		"Converts an input string from the user into a keyword index"
		# TODO: Check arguments
		# ['out', 'retval'] Value:str
		# VBA: Value = object.GetInput ()
		return self.com_parent.GetInput()

	def getinteger(self, Prompt: tagVARIANT) -> int:
		"Gets an integer value from the user"
		# TODO: Check arguments
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] Value:int
		# VBA: Value = object.GetInteger (Prompt)
		return self.com_parent.GetInteger(Prompt)

	def getkeyword(self, Prompt: tagVARIANT) -> str:
		"Gets a keyword string from the user"
		# TODO: Check arguments
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] bstrKeyword:str
		# VBA: bstrKeyword = object.GetKeyword (Prompt)
		return self.com_parent.GetKeyword(Prompt)

	def getobjectidstring(self, Object: POINTER(IDispatch), bHex: bool) -> str:
		"None"
		# TODO: Check arguments
		# ['in'] Object:POINTER(IDispatch)
		# ['in'] bHex:bool
		# ['out', 'retval'] ObjectIdString:str
		# VBA: ObjectIdString = object.GetObjectIdString (Object, bHex)
		return self.com_parent.GetObjectIdString(Object, bHex)

	def getorientation(self, Point: tagVARIANT, Prompt: tagVARIANT) -> float:
		"Gets the angle specified. Ignores the setting of the ANGBASE system variable"
		# TODO: Check arguments
		# ['in', '16'] Point:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] Angle:float
		# VBA: Angle = object.GetOrientation (Point, Prompt)
		return self.com_parent.GetOrientation(Point, Prompt)

	def getpoint(self, Point: tagVARIANT, Prompt: tagVARIANT) -> tagVARIANT:
		"Gets the point selected in AutoCAD"
		# TODO: Check arguments
		# ['in', '16'] Point:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] inputPoint:tagVARIANT
		# VBA: inputPoint = object.GetPoint (Point, Prompt)
		return self.com_parent.GetPoint(Point, Prompt)

	def getreal(self, Prompt: tagVARIANT) -> float:
		"Gets a real (double) value from the user"
		# TODO: Check arguments
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] Value:float
		# VBA: Value = object.GetReal (Prompt)
		return self.com_parent.GetReal(Prompt)

	def getremotefile(self, URL: str, IgnoreCache: bool) -> str:
		"Downloads the file specified by a URL"
		# TODO: Check arguments
		# ['in'] URL:str
		# ['out'] LocalFile:str
		# ['in'] IgnoreCache:bool
		# VBA: object.GetRemoteFile URL, LocalFile, IgnoreCache
		return self.com_parent.GetRemoteFile(URL, IgnoreCache)

	def getstring(self, HasSpaces: int, Prompt: tagVARIANT) -> str:
		"Gets a string from the user"
		# TODO: Check arguments
		# ['in'] HasSpaces:int
		# ['in', '16'] Prompt:tagVARIANT
		# ['out', 'retval'] bstrValue:str
		# VBA: bstrValue = object.GetString (HasSpaces, Prompt)
		return self.com_parent.GetString(HasSpaces, Prompt)

	def getsubentity(self, Prompt: tagVARIANT):
		"Gets an object or subentity interactively"
		# TODO: Check arguments
		# ['out'] Object:POINTER(IDispatch)
		# ['out'] PickedPoint:tagVARIANT
		# ['out'] transMatrix:tagVARIANT
		# ['out'] ContextData:tagVARIANT
		# ['in', '16'] Prompt:tagVARIANT
		# VBA: object.GetSubEntity Object, PickedPoint, transMatrix, ContextData, Prompt
		return self.com_parent.GetSubEntity(Prompt)

	def initializeuserinput(self, Bits: int, KeyWordList: tagVARIANT):
		"Initializes the GetKeyword method"
		# TODO: Check arguments
		# ['in'] Bits:int
		# ['in', '16'] KeyWordList:tagVARIANT
		# VBA: object.InitializeUserInput Bits, KeyWordList
		self.com_parent.InitializeUserInput(Bits, KeyWordList)

	def isremotefile(self, LocalFile: str):
		"Returns the URL that a remote file was downloaded from"
		# TODO: Check arguments
		# ['in'] LocalFile:str
		# ['out'] URL:str
		# ['out', 'retval'] IsDownloadedFile:bool
		# VBA: IsDownloadedFile = object.IsRemoteFile (LocalFile, URL)
		return self.com_parent.IsRemoteFile(LocalFile)

	def isurl(self, URL: str) -> bool:
		"Validates a given URL"
		# TODO: Check arguments
		# ['in'] URL:str
		# ['out', 'retval'] IsValidURL:bool
		# VBA: IsValidURL = object.IsURL (URL)
		return self.com_parent.IsURL(URL)

	def launchbrowserdialog(self, DialogTitle: str, OpenButtonCaption: str, StartPageURL: str, RegistryRootKey: str, OpenButtonAlwaysEnabled: bool):
		"Launches the Web Browser dialog that allows the user to navigate to any URL and select a URL"
		# TODO: Check arguments
		# ['out'] SelectedURL:str
		# ['in'] DialogTitle:str
		# ['in'] OpenButtonCaption:str
		# ['in'] StartPageURL:str
		# ['in'] RegistryRootKey:str
		# ['in'] OpenButtonAlwaysEnabled:bool
		# ['out', 'retval'] success:bool
		# VBA: success = object.LaunchBrowserDialog (SelectedURL, DialogTitle, OpenButtonCaption, StartPageURL, RegistryRootKey, OpenButtonAlwaysEnabled)
		return self.com_parent.LaunchBrowserDialog(DialogTitle, OpenButtonCaption, StartPageURL, RegistryRootKey, OpenButtonAlwaysEnabled)

	def polarpoint(self, Point: tagVARIANT, Angle: float, Distance: float) -> tagVARIANT:
		"Gets the point at a specified angle and distance from a given point"
		# TODO: Check arguments
		# ['in'] Point:tagVARIANT
		# ['in'] Angle:float
		# ['in'] Distance:float
		# ['out', 'retval'] inputPoint:tagVARIANT
		# VBA: inputPoint = object.PolarPoint (Point, Angle, Distance)
		return self.com_parent.PolarPoint(Point, Angle, Distance)

	def prompt(self, Message: str):
		"Posts a prompt to the command line"
		# ['in'] Message:str
		# VBA: object.Prompt Message
		self.com_parent.Prompt(Message)

	def putremotefile(self, URL: str, LocalFile: str):
		"Uploads a file to a remote location specified by a URL"
		# ['in'] URL:str
		# ['in'] LocalFile:str
		# VBA: object.PutRemoteFile URL, LocalFile
		self.com_parent.PutRemoteFile(URL, LocalFile)

	def realtostring(self, Value: float, Unit: int, precision: int) -> str:
		"Converts a real (double) value to a string"
		# TODO: Check arguments
		# ['in'] Value:float
		# ['in'] Unit:int
		# ['in'] precision:int
		# ['out', 'retval'] bstrValue:str
		# VBA: bstrValue = object.RealToString (Value, Unit, precision)
		return self.com_parent.RealToString(Value, Unit, precision)

	def sendmodelessoperationended(self):
		"Indicates a modeless operation has ended."
		# [] Context:str
		# VBA: object.SendModelessOperationEnded Context
		self.com_parent.SendModelessOperationEnded()

	def sendmodelessoperationstart(self):
		"Indicates a modeless operation will start."
		# [] Context:str
		# VBA: object.SendModelessOperationStart Context
		self.com_parent.SendModelessOperationStart()

	def translatecoordinates(self, Point: tagVARIANT, FromCoordSystem: int, ToCoordSystem: int, Displacement: int, OCSNormal: tagVARIANT) -> tagVARIANT:
		"Translates a point from one coordinate system to another coordinate system"
		# TODO: Check arguments
		# ['in'] Point:tagVARIANT
		# ['in'] FromCoordSystem:int
		# ['in'] ToCoordSystem:int
		# ['in'] Displacement:int
		# ['in', '16'] OCSNormal:tagVARIANT
		# ['out', 'retval'] transPt:tagVARIANT
		# VBA: transPt = object.TranslateCoordinates (Point, FromCoordSystem, ToCoordSystem, Displacement, OCSNormal)
		return self.com_parent.TranslateCoordinates(Point, FromCoordSystem, ToCoordSystem, Displacement, OCSNormal)


class AcadView(POINTER(_dll.IAcadView), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadView
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadView VBA-class wrapped as AcadView python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadView__com__get_CategoryName
	#	_IAcadView__com__get_Center
	#	_IAcadView__com__get_Direction
	#	_IAcadView__com__get_HasVpAssociation
	#	_IAcadView__com__get_Height
	#	_IAcadView__com__get_LayerState
	#	_IAcadView__com__get_LayoutId
	#	_IAcadView__com__get_Name
	#	_IAcadView__com__get_Target
	#	_IAcadView__com__get_Width
	#	_IAcadView__com__set_CategoryName
	#	_IAcadView__com__set_Center
	#	_IAcadView__com__set_Direction
	#	_IAcadView__com__set_HasVpAssociation
	#	_IAcadView__com__set_Height
	#	_IAcadView__com__set_LayerState
	#	_IAcadView__com__set_LayoutId
	#	_IAcadView__com__set_Name
	#	_IAcadView__com__set_Target
	#	_IAcadView__com__set_Width
	# Properties
	@indexedproperty
	def categoryname(self) -> str:
		"RReturns and sets the name of the category of the view."
		# TODO: Check arguments
		# ['out', 'retval'] category:str
		return self.com_parent.CategoryName
	@categoryname.setter
	def _(self, category:str):
		# ['in'] category:str
		self.com_parent.CategoryName = category

	@indexedproperty
	def center(self) -> tagVARIANT:
		"Specifies the center of an arc, circle, ellipse, view, or viewport"
		# TODO: Check arguments
		# ['out', 'retval'] Center:tagVARIANT
		return self.com_parent.Center
	@center.setter
	def _(self, Center:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		self.com_parent.Center = Center

	@indexedproperty
	def direction(self) -> tagVARIANT:
		"Specifies the viewing direction for a 3D visualization of the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] dirVec:tagVARIANT
		return self.com_parent.Direction
	@direction.setter
	def _(self, dirVec:tagVARIANT):
		# TODO: Check arguments
		# ['in'] dirVec:tagVARIANT
		self.com_parent.Direction = dirVec

	@indexedproperty
	def hasvpassociation(self) -> bool:
		"Specifies whether the view is associated with a paperspace viewport."
		# TODO: Check arguments
		# ['out', 'retval'] bVpAssoc:bool
		return self.com_parent.HasVpAssociation
	@hasvpassociation.setter
	def _(self, bVpAssoc:bool):
		# ['in'] bVpAssoc:bool
		self.com_parent.HasVpAssociation = bVpAssoc

	@indexedproperty
	def height(self) -> float:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@indexedproperty
	def layerstate(self) -> str:
		"Returns and sets the name of the layer state of the view."
		# TODO: Check arguments
		# ['out', 'retval'] LayerState:str
		return self.com_parent.LayerState
	@layerstate.setter
	def _(self, LayerState:str):
		# ['in'] LayerState:str
		self.com_parent.LayerState = LayerState

	@indexedproperty
	def layoutid(self) -> int:
		"Returns and sets the layout of the view."
		# TODO: Check arguments
		# ['out', 'retval'] ObjectID:int
		return self.com_parent.LayoutId
	@layoutid.setter
	def _(self, ObjectID:int):
		# ['in'] ObjectID:int
		self.com_parent.LayoutId = ObjectID

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def target(self) -> tagVARIANT:
		"Specifies the target point for the view or viewport"
		# TODO: Check arguments
		# ['out', 'retval'] targetPoint:tagVARIANT
		return self.com_parent.Target
	@target.setter
	def _(self, targetPoint:tagVARIANT):
		# TODO: Check arguments
		# ['in'] targetPoint:tagVARIANT
		self.com_parent.Target = targetPoint

	@indexedproperty
	def width(self) -> float:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadViewport(POINTER(_dll.IAcadViewport), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadViewport
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadViewport VBA-class wrapped as AcadViewport python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadViewport__com_GetGridSpacing
	#	_IAcadViewport__com_GetSnapSpacing
	#	_IAcadViewport__com_SetGridSpacing
	#	_IAcadViewport__com_SetSnapSpacing
	#	_IAcadViewport__com_SetView
	#	_IAcadViewport__com_Split
	#	_IAcadViewport__com__get_ArcSmoothness
	#	_IAcadViewport__com__get_Center
	#	_IAcadViewport__com__get_Direction
	#	_IAcadViewport__com__get_GridOn
	#	_IAcadViewport__com__get_Height
	#	_IAcadViewport__com__get_LowerLeftCorner
	#	_IAcadViewport__com__get_Name
	#	_IAcadViewport__com__get_OrthoOn
	#	_IAcadViewport__com__get_SnapBasePoint
	#	_IAcadViewport__com__get_SnapOn
	#	_IAcadViewport__com__get_SnapRotationAngle
	#	_IAcadViewport__com__get_Target
	#	_IAcadViewport__com__get_UCSIconAtOrigin
	#	_IAcadViewport__com__get_UCSIconOn
	#	_IAcadViewport__com__get_UpperRightCorner
	#	_IAcadViewport__com__get_Width
	#	_IAcadViewport__com__set_ArcSmoothness
	#	_IAcadViewport__com__set_Center
	#	_IAcadViewport__com__set_Direction
	#	_IAcadViewport__com__set_GridOn
	#	_IAcadViewport__com__set_Height
	#	_IAcadViewport__com__set_Name
	#	_IAcadViewport__com__set_OrthoOn
	#	_IAcadViewport__com__set_SnapBasePoint
	#	_IAcadViewport__com__set_SnapOn
	#	_IAcadViewport__com__set_SnapRotationAngle
	#	_IAcadViewport__com__set_Target
	#	_IAcadViewport__com__set_UCSIconAtOrigin
	#	_IAcadViewport__com__set_UCSIconOn
	#	_IAcadViewport__com__set_Width
	# Methods
	def getgridspacing(self):
		"Gets the grid spacing for the viewport"
		# TODO: Check arguments
		# ['out'] XSpacing:float
		# ['out'] YSpacing:float
		# VBA: object.GetGridSpacing XSpacing, YSpacing
		return self.com_parent.GetGridSpacing()

	def getsnapspacing(self):
		"Gets the snap spacing for the viewport"
		# TODO: Check arguments
		# ['out'] XSpacing:float
		# ['out'] YSpacing:float
		# VBA: object.GetSnapSpacing XSpacing, YSpacing
		return self.com_parent.GetSnapSpacing()

	def setgridspacing(self, XSpacing: float, YSpacing: float):
		"Sets the grid spacing for the viewport"
		# ['in'] XSpacing:float
		# ['in'] YSpacing:float
		# VBA: object.SetGridSpacing XSpacing, YSpacing
		self.com_parent.SetGridSpacing(XSpacing, YSpacing)

	def setsnapspacing(self, XSpacing: float, YSpacing: float):
		"Sets the snap spacing for the viewport"
		# ['in'] XSpacing:float
		# ['in'] YSpacing:float
		# VBA: object.SetSnapSpacing XSpacing, YSpacing
		self.com_parent.SetSnapSpacing(XSpacing, YSpacing)

	def setview(self, View: AcadView):
		"Sets the view in a viewport to a saved view in the Views Collection object"
		# TODO: Check arguments
		# ['in'] View:AcadView
		# VBA: object.SetView View
		self.com_parent.SetView(View)

	def split(self, NumWins: int):
		"Splits a viewport into the given number of views"
		# ['in'] NumWins:int
		# VBA: object.Split NumWins
		self.com_parent.Split(NumWins)

	# Properties
	@indexedproperty
	def arcsmoothness(self) -> int:
		"Specifies the smoothness of circles, arcs, and ellipses"
		# TODO: Check arguments
		# ['out', 'retval'] arcSmooth:int
		return self.com_parent.ArcSmoothness
	@arcsmoothness.setter
	def _(self, arcSmooth:int):
		# ['in'] arcSmooth:int
		self.com_parent.ArcSmoothness = arcSmooth

	@indexedproperty
	def center(self) -> tagVARIANT:
		"Specifies the center of an arc, circle, ellipse, view, or viewport"
		# TODO: Check arguments
		# ['out', 'retval'] Center:tagVARIANT
		return self.com_parent.Center
	@center.setter
	def _(self, Center:tagVARIANT):
		# TODO: Check arguments
		# ['in'] Center:tagVARIANT
		self.com_parent.Center = Center

	@indexedproperty
	def direction(self) -> tagVARIANT:
		"Specifies the viewing direction for a 3D visualization of the drawing"
		# TODO: Check arguments
		# ['out', 'retval'] dirVec:tagVARIANT
		return self.com_parent.Direction
	@direction.setter
	def _(self, dirVec:tagVARIANT):
		# TODO: Check arguments
		# ['in'] dirVec:tagVARIANT
		self.com_parent.Direction = dirVec

	@indexedproperty
	def gridon(self) -> bool:
		"Specifies the status of the viewport grid"
		# TODO: Check arguments
		# ['out', 'retval'] bGridOn:bool
		return self.com_parent.GridOn
	@gridon.setter
	def _(self, bGridOn:bool):
		# ['in'] bGridOn:bool
		self.com_parent.GridOn = bGridOn

	@indexedproperty
	def height(self) -> float:
		"Height of the attribute, shape, text, or view toolbar or the main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Height:float
		return self.com_parent.Height
	@height.setter
	def _(self, Height:float):
		# ['in'] Height:float
		self.com_parent.Height = Height

	@indexedproperty
	def lowerleftcorner(self) -> tagVARIANT:
		"Gets the lower-left corner of the current active viewport"
		# TODO: Check arguments
		# ['out', 'retval'] lowLeft:tagVARIANT
		return self.com_parent.LowerLeftCorner

	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def orthoon(self) -> bool:
		"Specifies the status of the Ortho mode for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] bOrthoOn:bool
		return self.com_parent.OrthoOn
	@orthoon.setter
	def _(self, bOrthoOn:bool):
		# ['in'] bOrthoOn:bool
		self.com_parent.OrthoOn = bOrthoOn

	@indexedproperty
	def snapbasepoint(self) -> tagVARIANT:
		"Specifies the snap base point for the viewport"
		# TODO: Check arguments
		# ['out', 'retval'] lowLeft:tagVARIANT
		return self.com_parent.SnapBasePoint
	@snapbasepoint.setter
	def _(self, lowLeft:tagVARIANT):
		# TODO: Check arguments
		# ['in'] lowLeft:tagVARIANT
		self.com_parent.SnapBasePoint = lowLeft

	@indexedproperty
	def snapon(self) -> bool:
		"Specifies the status of snap"
		# TODO: Check arguments
		# ['out', 'retval'] bSnapOn:bool
		return self.com_parent.SnapOn
	@snapon.setter
	def _(self, bSnapOn:bool):
		# ['in'] bSnapOn:bool
		self.com_parent.SnapOn = bSnapOn

	@indexedproperty
	def snaprotationangle(self) -> float:
		"Specifies the snap rotation angle of the viewport relative to the current UCS"
		# TODO: Check arguments
		# ['out', 'retval'] Angle:float
		return self.com_parent.SnapRotationAngle
	@snaprotationangle.setter
	def _(self, Angle:float):
		# ['in'] Angle:float
		self.com_parent.SnapRotationAngle = Angle

	@indexedproperty
	def target(self) -> tagVARIANT:
		"Specifies the target point for the view or viewport"
		# TODO: Check arguments
		# ['out', 'retval'] targetPoint:tagVARIANT
		return self.com_parent.Target
	@target.setter
	def _(self, targetPoint:tagVARIANT):
		# TODO: Check arguments
		# ['in'] targetPoint:tagVARIANT
		self.com_parent.Target = targetPoint

	@indexedproperty
	def ucsiconatorigin(self) -> bool:
		"Specifies if the UCS icon is displayed at the origin"
		# TODO: Check arguments
		# ['out', 'retval'] bIconAtOrigin:bool
		return self.com_parent.UCSIconAtOrigin
	@ucsiconatorigin.setter
	def _(self, bIconAtOrigin:bool):
		# ['in'] bIconAtOrigin:bool
		self.com_parent.UCSIconAtOrigin = bIconAtOrigin

	@indexedproperty
	def ucsiconon(self) -> bool:
		"Specifies if the UCS icon is on"
		# TODO: Check arguments
		# ['out', 'retval'] bIconOn:bool
		return self.com_parent.UCSIconOn
	@ucsiconon.setter
	def _(self, bIconOn:bool):
		# ['in'] bIconOn:bool
		self.com_parent.UCSIconOn = bIconOn

	@indexedproperty
	def upperrightcorner(self) -> tagVARIANT:
		"Gets the upper-right corner of the current active viewport"
		# TODO: Check arguments
		# ['out', 'retval'] UpperRight:tagVARIANT
		return self.com_parent.UpperRightCorner

	@indexedproperty
	def width(self) -> float:
		"Specifies the width of the text boundary, view, image, toolbar, or main application window"
		# TODO: Check arguments
		# ['out', 'retval'] Width:float
		return self.com_parent.Width
	@width.setter
	def _(self, Width:float):
		# ['in'] Width:float
		self.com_parent.Width = Width


class AcadViewports(POINTER(_dll.IAcadViewports), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadViewports
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadViewports VBA-class wrapped as AcadViewports python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadViewports__com_Add
	#	_IAcadViewports__com_DeleteConfiguration
	#	_IAcadViewports__com_Item
	#	_IAcadViewports__com__get_Count
	#	_IAcadViewports__com__get__NewEnum
	# Methods
	def add(self, Name: str) -> AcadViewport:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pRegApp:AcadViewport
		# VBA: pRegApp = object.Add (Name)
		return self.com_parent.Add(Name)

	def deleteconfiguration(self, Name: str):
		"Deletes a viewport configuration"
		# ['in'] Name:str
		# VBA: object.DeleteConfiguration Name
		self.com_parent.DeleteConfiguration(Name)

	def item(self, Index: tagVARIANT) -> AcadViewport:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadViewport
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadViews(POINTER(_dll.IAcadViews), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadViews
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadViews VBA-class wrapped as AcadViews python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadViews__com_Add
	#	_IAcadViews__com_Item
	#	_IAcadViews__com__get_Count
	#	_IAcadViews__com__get__NewEnum
	# Methods
	def add(self, Name: str) -> AcadView:
		"Creates a member object and adds it to the appropriate collection"
		# TODO: Check arguments
		# ['in'] Name:str
		# ['out', 'retval'] pRegApp:AcadView
		# VBA: pRegApp = object.Add (Name)
		return self.com_parent.Add(Name)

	def item(self, Index: tagVARIANT) -> AcadView:
		"Gets the member object at a given index in a collection, group, or selection set"
		# TODO: Check arguments
		# ['in'] Index:tagVARIANT
		# ['out', 'retval'] pItem:AcadView
		# VBA: pItem = object.Item (Index)
		return self.com_parent.Item(Index)

	# Properties
	@indexedproperty
	def _newenum(self) -> POINTER(IUnknown):
		# TODO: Check arguments
		# ['out', 'retval'] pVal:POINTER(IUnknown)
		return self.com_parent._NewEnum

	@indexedproperty
	def count(self) -> int:
		"Gets the number of items in the collection, dictionary, group, or selection set"
		# TODO: Check arguments
		# ['out', 'retval'] pCount:int
		return self.com_parent.Count


class AcadXRecord(POINTER(_dll.IAcadXRecord), _ez_ptr):
	"TODO: ADD DOC"
	#IAcadXRecord
	#	IAcadObject
	#		IDispatch
	#			IUnknown
	#				object
	# Prototype for IAcadXRecord VBA-class wrapped as AcadXRecord python-class
	# TODO list:
		# 1. COM-types to python-types vars and props
		# 2. ByRef inputs/outputs
		# 3. Inherits
		# 4. __new__
		# 5. Aliases
		# 6. Overloads
		# 9999. Tests
	# Interfaced methods (remove after checking):
	#	_IAcadObject__com_Delete
	#	_IAcadObject__com_Erase
	#	_IAcadObject__com_GetExtensionDictionary
	#	_IAcadObject__com_GetXData
	#	_IAcadObject__com_SetXData
	#	_IAcadObject__com__get_Application
	#	_IAcadObject__com__get_Database
	#	_IAcadObject__com__get_Document
	#	_IAcadObject__com__get_Handle
	#	_IAcadObject__com__get_HasExtensionDictionary
	#	_IAcadObject__com__get_ObjectID
	#	_IAcadObject__com__get_ObjectName
	#	_IAcadObject__com__get_OwnerID
	#	_IAcadXRecord__com_GetXRecordData
	#	_IAcadXRecord__com_SetXRecordData
	#	_IAcadXRecord__com__get_Name
	#	_IAcadXRecord__com__get_TranslateIDs
	#	_IAcadXRecord__com__set_Name
	#	_IAcadXRecord__com__set_TranslateIDs
	# Methods
	def getxrecorddata(self):
		"Gets the extended record data (XRecordData) associated with a dictionary"
		# TODO: Check arguments
		# ['out'] XRecordDataType:tagVARIANT
		# ['out'] XRecordDataValue:tagVARIANT
		# VBA: object.GetXRecordData XRecordDataType, XRecordDataValue
		return self.com_parent.GetXRecordData()

	def setxrecorddata(self, XRecordDataType: tagVARIANT, XRecordDataValue: tagVARIANT):
		"Sets the extended record data (XRecordData) associated with a dictionary"
		# TODO: Check arguments
		# ['in'] XRecordDataType:tagVARIANT
		# ['in'] XRecordDataValue:tagVARIANT
		# VBA: object.SetXRecordData XRecordDataType, XRecordDataValue
		self.com_parent.SetXRecordData(XRecordDataType, XRecordDataValue)

	# Properties
	@indexedproperty
	def name(self) -> str:
		"Specifies the name of the object"
		# TODO: Check arguments
		# ['out', 'retval'] bstrName:str
		return self.com_parent.Name
	@name.setter
	def _(self, bstrName:str):
		# ['in'] bstrName:str
		self.com_parent.Name = bstrName

	@indexedproperty
	def translateids(self) -> bool:
		"Specifies the translation of any contained object IDs during deepClone or wblockClone operations"
		# TODO: Check arguments
		# ['out', 'retval'] xlateIds:bool
		return self.com_parent.TranslateIDs
	@translateids.setter
	def _(self, xlateIds:bool):
		# ['in'] xlateIds:bool
		self.com_parent.TranslateIDs = xlateIds

	