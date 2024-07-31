'''
Primarily there are two types of loops in python.
• while loops
• for loops
'''
for i in range(1,6):
    print(i)

i=1
while i<6:
    print(i)
    i+=1
'''
In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False.
'''
# Quick Quiz: Write a program to print the content of a list using while loops.
l=['Rohan','Subham','harry',1,False]
i=0
while i<len(l):
    print(l[i])
    i+=1

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size.
# An optional else can be used with a for loop if the code is to be executed when the
# loops exhausts.
l= [1,7,8]
for item in l:
    print(item) 
else:
    print("done") # this is printed when the loop exhausts!
#loop else statement executes when the loop terminates normally without encountering any break statement
''''break' is used to come out of the loop when encountered. It instructs the program to –
exit the loop now'''
for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break
'''
'continue' is used to stop the current iteration of the loop and continue with the next
one. It instructs the Program to “skip this iteration”.
'''
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
'''pass is a null statement in python.
It instructs to “do nothing”.
'''

