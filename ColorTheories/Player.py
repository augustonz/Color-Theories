import pygame

class Player(pygame.sprite.Sprite):

         def __init__(self):
            self.pos = (216,416)

            self.direct = LEFT
            self.last_direct = LEFT
            self.memory_direct = LEFT
            self.change_direct = 0

            self.img_index=0
            self.imgs = [patoFC,patoFD,patoFB,patoFE,patoAC,patoAD,patoAB,patoAE]
            self.image = patoFC
            self.aberto=False
            
            
            self.rect = self.image.get_rect()

            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
            self.rect.height = 16
            self.rect.width = 16

            self.eaten_phantom = 0
            self.set_image()
            self.count = True

            self.time=0
            self.normal_speed=player_normal_speed
            self.fast_speed=player_fast_speed
            self.speed=self.normal_speed
         def set_xy(self):
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

         def change_sound(self):
            #change chomp sound
            if self.count:
               eat1.play()
            else:
               eat2.play()
            self.count = not self.count
            
         def move(self):
            
            #Try (only one time) to do the memory direction
            if self.change_direct == 1:
               self.direct = self.memory_direct

            if self.direct == UP:
               self.pos = (self.pos[0],self.pos[1]-1)
            if self.direct == RIGHT:
               self.pos = (self.pos[0]+1,self.pos[1])
            if self.direct == DOWN:
               self.pos = (self.pos[0],self.pos[1]+1)
            if self.direct == LEFT:
               self.pos=(self.pos[0]-1,self.pos[1])
                   
            if self.pos[1] == 272:
               if self.pos[0] < 0:
                  self.move_absolute(screen.get_width()-1,self.pos[1])
               elif self.pos[0] >= screen.get_width():
                  self.move_absolute(0,self.pos[1])

            if matriz[self.pos[1]][self.pos[0]] == 1:
               if self.direct == UP:
                  self.pos = (self.pos[0], self.pos[1] + 1)
               if self.direct == RIGHT:
                  self.pos = (self.pos[0] - 1, self.pos[1])
               if self.direct == DOWN:
                  self.pos = (self.pos[0], self.pos[1] - 1)
               if self.direct == LEFT:
                  self.pos = (self.pos[0] + 1, self.pos[1])

               if self.last_direct != self.direct:

                  #If direction is invalid, memory_direction save it
                  self.memory_direct = self.direct
                  self.change_direct += 1

                  self.direct = self.last_direct
                  self.move()

            self.last_direct = self.direct
            self.set_xy()
            self.set_image()

         def move_absolute(self,x,y):
            self.pos=(x,y)
            self.set_xy()

         def death(self):
            rotate = pygame.transform.rotate
            for frame in range(-1,7):
               screen.fill((0, 0, 0))
               score.display()
               lives.display()
               screen.blit(background,(0,48))
               consumables.draw(screen)
               screen.blit(rotate(patoAD,-((frame+1)*90)),(self.pos[0]-4,self.pos[1]-4))
               pygame.display.update()
               pygame.time.wait(150)
            pygame.time.wait(800)
            
         def set_image(self):
            self.img_index=0
            if self.aberto:
               self.img_index+=4
            if self.direct==RIGHT:
               self.img_index+=1
            elif self.direct==DOWN:
               self.img_index+=2
            elif self.direct==LEFT:
               self.img_index+=3
            self.set_xy()

         def display(self):
            screen.blit(self.imgs[self.img_index],(self.pos[0]-4,self.pos[1]-4))
            
         def collision(self):
            
            phantom_player_collision = pygame.sprite.spritecollide(player, phantom_list, False)
            
            for ghost in phantom_player_collision:
                
               if (ghost.mode == EATEN):
                  continue
               if (ghost.mode == FRIGHTENED):
                    
                  phantom[ghost.ghost].mode = EATEN
                  eat_ghost.play()

                  #display everything but pacman and eaten ghost
                  screen.fill((0, 0, 0))
                  score.display()
                  lives.display()
                  screen.blit(background,(0, 48))                    
                  consumables.draw(screen)
                  for i in range(4):
                     if i!=ghost.ghost:
                        screen.blit(phantom[i].img, (phantom[i].pos[0]-Ajuste, phantom[i].pos[1]-Ajuste))

                  #display score got
                  screen.blit(load_img('score'+str(self.eaten_phantom)+'.png'),(ghost.pos[0]-7,ghost.pos[1]))
                  pygame.display.update()

                  pygame.time.wait(1000)

                  #displays everything normally
                  screen.fill((0, 0, 0))
                  score.display()
                  lives.display()
                  screen.blit(background,(0, 48))                    
                  consumables.draw(screen)
                  for i in range(4):
                     screen.blit(phantom[i].img, (phantom[i].pos[0]-Ajuste, phantom[i].pos[1]-Ajuste))
                  self.display()
                  pygame.display.update()
                    
                  phantom[ghost.ghost].box = False
                  score.add(200 * (2 ** self.eaten_phantom))
                  self.eaten_phantom += 1
               else:
                  pygame.mixer.music.pause()
                  pygame.time.wait(750)
                  death.play()
                  self.death() #death animation
                  lives.remove()
                  reset()

         def collision_CP(self):
            #pato-man eats a normal pellet
            if matriz[self.pos[1]][self.pos[0]] == 2:
               for coins in consumables: #Search the atual coins in coins_list
                  if coins.rect.x == player.pos[0] and coins.rect.y == player.pos[1]:
                     coins.kill() #Remove from all groups
                     break
                   
               matriz[self.pos[1]][self.pos[0]] = 0
               score.add(10)
                   
               player.change_sound()

			#Pato-man eats a power pellet
            elif matriz[self.pos[1]][self.pos[0]] == 3:
               player.eaten_phantom=0#keeps track of currently eaten ghosts
               for i in range(4):
                  if(phantom[i].mode == WAITING or phantom[i].mode == LEAVE):
                     phantom[i].frightened = True
                  else:
                     if(phantom[i].mode != FRIGHTENED):
                        phantom[i].change_direct()
                        phantom[i].mode = FRIGHTENED
                  phantom[i].reset_time()
                               
               for power in consumables: #Search the atual power in power_list
                  if power.rect.x == player.pos[0] and power.rect.y == player.pos[1]:
                     power.kill() #Remove from all groups
                     break
               
               matriz[self.pos[1]][self.pos[0]] = 0
               score.add(50)

               player.change_sound()