'''
Student Class
Outline - Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output
'''
class Student:
    grade = 10
    print('Hi im a student of Grade', grade)
object1 = Student()
'''
Class Vehicle
Outline:
Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object
'''
class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
Mclaren = vehicle(100,30)
print('Car Maxspeed:',Mclaren.maxspeed)
print('Car Milage:',Mclaren.mileage)
'''
Class Parrot
Outline:
Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
'''
class Parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue = Parrot('John', 55)
green = Parrot('Pete', 44)
print('My parrots name is:',blue.name,'who is',blue.age,'years old. The other parrots name is', green.name, 'who is', green.age, 'years old.')