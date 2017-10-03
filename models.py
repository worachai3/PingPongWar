import arcade
import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player1 = Player(20, 300)
        self.player2 = Player(580, 300)

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

    def on_key_press(key, key_modifiers):
        if key == arcade.key.w:
            pass

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        pass
