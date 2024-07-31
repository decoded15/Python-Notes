a={1,5,6} #set
e=set() #empty set
print(type(e))
# Dony use e={} as it will create an empty dictionary not set
# Set is a collection of non-repetitive elements.
a={1,5,2,4,3,1,2,3,5,6,4,1}
print(a)
b={1,5,6,'Ommi'}
print(b,type(b))
b.add(10) #adds element to set..!
b.add('Harry')
print(b)
print(len(b))
# len(s): Returns 4, the length of the set
# • s.remove(8): Updates the set s and removes 8 from s.
# • s.pop(): Removes an arbitrary element from the set and return the element
# removed.
# • s.clear():empties the set s.
# • s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
# • s.intersection({8,11}): Return a set which contains only item in both sets {8}.
b.remove(10)
print(b)
#alt+shift+down arrow--> copies
a={8,9,6,2,4,7}
b={5,6,3,9,7,8,10}
print(a.union(b))
print(a.intersection(b))
s1 = {1, 2}
s2 = {1, 2, 3}
result = s1.issubset(s2)  # result is True
s1 = {1, 2, 3}
s2 = {1, 2}
result = s1.issuperset(s2)  # result is True
s1 = {1, 2, 3}
s2 = {4, 5, 6}
result = s1.isdisjoint(s2)  # result is True
