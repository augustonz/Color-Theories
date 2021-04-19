from Button import Button
from tools import *
import Menu
import Level
import constants
import pickle

def run():

    screen = pygame.display.set_mode(screenResolution)

    #Loads images
    background = load_img('background.png')
    
    #Plays the beginning sound
    if (not pygame.mixer.music.get_busy()): 
        play_music('Game-Menu_Looping.wav')

    titleFont=load_font("title.ttf",66)

    #Menu options
    levelSelect = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    menuButton = Button((24,24),48,48,text="",font="menu.otf",img="menuBackMini.png",func=backMenu)
    buttons.add(menuButton)
    levelSelect.add(menuButton)
    levels = constants.levels
    with open('mypickle.pk', 'rb') as fi:
        openLevels = pickle.load(fi)

    for i in range(20):
        
        but=Button((100+(i%5)*122,76+(i//5)*124),110,112,text=str(1+i),font="menu.otf",img="levelSelectLevelMini.png",func=level,args=levels[i])
        if openLevels.count(i)==0:
            but.image=load_img('lockedLevel.png')
            but.func=None
        buttons.add(but)
        levelSelect.add(but)
    
    #Clock Speed
    clock = pygame.time.Clock()
    global running
    running=True
    while running:
        for event in pygame.event.get():
            for button in buttons.sprites():
                button.handleEvent(event)

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        #Display objects on screen
        screen.blit(background,(0,0))
        screen.blit(titleFont.render("Levels",True,pygame.Color("purple")),(316,0))
        levelSelect.update()
        levelSelect.draw(screen)
        pygame.display.update()
        clock.tick(60)

def backMenu(val):
    global running
    running=False
    Menu.run()

def level(val):
    global running
    running = False
    Level.run(val)