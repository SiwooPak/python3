#-*-coding:utf-8 -*-
def is_int(data):
    return data if type(data) == int else int(data)

def plus(a=0,b=0):
    return is_int(a)+is_int(b)

def minus(a=0,b=0):
    return is_int(a)-is_int(b)

def prouduct(a=0,b=0):
    return is_int(a)*is_int(b)

def divide(a=0, b=0):
    return is_int(a)/is_int(b)

def remain(a, b):
    return is_int(a)%is_int(b)

def negate(x):
    return -(is_int(x))
def power(x,y):
    return pow(x,y)    

print(plus(1,"3"))
