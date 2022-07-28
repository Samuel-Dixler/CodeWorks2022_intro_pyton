#import arcade module
import arcade
#define screen properties (width, height, and title)
width = 600
height = 600
title = "Coffee Cup"
#open window
arcade.open_window(width, height, title)
#set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#start render
arcade.start_render()
#drawing code here
arcade.draw_polygon_filled(((50, 550),
                            (350, 550),
                            (300, 100),
                            (100, 100)
                            ),
                           arcade.csscolor.WHITE)

img = arcade.load_texture('starbucks.png')
arcade.draw_texture_rectangle(200, 400, 200, 200, img)


#finish render
arcade.finish_render()
#run
arcade.run()
