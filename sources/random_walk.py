import random
from sources import Source

class RandomWalk(Source):
    key = "random_walk"

    def __init__(self, source_settings_dict, canvas):
        self.x = source_settings_dict.get("x", random.randint(settings["width"]))
        self.y = source_settings_dict.get("y", random.randint(settings["height"]))
        self.canvas = canvas
        pass

print("sanity check", issubclass(RandomWalk, Source))
