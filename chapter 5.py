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

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print("0 to 100:", sum_all(0,100))

# <혼자 공부하는 파이썬> 챕터 5-2

# 재귀함수를 이용하여 팩토리얼 구하기, 재귀함수란 나 자신을 호출하는 것을 말한다.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("5!:", factorial(5))

# 피보나치 수열을 재귀함수로 구현하기
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(5):", fibonacci(5))

# 메모화 : 딕셔너리를 사용하여 한번 계산한 값을 저장하는 것을 메모라고 하는데 이를 이용하면 재귀함수도 매우 빠르게 계산할 수 있다.
dictionary = {
    1: 1,
    2: 1,
}

def fibonacci_1(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci_1(n-1) + fibonacci_1(n-2)
        dictionary[n] = output
        return output

# print("fibonacci(35):", fibonacci(35))
print("fibonacci_1(35):", fibonacci_1(35))


# <혼자 공부하는 파이썬> 챕터 5-3

# 튜플의 특이한 사용, 튜플은 따로 괄호를 사용하지 않아도 파이썬은 튜플로 인식할 수 있다.
tuple_test = 10,20,30,40
print("tuple_test:", tuple_test)
print(type(tuple_test))
print()

a, b, c = 10, 20, 30
print("a:", a)
print("b:", b)
print("c:", c)

# 변수의 값을 교환하는 튜플, 자주 사용되는 방식이니 기억해두는 것이 좋다.
a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)

# 여러 개의 값을 리턴하기, 괄호 없이 할당할 수 있는 것은 튜플만이 가능한 일이니 튜플이랑 같이 기억해두는 것이 좋다.
def test():
    return (10, 20)

a, b = test()
print("a:", a)
print("b:", b)

# 함수의 매개 변수로 함수 전달하기
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

# map() 함수와 filter()함수
def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("map(power, list_input_a):", list(output_a)) # map 함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 만들어주는 함수이다.
print()

output_b = filter(under_3, list_input_a)
print("filter(under_3, list_input_a):", list(output_b)) # filter 함수는 리스트의 요소를 함수에 넣고 그 중 참인 값으로 새로운 리스트를 만들어주는 함수이다.
print()

# lambda는 함수를 매우 쉽게 선언할 수 있다. 파이썬에 있는 대표적인 기능 중 하나이며 간단한 함수를 선언할 때 자주 이용된다.

# 이 함수를 람다를 사용하면 다음과 같이 표현된다.
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

power = lambda x : x * x
under_3 = lambda x : x < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a) # 위에서 람다로 함수를 미리 선언하지 않고 power의 위치, 즉, 매개변수에 람다를 넣을 수 있다.
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("filter(under_3, list_input_a):", list(output_b))
print()

# 제너레이터 함수 : 이터레이터를 만드는 함수이다. 쉽게 나눠서 yield와 next를 이용하여 함수를 yield에 따라 구분하여 나눠서 사용할 수 있다는 것이다.
def test():
    print("함수가 호출되었습니다")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
print()

# 제너레이어 객체와 next()함수
def test1():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test1()

print("D 지점 통과")
a = next(output) # next 함수는 함수 속 yield 위에까지 실행하고 yield 뒤에 나온 값을 반환한다.
print(a)

print("E 지점 통과")
b = next(output)
print(b)

# next(output) 함수의 범위를 벗어나면 오류가 생기게 된다. 여기서는 C 지점 통과까지 나오고 오류가 생긴다.