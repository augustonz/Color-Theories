     class Lives:

         def __init__(self,current_lives,gamer):
            self.lives=current_lives
            self.is_gamer=gamer

         def add(self):
            if self.lives<5 and not is_gamer:
               self.lives+=1

         def remove(self):
            self.lives-=1
            if self.lives==0:
               #Game over screen
               screen.fill((0, 0, 0))
               score.display()
               lives.display()
               screen.blit(background,(0,48))
               consumables.draw(screen)
               screen.blit(font.render("Game over",False,pygame.Color("red")),(152,320))
               pygame.display.update()
               pygame.time.wait(3500)
               go_to_menu()

         def display(self):
            for i in range(self.lives):
               screen.blit(patoAD,(8+i*32,548))