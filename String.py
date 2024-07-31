a='Mango'
l=len(a)
print('Length of string is',l)
print('first three characters of string are', a[0:2])
print('first three characters of string are', a[:3])
# negative index starts from the back and with -1
print('first three characters of string are', a[:-2])
print(a[-1:-3:-1]) #starts from the last letter and goes upto second last with negative step value
print(a[-3:-1])
# slicing includes the starting value and ignores the ending value
s='hello'
for i in s:
    print(i)
for i in a:
    print(i)