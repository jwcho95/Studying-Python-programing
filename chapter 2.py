# <혼자 공부하는 파이썬> 챕터 2-1

print(type('안녕하세요'))

print(type(273))

# 따옴표 사용하는 방법
print('"안녕하세요"라고 말했습니다')

print("\"안녕하세요\"라고 말했습니다")

print('\'배가 고픕니다\'라고 생각했습니다')

# 이스케이프 문자(\t)로 탭 사용하기
print("이름\t나이\t지역")
print("조재완\t25\t남양주") # \n 줄바꿈을 의미한다.

# '''를 사용하면 엔터를 누르는 곳마다 줄바꿈이 일어난다.
print('''\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
''')

# 문자 선택 연산자의 결과 출력
print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4]) # 리스트.[]를 하지 않아도 문자열에서는 인덱싱을 할 수 있다.

# 거꾸로 선택하기
print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[-5])
print("안녕하세요"[-4])
print("안녕하세요"[-3])
print("안녕하세요"[-2])
print("안녕하세요"[-1])


# <혼자 공부하는 파이썬> 챕터 2-2

# 파이썬에서의 지수 표현
print(0.52273e2) # 결과값 52.273
print(0.52273e-2) # 결과값 0.0052273

# 제곱 연산자
# 원주율을 이용하여 원의 둘레와 넓이 구하기
pi = 3.14159265
r = int(input("원의 반지름을 입력해주세요:"))
circumference = 2 * pi * r
area = pi * r ** 2
print("원의 둘레는", circumference, "이고, 원의 넓이는", area, "입니다.")

# 연산자의 우선순위는 일반적인 산수와 같이 *,/가 우선순위이고 그 다음이 +, - 이다. 그러나 내가 작성한 코드를 보는 사람이 헷갈릴 수 있으므로 항상 ()를 붙여주는 습관을 들이자.


# <혼자 공부하는 파이썬> 챕터 2-3

# 복합 대입 연산자 : 복합대입연산자를 활용한다면 a = a + 1 과 같이 번거롭게 코드를 작성할 필요가 없다.
string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)

# 입력 자료형
str = input("입력>")
print("자료:", str)
print("자료형:", type(str))
# print("입력 + 100:", str + 100) # 이 경우에 오류가 난다. 왜냐하면 입력값으로 받는 것은 숫자형이 아니라 자료형이기 때문이다.

# int()함수 활용하기
string_a = input("입력A>")
int_a = int(string_a)

string_b = input("입력B>")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)


# <혼자 공부하는 파이썬> 챕터 2-4

# format 함수로 숫자를 문자열로 변환하기

string_c = "{}".format(10)
print(string_c)
print(type(string_c))

# format() 함수의 다양한 형태

format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# 정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

# 기호 붙여 출력하기
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print(output_f)
print(output_g)
print(output_h)
print(output_i)

# 조합해보기
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print(output_j)
print(output_k)
print(output_l)
print(output_m)

# float 자료형 기본
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)

# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)

# 의미없는 소수점 제거하기
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)
print(type(output_b))

# 문자열 양옆의 공백 제거하기
input_a = """
    안녕하세요
문자열의 함수를 알아봅시다
"""
print(input_a)

print(input_a.strip())

# 문자열 찾기
output_a = "안녕안녕하세요".find("안녕")
print(output_a) # 결과값이 0이 나오는 이유는 문자열에서 안녕의 시작이 문자열의 0번째이기 때문이다.

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b) # 결과값이 2가 나오는 이유는 문자열을 뒤에서부터 거꾸로 셀 경우 안녕의 시작이 문자열의 2번째이기 때문이다.

# split() 함수
a = "10 20 30 40 50".split(" ") # split 함수 속에 있는 문자를 기준으로 문자열을 나눈다.
print(a)
