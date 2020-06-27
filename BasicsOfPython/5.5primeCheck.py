n=int(input("Enter a number: "))
div=[]
if(n<2):
    print("{:d} is not Prime".format(n))
else:
    for i in range(2,n):
        if(n%i==0):
            div.append(i)
    if(len(div)==0):
        print("{:d} is Prime".format(n))
    else:
        print("{:d} is not Prime and its divisors are {:}".format(n,str(div)))    
