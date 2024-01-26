#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .types import com_parse_dict

def dict_fix(kw: dict):
	# Remove all items with None value
	kk = []
	for k, v in kw.items():
		if v is None:
			kk.append(k)
	for k in kk:
		kw.pop(k)

def arr_cont(var):
	try:
		res = []
		for v in var:
			res.extend(_cont(v))
		return res
	except:
		return [var]


def arr_check(var, t):
	try:
		for item in var:
			if not isinstance(item, t):
				raise TypeError("Variable '{0}' from '{1}' must be '{2}'".format(item, var, t))
	except:
		if not isinstance(var, t):
			raise TypeError("Variable '{0}' must be '{1}'".format(var, t))


def recast(com_obj_ptr):
	if not isinstance(com_obj_ptr,	POINTER):
		raise TypeError("Can't recast {0}".format(com_obj_ptr))
	if com_obj_ptr.ObjectName in com_parse_dict.keys():
		com_obj_ptr.__class__ = com_parse_dict[key]
	else:
		pass
	return com_obj_ptr