s=''' <35 F
35 to 59 D
60 to 79 C
80 to 89 B
90 to 100 A
'''
print(s)
m=int(input("\nPlease Enter your Marks:\n"))

if(m<35):
    print("F")
elif(m>=35 and m<60):
    print("D")
elif(m>=60 and m<80):
    print("C")
elif(m>=80 and m<90):
    print("B")
elif(m>=90 and m<101):
    print("A")
else:
    print("Invalid")    







# not

if(not False):
    print("hhh")

if(3!=6):
    print("fdsfsdhhh")

if(3 is not 6):
    print("dkhsdfkdkhdgkdgkjdkjdghhh")
