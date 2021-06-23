import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):

    def __init__(self):
        super().__init__()
        self.set_text("☃")
        self._points = 0 
        self.reset()
        

    def reset(self):
        self._points = random.randint(1,5)
        position = Point(random.randint(1,constants.MAX_X-1),random.randint(1,constants.MAX_Y-1))
        self.set_position(position)

    def get_points(self):
        return self._points