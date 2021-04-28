import copy
import math

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

	def __init__(self, name, red, green, blue, alpha):
		self.name = name
		self.red = min(red, 255)
		self.green = min(green, 255)
		self.blue = min(blue, 255)
		self.alpha = min(alpha, 255)
		Color.color_names.add(self)

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
		return (self.red == red) and (self.green == green) and (self.blue == blue) and (self.alpha == alpha)

	def __add__(self, other: object):
		_tmp = copy.deepcopy(self)
		if type(other) is str:
			_tmp.name = other
			Color.color_names.add(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.name = "unknown"
			_tmp.red = min(_tmp.red + other.red, 255)
			_tmp.green = min(_tmp.green + other.green, 255)
			_tmp.blue = min(_tmp.blue + other.blue, 255)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
			if _tmp in Color.color_names:
				for color in Color.color_names:
					if color == _tmp:
						_tmp.name = color.name
		return _tmp

	def __sub__(self, other):
		_tmp = copy.deepcopy(self)
		if type(other) is str:
			_tmp.name = other
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.red = abs(_tmp.red - other.red)
			_tmp.green = abs(_tmp.green - other.green)
			_tmp.blue = abs(_tmp.blue - other.blue)
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
		return _tmp

	def __mul__(self, other):
		_tmp = copy.deepcopy(self)
		if type(other) is not Color:
			return _tmp
		else:
			_tmp.name = "unknown"
			_tmp.red = other.red and _tmp.red
			_tmp.green = other.green and _tmp.green
			_tmp.blue = other.blue and _tmp.blue
			_tmp.alpha = min(math.floor(((_tmp.alpha/255)+((other.alpha/255)*_tmp.alpha/255))*255), 255)
		return _tmp

	