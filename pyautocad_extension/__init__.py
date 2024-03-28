#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	pyautocad_extension 
	~~~~~~~~~

	Additional functions, variables, constant and classes for pyautocad module (https://pypi.org/project/pyautocad/ or https://github.com/reclosedev/pyautocad)

	:copyright: (c) 2024 by Pavel Komisarov aka PavelKom.
	:license: BSD, see LICENSE.md for more details.
"""

__docformat__ = 'restructuredtext en'
__version__ = '0.0.1'

import platform
if platform.system() != "Windows":
	raise Exception("This module created for OS Windows ONLY")


# From https://stackoverflow.com/questions/14508809/run-powershell-function-from-python-script
def get_win_os_disk() -> str:
	"""
	Get OS Windows installation disk from PowerShell application path
	:return: Disk symbol
	"""
	import subprocess
	process = subprocess.Popen("where powershell", stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW)
	stdout, stderr = process.communicate()
	stdout = stdout.decode('utf-8')
	powershell_path = stdout.strip()
	return powershell_path[0]


# AutoCAD
from api import * #TODO: api -> .api
'''
from .application import *
from .document import *
from .enum import *
from .geometry import *
from .blocks import *
'''

