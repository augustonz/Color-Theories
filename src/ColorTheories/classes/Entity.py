from typing import Callable
from pygame import Surface

class Entity:
	def __init__(self, _id: int, name:str, render: Callable[[Surface, int, int],str], difficulty=1) -> None:
		self.id = _id
		self.name = name
		self.render = render
		self.difficulty = difficulty

	def render(self, surface, x, y):
		self.render(surface, x, y)