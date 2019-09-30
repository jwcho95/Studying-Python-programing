n = int(input("팩토리얼로 나눌 수를 입력하시오.: "))
result = 1
while n > 1:
    new_number = n
    result *= new_number
    n -= 1

print(result)