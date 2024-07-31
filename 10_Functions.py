'''
A function is a group of statements performing a specific task.
When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!
A function can be reused by the programmer in a given program any number of times.
'''

# def average(): #function header/definition
#     a=int(input('Enter your number: '))
#     b=int(input('Enter your number: '))
#     c=int(input('Enter your number: '))
#     avg=(a+b+c)/3
#     print(avg)
# average() #function call

'''
There are two types of functions in python:
• Built in functions (Already present in python)
• User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc.
The average() function we defined is an example of user defined function.
A function can accept some value it can work with. We can put these values in the
parentheses called arguements.
'''

def gd(name,ending):
    print('Good day',name)
    print(ending)
    return "done"
gd('Harry','Thank you')
a=gd('Ommi','Thanks')
print(a) 

def average(): #function header/definition
    a=int(input('Enter your number: '))
    b=int(input('Enter your number: '))
    c=int(input('Enter your number: '))
    avg=(a+b+c)/3
    return avg
a=average() #function call
print(a)

'''
We can have a value as default as default argument in a function.
If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.
Example:
def greet(name = "stranger"):
    # function body
greet() # name will be "stranger" in function body (default)
greet("harry") # name will be "harry" in function body (passed)
'''