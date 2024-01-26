#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Collection(object):
    def __init__(self, obj=None):
		if obj is not None:
			self._me = obj
		else:
			# ToDo: Add CreateObject call. And get Collection classname (like Scripting.Dictionary)
			#self._me = 
			pass

    def Add(self, item, key=None, before=None, after=None):
		if self._me is None:
			return None
		if key is None and before is None and after is None:
			return self._me.Add(item)
		elif key is not None:
			if before is None and after is None:
				return self._me.Add(item, key)
			elif after is None:
				return self._me.Add(item, key, before)
			else:
				# ToDo: ??????????
				return self._me.Add(item, key, After:=after)
		
        kw = dict()
        kw["Item"] = item
        if key is not None:
            kw["Key"] = key
        if before is not None:
            kw["Before"] = before
        if after is not None:
            kw["after"] = after
        return self._add(kw)

    def _add(self, kwargs):
        self._me.Add(**kwargs)
        """
        match key, before, after:
            case None, None, None:
                self._me.Add(obj)
            case str(), None, None:
                self._me.Add(obj, key)
            case None, int(), None:
                """