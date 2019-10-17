# <혼자 공부하는 파이썬> 챕터 5-1

# 기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# 매개변수의 기본

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5)

# 가변 매개변수 함수
def print_n_times(n, *values): # 가변 매개변수는 뒤에 나오는 모든 변수들을 하나의 튜플로 만들어준다.
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# 기본 매개변수

def print_k_times(value, n=2):
    for i in range(n):
        print(value)

print_k_times("안녕하세요")

# 키워드 매개변수
def print_l_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_l_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# 여러 함수 호출 형태
def test(a, b=10, c=100): # 변수 안에 특정한 값을 지정하지 않는다면 함수에 선언된 그 숫자들로 함수가 처리된다.
    print(a + b + c)

test(10,20,30)

test(a=10, b=100, c=200)

test(c=10, a=100, b=200)

test(10, c=200)

# 아무 자료 없이 리턴하기
def return_test():
    print("A 위치입니다.")
    return # 함수를 종료하라는 의미를 담고 있기도 하다.
    print("B 위치입니다.")

return_test()

# 자료와 함께 리턴하기

def return_test():
    return 100

value = return_test()
print(value)