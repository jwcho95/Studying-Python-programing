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

# 유머를 조건문으로 구현하기(1)
score = float(input("학점 입력> "))

if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif 0 <= score < 0.5:
    print("플랑크톤")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗") 


# 유머를 조건문으로 구현하기(2)
score = float(input("학점 입력> "))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗") # 위 조건문과 다른 점은 이 조건문에는 이미 한번 비교하였던 것은 제외하고 있다는 점이다.

# pass 키워드를 사용한 미구현 부분 입력
number = input("정수 입력> ")
number = int(number)

if number > 0:
    pass

else:
    pass # 코딩을 하다보면 큰 골격을 먼저 잡고 나중에 세부적인 것을 코딩하는 경우가 많은데 이 경우에 파이썬은 pass를 사용하여 미구현 부분이 있더라도 정상적으로 나머지 부분이 실행되도록 만들어졌다.
         # raise NotImplementError를 이용해서 강제로 오류를 일으켜 미구현 부분임을 알려줄 수도 있다.