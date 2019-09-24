# <혼자 공부하는 파이썬> 챕터 4-1

# 리스트의 특징
# 1. 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있다.
# 2. 리스트 접근 연산자를 이중으로 사용할 수 있다.
# 3. 리스트 안에 리스트를 사용할 수도 있다.

# 리스트 연산자
list_a = [1,2,3]
list_b = [4,5,6]
print("list_a =", list_a)
print("list_b =", list_b)
print()

print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

print("len(list_a) =", len(list_a))

# 리스트에 요소 추가하기
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)
print(list_a)
print()

list_a.insert(2,10)
print(list_a)

list_a.extend([4,5,6]) # 한번에 여러가지 요소를 추가하고 싶을 때 사용하는 함수이다.
print(list_a)

# 리스트에 요소 제거하기
# 1. del
# 2. pop
list_a = [0,1,2,3,4,5]

del list_a[1]
print("del list_a[1] =", list_a)

list_a.pop(2)
print("pop(2) =", list_a)

# 특정한 값으로 요소 제거하기
list_c = [1,2,1,2]
list_c.remove(2) # remove 함수와 반복문을 조합하면 중복 값을 제거하는 함수를 만들 수 있다.
print(list_c) # 요소를 모두 제거하고 싶을 땐 clear 함수를 사용한다.

# for 반복문
array = [273,32,103,57,52]

for element in array:
    print(element)


# <혼자 공부하는 파이썬> 챕터 4-2

# 딕셔너리의 요소에 접근하기
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

print("name :", dictionary["name"])
print("type :", dictionary["type"])
print("ingredient :", dictionary["ingredient"])
print("origin :", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"])

print(dictionary["ingredient"][1]) # 딕셔너리 안에 있는 리스트의 특정 요소도 불러올 수 있다.

# 딕셔너리에 요소 추가하기
dictionary = {}

print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

# 딕셔너리 내부에 키가 존재하는지 확인하고 값에 접근하기
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}

key = input(">접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get()함수를 통하여 존재하지 않는 키 확인하기
value = dictionary.get("존재하지 않는 키")
print("값:",value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")


# <혼자 공부하는 파이썬> 챕터 4-3

# 리스트와 범위를 조합해서 사용하기
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i,array[i]))

# 반대로 반복하기
for i in range(4,0-1,-1):
    print("현재 반복 변수: {}".format(i))

for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i)) # reversed 함수를 이용하면 파이썬이 알아서 뒤집어서 반복문을 돌려준다.


# while 반복문
# while True:
#     print(".",end=" ")

# while 반복문을 for 반복문처럼 사용하기
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# 해당하는 값 모두 제거하기
list_test = [1, 2, 1, 2]
value = 2
while value in list_test:
    list_test.remove(value)
print(list_test)

# 시간을 기반으로 반복하기
import time

print(time.time())

# 5초동안 반복하기
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초동안 {}번 반복했습니다.".format(number)) # 이 코드는 통신을 할 때 자주 사용하는 코드이니 시간을 기반으로 조건을 걸 때는 while 반복문을 활용한다고 기억해두자.

# break 키워드
i = 0

while(1):
    print("{}번째 반복문입니다.".format(i))
    i += 1
    input_text = input("> 종료하시겠습니까?(y/n): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break

# continue 키워드
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)


# <혼자 공부하는 파이썬> 챕터 4-4

# reversed() 함수
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("reversed([1,2,3,4,5]):", list_reversed)
print("list(reversed[1,2,3,4,5]):", list(list_reversed))
print()

print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

# enumerate() 함수와 리스트
example_list = ["요소A", "요소B", "요소C"]

print("enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("반복문과 조합하기")
for i,value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))