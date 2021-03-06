import pygame
from ColorTheories.classes.Level import Level
from ColorTheories.classes.Entity import Entity

from ColorTheories.tools import load_font, load_img
pygame.font.init()
roboto = load_font('Roboto-Thin.ttf',25)
roboto.bold = True

_E_MACA = Entity(1, 'Maçã', lambda surface, x, y: surface.blit(load_img('maca.png'),(x,y)))
_E_MACA2 = Entity(1, 'Maçã', lambda surface, x, y: surface.blit(load_img('maca2.png'),(x,y)))
_E_LARANJA = Entity(1, 'Laranja', lambda surface, x, y: surface.blit(load_img('laranja.png'),(x,y)))
_E_CEREJA = Entity(1, 'Cereja', lambda surface, x, y: surface.blit(load_img('cereja.png'),(x+2,y)))
_E_BANANA = Entity(1, 'Banana', lambda surface, x, y: surface.blit(load_img('banana.png'),(x,y)))
_E_UVA = Entity(1, 'Uva', lambda surface, x, y: surface.blit(load_img('uva.png'),(x,y)))
_E_MORANGO = Entity(1, 'Morango', lambda surface, x, y: surface.blit(load_img('morango.png'),(x,y)))
_E_MELANCIA = Entity(1, 'Melancia', lambda surface, x, y: surface.blit(load_img('melancia.png'),(x,y)))
_E_PERA = Entity(1, 'Pera', lambda surface, x, y: surface.blit(load_img('pera.png'),(x,y)))
_E_LIMAO = Entity(1, 'Limão', lambda surface, x, y: surface.blit(load_img('limao.png'),(x,y)))

_E_LETRA_E = Entity(1, 'letra e', lambda surface, x, y: surface.blit(roboto.render(' e ', True, 'white', 'black'), (x+15,y+18)))
_E__LETRA_A = Entity(1, 'letra a', lambda surface, x, y: surface.blit(roboto.render(' a ', True, 'white', 'black'), (x+15,y+18)))
_E_LETRA_B = Entity(1, 'letra b', lambda surface, x, y: surface.blit(roboto.render(' b ', True,  'white', 'black'), (x+15,y+18)))

entities = [prop for prop in dir() if '_E_' in prop]

level_objects = [
    Level('1', [_E_LETRA_E, _E__LETRA_A], [_E_LETRA_E, _E__LETRA_A],
    [[_E_LETRA_E, _E__LETRA_A],
    [_E__LETRA_A, _E_LETRA_E]], 1, [(0,0)]), 
    Level('2', [_E_LETRA_E, _E__LETRA_A, _E_LETRA_B], [_E_LETRA_E, _E__LETRA_A, _E_LETRA_B],
    [[_E_LETRA_E, _E__LETRA_A, _E_LETRA_B],
    [_E__LETRA_A, _E_LETRA_B, _E_LETRA_E],
    [_E_LETRA_B, _E_LETRA_E, _E__LETRA_A]], 1, [(0,0)]), 
    Level('3', [_E_BANANA, _E_CEREJA], [_E_BANANA, _E_CEREJA],
    [[_E_BANANA, _E_CEREJA],
    [_E_CEREJA, _E_BANANA]], 1, [(0,0)]), 
    Level('4', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('5', [_E_UVA, _E_LARANJA,_E_BANANA], [_E_BANANA, _E_UVA,_E_LARANJA],
    [[_E_BANANA, _E_UVA,_E_LARANJA],
    [_E_UVA, _E_LARANJA,_E_BANANA],
    [_E_LARANJA, _E_BANANA,_E_UVA]], 1, [(1,1)]),
    Level('6', [_E_MACA2, _E_PERA,_E_MACA], [_E_MACA, _E_PERA,_E_MACA2],
    [[_E_MACA, _E_MACA2,_E_PERA],
    [_E_PERA, _E_MACA,_E_MACA2],
    [_E_MACA2, _E_PERA,_E_MACA]], 1, [(1,2)]),
    Level('7', [_E_CEREJA, _E_MELANCIA,_E_MORANGO], [_E_MELANCIA, _E_CEREJA,_E_MORANGO],
    [[_E_MORANGO, _E_CEREJA,_E_MELANCIA],
    [_E_MELANCIA, _E_MORANGO,_E_CEREJA],
    [_E_CEREJA, _E_MELANCIA,_E_MORANGO]], 1, [(1,0)]),
    Level('8', [_E_LIMAO, _E_LARANJA,_E_UVA,_E_PERA], [_E_LARANJA, _E_UVA,_E_PERA,_E_LIMAO],
    [[_E_PERA, _E_UVA,_E_LARANJA,_E_LIMAO],
    [_E_LIMAO, _E_LARANJA,_E_UVA,_E_PERA],
    [_E_LARANJA, _E_LIMAO,_E_PERA,_E_UVA],
    [_E_UVA, _E_PERA,_E_LIMAO,_E_LARANJA]], 1, [(0,0),(2,0),(1,1),(1,2),(2,3)]),
    Level('9', [_E_LIMAO, _E_MACA2,_E_MELANCIA,_E_CEREJA], [_E_MACA2, _E_MELANCIA,_E_CEREJA,_E_LIMAO],
    [[_E_MACA2, _E_CEREJA,_E_LIMAO,_E_MELANCIA],
    [_E_MELANCIA, _E_LIMAO,_E_CEREJA,_E_MACA2],
    [_E_CEREJA, _E_MELANCIA,_E_MACA2,_E_LIMAO],
    [_E_LIMAO, _E_MACA2,_E_MELANCIA,_E_CEREJA]], 1, [(0,0),(1,2),(2,3)]),
    Level('10', [None, _E_BANANA,None], [_E_MORANGO, _E_MACA2,_E_BANANA],
    [[_E_MORANGO, _E_BANANA,_E_MACA2],
    [_E_MACA2, _E_MORANGO,_E_BANANA],
    [_E_BANANA, _E_MACA2,_E_MORANGO]], 1, [(0,1),(0,2)]),
    Level('11', [_E_CEREJA, None,_E_PERA], [None, _E_LARANJA,None],
    [[_E_CEREJA, _E_LARANJA,_E_PERA],
    [_E_LARANJA, _E_PERA,_E_CEREJA],
    [_E_PERA, _E_CEREJA,_E_LARANJA]], 1, [(2,0),(0,2)]),
    Level('12', [_E_LIMAO, None,None,_E_CEREJA], [_E_MACA2, _E_MELANCIA,_E_CEREJA,_E_LIMAO],
    [[_E_MACA2, _E_CEREJA,_E_LIMAO,_E_MELANCIA],
    [_E_MELANCIA, _E_LIMAO,_E_CEREJA,_E_MACA2],
    [_E_CEREJA, _E_MELANCIA,_E_MACA2,_E_LIMAO],
    [_E_LIMAO, _E_MACA2,_E_MELANCIA,_E_CEREJA]], 1, [(3,1),(2,0),(1,1),(2,3)]),
    Level('13', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('14', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('15', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('16', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('17', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('18', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('19', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
    Level('20', [_E_MACA, _E_LARANJA,_E_LIMAO], [_E_MACA, _E_LARANJA,_E_LIMAO],
    [[_E_MACA, _E_LARANJA,_E_LIMAO],
    [_E_LARANJA, _E_LIMAO,_E_MACA],
    [_E_LIMAO, _E_MACA,_E_LARANJA]], 1, [(0,1),(0,2)]),
]

levels = [dict(level) for level in level_objects]
