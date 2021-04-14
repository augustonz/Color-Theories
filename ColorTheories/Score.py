class Score:

         def __init__(self,current_score,gamer):
            self.score=current_score #starting score
            self.is_gamer=gamer
            self.limit=int(self.score)//10000 + 1
            
            d = shelve.open(shelve_path)#open high score memory
            self.high_score='00'
            if not self.is_gamer and 'score' in d:
               self.high_score=d['score'] #Starts as last high value if played before (modo normal)
            elif self.is_gamer and 'score_gamer' in d:
               self.high_score=d['score_gamer'] #Starts as last high value if played before (modo gamer)
            d.close() #close high score memory

            self.high_score_text=font.render(self.high_score,False,pygame.Color("white")) #makes starter high score text 
            self.score_text=font.render(self.score,False,pygame.Color("white")) #makes starter score text

         def display(self):
            screen.blit(font.render("high score",False,pygame.Color("white")),(144,0)) #display "high score" on screen
            screen.blit(self.score_text,(112-16*len(self.score),16)) #display current score on screen
            screen.blit(self.high_score_text,(272-16*len(self.high_score),16)) #display current high score on screen


         def add(self,num):
            new_score=int(self.score)+num
            if new_score>=10000*self.limit:
               lives.add()
               self.limit+=1
               oneup.play() #som de 1up
            self.score=str(new_score) #updates current score
            if int(self.score)>int(self.high_score): #checks if we need new high score
               d = shelve.open(shelve_path) #open high score memory
               if not self.is_gamer:
                  d['score'] = self.score #update high score memory (modo normal)
               if self.is_gamer:
                  d['score_gamer'] = self.score #update high score memory (modo gamer)

               d.close() #close high score memory
               self.high_score=self.score #gets new high score value
               self.high_score_text=font.render(self.high_score,False,pygame.Color("white")) #makes new high score text
            
            self.score_text=font.render(self.score,False,pygame.Color("white")) #makes new score text
