# <혼자 공부하는 파이썬> 챕터 5-1

# 기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# 매개변수의 기본

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)