fname=input("Enter First Name").title()
mname=input("Enter Middle Name").title()
lname=input("Enter Last Name").title()

name="{fn} {mn:1.3s} {ln} "
print(name.format(fn=fname,mn=mname,ln=lname))