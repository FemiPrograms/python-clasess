class Circle:
    def __init__(self,r):
        self.pi = 3.14
        self.r = r
    def area(self):
        print ('Area:', (self.pi*self.r)**2)
    def perimeter(self):
        print ('Perimeter:', (self.pi*self.r)*2)
circle = Circle(5)
circle.area() 
circle.perimeter()
        

