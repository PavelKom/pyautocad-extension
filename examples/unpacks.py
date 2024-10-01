# ...\Lib\site-packages\comtypes\gen\_5732349B_A023_4237_BA1D_6DFCFBAD5E64_0_1_0.py
import inspect
import  comtypes.gen.AutoCAD as acadlib
import os
import re
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += r"\raw_classes2.py"

'''
for n in dir(acadlib):
	if n.startswith("IAcad"):
		c = getattr(acadlib, n)
		for m in c._methods_:
			print(*m)
		print()
'''
pytype_parse_dict = {
	'BSTR': 'str', # byte string
	'c_long': 'int',
	'c_ulong': 'int',
	'c_double': 'float',
	'VARIANT_BOOL': 'bool',
	#'tagVARIANT': 'Any', # VARIANT
	
	# REMOVE AFTER TESTS
	#'POINTER(IUnknown)': None,
	#'POINTER(IDispatch)': None,
	#'SAFEARRAY_tagVARIANT': None,
}
pytype_parse_dict2 = {
	'POINTER(IAcadAcCmColor)': 'AcadAcCmColor',
	'POINTER(IAcadView)': 'AcadView',
	'POINTER(IAcadViewport)': 'AcadViewport',
	'POINTER(IAcadUCS)': 'AcadUCS',
	'POINTER(IAcadToolbar)': 'AcadToolbar',
	'POINTER(IAcadMenuGroup)': 'AcadMenuGroup',
	'POINTER(IAcadApplication)': 'AcadApplication',
	'POINTER(IAcadToolbarItem)': 'AcadToolbarItem',
	'POINTER(IAcad3DSolid)': 'Acad3DSolid',
	'POINTER(IAcadRegion)': 'AcadRegion',
	'POINTER(IAcadDocument)': 'AcadDocument',
	'POINTER(IAcadPreferences)': 'AcadPreferences',
	'POINTER(IAcadMenuGroups)': 'AcadMenuGroups',
	'POINTER(IAcadMenuBar)': 'AcadMenuBar',
	'POINTER(IAcadDocuments)': 'AcadDocuments',
	'POINTER(IAcadState)': 'AcadState',
	'POINTER(IAcadEntity)': 'AcadEntity',
	'POINTER(IAcad3DFace)': 'Acad3DFace',
	'POINTER(IAcadPolygonMesh)': 'AcadPolygonMesh',
	'POINTER(IAcad3DPolyline)': 'Acad3DPolyline',
	'POINTER(IAcadArc)': 'AcadArc',
	'POINTER(IAcadAttribute)': 'AcadAttribute',
	'POINTER(IAcadCircle)': 'AcadCircle',
	'POINTER(IAcadDimAligned)': 'AcadDimAligned',
	'POINTER(IAcadDimAngular)': 'AcadDimAngular',
	'POINTER(IAcadDimDiametric)': 'AcadDimDiametric',
	'POINTER(IAcadDimRotated)': 'AcadDimRotated',
	'POINTER(IAcadDimOrdinate)': 'AcadDimOrdinate',
	'POINTER(IAcadDimRadial)': 'AcadDimRadial',
	'POINTER(IAcadEllipse)': 'AcadEllipse',
	'POINTER(IAcadLeader)': 'AcadLeader',
	'POINTER(IAcadMText)': 'AcadMText',
	'POINTER(IAcadPoint)': 'AcadPoint',
	'POINTER(IAcadLWPolyline)': 'AcadLWPolyline',
	'POINTER(IAcadPolyline)': 'AcadPolyline',
	'POINTER(IAcadRay)': 'AcadRay',
	'POINTER(IAcadShape)': 'AcadShape',
	'POINTER(IAcadSolid)': 'AcadSolid',
	'POINTER(IAcadSpline)': 'AcadSpline',
	'POINTER(IAcadText)': 'AcadText',
	'POINTER(IAcadTolerance)': 'AcadTolerance',
	'POINTER(IAcadTrace)': 'AcadTrace',
	'POINTER(IAcadXline)': 'AcadXline',
	'POINTER(IAcadBlockReference)': 'AcadBlockReference',
	'POINTER(IAcadHatch)': 'AcadHatch',
	'POINTER(IAcadRasterImage)': 'AcadRasterImage',
	'POINTER(IAcadLine)': 'AcadLine',
	'POINTER(IAcadLayout)': 'AcadLayout',
	'POINTER(IAcadMInsertBlock)': 'AcadMInsertBlock',
	'POINTER(IAcadPolyfaceMesh)': 'AcadPolyfaceMesh',
	'POINTER(IAcadMLine)': 'AcadMLine',
	'POINTER(IAcadDim3PointAngular)': 'AcadDim3PointAngular',
	'POINTER(IAcadDatabase)': 'AcadDatabase',
	'POINTER(IAcadExternalReference)': 'AcadExternalReference',
	'POINTER(IAcadTable)': 'AcadTable',
	'POINTER(IAcadDimArcLength)': 'AcadDimArcLength',
	'POINTER(IAcadDimRadialLarge)': 'AcadDimRadialLarge',
	'POINTER(IAcadSection)': 'AcadSection',
	'POINTER(IAcadMLeader)': 'AcadMLeader',
	'POINTER(IAcadBlock)': 'AcadBlock',
	'POINTER(IAcadModelSpace)': 'AcadModelSpace',
	'POINTER(IAcadPaperSpace)': 'AcadPaperSpace',
	'POINTER(IAcadBlocks)': 'AcadBlocks',
	'POINTER(IAcadGroups)': 'AcadGroups',
	'POINTER(IAcadDimStyles)': 'AcadDimStyles',
	'POINTER(IAcadLayers)': 'AcadLayers',
	'POINTER(IAcadLineTypes)': 'AcadLineTypes',
	'POINTER(IAcadDictionaries)': 'AcadDictionaries',
	'POINTER(IAcadRegisteredApplications)': 'AcadRegisteredApplications',
	'POINTER(IAcadTextStyles)': 'AcadTextStyles',
	'POINTER(IAcadUCSs)': 'AcadUCSs',
	'POINTER(IAcadViews)': 'AcadViews',
	'POINTER(IAcadViewports)': 'AcadViewports',
	'POINTER(IAcadLayouts)': 'AcadLayouts',
	'POINTER(IAcadPlotConfigurations)': 'AcadPlotConfigurations',
	'POINTER(IAcadDatabasePreferences)': 'AcadDatabasePreferences',
	'POINTER(IAcadSummaryInfo)': 'AcadSummaryInfo',
	'POINTER(IAcadSectionManager)': 'AcadSectionManager',
	'POINTER(IAcadMaterials)': 'AcadMaterials',
	'POINTER(IAcadObject)': 'AcadObject',
	'POINTER(IAcadDictionary)': 'AcadDictionary',
	'POINTER(IAcadXRecord)': 'AcadXRecord',
	'POINTER(IAcadDimStyle)': 'AcadDimStyle',
	'POINTER(IAcadPlot)': 'AcadPlot',
	'POINTER(IAcadLayer)': 'AcadLayer',
	'POINTER(IAcadLineType)': 'AcadLineType',
	'POINTER(IAcadTextStyle)': 'AcadTextStyle',
	'POINTER(IAcadPViewport)': 'AcadPViewport',
	'POINTER(IAcadSelectionSets)': 'AcadSelectionSets',
	'POINTER(IAcadSelectionSet)': 'AcadSelectionSet',
	'POINTER(IAcadUtility)': 'AcadUtility',
	'POINTER(IAcadMaterial)': 'AcadMaterial',
	'POINTER(IAcadHyperlinks)': 'AcadHyperlinks',
	'POINTER(IAcadGroup)': 'AcadGroup',
	'POINTER(IAcadHyperlink)': 'AcadHyperlink',
	'POINTER(IAcadPopupMenu)': 'AcadPopupMenu',
	'POINTER(IAcadPopupMenus)': 'AcadPopupMenus',
	'POINTER(IAcadToolbars)': 'AcadToolbars',
	'POINTER(IAcadPlotConfiguration)': 'AcadPlotConfiguration',
	'POINTER(IAcadPopupMenuItem)': 'AcadPopupMenuItem',
	'POINTER(IAcadPreferencesFiles)': 'AcadPreferencesFiles',
	'POINTER(IAcadPreferencesDisplay)': 'AcadPreferencesDisplay',
	'POINTER(IAcadPreferencesOpenSave)': 'AcadPreferencesOpenSave',
	'POINTER(IAcadPreferencesOutput)': 'AcadPreferencesOutput',
	'POINTER(IAcadPreferencesSystem)': 'AcadPreferencesSystem',
	'POINTER(IAcadPreferencesUser)': 'AcadPreferencesUser',
	'POINTER(IAcadPreferencesDrafting)': 'AcadPreferencesDrafting',
	'POINTER(IAcadPreferencesSelection)': 'AcadPreferencesSelection',
	'POINTER(IAcadPreferencesProfiles)': 'AcadPreferencesProfiles',
	'POINTER(IAcadRegisteredApplication)': 'AcadRegisteredApplication',
	'POINTER(IAcadSectionSettings)': 'AcadSectionSettings',
	'POINTER(IAcadSectionTypeSettings)': 'AcadSectionTypeSettings',
}

