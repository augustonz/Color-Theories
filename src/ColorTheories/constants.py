from classes.Color import Color
from classes.Level import Level

# as cores de dificuldade 0 são padrão, e devem poder ser utilizadas em qualquer nível
RED=Color("Vermelho", 255,0,0,255, 0)
GREEN=Color("Verde", 0,255,0,255, 0)
BLUE=Color("Azul", 0,0,255,255, 0)
WHITE=Color("Branco", 255,255,255,255, 0)
BLACK=Color("Preto", 0,0,0,255, 0)
# as cores de dificuldade 1 são resultado da operação entre duas cores base RGB
GRAY=Color("Cinza", 128,128,128,255, 1)
YELLOW=Color.fromNewColor(RED + GREEN, "Amarelo", 1)
MAGENTA=Color.fromNewColor(RED + BLUE, "Magenta", 1)
CYAN=Color.fromNewColor(GREEN + BLUE, "Ciano", 1)
# as cores da dificuldade 2 são resultado da operação entre cores da dificuldade 0
PINK=Color.fromNewColor(RED + GRAY, "Rosa", 2)
MINT=Color.fromNewColor(GREEN + GRAY, "Menta", 2)
LIGHT_BLUE=Color.fromNewColor(BLUE + GRAY, "Azul Claro", 2)
MAROON=Color.fromNewColor(RED * GRAY, "Bordô", 2)
OFFICE_GREEN=Color.fromNewColor( GREEN * GRAY,  "Verde Escuro", 2)
NAVY=Color.fromNewColor(BLUE * GRAY, "Azul Marinho", 2)
# as cores da dificuldade 3 são resultado da operação entre cores mais avançadas e grayscale
FUCHSIA=Color.fromNewColor(MAGENTA + GRAY, "Fúcsia", 3)
BRIGHT_YELLOW=Color.fromNewColor(YELLOW + GRAY, "Amarelo Claro", 3)
ELECTRIC=Color.fromNewColor(CYAN + GRAY, "Azul Elétrico", 3)
TEAL=Color.fromNewColor(CYAN * GRAY, "Verde-azulado", 3)
OLIVE=Color.fromNewColor(YELLOW * GRAY, "Oliva", 3)
PURPLE=Color.fromNewColor(MAGENTA * GRAY, "Roxo", 3)

