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