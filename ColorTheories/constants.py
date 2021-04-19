import pygame

WHITE=pygame.Color('white')
BLACK=pygame.Color('black')
RED=pygame.Color('red')
GREEN=pygame.Color('green')
BLUE=pygame.Color('blue')
YELLOW=pygame.Color('yellow')
PURPLE=pygame.Color('purple')
CYAN=pygame.Color('cyan')


levels = [
    {'num':'1','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'2','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[WHITE,YELLOW,PURPLE],[YELLOW,WHITE,CYAN],[PURPLE,CYAN,WHITE]]},
    {'num':'3','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'4','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'5','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'6','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'7','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'8','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'9','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'10','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'11','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'12','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'13','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'14','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'15','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'16','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'17','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'18','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'19','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]},
    {'num':'20','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE],
    'win':[[BLACK,YELLOW,PURPLE],[YELLOW,BLACK,CYAN],[PURPLE,CYAN,BLACK]]}]