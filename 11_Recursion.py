'''
factorial(n)=n*factorial(n-1)
'''
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input('Enter your number: '))
print(f'Factorial of {n} is {factorial(n)}')
