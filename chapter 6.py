# <혼자 공부하는 파이썬> 챕터 6-1

# 프로그램을 실행할때는 두 가지의 오류가 존재한다.
# 1. 프로그램 실행 전 발생하는 오류: 구문 오류(syntax error)
# 2. 프로그램 실행 중에 발생하는 오류: 예외(exception)

# 예외의 경우 프로그램이 정상적으로 작동하는 것처럼 보이다가 갑자기 프로그램을 죽게 만든다. 그러므로 예외 처리를 꼭 해주어야한다.
# 이 챕터에서는 예외 처리에 관해서 공부할 것이다.

# 예외를 처리하는 방법은 두 가지로 나뉜다.
# 1. 조건문을 사용하는 방법 (기본 예외 처리)
# 2. try 구문을 사용하는 방법
# 단, 구문 오류의 경우는 프로그램 자체가 실행되지 않기 때문에 예외 처리 방법으로 처리할 수 없다.

user_input_a = input("정수 입력> ")

if user_input_a.isdigit(): # isdigit()함수는 문자열이 숫자로 인식될 수 있는지를 확인하는 함수이다.
    number_input_a = int(user_input_a)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else: # 이 부분이 이번 챕터에서 중요시 봐야하는 부분이다. 정수를 입력하지 않았을 경우까지 고려해주어야 프로그램이 오류가 나지 않는다.
    print("정수를 입력하지 않았습니다.")

# try except 구문 : 예외가 발생할 가능성이 있는 코드를 try 구문 안에 넣고, 예외가 발생했을 시에 실행할 코드를 except 구문 안에 넣으면 된다.
try:
    number_input_b = int(input("정수 입력> "))
    print("원의 반지름:", number_input_b)
    print("원의 둘레:", 2 * 3.14 * number_input_b)
    print("원의 넓이:", 3.14 * number_input_b * number_input_b)
except:
    print("무언가 잘못되었습니다.")