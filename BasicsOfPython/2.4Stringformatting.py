n=512
a=10.343443
p="KaleenBhai"

print("{:x}".format(n));
print("{:.3f}".format(a));
print("{:11.3f}".format(a));
print("{:011.3f}".format(a));

'''
d - decimal
o - octal
x - hex
b - binary
s - string(default)
e - expo
'''

print("{name} is not eligible in {exam} of mid term {one} of Sem {sem}".format(
    name="Munna",
    exam = "all four exam",
    one = 1,
    sem = 8
));
