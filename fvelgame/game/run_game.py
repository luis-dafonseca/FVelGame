#------------------------------------------------------------------------------#

import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import argparse
import pygame

from world.game_world import GameWorld
from world.meta_world import MetaWorld
from game.engine      import Engine

#------------------------------------------------------------------------------#
def main(path):
    '''
    This function runs the game

    arg can be a file name with a MetaWorld or a MetaWorld itself
    '''

    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_mode( (0,0), pygame.FULLSCREEN )

    if path:
        meta = MetaWorld.load(path)
    else:
        meta = MetaWorld()

    world  = GameWorld(meta)
    engine = Engine  (world)
    
    while True:
    
        # Restart engine and waits for user press any key
        if not engine.start():
            break
    
        # Main game loop
        if not engine.game_loop():
            break

    return 0

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='FVelGame')
    parser.add_argument( 'world', help='Game World file name', nargs='?' )
    args = parser.parse_args()

    sys.exit( main(args.world) )

#------------------------------------------------------------------------------#
