#!/usr/bin/env python
# -*- coding: utf-8 -*-
from comtypes.client import GetModule, CreateObject
from pathlib import Path
from . import get_win_os_disk
import re


_pattern = 'apc[0-9]+.dll'


class VBA(object):
	_path = ""
	_dll = None
	_version = ""
	def __init__(self):
		"""
		Create VBA library manager
		"""
		p = Path(get_win_os_disk() + ":\\Program Files\\Common Files\\microsoft shared\\VBA")
		for f in p.rglob("apc*.dll"):
			if re.match(_pattern, f.name):
				self._path = str(f)
		self._version = self._path.split("\\")[-1].replace("apc", "").replace(".dll", "")
		self._dll = GetModule(self._path)
	
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
	
	def CreateObject(self, cls):
		return CreateObject(self._dll.cls)
		
	def new_collection(self):
		return CreateObject(self._dll.Collection)
