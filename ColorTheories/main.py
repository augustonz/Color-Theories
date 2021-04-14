import pygame
import tools
from pygame.locals import *
import Menu

def run(volume):
   pygame.init()
   pygame.mixer.init()
   screen = pygame.display.set_mode(tools.screenResolution)
   pygame.display.set_caption("Color-Theories")
   tools.globalVolume=volume
   Menu.run()

   
if __name__=='__main__':
   run(0.50)
