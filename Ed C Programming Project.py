import pygame, os, math
pygame.init()

#chooses monitor one as the monitor to display the window on
os.environ['SDL_VIDEO_CENTERED'] = "1"

#sets the screen width and height
screen_width = 1440
screen_height = 810

#creates the screen the game will run on
screen = pygame.display.set_mode((screen_width, screen_height))

#initialises the clock which will be used to set an FPS for the game
Clock = pygame.time.Clock()

#continuous game loop
running = True

#main game loop
while running:

	#needed for closing the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.flip
	Clock.tick(30)
