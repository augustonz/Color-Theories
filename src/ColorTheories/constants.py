from classes.Color import Color
from classes.Level import Level

# as cores de dificuldade 0 são padrão, e devem poder ser utilizadas em qualquer nível
RED=Color("red", 255,0,0,255, 0)
GREEN=Color("green", 0,255,0,255, 0)
BLUE=Color("blue", 0,0,255,255, 0)
WHITE=Color("white", 255,255,255,255, 0)
BLACK=Color("black", 0,0,0,255, 0)
# as cores de dificuldade 1 são resultado da operação entre duas cores base RGB
GRAY=Color("gray", 128,128,128,255, 1)
YELLOW=Color.fromNewColor(RED + GREEN, "yellow", 1)
MAGENTA=Color.fromNewColor(RED + BLUE, "magenta", 1)
CYAN=Color.fromNewColor(GREEN + BLUE, "cyan", 1)
# as cores da dificuldade 2 são resultado da operação entre cores da dificuldade 0
PINK=Color.fromNewColor(RED + GRAY, "pink", 2)
MINT=Color.fromNewColor(GREEN + GRAY, "mint", 2)
LIGHT_BLUE=Color.fromNewColor(BLUE + GRAY, "light_blue", 2)
MAROON=Color.fromNewColor(RED * GRAY, "maroon", 2)
OFFICE_GREEN=Color.fromNewColor( GREEN * GRAY,  "office_green", 2)
NAVY=Color.fromNewColor(BLUE * GRAY, "navy", 2)
# as cores da dificuldade 3 são resultado da operação entre cores mais avançadas e grayscale
FUCHSIA=Color.fromNewColor(MAGENTA + GRAY, "fuchsia", 3)
BRIGHT_YELLOW=Color.fromNewColor(YELLOW + GRAY, "bright_yellow", 3)
ELECTRIC=Color.fromNewColor(CYAN + GRAY, "electric", 3)
TEAL=Color.fromNewColor(PINK - WHITE, "purple", 3)
OLIVE=Color.fromNewColor(LIGHT_BLUE - WHITE, "olive", 3)
PURPLE=Color.fromNewColor(MINT - WHITE, "purple", 3)

colors = [prop for prop in dir() if '_' != prop[0] and prop not in ['Color', 'Level']]

level_objects = [
    Level('1', [RED,GREEN,BLUE], [RED,GREEN,BLUE], 
        None, 'math', '+', 1,
        msg={'title': 'Nível 1', 'content': 'Bem vindo!'}),
    Level('2', [YELLOW,RED,BLUE], [RED,BLUE,YELLOW], 
        None, 'math', '+', 1,
        msg={'title': 'Nível 2', 'content': 'Continue, você está melhorando :)'}),
    Level('3', [RED,GREEN,BLUE,WHITE], [RED,GREEN,BLUE,WHITE], 
        None, 'math', '+', 1),
    Level('4', [RED,GREEN,BLUE], [WHITE,BLACK,GRAY], 
        None, 'math', '+', 2),
    Level('5', [RED,None,BLUE], [RED,GREEN,BLUE], 
        [[BLACK,    YELLOW, MAGENTA],
        [YELLOW,    BLACK,  CYAN],
        [MAGENTA,   CYAN,   BLACK]], 
        'arbitrary', '+', 1),
    # a versão que já tinha do level 6 era o método "multiplicativo", então mudei para resolução aritmética.
    Level('6', [CYAN,YELLOW,MAGENTA], [CYAN,YELLOW,MAGENTA],
        [[CYAN, GREEN,  BLUE],
        [GREEN, YELLOW, RED],
        [BLUE,  RED,    MAGENTA]], 
        'math', '*', 3),
    # a versão que já tinha onde VERMELHO X VERMELHO = PRETO era o método "subtrativo", onde a identidade - identidade = "elemento nulo"
    # o lvl 7 usa a subtração.
    Level('7', [RED,GREEN,BLUE], [RED,GREEN,BLUE], 
        None, 'math', '-', 4),
    # o lvl 8 explica a interação multiplicativa do CMYK com as cores base do RGB
    Level('8', [CYAN,MAGENTA,YELLOW], [RED,GREEN,BLUE], None, 
        'math', '*', 4),
    # o lvl 9 continua a interação do lvl 8 para os grayscale
    Level('9', [RED,GREEN,BLUE], [WHITE,GRAY,BLACK], None, 'math', '*', 4),
    # o lvl 10 mostra a soma dos CMYK com os greyscale
    Level('10', [CYAN,MAGENTA,YELLOW], [WHITE,GRAY,BLACK], None, 'math', '+', 4),
    # o lvl 11 mostra a interação das cores claras no método subtrativo com os greyscale
    Level('11', [PINK,MINT,LIGHT_BLUE], [WHITE,GRAY,BLACK], None, 'math', '-', 4),
    Level('12', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('13', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('14', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('15', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('16', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('17', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('18', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('19', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
    Level('20', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 4),
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

