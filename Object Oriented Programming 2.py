'''String Upper Case
    Outline:
    Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.'''
'''
class IOString:
    def __init__(self):
        self.str1 = ''
    def input(self):
        self.str1 = input('Input a string: ')
    def upper(self):
        print(self.str1.upper())
object1 = IOString()
object1.input()
object1.upper()
'''
'''Employee in and Out
    Outline:
    Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!'''
'''
class Bob:
    def __init__(self):
        print('Contructor called')
    def __del__(self):
        print('Destructor called')

def delete():
    bob = Bob()
    print('Object created')
    del bob
    print('Object deleted')
delete()
'''
'''Pair of Elements
    Outline:
    Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)'''
class find:

    def sum(self):
        number = int(input('Enter a multiple of 10: '))
        set = (10,20,30,40,50,60,70)
        set = enumerate(set)
        for i in set:
            for j in set:
                if i[1] + j[1] == number:
                    print('The numbers are:', i[1], 'and', j[1], 'at positions', i[0], 'and', j[0])
find = find()
find.sum()

