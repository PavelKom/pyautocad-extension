from comtypes import POINTER
from comtypes.automation import IDispatch
from comtypes.client import GetEvents, ShowEvents
from comtypes.client import GetModule, CreateObject, GetActiveObject

from event_sink import _AcadEventDumper
from api import acad_dll #TODO: api -> .api
_dll = acad_dll.dll

