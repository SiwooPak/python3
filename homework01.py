#-*-coding:utf-8 -*-
def is_int(data):
    return True if type(data) == int else False

def plus(a=0,b=0):
    return a+b if is_int(a) and is_int(b) else "1개 이상의 인자타입이 int형이 아닙니다." 

def minus(a=0,b=0):
    return a-b if is_int(a) and is_int(b) else "1개 이상의 인자타입이 int형이 아닙니다."

def product(a=0,b=0):
    return a*b if is_int(a) and is_int(b) else "1개 이상의 인자타입이 int형이 아닙니다."

def divide(a=0, b=0):
    return a/b if is_int(a) and is_int(b) else "1개 이상의 인자타입이 int형이 아닙니다."

def remain(a, b):
    return a%b if is_int(a) and is_int(b) else "1개 이상의 인자타입이 int형이 아닙니다."

def negate(x):
    return -(x) if is_int(x) else "인자타입이 int형이 아닙니다."
def power(x,y):
    return pow(x,y) if is_int(x) and is_int(y) else "1개 이상의 인자타입이 int형이 아닙니다."    

print(plus(1,"3"))
print(minus(1,3))
print(product(1,3))
print(divide(4,2))
print(remain(3,2))
print(negate("3"))
print(power("2",3))
