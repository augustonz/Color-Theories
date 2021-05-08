import pygame
import sys 
import tools
from pygame.locals import *
import Menu
import pickle

def run(volume):
   pygame.init()
   pygame.mixer.init()
   screen = pygame.display.set_mode(tools.screenResolution)
   pygame.display.set_caption("Color-Theories")
   tools.globalVolume=volume

   running = True
   Menu.run()

   
if __name__=='__main__':
   if (len(sys.argv)>1):
      with open(tools.pickle_path(), 'wb') as fi:
         pickle.dump([0], fi)
   run(0.2)
   
