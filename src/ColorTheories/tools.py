import os
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]
screenResolution=(800,600)
globalVolume = 0.1

def pickle_path():
   return os.path.join(main_dir,"mypickle.pk")

def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

def load_sound(name,volume):
   path=os.path.join(main_dir,"sounds",name)
   this_sound = pygame.mixer.Sound(path)
   this_sound.set_volume(volume)
   return this_sound

def play_music(name):
   path=os.path.join(main_dir,"sounds",name)
   pygame.mixer.music.load(path)
   pygame.mixer.music.set_volume(globalVolume)
   pygame.mixer.music.play(loops=-1)

def load_font(name,size):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,size)

def go_to_menu():
   running=False
   pygame.mixer.music.unload()
   pygame.mixer.pause()
   menu.run()
