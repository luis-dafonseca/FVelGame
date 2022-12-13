#------------------------------------------------------------------------------#
'''This module defines the GameWorld class.

The GameWorld class stores all parameters defined by the game creator
using pygame structures to be used directly by de Engine.
An instance of GameWoclass is created from an instance of MetaWorld.

Here the lengths are measured in pixels.
'''

# TODO take scrolling direction in account

#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp
from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
def surface_from_meta_image(meta):
    '''Create a pygame surface from a MetaImage object'''

    if meta.image_path:
        surf = pygame.image.load(meta.image_path).convert_alpha()
        surf = pygame.transform.scale(surf, meta.size )
    else:
        surf = pygame.Surface(meta.size)
        surf.fill(meta.color)

    return surf

#------------------------------------------------------------------------------#
class GameObjectParam:
    '''Stores all parameters needed to create game objects (sprite).'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create game object parameters from a meta object.'''

        self.image = surface_from_meta_image(meta.image)

        self.collision_score = meta.score
        self.collision_sound = meta.sound

#------------------------------------------------------------------------------#
class GameWorld:
    '''Manages all parameters needed by the game Engine.'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create a GameWorld from MetaWorld.'''

        self.vertical = meta.dynamics['vertical']
        self.ambience_sound = meta.ambience_sound

        # TODO Replace uniform distribution for a arrivel distribution
        self.obstacles_frequency = meta.dynamics['obstacles_frequency']
        self.treasures_frequency = meta.dynamics['treasures_frequency']

        self.obstacles_min_time =  100
        self.obstacles_max_time = 1000
        self.treasures_min_time =  500
        self.treasures_max_time = 4000

        self.score_time_bonus = meta.dynamics['score_time_bonus']

        self.ost_bgcolor = meta.appearance['ost_bgcolor']
        self.ost_fgcolor = meta.appearance['ost_fgcolor']

        self.player_speed   = meta.dynamics['player_speed']
        self.param_player   = GameObjectParam( meta.objects['player'   ] )
        self.param_obstacle = GameObjectParam( meta.objects['obstacles'] )
        self.param_treasure = GameObjectParam( meta.objects['treasures'] )

        # TODO Compute ost size properly
        self.ost_area = pygame.Rect( meta.appearance['ost_position'], (260,110) )
        
        # Background and track images
        self.background = surface_from_meta_image( meta.appearance['background'] )
        # self.track    = surface_from_meta_image( meta.appearance['track'     ] )

        # Geting constant track rectangle
        # TODO take horizontal scrolling in account
        margins    = meta.margins.eval(0)
        left       = int( gp.FULLHD_SIZE[0] * margins[0] )
        width      = int( gp.FULLHD_SIZE[0] * (margins[1]-margins[0]) )
        self.track = pygame.Rect( left, 0, width, gp.FULLHD_SIZE[1] )

        # Old method of drawing track on background
        color = meta.appearance['track'].color 
        pygame.draw.rect( self.background, color, self.track )

        self.velocity = meta.velocity

    #--------------------------------------------------------------------------#
    def eval_velocity(self, time):
        ''' Eval scrolling velocity in pixels'''

        # TODO take horizontal scrolling in account
        return int( self.velocity.eval(time) )

    #--------------------------------------------------------------------------#
    def eval_margins(self, time):
        ''' Eval margins in pixels'''

        pass

    #--------------------------------------------------------------------------#
    def get_track_boundaries(self):

        return { 
            'top':    [self.track.top,    self.track.left, self.track.right],
            'bottom': [self.track.bottom, self.track.left, self.track.right],
        }

#------------------------------------------------------------------------------#