def parse_type(val):
	name = val.__name__
	m = 1
	if name.startswith("LP_"):
		name = name[3:]
		m = -1
	if name in pytype_parse_dict.keys():
		return m*1
	elif name in pytype_parse_dict2.keys():
		return m*2
	
	return 0

def is_parsed(val):
	name = val
	if name.startswith("LP_"):
		name = name[3:]
	if name in pytype_parse_dict.keys():
		return True
	elif name in pytype_parse_dict2.keys():
		return True
	
	return False

def pytype_parse(val):
	name = val.__name__
	if name.startswith("LP_"):
		name = name[3:]
	if name in pytype_parse_dict.keys():
		return pytype_parse_dict[name]
	elif name in pytype_parse_dict2.keys():
		return pytype_parse_dict2[name]
	if name.startswith("LP_"):
		return name.replace(".LP_",".")
	return name





class Prop:
	def __init__(self, name, doc=None, getter=None, setter=None):
		self.name = name
		self.doc = doc
		self.getter = getter
		self.setter = setter
		self.args_get = []
		self.args_set = []
	
	def add_getter_args(self, m):
		for i, arg in enumerate(m.paramflags):
			self.args_get.append(Argument(arg, m.argtypes[i]))
	def add_setter_args(self, m):
		for i, arg in enumerate(m.paramflags):
			self.args_set.append(Argument(arg, m.argtypes[i]))
		
	def __str__(self):
		if len(self.args_get) == 0:
			buffer = "@property\n"
		else:
			buffer = "@indexedproperty\n"
		buffer += "def {}(self".format(self.name.lower())
		is_todo = False
		if self.getter is not None:
			outp = "???"
			for arg in self.args_get:
				if arg.is_retval:
					outp = arg.type
				elif arg.is_in:
					buffer += ", {}:{}".format(arg.name, arg.type)
				is_todo = is_todo or parse_type(arg.raw_type) != 1
			buffer += ") -> {}".format(outp)
		else:
			buffer += ")"
		buffer += ":\n"
		if self.doc is not None:
			buffer += "\t\"{}\"\n".format(self.doc)
		if is_todo:
			buffer += "\t# TODO: Check arguments\n"
		is_todo = False
		for arg in self.args_get:
			buffer += "\t# {}\n".format(arg)
		if self.getter is None:
			buffer += "Exception(\"Can't GET {} value\") ".format(self.name)
		else:
			buffer += "\treturn self.com_parent.{}".format(self.getter)
			for i in range(len(self.args_get)-1):
				buffer += "[{}]".format(self.args_get[i].name)
			buffer += "\n"
		if self.setter is not None:
			buffer += "@{}.setter\ndef _(self".format(self.name.lower())
			for arg in self.args_set:
				buffer += ", {}:{}".format(arg.name, arg.type)
				is_todo = is_todo or parse_type(arg.raw_type) != 1
			buffer += "):\n"
			if is_todo:
				buffer += "\t# TODO: Check arguments\n"
			ret = ""
			for arg in self.args_set:
				buffer += "\t# {}\n".format(arg)
				ret = arg.name
			if len(self.args_set) == 1:
				buffer += "\tself.com_parent.{} = {}\n".format(self.setter, ret)
			else:
				buffer += "\tself.com_parent.{}".format(self.setter)
				for i in range(len(self.args_set)-1):
					buffer += "[{}]".format(self.args_set[i].name)
				buffer += " = {}\n".format(ret)
		return buffer
	__repr__ = __str__
	
	def __lt__(self, obj):
		return ((self.name) < (obj.name))
	def __gt__(self, obj):
		return ((self.name) > (obj.name))
	def __le__(self, obj):
		return ((self.name) <= (obj.name))
	def __ge__(self, obj):
		return ((self.name) >= (obj.name))
	def __eq__(self, obj):
		return (self.name == obj.name)

