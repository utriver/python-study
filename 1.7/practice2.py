class Shape:
    def __init__(self,sides,base):
        self.sides = sides
        self.base = base
    
    def printinfo(self):
        print(f"""변의 개수: {self.sides}
밑변의 길이: {self.base}""")
    def area(self):
        print("넓이 계산이 정의되지 않습니다.")
        
        
class Rectangle(Shape):
    def __init__(self, sides, base,height):
        super().__init__(sides, base)
        self.height=height
    def area(self):
        print(self.height*self.base)
    
class Triangle(Shape):
    def __init__(self, sides, base,height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self):
        print((self.base*self.height)/2)

shape = Shape(10,20)
rectan = Rectangle(20,30,40)
trian = Triangle(10,20,2)
shape.printinfo()
shape.area()
rectan.printinfo()
rectan.area()
trian.printinfo()
trian.area()