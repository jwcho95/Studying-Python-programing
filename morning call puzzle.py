# 핸드폰 속 알람 기능 중 간단한 퍼즐로 해제하는 기능을 파이썬으로 구현하였다.

import random
number_list = []
new_number = random.randrange(1,10)
number_list.append(new_number)
n = 4 # 이 숫자를 조정하면 퍼즐에 등장하는 수의 갯수를 최대 9개까지 마음껏 늘릴 수 있다.
for i in range(n-1):
    while(1):
        new_number = random.randrange(1, 10)
        if new_number in number_list:
            new_number = random.randrange(1,10)
            if new_number in number_list:
                continue
            else:
                number_list.append(new_number)
                break
        else:
            number_list.append(new_number)
            break

print("다음 이 수들을 차례대로 입력해야 알람이 꺼집니다. 하나씩 입력하세요.", number_list)

while(1):
    result = []
    arranged_list = []
    for i in range(n):
        input_num = int(input("숫자를 하나씩 입력하세요: "))
        result.append(input_num)

    for i in result:
        arranged_list.append(i)
    arranged_list.sort()

    if result == arranged_list:
        print("알람을 해지합니다.")
        break
    else:
        print("알람이 계속됩니다. 다시 입력하십시요!")
        print()
        continue