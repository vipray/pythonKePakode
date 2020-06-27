import math
# importing this style requried 'math.' to call any fuction inside the module.

from math import pi
# here u can directly use pi without any prefix of 'math.'

from math import *
# it works same as first one but here also u not need the prfix, just can directly call the function

from math import factorial as fac 
# to change the name as per convenience

print(math.pi)
print(pi)
print(factorial(4))
print(fac(4))