from math import pi


def sphere_vol(r):
    return (4/3)*pi*r**3

def cube_vol(l,b,h):
    return l*b*h

def cone_vol(r,h):
    return (1/3)*pi*(r**2)*h
