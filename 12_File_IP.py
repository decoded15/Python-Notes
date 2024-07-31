'''
a="a very long strings with emails"

emails=[]
3 seconds

There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)

'''
f=open("file.txt",'r')
data=f.read()
print(data)
f.close()

s='Hey Ommi you are amazing'
f=open('MyFile.txt','w')
f.write(s)
f.close()

f=open('file.txt')
lines=f.readlines()
print(lines)
print(type(lines))
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()

f=open('file.txt','r')
line=' '
while line!='':
    line = f.readline() 
    print(line)

'''
MODES OF OPENING A FILE
r - open for reading
w - open for writing
a - open for appending
+ - open for updating.
'rb' will open for read in binary mode.
'rt' will open for read in text mode.
'''

with open('file.txt') as f:
    print(f.read())
#u dont have to close the file using with open..!!