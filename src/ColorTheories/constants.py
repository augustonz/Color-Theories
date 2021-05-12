from ColorTheories.classes.Level import Level
from ColorTheories.classes.Entity import Entity
from pygame.draw import circle, polygon, rect

_E_QUADRADO = Entity(1, 'quadrado', lambda surface, x, y: rect(surface, 'black', (x-26,y-26, 52,52)))
_E_CIRCULO = Entity(1, 'circulo', lambda surface, x, y: circle(surface, 'black', (x,y), 26))
_E_TRIANGULO = Entity(1, 'triangulo', lambda surface, x, y: polygon(surface, 'black', [(x,y-26), (x-26, y+26), (x+26, y+26)]))
entities = [prop for prop in dir() if '_E_' in prop]

level_objects = [ 
    Level('1', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('2', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('3', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('4', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('5', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('6', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('7', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('8', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('9', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('10', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('11', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('12', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('13', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('14', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('15', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('16', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('17', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('18', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('19', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
    Level('20', [_E_QUADRADO, _E_QUADRADO], [_E_QUADRADO, _E_QUADRADO],
    [[_E_QUADRADO, _E_QUADRADO]
    ,[_E_QUADRADO, _E_QUADRADO]], 1, [(0,0)]),
]

levels = [dict(level) for level in level_objects]
