#!/usr/bin/env python
# -*- coding: utf-8 -*-
from comtypes.client import GetModule, CreateObject, GetActiveObject
from pathlib import Path
from __init__ import get_win_os_disk #TODO: __init__ -> .


class AcadDLL:
    _adll = None
    _path = ""
    _dll = None
    _version = ""
    # Avoid multiply connections.
    def __new__(cls, *args, **kwargs):
        if AcadDLL._adll is None:
            return super().__new__(cls)
        return AcadDLL._adll
    
    def __init__(self):
        """
        Create Autocad library manager
        """
        p = Path(get_win_os_disk() + r":\Program Files\Common Files\Autodesk Shared")
        for f in p.rglob("acax*enu.tlb"):
            self._path = str(f)
        self._version = self._path.split("\\")[-1].replace("acax", "").replace("enu.tlb", "")
        self._dll = GetModule(self._path)
        AcadDLL._adll = self
    
    @property
    def dll(self):
        return self._dll
        
    @property
    def path(self):
        return self._path
    
    @property
    def version(self):
        return self._version

    def get_types_info(self) -> tuple:
        import pythoncom
        dll = pythoncom.LoadTypeLib(self._path)
        return [dll.GetDocumentation(index) for index in range(0, dll.GetTypeInfoCount())]
    
    def get_my_dir(self):
        return dir(self._dll)
        
    def __call__(self):
        return self._dll

# Global AutoCAD library manager
acad_dll = AcadDLL()

__all__ = (
"acad_dll",
)



# for debugging
# get list of all Acad interfaces with methods and props
if __name__ == "__main__":
    import os
    path = os.path.dirname(__file__).replace("\\", "/") + "/"
    dump = ""
    for obj in dir(acad_dll.dll):
        if not obj.startswith("IAcad"):
            continue
        dump += "\n" + obj + "\n"
        cls = getattr(acad_dll.dll, obj)
        for method in dir(cls):
            if not method.startswith("_IAcad"):
                continue
            dump += "\t"+ method + "\n"
    f = open(path + "dump_api.txt", "w")
    f.write(dump)
    f.close()
    


