import random
n=random.randint(1,10)
a=-1
c=0
while (a!=n):
    c+=1
    a=int(input('Guess the number'))
    if (a>n):
        print('Lower number please..!!')
    elif (a<n):
        print('Higher number please..!!')
print(f'You have guessed the correct number in {c} attempts..!!')