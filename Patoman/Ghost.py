import random
import pygame
from pygame.locals import *
import Matriz

matriz = Matriz.mat();

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

Inky = 0
Blinky = 1
Clyde = 2
Pinky = 3

SCATTER = 0
CHASE = 1
EATEN = 2
FRIGHTENED = 3
LEAVE = 4

TS = 8

Blinky_img = pygame.Surface((16,16))
Blinky_img.fill((255,0,0))

Inky_img = pygame.Surface((16,16))
Inky_img.fill((19,249,226))

Clyde_img = pygame.Surface((16,16))
Clyde_img.fill((209,239,13))

Pinky_img = pygame.Surface((16,16))
Pinky_img.fill((218,15,245))

class Ghost(pygame.sprite.Sprite):
	
	def __init__(self, type_ghost):
		self.ghost = type_ghost
		
		if(self.ghost == Inky):
			self.pos = (22 * TS, 36 * TS)
			self.img = Inky_img
		if(self.ghost == Blinky):
			self.pos = (27 * TS, 28 * TS)
			self.img = Blinky_img
		if(self.ghost == Clyde):
			self.pos = (32 * TS, 36 * TS)
			self.img = Clyde_img
		if(self.ghost == Pinky):
			self.pos = (27 * TS, 36 * TS)
			self.img = Pinky_img
			
		self.mode = LEAVE
		
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.img.get_rect()
		self.rect.x = 6*TS
		self.rect.y = 8*TS
		self.direct = LEFT
		
		self.box = False
		
		self.moviments = 0
	
	def dis(self, x, y):
		return (self.target[0] - x) ** 2 + (self.target[1] - y) ** 2
	
	def change_direct(self):
		
		if(self.direct == UP):
			self.direct = DOWN
		elif(self.direct == DOWN):
			self.direct = UP
		elif(self.direct == RIGHT):
			self.direct = LEFT
		elif(self.direct == LEFT):
			self.direct = RIGHT
	
	def move(self, x, y, direct, redx, redy, coins_left):
		possible_moviments = []
		
		self.moviments += 1
		
		if(self.mode == SCATTER):
			if(self.ghost == Inky):
				self.target = (71, 55)
			if(self.ghost == Blinky):
				self.target = (-1, 52)
			if(self.ghost == Clyde):
				self.target = (71, 0)
			if(self.ghost == Pinky):
				self.target = (-1, 4)
			
			#Find possible Moviments for Ink
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]// TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1 and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 4):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
			
			if(self.moviments == 112):
				self.mode = CHASE
				self.moviments = 0
				
				self.change_direct()
		elif(self.mode == FRIGHTENED):
		
			#Find possible Moviments
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS + 1) % 56, RIGHT])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56, LEFT])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1 and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 4):
				possible_moviments.append([self.pos[1] // TS + 1, self.pos[0] // TS, DOWN])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)): can = False
				
				if(can):
					possible_moviments.append([self.pos[1] // TS - 1, self.pos[0] // TS, UP])
			
			#Choose a random direction
			random_direct = random.choice(possible_moviments)
			self.pos = (random_direct[1] * TS, random_direct[0] * TS)
			self.rect.x = random_direct[1] * TS
			self.rect.y = random_direct[0] * TS
			self.direct = random_direct[2]
			
			if(self.moviments == 192):
				if(coins_left < 80 and self.ghost == Blinky):
					self.mode = CHASE
				else:
					self.mode = SCATTER
				self.moviments = 0
				self.change_direct()
		
		elif(self.mode == EATEN):
			
			if(self.box):
				if(self.ghost == Inky):
					self.target = (36, 22)
				if(self.ghost == Blinky):
					self.target = (36, 27)
				if(self.ghost == Clyde):
					self.target = (36, 32)
				if(self.ghost == Pinky):
					self.target = (36, 27)
			else: 
				self.target = (28, 27)
			
			#Find possible Moviments
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
			
			if(self.target[0] == (self.pos[1] // TS) and self.target[1] == (self.pos[0] // TS)):
				
				if(self.box):
					self.mode = LEAVE
					self.change_direct()
				else:
					self.box = True
				
				self.moviments = 0
		elif(self.mode == CHASE):
			if(self.ghost == Inky):
				self.target = (x - (redx - x), y - (redy - y))
				
			if(self.ghost == Blinky):
				self.target = (x, y)
			if(self.ghost == Clyde):
				self.target = (x, y)
				if(self.dis(self.pos[1] // TS, self.pos[0] // TS) < 256):
					self.target = (71, 0)
			if(self.ghost == Pinky):
				if(direct == LEFT):
					self.target = (x, y - 8)
				if(direct == RIGHT):
					self.target = (x, y + 8)
				if(direct == DOWN):
					self.target = (x + 8, y)
				if(direct == UP):
					self.target = (x - 8, y - 8)		
			#Find possible Moviments
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1 and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 4):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
			
			if(self.moviments == 320):
				
				if(coins_left < 80 and self.ghost == Blinky):
					self.mode = CHASE
				else:
					self.mode = SCATTER
					self.change_direct()
					
				self.moviments = 0
		elif(self.mode == LEAVE):
			self.target = (28, 27)
			
			#Find possible Moviments
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
			
			if(self.target[0] == (self.pos[1] // TS) and self.target[1] == (self.pos[0] // TS)):
				if(coins_left < 80 and self.ghost == Blinky):
					self.mode = CHASE
				else:
					self.mode = SCATTER
				
				self.change_direct()
					
				self.moviments = 0
		
	def display(self):
		screen.blit(self.img,(self.pos[0]-4,self.pos[1]-8))
		