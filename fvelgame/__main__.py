#!/usr/bin/python
# ./fvelgame/__main__.py
#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
sys.path.append('./world')
sys.path.append('./game' )
sys.path.append('./ui'   )

import fvelgame

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    fvelgame.main( sys.argv )

#------------------------------------------------------------------------------#
