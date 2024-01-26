#!/usr/bin/env python
# -*- coding: utf-8 -*-
from comtypes.client import GetModule, CreateObject, GetActiveObject
from pathlib import Path
from . import get_win_os_disk


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
