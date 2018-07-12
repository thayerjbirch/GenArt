import numpy as np
import random
from brushes import PriorityTracker

class Canvas():
    def __init__(self, settings_dict):
        settings_dict["width"] = settings_dict.get("width", random.choice([1366, 1920, 2436, 2560, 3440, 3200, 3840]))
        settings_dict["height"] = settings_dict.get("height", random.choice([768, 1080, 1125, 1920, 1440, 1800, 2160]))
        self.max_x = settings_dict["width"]
        self.max_y = settings_dict["height"]

        self.pixels = np.zeros((self.max_x, self.max_y, 3))
        self.priorities = [[PriorityTracker(-1) for _ in range(self.max_x)] for _ in range(self.max_y)]

    def alter_pixel(self, x, y, rgb, priority):
        if priority.is_greater(self.priorities[x][y]):
            self.pixels[x][y] = rgb
            self.priorities[x][y] = priority
            return True
        return False
