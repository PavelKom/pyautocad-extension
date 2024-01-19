import pythoncom, win32com.client, comtypes
from comtypes.client import GetModule, CreateObject

# https://timgolden.me.uk/pywin32-docs/pythoncom.html
# Get VBA dll and iterate all types
dll = pythoncom.LoadTypeLib('C:\\Program Files\\Common Files\\microsoft shared\\VBA\\VBA7.1\\apc71.dll')
print(path, "\n",dll,"\n")

for index in range(0, dll.GetTypeInfoCount()):
	#doc = dll.GetDocumentation(index)
	#print(doc)
	
	type_name = doc[0]
	try:

		type_iid = dll.GetTypeInfo(index).GetTypeAttr().iid
		stat = win32com.client.Dispatch(type_iid)
		print(type_name)
		print("\t", type_iid)
		print("\t\t", stat)
	except:
		pass

# Creating COM object from dll
dll2 = GetModule(
    'C:\\Program Files\\Common Files\\microsoft shared\\VBA\\VBA7.1\\apc71.dll')
print(dll2)
# Create new Collection from VBA library
coll = CreateObject(dll2.Collection)
print(coll)
print(coll.Count())