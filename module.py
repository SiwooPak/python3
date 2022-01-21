# -*-coding:utf-8 -*-
# import math
from calculator import plus, minus
from math import ceil, fabs
# 자바스크립트식으로 표현하면
# const {ceil, fabs} = require('math')
# 자바스크립트 처럼 as로 별칭을 붙여서 사용가능

print(ceil(5.89))
print(fabs(-1.2))
nums = [1, 2, 3, 4]


def add(num):
    return num + 1


result = list(map(add, nums))
print(list)
print(result)

# calculater
print(plus(1, 3))
print(minus(3, 1))
