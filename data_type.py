#-*-coding:utf-8 -*-
# 변수
a = 2
b = 3
print(a+b)

a = 'like this'
c = False
print(a+str(b))
print(b+int(c))
# 파이썬도 할당되는 값에 따라 데이터형이 바뀌는 동적 타입.
print(type(a))
print(type(b))
print(type(c))

d = None # 존재하지 않는다, 없다.. 자바스크립트에서 null or undefined 인데, null에 가까움
# 변수명은 snake 형식으로 (ex: is_valid, get_user_info)