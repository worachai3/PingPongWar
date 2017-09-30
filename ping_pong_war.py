import arcade

from models import Player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class PingPongWarWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        
        self.player1 = Player(20, 300)
        self.player1_sprite = arcade.Sprite('images/Player1.png')
        
        self.player2 = Player(580, 300)
        self.player2_sprite = arcade.Sprite('images/Player2.png')

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()

        self.player1_sprite.draw()
        self.player2_sprite.draw()

    def update(self, delta):
        player1 = self.player1
        player2 = self.player2

        player1.update(delta)
        player2.update(delta)

        self.player1_sprite.set_position(player1.x, player1.y)
        self.player2_sprite.set_position(player2.x, player2.y)

def main():
    window = PingPongWarWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
