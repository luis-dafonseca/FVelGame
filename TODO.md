
# FVelGame

## In progress...

## TODO

- Implement build structure

### New features

- Implement achievements: 5 stars, the creator choses the score of each star
- Implement a initial screen
- Implement print screen

#### Game engine

- Implement variable tracks
  - Take care of spawning objects outside screen
- Implement blits of track and background images using mask
- Add transparent option to MetaImage
- Stop computing elapsed_time when showing the help message
- Use get_bounding_rect() to get objects real rectangle
- Implement save MetaWorld storing all resources files in a zip directory

#### Games

- Ship on ocean colecting precious stones and chests
  - Vertical scrolling

- student
  - Adjust confident student image to better scale down
  - add sounds
  - add background
  - add track image

#### Graphical Interface

- Export track mask
- Implement callbacks
- Implement undo
- Set proper maximum values to positions and sizes based on vertical em horizontal scrolling
- Replace minimum/maximum to left/rigth or top/bottom depending on scrooling direction

- Implement simple media player
  - play, stop, pause, quit

- Implement appearence preview

- Scoreboard
  - Allow creator to choose what is show on scoreboard
  - Allow creator to write a scoreboard title
  - GUI
    - Show preview using selected font
    - Implement font selection

- Implement a simple image editor 
  - Set size
  - Fill with color
  - Load image
  - Add transparency
  - Rotate and flip
  - Crop
  - Zoom

### Bugs

- Remove delay before playing sounds

### Windows

- Create instalator and standalony executable

## DONE

- Implement track scrolling
- Implement function evaluation
- Configure default Qt theme to show button bar icons
- Allow creator to make margins kill the player
- Replace select by edit on image forms
- On object forms
  - Add a duplicate button
  - Replace select by edit button

2022-12-31
- Take care of background images smaller than screen

2022-12-30
- Size of OST is now defined by font size 
- Fist scratch of image editor dialog

2022-12-28
- Keep ratio of images 
- Replace os.system by QProcess
- Scoreboard
  - Add font selection
  - Merge label and buttons on color selection

2022-12-27
- Implement horizontal scrolling background

2022-12-22
- Events
  - Deal with pygame.ACTIVEEVENT events as the display gains and loses input focus
  - Control the event queue pygame.event.set_allowed()
- Compute elapsed time using pygame function
- racing
  - add sound to treasure catch
  - add oil spill
  - add background
  - add track image

2022-12-21
- Load a scoreboard background image
- Allow creator to define sound volume for each sprite, 1 is the music volume

2022-12-20
- GUI - Implement open game file, to allow selection playing by the interface
- Show game information on help
- Implement scrolling background
- game_world.py: Take scrolling direction in account
- game_world.py: Compute OST size properly
- engine.py:     Take care when the track is smaller than the object
- Sound
  - Reimplement mute do stop music
  - Implement volume control
- Help message must be aware of vertical or horizontal scrolling
- Implement the scoreboard display
- Use a system font that offers unicode support

2022-12-17
- Improve collision boundaries on transparent pngs
- Game: Student running from study
  - Horizontal scrolling
- Volume Control
  - [-] decrease volume - decided to not implement
  - [+] increase volume - decided to not implement
  - [M] toggle mute
- Implement Horizontal scrolling
- Add elapsed time to scoreboard

## GAVE UP

2022-12-28 - Replaced by adding selected fonts to resources
- OST
  - Create a table os equivalent fonts in all systems
  - Select the fonts presente on all systems

