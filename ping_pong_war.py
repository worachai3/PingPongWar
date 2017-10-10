import arcade
import arcade.key

from models import World
from models import Player

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class PingPongWarWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.player1_sprite = ModelSprite('images/Player1.png',
                                          model=self.world.player1)
        self.player2_sprite = ModelSprite('images/Player2.png',
                                          model=self.world.player2)
        self.ball_sprite = ModelSprite('images/Ball.png',
                                       model=self.world.ball)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()

        self.player1_sprite.draw()
        self.player2_sprite.draw()
        self.ball_sprite.draw()

    def update(self, delta):
        self.world.update(delta)

def main():
    window = PingPongWarWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
