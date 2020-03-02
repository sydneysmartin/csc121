import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = " Drawing with Loops Example"


def draw_background():

    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 3, 
                                 SCREEN_WIDTH - 1, SCREEN_HEIGHT * 2 / 3, 
                                 arcade.color.SUNSET)

    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6, 
                                 SCREEN_WIDTH - 1, SCREEN_HEIGHT / 3, 
                                 arcade.color.DARK_SPRING_GREEN)


def draw_bird(x, y):

    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)

def draw_pine_tree(center_x, center_y):

    arcade.draw_rectangle_filled(center_x, center_y, 20, 40,
                                 arcade.color.DARK_BROWN)

    tree_bottom_y = center_y + 20

    point_list = ((center_x - 40, tree_bottom_y),
                  (center_x, tree_bottom_y + 100),
                  (center_x + 40, tree_bottom_y))
                
    arcade.draw_polygon_filled(point_list, arcade.color.DARK_GREEN)

birds = []
for i in range(10):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(SCREEN_HEIGHT / 3, SCREEN_HEIGHT - 20)
    birds.append([x, y])

def on_draw(delta_time):

    arcade.start_render()

    draw_background()
    
    for i, (x, y) in enumerate(birds):
        draw_bird (x, y)
        x += random.randrange(-2, 2)
        y += random.randrange(-2, 2)
        birds[i] = [x, y]
    
    for x in range(45, SCREEN_WIDTH, 90):
        draw_pine_tree(x, (SCREEN_HEIGHT / 3)) 




def main(): 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()

