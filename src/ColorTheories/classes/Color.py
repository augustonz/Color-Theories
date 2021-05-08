import copy
import math
import operator

# Implementação de Color:
# - exemplo para criar uma cor independentemente de outra:
# 		Color("nome", red=213, green="123", blue="0", alpha="50")
# - exemplo para criar uma cor como resultado de um processo aditivo entre duas cores:
#		red = Color("red", 255, 0, 0, 255)
# 		green = Color("green", 0, 255, 0, 255)
#		yellow = red + green + "yellow"
# 	+ note que quando uma cor é somada a outra, ela resultará noutra cor,
# 	+ e que quando uma cor for somada a uma string, a string definirá o nome da cor.
# - exemplo para criar uma cor como resultado de um processo subtrativo entre duas cores:
# 		green = Color("green", 0, 255, 0, 255)
# 		blue = Color("blue", 0, 0, 255, 255)
#		cyan = green + blue + "cyan"
#		blue == cyan - green - "blue" -> True


class Color:
	
	color_names = set()

	def __hash__(self):
		return hash((self.red, self.green, self.blue))

	def __init__(self, name, red, green, blue, alpha, difficulty):
		self.name = name
		self.red = min(red, 255)
		self.green = min(green, 255)
		self.blue = min(blue, 255)
		self.alpha = min(alpha, 255)
		self.difficulty = difficulty
		Color.color_names.add(self)

	@classmethod
	def fromNewColor(cls, obj, new_name, new_diff):
		obj.name = new_name
		obj.difficulty = new_diff
		if(obj in Color.color_names):
			Color.color_names.remove(obj)
		Color.color_names.add(obj)
		return cls(obj.name,*tuple(obj), obj.difficulty)

	def __iter__(self):
		yield self.red
		yield self.green
		yield self.blue
		yield self.alpha

	def __eq__(self, o: object) -> bool:
		#sanitization
		if not callable(getattr(o, "__iter__", None)): return False
		iterable = iter(o)
		red = next(iterable)
		green = next(iterable)
		blue = next(iterable)
		alpha = next(iterable)
		return (-1 <= self.red - red <= 1) and (-1 <= self.green - green <= 1) and (-1 <= self.blue - blue <= 1) and (self.alpha == alpha)

	def __add__(self, other: object):
		_tmp = copy.deepcopy(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.red = min(_tmp.red + other.red, 255)
			_tmp.green = min(_tmp.green + other.green, 255)
			_tmp.blue = min(_tmp.blue + other.blue, 255)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
			_tmp = self._update_static_values(_tmp)
		return _tmp

	def __sub__(self, other):
		_tmp = copy.deepcopy(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.red = max(_tmp.red - other.red,0)
			_tmp.green = max(_tmp.green - other.green,0)
			_tmp.blue = max(_tmp.blue - other.blue,0)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
			_tmp = self._update_static_values(_tmp)
		return _tmp

	def __mul__(self, other):
		_tmp = copy.deepcopy(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.name = "unknown"
			_tmp.red = min(other.red, _tmp.red)
			_tmp.green = min(other.green, _tmp.green)
			_tmp.blue = min(other.blue, _tmp.blue)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
			_tmp = self._update_static_values(_tmp)
		return _tmp

	def __truediv__(self, other):
		_tmp = copy.deepcopy(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.red = abs(_tmp.red - other.red)
			_tmp.green = abs(_tmp.green - other.green)
			_tmp.blue = abs(_tmp.blue - other.blue)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
			_tmp = self._update_static_values(_tmp)
		return _tmp

	@classmethod
	def sorted(cls, colors: list):
		bwg = [color for color in colors if color.name in ('black', 'white', 'gray')]
		colors = [color for color in colors if color not in bwg]
		bwg = sorted(bwg, key=lambda c: c.red+c.green+c.blue, reverse=True)
		colors = sorted(colors, key=lambda c: c.red+c.green+c.blue)
		return bwg + colors

	def _update_static_values(self, _tmp):
		known_color = [color for color in Color.color_names if _tmp == color]
		_tmp.name = known_color[0].name if known_color else 'unknown'
		_tmp.difficulty = known_color[0].difficulty if known_color else _tmp.difficulty
		return _tmp
	