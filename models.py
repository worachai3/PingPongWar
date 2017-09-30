import arcade
import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        pass
