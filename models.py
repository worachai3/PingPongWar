import arcade
import arcade.key
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#        self.player1 = Player(20, 300, 0)
#        self.player2 = Player(580, 300, 0)
        self.player1 = Player(20, height/2, 0, 5)
        self.player2 = Player(width-20, height/2, 0, 5)

        self.ball = Ball(width/2, randint(0,width), randint(0,1), randint(0,1), 3 )

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

        self.ball.update(delta)
        self.ball_bounce(delta)
        if randint(1,10) <= 1:
            self.potion = Potions(300, randint(0,600), randint(0,1))

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
            print("p2 up")
            self.player2.move('UP')
        elif key == arcade.key.DOWN and self.player2.y > 0:
            print("p2 down")
            self.player2.move('DOWN')
        else:
            pass

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W and self.player1.y < 600:
            print("p1 STOP u")
            self.player1.move('STOP')
        elif key == arcade.key.S and self.player1.y > 0:
            print("p1 STOP d")
            self.player1.move('STOP')
        else:
            pass
        if key == arcade.key.UP and self.player2.y+35 < 600:
            print("p2 STOP u")
            self.player2.move('STOP')
        elif key == arcade.key.DOWN and self.player2.y-35 > 0:
            print("p2 STOP d")
            self.player2.move('STOP')
        else:
            pass

    def ball_bounce(self, delta):
        if ((self.ball.x >= self.player1.x-5 and self.ball.x <= self.player1.x+5) 
        and (self.ball.y >= self.player1.y-35 and self.ball.y <= self.player1.y+35)
        and self.ball.vx == -1):
            self.player1.speed += 1
            self.ball.speed += 1
            self.ball.bounce()

        if ((self.ball.x >= self.player2.x-5 and self.ball.x <= self.player2.x+5) 
        and (self.ball.y >= self.player2.y-38 and self.ball.y <= self.player2.y+38)
        and self.ball.vx == 1):
            self.player2.speed += 1
            self.ball.speed += 1
            self.ball.bounce()

class Player:
    def __init__(self, x, y, v, speed):
        self.x = x
        self.y = y
        self.v = v
        self.speed = speed

    def update(self, delta):
        self.y += self.speed*self.v
        if self.y >= 600:
            self.y = 0
        elif self.y <= 0:
            self.y = 600

    def move(self, direction):
        if direction == 'UP':
            self.v = 2
        elif direction == 'DOWN':
            self.v = -2
        elif direction == 'STOP':
            self.v = 0

class Ball:
    def __init__(self, x, y, vx, vy, speed):
        self.x = x
        self.y = y
        self.speed = speed
        if vx == 1:
            self.vx = vx
        else:
            self.vx = -1
        if vy == 1:
            self.vy = vy
        else:
            self.vy = -1

    def update(self, delta):
        self.x += self.speed*self.vx
        self.y += self.speed*self.vy

        if self.x >= 800 or self.x <= 0:
            self.x = 400
            self.y = randint(0,600)
            self.speed = 3
            if randint(0,1) == 1:
                self.vx = 1
            else:
                self.vy = -1

        if self.y >= 600 or self.y <= 0:
            self.vy *= -1

    def bounce(self):
        self.vx *= -1

    def out(self):
        if self.x >= 800 or self.x <= 0:
            return True

class Potions:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        if v == 1:
            self.v = v
        else:
            self.v = -1

    def update(self, delta):
        self.x += 3*self.vx
        self.y += 3*self.vy
        
        if self.y >= 600 or self.y <= 0:
            self.vy *= -1
