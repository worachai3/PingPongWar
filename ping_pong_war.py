import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class PingPongWarWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.player1_sprite = arcade.Sprite('images/Player1.png')
        self.player1_sprite.set_position(20, 300)

        self.player2_sprite = arcade.Sprite('images/Player2.png')
        self.player2_sprite.set_position(580, 300)

    def on_draw(self):
        arcade.start_render()

        self.player1_sprite.draw()
        self.player2_sprite.draw()

def main():
    window = PingPongWarWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
