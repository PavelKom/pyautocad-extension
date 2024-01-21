import pythoncom, win32com.client, comtypes
from comtypes.client import GetModule, CreateObject
from ctypes import c_int, c_char_p

# https://timgolden.me.uk/pywin32-docs/pythoncom.html
# Get VBA dll and iterate all types
dll = pythoncom.LoadTypeLib('C:\\Program Files\\Common Files\\microsoft shared\\VBA\\VBA7.1\\apc71.dll')
print(dll)

for index in range(0, dll.GetTypeInfoCount()):
	doc = dll.GetDocumentation(index)
	#print(doc)
	typee = dll.GetTypeInfo(index)
	type_name = doc[0]
	#try:
	print(type_name)
	print("\t", typee.GetFuncDesc(index))
		#type_iid = dll.GetTypeInfo(index).GetTypeAttr().iid
		#print("\t", type_iid)
		#stat = win32com.client.Dispatch(type_iid)
		#print("\t\t", stat)
	#except:
	#	pass
print("a")

# Creating COM object from dll
dll2 = GetModule(
    'C:\\Program Files\\Common Files\\microsoft shared\\VBA\\VBA7.1\\apc71.dll')
print(dll2)
print("a")
# Create new Collection from VBA library
coll = CreateObject(dll2.Collection)
print(coll)
coll.Add(50, "a")
for i in range(10):
	coll.Add(i)
coll.Add(100, "b")
d = dict()
d["Item"] = 200
d["Key"] = "A"
coll.Add(**d)
print(coll.Count())
for i in range(1,coll.Count()+1):
	print(coll.Item(i))
# For PowerShell
# (Get-WmiObject Win32_OperatingSystem).SystemDrive for getting OS drive
# For cmd
# python -m win32com.client.makepy -i
