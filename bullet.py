import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage Bullets from the Ship"""
	def __init__(self,ai_game):
		"""Create a bullet object at the ship current possition"""

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings		
		self.color = self.settings.bullet_color

		#create a bullet rect at (0,0) and them set correct possition

		self.rect = pygame.Rect(0,0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#store the bullets position as a decimal value

		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen"""
		#Update the decimal position of the bullet
		self.y -= self.settings.bullet_speed
		#Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw bullet into  th screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)
