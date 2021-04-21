from Button import Button
import levelSelect
from tools import *

running = True

def run():

    screen = pygame.display.set_mode(screenResolution)

    #Loads images
    background = load_img('background.png')
    #Plays the beginning sound
    if (not pygame.mixer.music.get_busy()): 
        play_music('Game-Menu_Looping.wav')
    

    #Loads the sounds
    testSound = load_sound('test.wav',0.3)

    titleFont=load_font("title.ttf",112)
    def displayTitle():
        screen.blit(titleFont.render("Color",True,pygame.Color("purple")),(281,8))
        screen.blit(titleFont.render("Theories",True,pygame.Color("purple")),(200,108))

    #Menu options
    Menu = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    playButton = Button((250,300),300,92,"start game","menu.otf",levelsScreen,img='menuButtonMini.png')
    buttons.add(playButton)
    Menu.add(playButton)

    #Clock Speed
    clock = pygame.time.Clock()
    global running
    running=True

    while running:
        for event in pygame.event.get():
            playButton.handleEvent(event)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        #Display objects on screen
        screen.blit(background,(0,0))
        Menu.update()
        Menu.draw(screen)
        displayTitle()
        pygame.display.update()
        clock.tick(60)

def levelsScreen(val):
    global running
    running = False
    levelSelect.run()