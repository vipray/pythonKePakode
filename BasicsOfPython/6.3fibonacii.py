n=int(input("Enter: "))
fibonacci =[0]*30
fibonacci[1] = fibonacci[2] = 1;

def fib(n):
    if(n==1 or n==2):
        return 1
    elif(fibonacci[n]!=0):
        return fibonacci[n]
    else:
        fibonacci[n] = fib(n-1)+fib(n-2)
        return fibonacci[n]



if(n<0):
    print('Invalid Input')
else:
    print(fib(n))
    print(fibonacci)