'''Keep It Private!
Outline:
Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.'''
'''class MyClass:
    __privatevar = 1
    def __privateMeth(self):
        print('private')
    def call(self):
        print(MyClass.__privatevar)
classes = MyClass()
classes.__privateMeth()
classes.call()
'''
'''
Computer Price
Outline:
Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
'''
class Computer:
    def __init__(self):
        self.__max_price = 800
    def display(self):
        print(self.__max_price)
    def setmaxprice(self):
        self.__max_price = int(input('New Price: '))

computer = Computer()
computer.setmaxprice()
computer.display()

        
'''
Point Function
Outline:
Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.'''

class Point:
    def __init__(self,x=0,y=2):
        self.x = x
        self.y = y
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
point = Point(6,7)
print (point)