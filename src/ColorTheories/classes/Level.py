from ColorTheories.classes.Entity import Entity

class Level:
	def __init__(self, num, columns, rows, win, difficulty, unveiled_cells, *args, **kwargs) -> None:
		self.num: int = num
		self.columns: list[Entity] = columns
		self.rows: list[Entity] = rows
		self.win: list[list[Entity]] = win
		self.difficulty = difficulty
		self.unveiled_cells = unveiled_cells
		if('msg' in kwargs.keys()):
			self.msg: dict = kwargs.get('msg')

	def __iter__(self):
		yield 'num', self.num
		yield 'columns', self.columns
		yield 'rows', self.rows
		yield 'win', self.win
		yield 'difficulty', self.difficulty
		yield 'unveiled_cells', self.unveiled_cells
		if(hasattr(self, 'msg')):
			yield 'msg', self.msg