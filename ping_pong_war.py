import arcade, arcade.key
from models import *

BALL_SCALE = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

TIMER = 2

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.started = False
        self.game_over = False
        self.end_score = 5
        self.background = None
        self.background = arcade.load_texture('images/background.png')

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Timer
        self.timer = 0

        # Sprites lists
        self.all_sprites_list = arcade.SpriteList()
        self.ball_sprites_lsit = arcade.SpriteList()

        self.player1 = self.world.player1
        self.player2 = self.world.player2

        image_list = ('images/ball.png')
        ball_sprites = Ball(self, 'images/ball.png', BALL_SCALE)
        self.all_sprites_list.append(ball_sprites)

    def on_draw(self):
        # Render the Screen
        arcade.start_render()
        if not self.game_over:
            arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

            self.all_sprites_list.draw()

            if not self.started:
                show_tutorial = False
                output = f"    Press Spacebar to start\nPress Enter to see potions list"
                self.score_text = arcade.create_text(output, arcade.color.BLACK,  14)
                arcade.render_text(self. score_text, self.width//2-135, 115)
            else:
                output = f"Player1: {self.world.player1.score}  Player2: {self.world.player2.score}"
                self.score_text = arcade.create_text(output, arcade.color.BLACK,  14)
                arcade.render_text(self. score_text, self.width//2-100, 100)

            arcade.draw_rectangle_filled(self.player1.x, self.player1.y, 20, self.player1.height, arcade.color.RED, 0)
            arcade.draw_rectangle_filled(self.player2.x, self.player2.y, 20, self.player2.height, arcade.color.BLUE, 0)

        else:
            if self.world.player1.score == self.end_score:
                output = f"Player 1 WIN {self.world.player1.score}:{self.world.player2.score}"
            elif self.world.player2.score == self.end_score:
                output = f"Player 2 WIN {self.world.player1.score}:{self.world.player2.score}"
            self.score_text = arcade.create_text(output, arcade.color.WHITE,  60)
            arcade.render_text(self. score_text, self.width//2-100, 100)


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W:
            self.player1.accel = 0
        if key == arcade.key.S:
            self.player1.accel = 0
        if key == arcade.key.UP:
            self.player2.accel = 0
        if key == arcade.key.DOWN:
            self.player2.accel = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W and not self.player1.con_potion:
            self.player1.accel = 1
        if key == arcade.key.S and not self.player1.con_potion:
            self.player1.accel = -1
        if key == arcade.key.UP and not self.player2.con_potion:
            self.player2.accel = 1
        if key == arcade.key.DOWN and not self.player2.con_potion:
            self.player2.accel = -1
        if key == arcade.key.W and self.player1.con_potion:
            self.player1.accel = -1
        if key == arcade.key.S and self.player1.con_potion:
            self.player1.accel = 1
        if key == arcade.key.UP and self.player2.con_potion:
            self.player2.accel = -1
        if key == arcade.key.DOWN and self.player2.con_potion:
            self.player2.accel = 1
        if key == arcade.key.SPACE:
            self.started = True

    def update(self, delta):
        if not self.game_over and self.started:
            self.world.update(delta)

            # Draw all sprites
            for items in self.all_sprites_list:
                if items != None:
                    items.update(delta)

            # Check game over
            if self.player1.score == self.end_score or self.player2.score == self.end_score:
                self.game_over = True

            # Timer count
            self.timer += delta
            if self.timer <= TIMER:
                return

            # Reset counter
            self.timer = 0
            if randint(1,10) <= 6:
                self.all_sprites_list.append(self.world.spawn_potion())

        elif self.game_over and self.started:
            self.remove_all_object()

    def remove_all_object(self):
            for items in self.all_sprites_list:
                if items != None:
                    items.kill()

def main():
    window = GameWindow()

    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
