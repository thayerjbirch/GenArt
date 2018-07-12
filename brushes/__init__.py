import importlib
import logging as log
import sys
import inspect
from abc import ABCMeta, abstractmethod
from pathlib import Path

class Brush(metaclass=ABCMeta):
    def __init__(self, canvas, settings_dict):
        self.canvas = canvas
        self.priority = 0

    @abstractmethod
    def alter_pixels(self, x, y):
        pass

class PriorityTracker():
    def __init__(self, value=0):
        self.value = value

    def update_priority(self):
        '''typically will be used to decay priority'''
        pass

    def get_priority(self):
        return self.value

    def is_greater(self, comparison):
        return self.value > comparison.get_priority()


available_brushes = {}

def get_brush(brush_settings_dict):
    try:
        key = brush_settings_dict["type"]
        if key in available_brushes:
            return available_brushes["key"](brush_settings_dict)
    except:
        raise Exception("Invalid type provided for brush type: {}"
                        .format(brush_settings_dict.get("type", "none")))

for path in __path__:
    for name in sorted(Path(path).glob('*.py')):
        if name.name.startswith('__'):#skip __init__.py
            continue
        m = '.' + name.stem
        members = inspect.getmembers(sys.modules[__name__])
        for name, value in members:
            if value == Brush:
                continue
            if not inspect.isclass(value) or not issubclass(value, Brush):
                continue
            available_brushes[value.key] = value
log.info(available_brushes)