class Method:
	def __init__(self, method):
		self.method = method
		#self.data = [*method]
		self.name = method.name
		self.doc = method.doc
		self.args = []
		for i, arg in enumerate(method.paramflags):
			self.args.append(Argument(arg, method.argtypes[i]))
	
	def __str__(self):
		buffer = "def {}(self".format(self.name.lower())
		buffer2 = ""
		buffer3 = "object.{} ".format(self.name)
		buf_args = ""
		buf_inputs = ""
		has_ret_val = False
		has_ret = 0
		ret_type = ""
		is_todo = False
		for arg in self.args:
			if parse_type(arg.raw_type) != 1:
				is_todo = True
			if arg.is_out:
				has_ret += 1
				if ret_type == "":
					ret_type = arg.type
			if arg.is_retval:
				buffer3 = "{} = {}".format(arg.name, buffer3)
				has_ret_val = True
			else:
				buf_args += "{}, ".format(arg.name)
			buffer2 += "\t# {}\n".format(arg)
			if arg.is_in:
				buffer += ", {}: {}".format(arg.name, arg.type)
				buf_inputs += "{}, ".format(arg.name)
		if buf_args.endswith(", "):
			buf_args = buf_args[:-2]
		if buf_inputs.endswith(", "):
			buf_inputs = buf_inputs[:-2]
		if has_ret_val:
			buf_args = "({})".format(buf_args)
		buffer3 = "\t# VBA: {}{}\n\t".format(buffer3, buf_args)
		buffer += ")"
		if has_ret == 1:
			buffer += " -> {}".format(ret_type)
		buffer += ":\n\t\"{}\"\n".format(self.doc)
		if is_todo:
			buffer += "\t# TODO: Check arguments\n"
		buffer += buffer2
		buffer += buffer3 
		if has_ret > 0:
			buffer += "return "
		buffer += "self.com_parent.{}({})\n".format(self.name, buf_inputs)
		return buffer
		
	def __lt__(self, obj):
		return ((self.name) < (obj.name))
	def __gt__(self, obj):
		return ((self.name) > (obj.name))
	def __le__(self, obj):
		return ((self.name) <= (obj.name))
	def __ge__(self, obj):
		return ((self.name) >= (obj.name))
	def __eq__(self, obj):
		return (self.name == obj.name)
		

