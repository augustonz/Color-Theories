import operator
from .Color import Color

class Level:
	arithmetic_operations = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
	}

	def __init__(self, num, columns, rows, win, condition, arithmetic_operation, difficulty, *args, **kwargs) -> None:
		self.num: int = num
		self.columns: list[Color] = columns
		self.rows: list[Color] = rows
		self.condition: str = condition
		self.win: list[list[Color]] = win
		self.arithmetic_operation = Level.arithmetic_operations[arithmetic_operation]
		self.difficulty = difficulty
		self.operation_symbol = arithmetic_operation
		if('msg' in kwargs.keys()):
			self.msg: dict = kwargs.get('msg')

	def __iter__(self):
		yield 'num', self.num
		yield 'columns', self.columns
		yield 'rows', self.rows
		yield 'condition', self.condition
		yield 'win', self.win
		yield 'arithmetic_operation', self.arithmetic_operation
		yield 'operation_symbol', self.operation_symbol
		yield 'difficulty', self.difficulty
		if(hasattr(self, 'msg')):
			yield 'msg', self.msg