'''Is this a bus?
Outline:
Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
Project:
'''
class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehicle):
    pass

Bus = bus('370', '100','10000')
print('Name of the bus:' ,Bus.name, 'maxspeed:',  Bus.maxspeed , 'mileage:', Bus.mileage)


'''
Employee Inheritance
Outline:
Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
Project:
'''
class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print('Name:',self.name)
        print('ID:',self.id)

class Employee(Person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        super().__init__(name,id)

John = Employee('John', 123, 250000, 'Front-end Software Engineer')
John.display()

'''
Super Penguin
Outline:
Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.
Project:
'''

class Bird:
    def __init__(self):
        print('Bird Is Ready!')
    def Fly(self):
        print('Go Higher!')
    def Speed(self):
        print('Go Faster!')
class Child(Bird):
    def __init__(self):
        super().__init__(self)
    def Good(self):
        print('Good Job')
    def Great(self):
        print('Great Job')
child = Child()
child.Good()
child.Great