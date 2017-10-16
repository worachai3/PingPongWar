import arcade
import arcade.key
from models import *

BALL_SCALE = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

TIMER = 2

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.game_over = False

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Timer
        self.timer = 0

        # Sprites lists
        self.all_sprites_list = arcade.SpriteList()
        self.ball_sprites_lsit = arcade.SpriteList()
        self.potion_sprites_list = arcade.SpriteList()

        self.player1 = self.world.player1
        self.player2 = self.world.player2

        image_list = ('images/ball.png')
        ball_sprites = Ball(self, 'images/ball.png', BALL_SCALE)
        self.all_sprites_list.append(ball_sprites)

    def on_draw(self):
        # Render the Screen
        arcade.start_render()

        self.all_sprites_list.draw()
        #output = f"Score: {self.score}"
        arcade.draw_rectangle_filled(self.player1.x, self.player1.y, 20, self.player1.height, arcade.color.YELLOW, 0)
        arcade.draw_rectangle_filled(self.player2.x, self.player2.y, 20, self.player2.height, arcade.color.BLUE, 0)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W :
            self.player1.accel = 0
        if key == arcade.key.S :
            self.player1.accel = 0
        if key == arcade.key.UP:
            self.player2.accel = 0
        if key == arcade.key.DOWN:
            self.player2.accel = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W :
            self.player1.accel = 1
        if key == arcade.key.S :
            self.player1.accel = -1
        if key == arcade.key.UP:
            self.player2.accel = 1
        if key == arcade.key.DOWN:
            self.player2.accel = -1

    def update(self, delta):
        self.world.update(delta)

        # Draw all sprites
        for items in self.all_sprites_list:
            items.update(delta)

        # Timer count
        self.timer += delta
        if self.timer <= TIMER:
            return
        self.timer = 0
        '''
        # Spawn potions
        potion_list = ('images/lo_potion.png',
                       'images/sh_potion.png',
                       'images/sp_potion.png',
                       'images/sl_potion.png',
                       'images/p_potion.png',
                       'images/con_potion.png',)
        if randint(1,10) <= 10:
            potion_type = randint(0,5)
            if potion_type == 0:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 1:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 2:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 3:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 4:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            elif potion_type == 5:
                potion = Potions(self, potion_type, potion_list[potion_type], POTION_SCALE)
            self.potion_sprites_list.append(potion)
        '''
        self.all_sprites_list.append(self.world.spawn_potion())

def main():
    window = GameWindow()

    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
