#------------------------------------------------------------------------------#

'''This script builds a Game example

Author: Luis D'Afonseca
Name:   Deep Sea

Description
An underwater adventure
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, BoundaryFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 03: Deep Seas')

    path_resources   = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'
    path_games       = path_resources/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'deep_sea.game'
    meta.soft_name        = 'Deep Sea'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = "Uma aventura em baixo d'água"
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = None

    # Appearance
    #--------------------------------------------------------------------------#

    meta.background_image   = MetaImage(path=path_backgrounds/'deep_sea_background.png')
    meta.background_scrolls = True

    meta.track_image   = MetaImage(color=(0, 91, 223))
    meta.track_scrolls = False
    meta.track_kills   = (False, True)

    path_font = path_fonts/'Party_Confetti.ttf'
    meta.scoreboard = MetaScoreboard(image=MetaImage(color=(55,55,55),size=(230,100)),
                                     image_position=(153,13),
                                     text_font      = path_font,
                                     text_font_size = 28,
                                     text_spacing   = 1,
                                     text_position  = (160,20),
                                     text_bgcolor   = (55,55,55))

    # Player
    #--------------------------------------------------------------------------#

    imag_player = MetaImage(path=path_objects/'submarine.png')
    meta.player = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage(path=path_objects/'mine.png')
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(path=path_objects/'diver-01.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))

    imag_collectible = MetaImage(path=path_objects/'diver-02.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('0.25 + 0.005*t')
    meta.boundary = BoundaryFunctions('0.18', '0.9 + 0.1*sin(pi*x/4)')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

