# duh
import pygame
# we need sys for QUIT 
import sys

def check_events():
			 # the escape hatch (from while)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# The user clicked the red x. Get out of the loop and kill the game
			sys.exit()
