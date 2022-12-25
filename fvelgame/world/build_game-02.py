#------------------------------------------------------------------------------#

'''This script builds a Game example.

Author: Luis D'Afonseca
Name:   Student

Description
A confident student runs from studying and seeks only playing video games.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld 

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 02: Student...')

    path_resources   = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects' 
    path_sounds      = path_resources/'sounds'
    path_games       = path_resources/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    meta.soft_name        = 'Student'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = 'A confident student runs from studying and seeks only playing video games.'
    meta.soft_icon        = None

    # Game 
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = -2
    meta.game_ambience   = None

    # Appearance
    #--------------------------------------------------------------------------#

    meta.background_image   = MetaImage(color=(55,55,55))
    meta.background_scrolls = False
    
    meta.track_image = MetaImage(color=(102,153,153))
    meta.scoreboard  = MetaScoreboard(text_rect    = (200,15,100,100),
                                      text_bgcolor = (55,55,55))

    # Player
    #--------------------------------------------------------------------------#

    path_player = path_objects/'confident_student.png'
    imag_player = MetaImage((90,140), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = -10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    # Image sizes
    # file = [ (110,143), (168,130), (92,124),
    #          (207,155), (203,103), (166,111), 
    #          (135,147), (204,114), (227,148) ]
    sizes = [ (80,104),  (100,77), (80,108), 
              (100,75),  (100,51), (100,67),
              (100,109), (100,56), (160,104) ]

    for ii in range(9):
        
        path_obstacle = path_objects / f'book-{ii+1}.png'
        imag_obstacle = MetaImage(sizes[ii], path=path_obstacle)

        meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = -100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    # Image sizes
    # file = [ (197, 133), (224, 221), (227, 219), (168, 223), (202, 133) ]
    sizes = [ (100,68), (100,99), (100,96), (80,106), (100,66) ]

    for ii in range(5):
        path_collectible = path_objects / f'video_game_controller-{ii+1}.png'
        imag_collectible = MetaImage(sizes[ii], path=path_collectible)
        meta.collectibles.append(MetaObject(imag_collectible, points))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction( 0.25, 0.005 )
    meta.margins  = MarginFunctions ( 0.12, 0.900 )

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/'student.game'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#
