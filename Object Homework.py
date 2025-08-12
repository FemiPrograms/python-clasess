'''Dog Breed
Outline:
Write a program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breeds.'''
class Dog:
    Origin = 'England.'
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
golden = Dog ('Golden',12)
poodle = Dog('Poodle', 10)
print('The first dog is:', golden.breed,'and it is', golden.age, 'years old.', 'The second dog is:', poodle.breed, 'and it is', poodle.age, 'years old. They are both from', poodle.Origin)