colors = [prop for prop in dir() if '_' != prop[0] and prop not in ['Color', 'Level']]
level_objects = [ 
    # Soma básica
    Level('1', [RED,BLUE], [GREEN], 
        None, 'math', '+', 1, None,
        msg={'title': 'Bem vindo!', 'content': 'Use a ideia da soma de cores para completar a tabela.'}),
    # Soma com repetição
    Level('2', [GREEN,RED], [RED,BLUE], 
        None, 'math', '+', 1, None,
        msg={'title': 'Bem jogado!', 'content': 'Agora, o que acontece quando se somam duas cores iguais?'}),
    # Soma com repetição e grande, introduz perto
    Level('3', [RED,GREEN,BLUE], [BLACK,GREEN,BLUE], 
        None, 'math', '+', 1, None,
         msg={'title': 'Cuidado!', 'content': 'Preto é uma cor curiosa, o que será que ela faz?'}),
    # Soma resultando em branco
    Level('4', [MAGENTA,GREEN,BLUE], [GREEN,BLACK], 
        None, 'math', '+', 1, None),
    #Somar composta com simples
    Level('5', [YELLOW,RED,BLUE], [RED,BLACK,CYAN],
            None, 'math', '+', 1, None),
    # Introdução de cor vazia
    Level('6', [RED,WHITE,BLACK], [None,GREEN,BLUE], 
        [[WHITE,    WHITE, CYAN],
        [YELLOW,    WHITE,  GREEN],
        [MAGENTA,   WHITE,   BLUE]], 
        'arbitrary', '+', 1, [(0,0),(0,2)],
        msg={'title': 'Oops!', 'content': 'Não tive muito tempo para terminar esse nível, espero que isso não lhe atrapalhe :)'}),
    # Cor vazia avançada
    Level('7', [None,RED,BLUE,YELLOW], [GREEN,YELLOW,None,BLUE], 
        [[WHITE, YELLOW, CYAN, YELLOW],
        [WHITE, YELLOW, WHITE,  YELLOW],
        [MAGENTA, RED, BLUE, YELLOW],
        [MAGENTA, MAGENTA, BLUE, WHITE]], 
        'arbitrary', '+', 1, [(0,0),(3,0),(2,2),(2,3)]),
    #Introdução substração
    Level('8', [RED, GREEN, BLUE], [RED, GREEN, BLUE, BLACK],
        None, 'math', '-', 0, None, 
        msg={'title': 'Mais um desafio!', 'content': 'Você se mostrou dominante da soma de cores, mas será que conseguirá subtrai-lás?'}),
    #Subtração avançada
    Level('9', [RED, GREEN, BLUE], [CYAN, MAGENTA, YELLOW], 
        None, 'math', '-', 1, None,
        msg={'title': 'O enigma continua!', 'content': 'Você certamente superou minhas expectativas. Mas por quanto tempo irá durar?'}),
    #Subtração com branco e preto
    Level('10', [WHITE, BLACK], [RED, GREEN, BLUE], 
        None, 'math', '-', 1, None),
    #Subtração com cor vazia
    Level('11', [RED, GREEN, YELLOW], [BLUE, None, CYAN],
        [[BLUE,BLUE,BLUE],
        [CYAN,MAGENTA,BLUE],
        [CYAN,BLUE,BLUE]],
        'arbitrary', '-', 1, [(1, 1),(1,2)],
        msg={'title': 'De novo!', 'content': 'Parece que esqueci de preencher umas cores aqui também, voce sabe o que fazer, né?'}),
    Level('12', [RED, MAGENTA], [RED, BLUE],None, 'math', '≠', 1, None,
        msg={'title': 'Seu último oponente!', 'content': 'O resultado da diferança entre cores é a soma dos seus elementos que não são iguais. Consegue achar essas diferenças?'}),
    Level('13', [CYAN, MAGENTA, YELLOW], [YELLOW, CYAN, WHITE],None, 'math', '≠', 1, None,
        msg={'title': 'Fique atento!', 'content': 'Lembre-se: Você deve achar os componentes diferentes das cores e somá-los.'}),
    Level('14', [BLACK, GREEN, YELLOW], [RED, CYAN, BLACK],None, 'math', '≠', 1, None),
     Level('15', [None, GREEN, WHITE, YELLOW], [None, BLUE, MAGENTA],
        [[CYAN,BLUE,RED,MAGENTA]
        ,[BLUE,CYAN,YELLOW,WHITE]
        ,[MAGENTA,WHITE,GREEN,CYAN]], 'arbitrary', '≠', 1, [(2,0), (0,1)]),
    Level('16', [WHITE,CYAN,MAGENTA], [BLACK,GRAY,WHITE], None, 'math', '-', 2, None,
        msg={'title': 'Não seja negativo!', 'content': 'Você tem que perceber que para escurecer uma cor deve-se remover igualmente todos os seus componentes.'}),
    Level('17',  [BLACK,GREEN,BLUE], [GRAY,None,None],[
        [GRAY,MINT,LIGHT_BLUE],
        [YELLOW,RED,WHITE],
        [RED,YELLOW,MAGENTA]], 'arbitrary', '≠', 2, [(1,1),(2,2)]),
    Level('18', [GRAY, LIGHT_BLUE, MAROON, PINK, NAVY], [RED, BLUE, GREEN],
        None, 'math', '+', 2, None,
        msg={'title': 'Esclareça sua mente!', 'content': 'Será que você terminará brilhantemente este nível?'}),
    Level('19', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 2, None),
    Level('20', [RED,GREEN,BLUE], [RED,GREEN,BLUE], None, 'math', '+', 2, None),
]

sugg_levels = [
    Level('18', [GRAY, MINT, WHITE, LIGHT_BLUE, MAROON, PINK], [RED, BLUE, GREEN, BLACK],
        None, 'math', '+', 2, None,
        msg={'title': 'Esclareça sua mente!', 'content': 'Será que você terminará brilhantemente este nível?'}),
    Level('19', [BLACK, CYAN], [RED, GREEN, BLUE, GRAY, MAGENTA], 
        None, 'math', '-', 1, None),
]

levels = [dict(level) for level in level_objects]
# a versão que já tinha do level 6 era o método "multiplicativo", então mudei para resolução aritmética.
# Level('6', [CYAN,YELLOW,MAGENTA], [CYAN,YELLOW,MAGENTA],
#     [[CYAN, GREEN,  BLUE],
#     [GREEN, YELLOW, RED],
#     [BLUE,  RED,    MAGENTA]], 
#     'math', '*', 2, None),
# a versão que já tinha onde VERMELHO X VERMELHO = PRETO era o método "subtrativo", onde a identidade - identidade = "elemento nulo"
# o lvl 8 explica a interação multiplicativa do CMYK com as cores base do RGB
# Level('8', [CYAN,MAGENTA,YELLOW], [RED,GREEN,BLUE], None, 
#     'math', '*', 3, None),
# o lvl 9 continua a interação do lvl 8 para os grayscale
# Level('9', [RED,GREEN,BLUE], [WHITE,GRAY,BLACK], None, 'math', '*', 3, None),
# o lvl 10 mostra a soma dos CMYK com os greyscale
# Level('10', [CYAN,MAGENTA,YELLOW], [WHITE,GRAY,BLACK], None, 'math', '+', 3, None),
# o lvl 11 mostra a interação das cores claras no método subtrativo com os greyscale
# Level('11', [PINK,MINT,LIGHT_BLUE], [WHITE,GRAY,BLACK], None, 'math', '-', 3, None),
# a versão que já tinha do level 6 era o método "multiplicativo", então mudei para resolução aritmética.
