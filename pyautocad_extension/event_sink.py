from comtypes.client import GetEvents
from comtypes.client._events import EventDumper
from enum import Enum

from api import acad_dll #TODO: api -> .api
_dll = acad_dll.dll

class _AcadEventDumper(EventDumper):
    _main = None
    def __new__(cls, use_main=True):
        if use_main and cls._main is not None:
            return cls._main
        sink = EventDumper()
        sink.__class__ = cls
        if cls._main is None:
            cls._main = sink
        return sink

