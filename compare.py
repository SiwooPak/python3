# -*-coding:utf-8 -*-
# 비교연산자와 조건문
# 자바스크립트와 거의 동일
# '==': 같다, '!=': 같지않다
# 'is': , 'is not':
# 객체 비교
# object.__lt__(self,other): <
# object.__le__(self,other): <=
# object.__eq__(self,other): ==
# object.__ne__(self,other): !=
# object.__gt__(self,other): >
# object.__ge__(self,other): >=

# 조건문
def plus(a, b):
    if type(b) != int:
        return None
    else:
        return a+b

# 간단하게


def s_plus(a, b):
   # return None if type(b) != int else a+b
    return a+b if type(b) is int or type(b) is float else None

# 불리언 연산자
# or(|), and(&), xor(^), << , >> , -x


def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you cant drink")
    elif age == 18 or age == 19:
        print("you are new to this")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(23)
