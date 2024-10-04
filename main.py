import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
		
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0))

		for updatables in updatable:
			updatables.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
		
		for drawables in drawable:
			drawables.draw(screen) 

		pygame.display.flip()
		
		dt = clock.tick(60) / 1000
	



if __name__ == "__main__":
	main()	
