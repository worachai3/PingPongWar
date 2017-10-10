import arcade
import arcade.key

from random import randint

class BouncingObject:
    def __init__(self, world, x, y, vx, vy, speed):
        self.world = world
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

        if self.x >= self.world.width or self.x <= 0:
            self.x = self.world.width/2
            self.y = randint(1, self.world.height-1)
        if self.y >= self.world.height or self.y <= 0:
            self.vy *= -1

    def hit(self, other, hit_size_x, hit_size_y):
        return (abs(self.x - other.x) <= hit_size_x) and (abs(self.y - other.y) <= hit_size_y)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player1 = Player(self, 20, height/2, 0, 5)
        self.player2 = Player(self, width-20, height/2, 0, 5)

        self.ball = Ball(self, width/2, randint(0,width), randint(0,1), randint(0,1), 3 )

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

        self.ball.update(delta)
#        if randint(1,10) <= 1:
#            self.potion = Potions(self, self.width/2, randint(0,self.height), randint(0,1))

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
        if key == arcade.key.W and self.player1.y < self.height:
            print("p1 STOP u")
            self.player1.move('STOP')
        elif key == arcade.key.S and self.player1.y > 0:
            print("p1 STOP d")
            self.player1.move('STOP')
        else:
            pass
        if key == arcade.key.UP and self.player2.y+35 < self.height:
            print("p2 STOP u")
            self.player2.move('STOP')
        elif key == arcade.key.DOWN and self.player2.y-35 > 0:
            print("p2 STOP d")
            self.player2.move('STOP')
        else:
            pass

class Player:
    HIT_BOX_X = 10
    HIT_BOX_Y = 37.5
    def __init__(self, world, x, y, v, speed):
        self.world = world
        self.x = x
        self.y = y
        self.v = v
        self.speed = speed

    def update(self, delta):
        self.y += self.speed*self.v
        if self.y >= self.world.height:
            self.y = 0
        elif self.y <= 0:
            self.y = self.world.height
        #print('Player:{} {}'.format(self.x, self.y))

    def move(self, direction):
        if direction == 'UP':
            self.v = 2
        elif direction == 'DOWN':
            self.v = -2
        elif direction == 'STOP':
            self.v = 0

class Ball(BouncingObject):
    HIT_BOX_X = 15
    HIT_BOX_Y = 15
    def __init__(self, world, x, y, vx, vy, speed):
        super().__init__(world, x, y, vx, vy, speed)

    def update(self, delta):
        #print('Ball: {} {}'.format(self.x, self.y))
        super().update(delta)
        self.bounce()

    def bounce(self):
        if self.vx == -1 and super().hit(self.world.player1, self.HIT_BOX_X+Player.HIT_BOX_X, self.HIT_BOX_Y+Player.HIT_BOX_Y):
            self.vx *= -1
        if self.vx == 1 and super().hit(self.world.player2, self.HIT_BOX_X+Player.HIT_BOX_X, self.HIT_BOX_Y+Player.HIT_BOX_Y):
            self.vx *= -1

    def out(self):
        if self.x >= self.world.width or self.x <= 0:
            return True
'''
class L_Potion(Potions):
    def __init__(self, world, x, y, v):
        self.x = x
        self.y = y
        if v == 1:
            self.v = v
        else:
            self.v = -1

    def update(self, delta):
        self.x += 3*self.vx
        self.y += 3*self.vy

        if self.y >= self.world.height or self.y <= 0:
            self.vy *= -1
'''
