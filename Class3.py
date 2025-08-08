'''1. Data types
    Outline:
    Write a program to find what type of datatype the given variable is?'''
apple = 'apple'
print(type(apple))
number = 2
print(type(number))
float = 3.3
print(type(float))
bol = True
print(type(bol))
'''2. Typecasting
    Outline:
    Write a program to change the datatype of given variables?'''
string = 3.0
string = int(string)
print(type(string))
'''3. String operation
    Outline:
    Write a program to print the “CODINGAL” word in a reverse direction.'''
word = 'CODINGAL'
word = word[::-1]
print(word)
hi = 'ALTERNATIVE'
hi = hi[::2]
print(hi)