import arcade

arcade.open_window(800,600, "Drawing Example")

# Background color
arcade.set_background_color(
    arcade.color.BEAU_BLUE
    )


arcade.start_render()

# Draw the road
arcade.draw_lrtb_rectangle_filled(
    0,800, 100,0, arcade.color.BLACK
    )

# Set of lines through road

point_list = ((100, 50),
              (250, 50),
              (300, 50),
              (450, 50),
              (500, 50),
              (650, 50))
    
arcade.draw_lines(point_list, arcade.color.YELLOW, 300)

 


arcade.finish_render()



arcade.run()