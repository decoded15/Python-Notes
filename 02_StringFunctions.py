a='RohitSharma'
print(a.upper()) #to convert into ucase
print(a.lower()) #to convert into lcase
# Strings are immutable
b='!!!Ommi!!!'
print(b.lstrip('!')) #to remove leading characters/spaces if no arg is given
print(b.rstrip('!')) #to remove trailing characters/spaces if no arg is given
print(a.replace("Rohit","ommi")) #replaces Rohit with ommi
c='hello my name is ommi'
print(c.split())
print(c.split(' ')) #default arguement of split is white space
print(c.split('o')) #arg se pehle aur arg ke baad mein jo hoga wo ayega..at every occurence
print(c.capitalize()) #first arguement ko ucase mein krta hai and baki ko lcase karta hai
print(a.center(30)) #moves the string (arg-len) spaces ahead
d=a.center(30)
print(len(d), len(a)) #30-11=19..moves string 'a' 19 spaces ahead
e='hello i am ommi'
print(e.count('m')) #counts the number of arg in specified string
print(e.startswith('Hello')) #checks whether specified string starts with given arg or not
# endswith() works the same way..both the functions return boolean value
print(e.find('lo')) #searches for first occurence of given arg and returns its index
print(e.index('am'))
f='ommi123'
print(f.isalnum())
print(a.isalnum())  
print(a.isalpha())
print(f.isalpha())
print(a.isupper())
print(a.islower())
print(a.isspace())
print(e.title()) #har word ke first letter ko capital krta hai
print(e.istitle())
g='Hello OMMI'
print(g.swapcase()) #converts ucase to lcase nd vice versa
