#------------------------------------------------------------------------------#

'''This script builds a Game example.

Author: Luis D'Afonseca
Name:   Racing

Description
Simple racing game with treasures and obstacles.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaWorld, MetaImage, MetaObject

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 01: Racing...')

    path_resources   = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_objects     = path_resources/'objects' 
    path_sounds      = path_resources/'sounds'
    path_games       = path_resources/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    meta.soft_name        = 'Racing'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = 'Simple racing game with treasures and obstacles'
    meta.soft_icon        = None

    # Game 
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True   
    meta.game_time_bonus = 1
    meta.game_ambience   = path_sounds/'music-1.mp3'

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'racing_background.png'
    imag_background = MetaImage( (1920,6000), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True
    
    meta.track_image      = None
    meta.scoreboard_image = None

    meta.scoreboard_text_position = (100,100)
    meta.scoreboard_text_bgcolor  = ( 55, 55, 55)
    meta.scoreboard_text_fgcolor  = (255,255,255)

    # Player
    #--------------------------------------------------------------------------#

    path_player = path_objects/'sport_car-1.png'
    imag_player = MetaImage((48,108), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 5

    # Obstacles
    #--------------------------------------------------------------------------#

    path_crash = path_sounds/'car_crash.mp3'   
    points     = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    for ii in range(2,10):
        
        path_obstacle = path_objects/f'sport_car-{ii}.png'
        imag_obstacle = MetaImage((40,90), path=path_obstacle)

        meta.obstacles.append(MetaObject(imag_obstacle, points, path_crash))

    # Collectibles
    #--------------------------------------------------------------------------#

    path_collect = path_sounds/'collect-ring.mp3'   
    points = 100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    for ii in range(1,5):

        path_collectible = path_objects/f'precious_stone-{ii}.png'
        imag_collectible = MetaImage((46,38), path=path_collectible)
        
        meta.collectibles.append(MetaObject(imag_collectible, points, path_collect))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction( 5.00, 0.50 )
    meta.margins  = MarginFunctions ( 0.35, 0.65 )

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/'racing.game'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#

