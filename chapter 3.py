# <혼자 공부하는 파이썬> 챕터 3-1

# not 연산자 조합하기
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20:", not under_20)

# 조건문의 기본 사용
number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다")

if number < 0:
    print("음수입니다")

if number == 0:
    print("0입니다")

# 날짜/시간 출력하기
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 날짜/시간 한 줄로 출력하기
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전과 오후를 구분하는 프로그램
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

else:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# 계절을 구분하는 프로그램
import datetime

now = datetime.datetime.now()

if now.month < 3 or now.month > 11:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

elif 3 <= now.month < 6:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

elif 6 <= now.month < 9:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

elif 9 <= now.month < 12:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

# 끝자리로 짝수와 홀수 구분
number = input("정수 입력> ")
last_character = number[-1]
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9 :
    print("홀수입니다")

# in 문자열 연산자를 이용해서 짝수, 홀수 구분하기
number = input("정수 입력> ")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다")

if last_character in "13579":
    print("홀수입니다")

# 나머지 연산자를 활용해서 짝수와 홀수 구분
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

if number % 2 == 1:
    print("홀수입니다")


# <혼자 공부하는 파이썬> 챕터 3-2

# else 조건문의 활용
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

else:
    print("홀수입니다")

# 계절 구하기
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다.")

elif 6 <= month <= 8:
    print("현재는 여름입니다.")

elif 9 <= month <= 11:
    print("현재는 가을입니다.")

else:
    print("현재는 겨울입니다.")

