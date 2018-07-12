import logging as log
import importlib
import sys
import inspect
from abc import ABCMeta, abstractmethod
from pathlib import Path

class Source():
    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def is_finished():
        pass

available_sources = {}

def get_source(source_settings_dict):
    log.info("sources:" + str(available_sources))
    try:
        key = source_settings_dict["type"]
        if key in available_sources:
            return available_sources["key"]
    except:
        raise Exception("Invalid type provided for source type: {}"
                        .format(source_settings_dict.get("type", "none")))

def populate_sources():
    for path in __path__:
        for name in sorted(Path(path).glob('*.py')):
            if name.name.startswith('__'):#skip __init__.py
                continue
            members = inspect.getmembers(sys.modules[__name__])
            for name, value in members:
                if "random" in name:
                    print(name)
                if "random" in str(value):
                    print(value)
                if value == Source:
                    continue
                if not inspect.isclass(value) or not issubclass(value, Source):
                    continue
                available_sources[value.key] = value

for path in __path__:
    print("__path__", __path__, "path", path)
    for name in sorted(Path(path).glob('*.py')):
        if "random" in str(name):
            print('hi')
        print("name", name, ":\n")
        if name.name.startswith('__'):#skip __init__.py
            continue
        members = inspect.getmembers(sys.modules[__name__])
        for name, value in members:
            print("    name", name, "\n    value", value, "\n\n")
            if "random" in name:
                print(name)
            if "random" in str(value):
                print(value)
            if value == Source:
                continue
            if not inspect.isclass(value) or not issubclass(value, Source):
                continue
            available_sources[value.key] = value
