import arcade
import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player1 = Player(20, 300, 0)
        self.player2 = Player(580, 300, 0)

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

    def on_key_press(self, key, key_modifiers):
        print(key)
        if key == arcade.key.W and self.player1.y < 600:
            print("p1 up")
            self.player1.move('UP')
        elif key == arcade.key.S and self.player1.y > 0:
            print("p1 down")
            self.player1.move('DOWN')
        else:
            pass
        if key == arcade.key.UP and self.player2.y < 600:
            print("p1 up")
            self.player2.move('UP')
        elif key == arcade.key.DOWN and self.player2.y > 0:
            print("p2 down")
            self.player2.move('DOWN')
        else:
            pass

class Player:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

    def update(self, delta):
        self.y += 5*self.v
        if self.y >= 600 or self.y <= 0:
            self.v = 0

    def move(self, direction):
        if direction == 'UP':
            self.v = 1
        elif direction == 'DOWN':
            self.v = -1
