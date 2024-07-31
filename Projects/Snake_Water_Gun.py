'''
1 for snake
-1 for water
0 for gun
'''
import random
n=int(input('How many times do you want to play?? '))
y=0
c=0
for i in range(n):
    comp=random.randint(-1,1)
    youstr=input('Enter your choice(s,w,g): ')
    youDict={'s':1,'w':-1,'g':0}
    reverseDict={1:'Snake',-1:'Water',0:'Gun'}
    you=youDict[youstr]

    print(f'You chose {reverseDict[you]} and computer chose {reverseDict[comp]}')

    if comp==you:
        print('Its a draw..!!')

    else:
        if comp==-1 and you==1:
            print('You Win..!!')
            y+=1


        elif comp==-1 and you==0:
            print('You Lose..!!')
            c+=1

        elif comp==1 and you==0:
            print('You Win..!!')
            y+=1
        
        elif comp==1 and you==-1:
            print('You Lose..!!')
            c+=1
        
        elif comp==0 and you==1:
            print('You Lose..!')
            c+=1
        
        elif comp==0 and you==-1:
            print('You Win..!!')
            y+=1
        
        else:
            print('Something went wrong..!!')
print(f'You got {y} points and computer got {c} points.')
if c>y:
    print('Computer Won..!! Better Luck next time..!!')
elif y>c:
    print('You won..!!')
elif c==y:
    print('Its a Draw..!!')