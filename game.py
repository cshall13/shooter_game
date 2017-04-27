# The reason you have access to this moduel, is because you reasonpip install pygame
# PYgame is NOT part of core (like math or random is)

import pygame

from player import Player
# import check_events from the game_functions module
from game_functions import *

# The core game functionality/loop
def run_game():
	# Init all the pygame stuff 
	pygame.init()
	# set up a tple for the xcreensize, (horiz,vert)
	screen_size = (1000,800)
	# set up a tupel for the background color
	background_color = (82,111,53) #<--- amounts of rgb out of 255
	# create a pygame screen to use
	screen = pygame.display.set_mode(screen_size)
	# set a caption on the terminal window
	pygame.display.set_caption("A heroic 3rd person shooter")
	the_player = Player(screen)
	# Main game loop. Run forever...(or until break)
	while 1:
		screen.fill(background_color)

		check_events()
		# Draw the player
		the_player.draw_me()
		# clear the screen for the next time through the loop
		pygame.display.flip()

# Start the game!
run_game()
