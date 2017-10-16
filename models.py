import arcade
from random import randint

POTION_SCALE = 0.3

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player1 = Player(self, 20, height//2, 0, 0)
        self.player2 = Player(self, width-20, height//2, 0, 0)

        self.potion_sprite_list = arcade.SpriteList()

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

    def spawn_potion(self):
        # Spawn potions
        potion_list = ('images/lo_potion.png',
                       'images/sh_potion.png',
                       'images/sp_potion.png',
                       'images/sl_potion.png',
                       'images/p_potion.png',
                       'images/con_potion.png',)
        if randint(1,10) <= 10:
            #potion_type = randint(0,5)

            # Test potion
            potion_type = 0
            if potion_type == 0:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 1:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 2:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 3:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 4:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 5:
                return Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)

class Player:
    def __init__(self, world, x, y, extra_height, accel):
        self.world = world
        self.x = x
        self.y = y
        self.extra_height = extra_height
        self.height = 100+self.extra_height
        self.score = 0
        self.accel = accel

        self.hit_box_x = 10
        self.hit_box_y = self.height//2

    def update(self, delta):
        self.y += 5*self.accel
        self.height = 100+self.extra_height
        self.hit_box_y = self.height//2
        if self.y+self.height//2 >= self.world.height or self.y-self.height//2 <= 0:
            self.accel = 0
        if self.y+self.height//2 >= self.world.height:
            self.y = self.world.height - self.height//2
        if self.y-self.height//2 <= 0:
            self.y = self.height//2

    def get_effect(self, potion_type):
        if potion_type == 0:
            if self.height + 100 > self.world.height:
                return
            if self.height <= self.world.height:
                self.extra_height += 100

class Potions(arcade.Sprite):
    def __init__(self, world, potion_type, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.world = world
        self.potion_type = potion_type

        # Set position
        self.center_x = self.world.width//2
        self.center_y = randint(0, self.world.height)
        self.speed = 6

        # Check type
        if potion_type == 0:
            self.hit_box_x = 49*POTION_SCALE
            self.hit_box_y = 92*POTION_SCALE
        elif potion_type == 1:
            self.hit_box_x = 70*POTION_SCALE
            self.hit_box_y = 70*POTION_SCALE
        elif potion_type == 2:
            self.hit_box_x = 42*POTION_SCALE
            self.hit_box_y = 72*POTION_SCALE
        elif potion_type == 3:
            self.hit_box_x = 50*POTION_SCALE
            self.hit_box_y = 94*POTION_SCALE
        elif potion_type == 4:
            self.hit_box_x = 50*POTION_SCALE
            self.hit_box_y = 74*POTION_SCALE
        elif potion_type == 5:
            self.hit_box_x = 45*POTION_SCALE
            self.hit_box_y = 80*POTION_SCALE


        if randint(0,1) == 1:
            self.accel_x = 1
        else:
            self.accel_x = -1
        if randint(0,1) == 1:
            self.accel_y = 1
        else:
            self.accel_y = -1

    def update(self, delta):
        super().update()
        # Move
        self.center_x += self.speed*self.accel_x
        self.center_y += self.speed*self.accel_y

        # Hit (player1)
        if (self.hit(self.world.player1, self.hit_box_x+self.world.player1.hit_box_x, self.hit_box_y+self.world.player1.hit_box_y)) and self.accel_x == -1:
            self.world.player1.get_effect(self.potion_type)
            self.kill()

        # Hit (player2)
        if (self.hit(self.world.player2, self.hit_box_x+self.world.player2.hit_box_x, self.hit_box_y+self.world.player2.hit_box_y)) and self.accel_x == 1:
            self.world.player2.get_effect(self.potion_type)
            self.kill()

        # Remove
        if self.center_x-self.hit_box_x <= 0 or self.center_x+self.hit_box_x >= self.world.width:
            self.kill()

        # Bounce (wall)
        if self.center_y-self.hit_box_y <= 0 or self.center_y+self.hit_box_y >= self.world.height:
            self.accel_y *= -1

    def hit(self, other, hit_size_x, hit_size_y):
        return (abs(self.center_x - other.x) <= hit_size_x) and (abs(self.center_y - other.y) <= hit_size_y)


class Ball(arcade.Sprite):
    HIT_BOX_X = 15
    HIT_BOX_Y = 15
    def __init__(self, world, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.world = world
        self.center_x = self.world.width//2
        self.center_y = randint(0, self.world.height)
        self.speed = 6
        self.hit_box_x = Ball.HIT_BOX_X*scale
        self.hit_box_y = Ball.HIT_BOX_Y*scale
        if randint(0,1) == 1:
            self.accel_x = 1
        else:
            self.accel_x = -1
        if randint(0,1) == 1:
            self.accel_y = 1
        else:
            self.accel_y = -1

    def update(self, delta):
        super().update()
        # Move
        self.center_x += self.speed*self.accel_x
        self.center_y += self.speed*self.accel_y

        # Bounce (player)
        if (self.hit(self.world.player1, self.hit_box_x+self.world.player1.hit_box_x, self.hit_box_y+self.world.player1.hit_box_y)) and self.accel_x == -1:
            self.accel_x = 1
        if (self.hit(self.world.player2, self.hit_box_x+self.world.player2.hit_box_x, self.hit_box_y+self.world.player2.hit_box_y)) and self.accel_x == 1:
            self.accel_x = -1
        # Bounce (wall)
        '''
        if self.center_x-self.hit_box_x <= 0 or self.center_x+self.hit_box_x >= self.world.width:
            self.accel_x *= -1
        '''
        if self.center_y-self.hit_box_y <= 0 or self.center_y+self.hit_box_y >= self.world.height:
            self.accel_y *= -1

    def hit(self, other, hit_size_x, hit_size_y):
        return (abs(self.center_x - other.x) <= hit_size_x) and (abs(self.center_y - other.y) <= hit_size_y)
