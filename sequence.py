# -*-coding:utf-8 -*-
# 파이썬에서 열거형 타입: list, tuple

# list
days = ["mon", "tue", "wed", "thur", "fri"]
print(days)
print(type(days))
# python list mutable
# index 0~
print("mon" in days)
print(days[3])
print(len(days))

# append()는 마지막 부분에 추가
days.append("sat")
print(days)

lists = [[]] * 3 # 빈 배열 3개의 요소를 갖는 배열 생성 [[],[],[]]
lists[0].append(3) # [[3],[3],[3]]

lists = [[] for i in range(3)]
lists[0].append(3) # [[3],[],[]]
lists[1].append(5) # [[3],[5],[]]
lists[0].append(7) # [[3],[5],[7]]
# insert(index, value) 첫번째인자는 인덱스, 두번째 인자는 값이 들어가고 해당하는 인덱스에 값이 삽입되며
# 기존 인덱스에 위치했던 값은 뒤로 밀려남
days.insert(0, "sun")
print(days)
# 복사
lists2 = lists.copy() # 값만 복사
lists.append("sun") # lists의 요소만 추가되고 lists2 요소는 그대로

# 리스트의 요소 꺼내기
lists.pop() # 해당하는 리스트에 마지막 인덱스값을 리턴하고, 그 해당요소는 리스트에서 삭제
lists.pop(i) # 해당하는 인데스값을 리턴하고 리스트에서 삭제
lists.remove(val) # 인자로 들어온 값과 일치하는 리스트의 요소를 삭제
# 리스트의 요소삭제
del lists[i:j] # i번재 인덱스부터 j번째까지 요소 삭제
del lists[3::] # 4번째 값을 포함한 이후부터의 요소값 삭제
lists.clear() # 모든 요소 제거
# 리스트의 순서를 반대로
lists.reverse()

# range()
list(range(i)) # 0-ㅑ번째까지 숫자를 요소를 갖는 배열 생성. 마지막 숫자는 ㅑ-1
list(range(i,j)) # i~j-1까지의 숫자를 요소를 갖는 배열생성. 
list(range(i,j,k)) # i~j까지 5씩 더한 숫자를 요소로 갖는 배열 생성
# tuple, dict
# tuple immutable
# ()로 감싼다
days = ("mon", "tue", "wed", "thur", "fri")
print(days)
print(type(days))
lists.extend(days) # 리스트에 튜플 이어붙이기
# 문자열에 리스트 이어붙이기 str.join(iter)
# bytes 객체를 연결하는 경우 bytes.join(iter)
# dictionary. js의 객체
name = "siwoo"
age = 37
korean = True
fav_food = ["milk", "hichu"]

siwoo = {
    "name": "siwoo",
    "age": 37,
    "korean": True,
    "fav_food": ["milk", "hichu"]
}
print(siwoo)
print(type(siwoo))
siwoo["handsome"] = True
print(siwoo)
siwoo.pop(["handsome"])
print(siwoo)
