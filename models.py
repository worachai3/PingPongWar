import arcade
import arcade.key
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player1 = Player(20, 300, 0)
        self.player2 = Player(580, 300, 0)

        self.ball = Ball(300, randint(0,600), randint(0,1), randint(0,1))

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

        self.ball.update(delta)
        self.ball_bounce(delta)

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

    def ball_bounce(self, delta):
        if ((self.ball.x >= self.player1.x-5 and self.ball.x <= self.player1.x+5) 
        and (self.ball.y >= self.player1.y-38 and self.ball.y <=
            self.player1.y+38)
        and self.ball.vx == -1):
            self.ball.bounce()

        if ((self.ball.x >= self.player2.x-5 and self.ball.x <= self.player2.x+5) 
        and (self.ball.y >= self.player2.y-38 and self.ball.y <= self.player2.y+38)
        and self.ball.vx == 1):
            self.ball.bounce()

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

class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        if vx == 1:
            self.vx = vx
        else:
            self.vx = -1
        if vy == 1:
            self.vy = vy
        else:
            self.vy = -1

    def update(self, delta):
        self.x += 3*self.vx
        self.y += 3*self.vy
        '''
        if self.x >= 600 or self.x <= 0:
            self.vx *= -1
        '''
        if self.y >= 600 or self.y <= 0:
            self.vy *= -1

    def bounce(self):
        self.vx *= -1
