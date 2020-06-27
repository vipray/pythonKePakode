# print in style
from pprint import pprint as pretty_print
from copy import copy

A2d=[
    [1,2,3,4,5,6,7],
    [12,26,35,43,35,63,74],
    [231,342,3343,4344,5343,633,7346570],
]


print(A2d[2][1])
print(A2d)
print('')
pretty_print(A2d)

l1=["a",'b','c','d','e','f']
l=[l1, l1, l1]
print(l)

# Jaaadoooooooooo
l[2][0]="z"

# here all the rows change the value at 0th position
pretty_print(l)
# bcoz line 18 place pointers to actual list l1

# So to overcome
print("After Smjhdhaari\n\n")
l=[copy(l1), copy(l1), copy(l1)]

l[1][0]="x"
pretty_print(l)