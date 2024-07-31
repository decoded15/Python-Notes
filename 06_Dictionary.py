a={
    'Ommi':75,
    'Duni':92,
    'Mamali':85
} #key:value pairs
print(type(a))
print(a['Ommi']) #index ki jageh key use krna hai
'''PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.'''
#dictionary methods:
print(a.items())
print(a.keys())
print(a.values())
a.update({'Ommi':98,'Subham':85}) #existing keys get updated..those dont exist gets added to the dictionary
print(a)

print(a.get('Ommi'))
print(a['Ommi']) #both will give same output
#difference between the two lines above is..get() gives 'None' if the key doesnt exist..the second statement gives error if the key doesnt exist

d={} #empty dictionary