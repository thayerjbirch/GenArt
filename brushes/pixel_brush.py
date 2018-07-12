from components.sources.brushes import Brush, PriorityTracker
from components.canvas import Canvas

class SinglePixelBrush(Brush):
    def __init__(self, canvas, settings_dict):
        self.canvas = canvas
        self.priority = PriorityTracker(settings_dict.get("priority", 0))

    def alter_pixels(self, x, y, rgb):
        '''Returns a boolean in case the source wants to die when it reaches
           a pixel with greater priority'''
        canvas.alter_pixel(x, y, rgb, priority)
        return True
