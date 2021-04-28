from classes.Color import Color
from classes.Level import Level

WHITE=Color("white", 255,255,255,255)
GRAY=Color("gray", 128,128,128,255)
BLACK=Color("black", 0,0,0,255)
RED=Color("red", 255,0,0,255)
GREEN=Color("green", 0,255,0,255)
BLUE=Color("blue", 0,0,255,255)
YELLOW=RED + GREEN + "yellow"
MAGENTA=RED + BLUE + "magenta"
CYAN=GREEN + BLUE + "cyan"
PINK=RED + GRAY + "pink"
MINT=GREEN + GRAY + "mint"
LIGHT_BLUE=BLUE + GRAY + "light_blue"

level_objects = [
    Level('1', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', msg='Bem vindo!'),
    Level('2', [YELLOW,RED,BLUE], [RED,BLUE,YELLOW], None, 'math', '+'),
    Level('3', [RED,GREEN,BLUE,WHITE], [RED,GREEN,BLUE,WHITE], None, 'math', '+'),
    Level('4', [RED,GREEN,BLUE], [WHITE,BLACK,GRAY], None, 'math', '+'),
    Level('5', [RED,None,BLUE], [RED,GREEN,BLUE], [[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]], 'arbitrary', '+'),
    # a versão que já tinha do level 6 era o método "multiplicativo", então mudei para resolução aritmética.
    Level('6', [CYAN,YELLOW,MAGENTA], [CYAN,YELLOW,MAGENTA], [[CYAN,GREEN,BLUE],[GREEN,YELLOW,RED],[BLUE,RED,MAGENTA]], 'math', '*'),
    # a versão que já tinha onde VERMELHO X VERMELHO = PRETO era o método "subtrativo", onde a identidade - identidade = "elemento nulo"
    # o lvl 7 usa a subtração.
    Level('7', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '-'),
    Level('8', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('9', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('10', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('11', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('12', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('13', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('14', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('15', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('16', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('17', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('18', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('19', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
    Level('20', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+'),
]

levels = [dict(level) for level in level_objects]
# levels = [
#     {'num':'1','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[RED,YELLOW,MAGENTA],[YELLOW,GREEN,CYAN],[MAGENTA,CYAN,BLUE]],
#     "msg":'Bem vindo!'},
#     {'num':'2','columns':[YELLOW,RED,BLUE],'rows':[RED,BLUE ,YELLOW], 'condition': 'math',
#     'win':[[YELLOW,RED,MAGENTA],[WHITE,MAGENTA,BLUE],[YELLOW,YELLOW,WHITE]]},
#     {'num':'3','columns':[RED,GREEN,BLUE,WHITE],'rows':[RED,GREEN,BLUE,WHITE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA,WHITE],[YELLOW,BLACK,CYAN,WHITE],[MAGENTA,CYAN,BLACK,WHITE],[YELLOW,BLACK,CYAN,WHITE]]},
#     {'num':'4','columns':[RED,GREEN,BLUE],'rows':[WHITE,BLACK,GRAY], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'5','columns':[RED,None,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'arbitrary',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'6','columns':[CYAN,YELLOW,MAGENTA],'rows':[CYAN,YELLOW,MAGENTA], 'condition': 'math',
#     'win':[[CYAN,GREEN,BLUE],[GREEN,YELLOW,RED],[BLUE,RED,MAGENTA]]},
#     {'num':'7','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'8','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'9','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'10','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'11','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'12','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'13','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'14','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'15','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'16','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'17','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'18','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'19','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]},
#     {'num':'20','columns':[RED,GREEN,BLUE],'rows':[RED,GREEN,BLUE], 'condition': 'math',
#     'win':[[BLACK,YELLOW,MAGENTA],[YELLOW,BLACK,CYAN],[MAGENTA,CYAN,BLACK]]}]