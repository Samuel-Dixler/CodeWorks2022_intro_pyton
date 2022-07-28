import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"

def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 10, arcade.csscolor.BLACK, 0, 180, 5)
    arcade.draw_arc_outline(x + 20, y, 20, 10, arcade.csscolor.BLACK, 0, 180, 5)

def cloud(x, y):
    arcade.draw_circle_filled(x, y, 20, arcade.color.WHITE)

    arcade.draw_circle_filled(x + 30, y + 5, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 60, y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 60, y - 10, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 90, y - 2, 20, arcade.color.WHITE)

    arcade.draw_circle_filled(x + 15, y + 25, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 45, y + 33, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 75, y + 20, 20, arcade.color.WHITE)


def main():
    arcade.open_window(screen_width, screen_height, screen_title)
    #set background color
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render( )

    #call drawing functioncs
    cloud(100, 100)
    cloud(400, 200)
    cloud(300, 500)
    cloud(200, 300)

    draw_bird(300,400)

    draw_bird(250,350)
    draw_bird(350,350)

    draw_bird(300,300)
    draw_bird(200,300)
    draw_bird(400,300)

    draw_bird(250,250)
    draw_bird(350,250)
    draw_bird(150,250)
    draw_bird(450,250)

    draw_bird(300,200)
    draw_bird(200,200)
    draw_bird(400,200)
    draw_bird(100,200)
    draw_bird(500,200)

    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
