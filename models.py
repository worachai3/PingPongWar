import arcade
from random import randint
from ping_pong_war import BALL_SCALE

POTION_SCALE = 0.3

TIMER = 5

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
        potion_type = randint(0, 5)
        # Test potion
        #potion_type = 0 # L_Potion
        #potion_type = 1 # Sh_Potion
        #potion_type = 2 # Sp_Potion
        #potion_type = 3 # Sl_Potion
        #potion_type = 4 # P_Potion
        #potion_type = 5 # Con_Potion
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
        self.speed = 7
        self.extra_height = extra_height
        self.height = 100+self.extra_height
        self.score = 0
        self.accel = accel
        self.sp_potion = False
        self.sp_potion_time = 0
        self.sl_potion = False
        self.sl_potion_time = 0
        self.p_potion = False
        self.con_potion = False
        self.con_potion_time = 0

        self.hit_box_x = 10
        self.hit_box_y = self.height//2

    def update(self, delta):
        self.y += self.speed*self.accel
        self.height = 100+self.extra_height
        self.hit_box_y = self.height//2
        if self.y+self.height//2 >= self.world.height or self.y-self.height//2 <= 0:
            self.accel = 0
        if self.y+self.height//2 >= self.world.height:
            self.y = self.world.height - self.height//2
        if self.y-self.height//2 <= 0:
            self.y = self.height//2

        # Sp potion effect
        if self.sp_potion:
            self.sp_potion_time += delta
            self.speed = 15
            if self.sp_potion_time >= TIMER or self.sl_potion:
                self.sp_potion_time = 0
                self.sl_potion_time = 0
                self.sp_potion = False
                self.sl_potion = False
                self.speed = 7

        # Sl potion effect
        if self.sl_potion:
            self.sl_potion_time += delta
            self.speed = 3
            if self.sl_potion_time >= TIMER or self.sp_potion:
                self.sp_potion_time = 0
                self.sl_potion_time = 0
                self.sp_potion = False
                self.sl_potion = False
                self.speed = 7

        # Con potion effect
        if self.con_potion:
            self.con_potion_time += delta
            if self.con_potion_time >= TIMER:
                self.con_potion_time = 0
                self.con_potion = False

    def get_effect(self, potion_type):
        # L Potion
        if potion_type == 0:
            if self.height + 100 > self.world.height:
                return
            if self.height <= self.world.height:
                self.extra_height += 100

        # Sh Potion
        if potion_type == 1:
            if self == self.world.player1:
                if self.world.player2.extra_height > 0:
                    self.world.player2.extra_height -= 100
            if self == self.world.player2:
                if self.world.player1.extra_height > 0:
                    self.world.player1.extra_height -= 100


        # Sp Potion
        if potion_type == 2:
            self.sp_potion = True

        # Sl Potion
        if potion_type == 3:
            if self == self.world.player1:
                self.world.player2.sl_potion = True
            elif self == self.world.player2:
                self.world.player1.sl_potion = True

        # P Potion
        if potion_type == 4:
            self.p_potion = True

        # Con Potion
        if potion_type == 5:
            if self == self.world.player1:
                self.world.player2.con_potion = True
            elif self == self.world.player2:
                self.world.player1.con_potion = True

class Potions(arcade.Sprite):
    def __init__(self, world, potion_type, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.world = world
        self.potion_type = potion_type

        # Set position
        self.center_x = self.world.width//2
        self.center_y = randint(40, self.world.height-40)
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
        self.center_y = randint(20, self.world.height-20)
        self.speed = 8
        self.scale = scale
        self.hit_box_x = Ball.HIT_BOX_X*self.scale
        self.hit_box_y = Ball.HIT_BOX_Y*self.scale
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
            if self.world.player1.p_potion:
                self.speed = 15
                self.world.player1.p_potion = False
            else:
                self.speed = 8
        if (self.hit(self.world.player2, self.hit_box_x+self.world.player2.hit_box_x, self.hit_box_y+self.world.player2.hit_box_y)) and self.accel_x == 1:
            self.accel_x = -1
            if self.world.player2.p_potion:
                self.speed = 15
                self.world.player2.p_potion = False
            else:
                self.speed = 8
        # Out
        if self.center_x-self.hit_box_x <= 0:
            self.world.player2.score += 1
            if self.world.player2.score < 15:
                print('Player1 Score: {}    Player2 Score: {}'.format(self.world.player1.score, self.world.player2.score))
                self.respawn(2)
        if self.center_x+self.hit_box_x >= self.world.width:
            self.world.player1.score += 1
            if self.world.player1.score < 15:
                self.respawn(1)
                print('Player1 Score: {}    Player2 Score: {}'.format(self.world.player1.score, self.world.player2.score))


        # Bounce (wall)
        if self.center_y-self.hit_box_y <= 0 or self.center_y+self.hit_box_y >= self.world.height:
            self.accel_y *= -1

    def respawn(self, side):
        self.center_x = self.world.width//2
        self.center_y = randint(0, self.world.height)
        self.speed = 6
        self.hit_box_x = Ball.HIT_BOX_X*self.scale
        self.hit_box_y = Ball.HIT_BOX_Y*self.scale
        if side == 1:
            self.accel_x = -1
        else:
            self.accel_x = 1
        if randint(0,1) == 1:
            self.accel_y = 1
        else:
            self.accel_y = -1
        

    def hit(self, other, hit_size_x, hit_size_y):
        return (abs(self.center_x - other.x) <= hit_size_x) and (abs(self.center_y - other.y) <= hit_size_y)
