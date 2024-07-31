# tuple is immutable..we cannot change the values of a tuple
a=(1,5,6,'hello',True,15.2,5)
print(type(a))
#creating single element tuple
t=(1,)
print(type(t))
# a[0]=45 this will show error..tuples are immutable
#tuple methods
print(a.count(5)) #count()-->counts number of given arg
i=a.index(5) #returns index of first occurence of given arg
print(i)
print(len(a)) #prints length of the tuple
