from Button import Button
import test
from tools import *

running = True

def run():

    screen = pygame.display.set_mode(screenResolution)
    #Loads images
    background = load_img('background.png')

    #Loads the sounds
    testSound = load_sound('test.wav',0.3)

    #loads the fonts
    testFont=load_font("emulogic.ttf",16) 

    #Plays the beginning sound
    play_music('test.wav')
    Menu = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    playButton = Button((10,10),100,200,"This is text",levelsScreen)
    buttons.add(playButton)
    Menu.add(playButton)
    #player = Player()

    #Clock Speed
    clock = pygame.time.Clock()
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons.sprites():
                    button.isClicked(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                print(event.pos)
                print("Mouse UNclicked")

            elif event.type == pygame.MOUSEMOTION:
                for button in buttons.sprites():
                    button.setHover(event.pos)

            elif event.type == pygame.DROPBEGIN:
                print(event)
                print("File drop begin!")
            
            elif event.type == pygame.DROPCOMPLETE:
                print(event)
                print("File drop complete!")

        #Display objects on screen
        screen.fill((255, 255, 255))
        Menu.update()
        Menu.draw(screen)
        pygame.display.update()
        clock.tick(30)

def levelsScreen():
    global running
    running = False
    test.run()