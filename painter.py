import numpy as np
import scipy.misc as smp
import sources as sources
import logging as log
from canvas import Canvas

class Painter():
    def __init__(self, settings):
        self.canvas = Canvas(settings)
        log.info(settings)
        log.info(settings.get("sources"))
        log.info(type(settings["sources"]))
        self.sources = [sources.get_source(s)(settings, self.canvas)
                        for s in settings.get("sources", [])]

    def sources_are_finished():
        #return any([x.
        pass

    def do_art():
        #while not
        pass
