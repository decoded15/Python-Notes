a=int(input('Enter your age '))
if a>=18:
    print('You are eligible to vote now')
    print('Good for you')
 
elif a<0:  
    print('You are entering an invalid age')

elif a==0:
    print('You are entering 0 which isnt a valid age')

else:
    print('You cannot vote now')
print('End of program')

#if elif else ladder above
#elif in python means [else if]. An if statements can be chained together with a lot of
# these elif statements followed by an else statement.

# Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18
n=int(input('Enter age '))
if n>=18:
    print('Yes')
else:
    print('No')

'''
Relational Operators are used to evaluate conditions inside the if statements. Some
examples of relational operators are:
== : equals.
>= : greater than/ equal to.
<= : lesser than/ equal to.

In python logical operators operate on conditional statements. For Example:
• and - true if both operands are true else false.
• or - true if at least one operand is true or else false.
• not - inverts true to false & false to true.

There can be any number of elif statements.
Last else is executed only if all the conditions inside elifs fail.
'''