class Argument:
	def __init__(self, paramflags, type):
		self.raw_type = type
		self.type = pytype_parse(type)
		self.name = paramflags[1]
		self.flags = get_flags(paramflags[0])
	
	def __str__(self):
		return "{} {}:{}".format(self.flags, self.name, self.type)
		
	@property
	def is_in(self):
		return 'in' in self.flags
	@property
	def is_out(self):
		return 'out' in self.flags
	@property
	def is_retval(self):
		return 'retval' in self.flags
	@property
	def is_unknown(self):
		return len(self.flags) == 0



props = {}
methods = {}

def is_prop(method):
	return method.name.startswith("_get_") or method.name.startswith("_set_")

def cut_prop_gs(name):
	return name.replace("_get_","").replace("_set_","")

def get_flags(arg):
	flags = []
	if arg & 1:
		flags.append('in')
	if arg & 2:
		flags.append('out')
	if arg & 4:
		flags.append('4')
	if arg & 8:
		flags.append('retval')
	if arg & 16:
		flags.append('16')
	return flags
	
pprops = {}
mmethods = {}

def get_as_prop(c, m):
	global pprops
	if pprops.get(c) is None:
		pprops[c] = {}
	name = cut_prop_gs(m.name.lower())
	#data = [*m]
	#for arg in data[3]:
	#	print(",,",arg, get_flags(arg[0]))
	if name not in pprops[c].keys():
		pprops[c][name] = Prop(cut_prop_gs(m.name))
	if m.name.startswith("_get_"):
		pprops[c][name].getter = cut_prop_gs(m.name)
		pprops[c][name].add_getter_args(m)
	if m.name.startswith("_set_"):
		pprops[c][name].setter = cut_prop_gs(m.name)
		pprops[c][name].add_setter_args(m)
	pprops[c][name].doc = m.doc
		
		

