#!/usr/bin/env python
# -*- coding: utf-8 -*-
from comtypes.client import GetModule, CreateObject
from pathlib import Path
import re

class VBA(object):
	_pattern = 'apc[0-9]+.dll'
	def __init__(self):
		"""
		Create VBA library manager
		"""
		_path = ""
		p = Path("C:/Program Files/Common Files/microsoft shared/VBA")
		for f in p.rglob("apc*.dll*"):
			print(f)
			if re.match(pattern, f.name):
				_path = f
		