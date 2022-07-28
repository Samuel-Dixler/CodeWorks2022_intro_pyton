#import arcade module
import arcade

#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "New Game"

#open window
arcade.open_window(screen_width, screen_height, screen_title)

#set background color
arcade.set_background_color(arcade.color.SKY_BLUE)
#start render
arcade.start_render()

#drawing code here
arcade.draw_circle_filled(300, 300, 100, arcade.color.YELLOW)


arcade.draw_line(100, 300, 500, 300, arcade.color.YELLOW, 10)
arcade.draw_line(300, 500, 300, 100, arcade.color.YELLOW, 10)

arcade.draw_line(150, 450, 450, 150, arcade.color.YELLOW, 10)
arcade.draw_line(150, 150, 450, 450, arcade.color.YELLOW, 10)


#finish render
arcade.finish_render( )
#run
arcade.run()
