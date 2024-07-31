a=['ommi',25,True,15.23]
# list can hv values of multiple data types
print(a[0]) #list indexing..0 as first element nd so on
a[0]='Ommi'
print(a)
#lists are mutable..we can change the values of a list
#slicing in list is same as in strings
print(a[0:2])
#using functions we can change the original list..functions dont return separate list(as in case of strings)..it updates the list.
a.append('Duni') #adds string 'Duni' at the end of list
print(a)
l=[1,6,3,78,45,26,9]
l.sort() #sorts the list in ascending order
print(l)
l.reverse() #reverses the list
print(l)
l.insert(0,36) #insert(index,object)..inserts 36 at 0th index
print(l)
l.pop(0) #pop(index)...removes element from 0th index
print(l)
print(l.pop(0)) #if we print the pop function, it returns the element which is removed from the list
print(l)
l.remove(6) #removes element 6 from the list
print(l)
c=l.count(9) #counts the number of given arg in the specified list
print(c)