# -*-coding:utf-8 -*-
# 반복문
days = ("mon", "tue", "wed", "thu", "fri")
new_list = []
for el in days:
    new_list.append(el)
print(new_list)
print(list(days))

for day in days:
    if day is "wed":
        break
    else:
        print(day)

for letter in "siwoopak":
    print(letter)
