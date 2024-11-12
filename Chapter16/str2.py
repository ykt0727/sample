class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

print(Point(1, 2)+Point(3, 4))