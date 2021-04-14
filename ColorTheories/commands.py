      def reset():
         #Inital screen appearence
         screen.fill((0, 0, 0))
         score.display()
         lives.display()
         screen.blit(background,(0,48))
         consumables.draw(screen) #displays the consumables
         screen.blit(font.render("ready!",False,pygame.Color("yellow")),(176,320))

         for i in range(4):
            if i==Inky:
               phantom[i].pos=(184,280)
               phantom[i].mode = WAITING
               phantom[i].waiting_movements = -30
               phantom[i].up = True
            elif i==Blinky:
               phantom[i].pos=(216,224)
               phantom[i].mode=SCATTER
            elif i==Clyde:
               phantom[i].pos=(248,280)
               phantom[i].mode = WAITING
               phantom[i].waiting_movements = 0
               phantom[i].up = True               
            elif i==Pinky:
               phantom[i].pos=(216,280)
               phantom[i].mode=LEAVE
            phantom[i].frightened = False
            phantom[i].box = False
            phantom[i].moviments = 0
            phantom[i].direct = DOWN
            phantom[i].change = 0
            phantom[i].rect = phantom[i].img.get_rect()
            phantom[i].rect.height = 16
            phantom[i].rect.width = 16
            phantom[i].rect.x = phantom[i].pos[0]-Ajuste
            phantom[i].rect.y = phantom[i].pos[1]-Ajuste
            phantom[i].set_image()
            screen.blit(phantom[i].img, (phantom[i].pos[0]-Ajuste, phantom[i].pos[1]-Ajuste))
         player.pos=(216,416)
         player.direct=LEFT
         player.display()
         pygame.display.update()
         pygame.time.wait(2150)
         pygame.mixer.music.unpause()

      def pause_game():
         running=False
         pygame.mixer.music.pause()
         pygame.mixer.pause()
         
         pause_screen=pygame.Surface((448, 576))
         pause_screen.set_alpha(100)
         cursor_index=0
         positions=[(72,228),(8,276)]
         while not running:

            clock.tick(40)
            for event in pygame.event.get():
               #Quit game
               if event.type == pygame.QUIT:
                  pygame.quit()

               #Directions keys
               if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                     running=True
                     pygame.mixer.music.unpause()
                     pygame.mixer.unpause()

                  if event.key == K_RETURN:

                     if cursor_index==0:
                        running=True
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                     else:
                        go_to_menu()
                         
                  if event.key == K_UP:
                     cursor_index+=1
                     if cursor_index==2:
                        cursor_index=0
                      
                  if event.key == K_DOWN:
                     cursor_index-=1
                     if cursor_index==-1:
                        cursor_index=1

            screen.fill((0, 0, 0))
            score.display()
            lives.display()
            screen.blit(background,(0, 48))
            consumables.draw(screen)
            player.display()  

            screen.blit(pause_screen,(0,0))
            screen.blit(big_font.render("PAUSED",False,pygame.Color("White")),(128,128))
            screen.blit(big_font.render("continue", False, pygame.Color('White')),(96,224))
            screen.blit(big_font.render("back to menu", False, pygame.Color('White')),(32,272))
            screen.blit(arrow,positions[cursor_index])

            pygame.display.update()
      
      def win_game():
         running=False
         pygame.mixer.music.pause()
         pygame.mixer.pause()
         
         path=os.path.join(main_dir,"sounds",'win_sound.wav')
         pygame.mixer.music.load(path)
         pygame.mixer.music.set_volume(volume)
         pygame.mixer.music.play(loops=1)
         
         pause_screen=pygame.Surface((448, 576))
         pause_screen.set_alpha(100)
         cursor_index=0
         positions=[(8,276)]
         while not running:
            
            clock.tick(60)
            for event in pygame.event.get():
               #Quit game
               if event.type == pygame.QUIT:
                  pygame.quit()

               #Directions keys
               if event.type == KEYDOWN:
                  if event.key == K_RETURN:
                     go_to_menu()
                     
            screen.fill((0, 0, 0))
            score.display()
            lives.display()
            screen.blit(background,(0, 48))
            consumables.draw(screen)
            player.display() 
            
            screen.blit(pause_screen,(0,0))
            screen.blit(big_font.render("YOU WIN", False, pygame.Color('Green')),(96,224))
            screen.blit(big_font.render("back to menu", False, pygame.Color('White')),(32,272))
            screen.blit(arrow,positions[cursor_index])

            pygame.display.update()
 