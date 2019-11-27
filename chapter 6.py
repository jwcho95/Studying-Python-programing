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

# try, except 구문과 pass 키워드 조합하기 (숫자로 변환되는 것들만 리스트에 넣기) : try, except 구문은 if 구문을 활용하는 코드보다 약간 느리다.
list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))

# try except else 구문 : 예외가 발생할 것 같은 구문을 try 안에 넣고 예외가 발생하지 않았을 경우 실행할 코드를 else 구문에 넣는 방식이다. 이런 방식은 파이썬이나 루비에서 볼 수 있다.
try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# finally 구문 : 예외가 발생하든 안하든 무조건적으로 실행하는 코드이다. 강제 실행 코드라고 생각하면 편하다.
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

# 파일이 제대로 닫혔는지 확인하기
try:
    file = open("info.txt", "w")
    file.close()

except Exception as e: # 예외를 예외변수에 넣어 출력하도록 하는 방법이다.
    print(e)

print("file.closed:", file.closed)
print()

# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()

except Exception as e: # 예외가 예외변수 e에 저장되었기 때문에 어떤 예외가 발생했는지 출력하도록 할 수 있다.
    print(e)

print("file.closed:", file.closed)
print()

# finally 구문 사용해 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()

except Exception as e:
    print(e)

finally: # 여기서는 굳이 finally 구문을 이용한 후 파일을 닫았지만 이거 없이 try, except 구문이 모두 끝난 후 파일을 닫아도 된다.
    file.close()

print("file.closed:", file.closed)
print()

# try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫줄 입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return # 반환을 하는 순간 이 함수는 종료된다. 그렇기 때문에 try 구문이 다 실행되지도 else 구문이 실행되지도 않는다.
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally: # 그러나 finally 구문은 다르다. 이것은 함수가 종료된다고 하더라도 실행이 된다. 이것이 굉장한 것이다.
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()
print()

# 반복문과 함께 사용하는 경우
print("프로그램이 시작되었습니다.")

while(1):
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally: # break 키워드로 try 구문 전체를 빠져나가도 finally 구문이 실행된다.
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막 줄입니다.")

print("프로그램이 종료되었습니다.")
print()

# 예외 객체 (Exception) : Exception은 클래스이다. 이것으로 예외의 종류를 알 수 있다.
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print('type(exception):' , type(exception))
    print("exception: ", exception)

# 여러가지 예외가 발생할 수 있는 코드
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception): ", type(exception))
    print("exception: ", exception)
print()

# 예외 구분하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError: # ValueError가 발생했을 때 아래의 구문이 실행된다.
    print("정수를 입력해주세요.")
except IndexError: # ValueError와 마찬가지로 다음과 같은 오류가 발생하면 아래의 구문이 실행된다.
    print("리스트의 인덱스를 벗어났어요!")
print()

# 예외 구문과 예외 객체
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception: # 예외 구문 뒤에 예외 객체를 추가해도 제대로 작동한다.
    print("정수를 입력해주세요.")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)
print()

# 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생() # 강제적으로 예외를 발생시킨다.
except ValueError as exception:
    print("정수를 입력해주세요.")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)
except Exception as exception: # 이 구문이 존재하지 않는다면 위에 작성된 코드는 오류가 나서 작동을 멈출 것이다.
    print("미리 파악하지 못한 예외가 발생하였습니다.")
    print(type(exception), exception)

# raise 구문
# 프로그램이 강제적으로 종료되는 것을 막기 위해서는 필히 예외를 처리해야하나 일부러 강제종료를 시키는 경우도 있다.
# 구현되지 못한 부분이나 꼭 한번 더 확인해야하는 구간에 raise 구문을 이용해 강제적으로 오류를 일으킬 수 있다.
# raise + 예외 객체
# raise 뒤에 예외 이름을 입력하면 오류가 발생한다.