def get_as_method(c, m):
	global mmethods
	name = m.name.lower()
	if mmethods.get(c) is None:
		mmethods[c] = {}
	mmethods[c][name] = Method(m)


def get_m(c, m):
	if is_prop(m):
		get_as_prop(c, m)
		return
	get_as_method(c, m)


for c in dir(acadlib):
	if not (c.startswith("IAcad") or c.startswith("_DAcad")):
		continue
	if getattr(acadlib, c)._methods_ is not None:
		#if getattr(acadlib, c)._methods_ is not None:
		#	print(c)
		for m in getattr(acadlib, c)._methods_:
			get_m(c, m)
ppmm = {}
for c, mm in mmethods.items():
	if ppmm.get(c) is None:
		ppmm[c] = []
	ppmm[c].append("# Methods")
	mkk = [*mm.keys()]
	mkk.sort()
	for mk in mkk:
		ppmm[c].append(str(mm[mk]))
for c, pp in pprops.items():
	if ppmm.get(c) is None:
		ppmm[c] = []
	ppmm[c].append("# Properties")
	pkk = [*pp.keys()]
	pkk.sort()
	for pk in pkk:
		ppmm[c].append(str(pp[pk]))

ckk = [*ppmm.keys()]
ckk.sort()

ent_buf = []
not_ent_buf = []
buf = ""
for ck in ckk:
	is_ent = False
	buf2 = "\n"
	buf2 += "class {}(POINTER(_dll.{}), _ez_ptr):".format(ck.replace("IAcad","Acad"), ck)
	buf2 += "\npass\n"
	#for i, mro in enumerate(inspect.getmro(getattr(acadlib, ck))):
	#	if mro.__name__ == "IAcadEntity" and ck != "IAcadEntity":
	#		buf2 += "# ENTITY"
	#		is_ent = True
	#buf2 += "\n\"TODO: ADD DOC\"\n"
	#for i, mro in enumerate(inspect.getmro(getattr(acadlib, ck))):
	#	buf2 += "#{}{}\n".format(i*"\t", mro.__name__)
	#buf2 += "# Prototype for {} VBA-class wrapped as {} python-class\n".format(ck, ck.replace("IAcad","Acad"))
	'''buf2 += """# TODO list:
	# 1. COM-types to python-types vars and props
	# 2. ByRef inputs/outputs
	# 3. Inherits
	# 4. __new__
	# 5. Aliases
	# 6. Overloads
	# 9999. Tests\n""" '''
	#buf2 += "# Interfaced methods (remove after checking):\n"
	#for m in dir(getattr(acadlib, ck)):
	#	if m.startswith("_IAcad"):
	#		buf2 += "#\t{}\n".format(m)
	#for pm in ppmm[ck]:
	#	buf2 += "{}\n".format(pm)
	#c = getattr(acadlib, ck)
	#print(c, "\n\t", "\n\t".join(dir(c)))
	#buf += buf2
	if is_ent:
		ent_buf.append(buf2)
	else:
		not_ent_buf.append(buf2)
	#break

for b in ent_buf:
	buf += b
for b in not_ent_buf:
	buf += b


buf = buf.replace("\n","\n\t").replace("\tclass", "class")
#print(buf.find("\t"))
re_tab = re.compile("\n[\t]+\n")
#print(dir(re_tab), "\n", re_tab.pattern)
while len(re_tab.findall(buf)) > 0:
	buf = re_tab.sub("\n\n", buf)
#pyperclip.copy(buf)

with open(dir_path, "w", encoding='utf-8') as f:
	f.write(buf)
	f.close()

