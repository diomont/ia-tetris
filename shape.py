from common import Dimensions


S = [['.....',
      '.....',
      '..11.',
      '.11..',
      '.....'],
     ['.....',
      '..1..',
      '..11.',
      '...1.',
      '.....']]

I = [['..1..',
      '..1..',
      '..1..',
      '..1..',
      '.....'],
     ['.....',
      '1111.',
      '.....',
      '.....',
      '.....']]

class Shape:
    def __init__(self, plan) -> None:
        self.plan = plan
        self.rotation = 0
        self.dimensions = Dimensions(5,5)

        self._x = 0
        self._y = 0
        self.rotate()

    def set_pos(self, x, y):
        x = int(x)
        y = int(y)
        self.positions = [(cx+x-self._x, cy+y-self._y) for cx,cy in self.positions]
        self._x = x
        self._y = y

    def rotate(self, step=1):
        self.rotation = (self.rotation+step) % len(self.plan)
        self.positions = [(self._x+x,self._y+y) for y,line in enumerate(self.plan[self.rotation]) for x,pos in enumerate(line) if pos == '1']

    def translate(self, x, y):
        self.set_pos(self._x+x, self._y+y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self.set_pos(x, self._y)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self.set_pos(self._x, y)

    def __str__(self) -> str:
        return f"Shape({self._x},{self._y}) -> {self.positions}"

SHAPES = [Shape(S), Shape(I)]

if __name__ == "__main__":
    s = Shape(S)
    print(s.positions)