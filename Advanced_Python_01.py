# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)

n : int = 5

def sum (a:int , b:int) -> int :
    return a+b
a=sum(5,2)
print(a)

from typing import List, Tuple, Dict
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

#matchcase
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
a=http_status(200)
print(a)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

'''
You can now use multiple context managers in a single with statement more cleanly
using the parenthesised context manager
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
);
'''

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")


try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("I am inside else")

def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

a = 89 #global variable

def fun(): 
    # global a
    a = 3 #local variable
    print(a)


fun()
print(a)

l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)