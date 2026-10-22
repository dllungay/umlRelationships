class Shape:                    
    def area(self):
        raise NotImplementedError

class Square(Shape):            
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

print(Square(3).area())