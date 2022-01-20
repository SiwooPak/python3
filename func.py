# def say():
#     print("hello")
#     print("bye")

def say(str):
    print(str)

say("hello")    

def plus(a=0,b=0): # 인자의 초기값 지정, 인자를 아무것도 넘겨주지 않을시 0 출력
    print(a+b)

plus()

def say_hello(name="siwoo"):
    print("hello", name)

say_hello()

# return
def r_plus(a,b):
    return a+b

def r_say_hello(name="siwoo"):
    return "hello "+ name

result = r_say_hello("shu")    
print(result)

# js의 경우, 들어온 인자의 순서대로 처리한다면, 파이썬은 지정해서 처리할수도 있음
# 인자의 순서를 기억하고 있다면 순서대로 값을 인자로 전송하지만, 파이썬처럼 키워드 인자로 넘기는 것이 더 편한것 같다
print(r_plus(b=10, a=1))
def minus(a,b):
    return a-b
print(minus(b=10, a=1)) 

# 문자열 앞에 F를 붙이면 문자열 리터럴 처리 가능
# js의 경우 ``로 함
def say_hello_arg(name,age):
    return f"hello {name} you are {age} years old"
print(say_hello_arg(age=37, name="siwoo"))        
