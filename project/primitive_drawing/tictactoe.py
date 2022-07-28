#import arcade module
import arcade

#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "Tic-Tac-Toe"

#open window
arcade.open_window(screen_width, screen_height, screen_title)

#set background color
arcade.set_background_color(arcade.color.MINT)
#start render
arcade.start_render()

#drawing code here
arcade.draw_line(10, 200, 590, 200, arcade.color.WHITE, 10)
arcade.draw_line(10, 400, 590, 400, arcade.color.WHITE, 10)

arcade.draw_line(200, 10, 200, 590, arcade.color.WHITE, 10)
arcade.draw_line(400, 10, 400, 590, arcade.color.WHITE, 10)

#finish render
arcade.finish_render()
#run
arcade.run()
