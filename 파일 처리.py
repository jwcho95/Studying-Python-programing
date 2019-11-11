# <혼자 공부하는 파이썬> 챕터 5-3 (파일처리는 파일이 생성되기에 따로 작업한다.)

file = open("basic.txt", "w")
file.write("Hello Python Programming...!")
file.close()

# with open("basic.txt", "w") as file:
#     file.write("Hello Python Programming...!")

#     위에 쓰여진 구문을 with 구문으로 바꾼 것이다.
#     이렇게 쓰면 close를 잊어도 자동으로 파일을 닫아준다.
#     파일로 흐르는 길을 만드는 함수인 open과 close를 잘 기억해두자.
#     이것은 네트워크에도 사용되는 개념이다.

with open("basic.txt", "r") as file:
    contents = file.read()
    print(contents)
    print()

# 랜덤하게 100명의 키와 몸무게를 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(100):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = format(round(random.randrange(140, 200) * 0.01,2),".2f")
        file.write("%s, %s, %s\n" %(name,weight,height))

# 만든 파일로 비만도 계산하기 (반복문으로 파일 한 줄씩 읽기)
with open("info.txt", "r") as file:
    print(type(height))
    for line in file:
        print(line.strip().split(", "))
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = float(weight) / (float(height) * float(height))
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join(["이름 : {}", "몸무게 : {}kg", "키 : {}m", "BMI : {}", "결과 : {}"]).format(name, weight, height, round(bmi,2), result))
        print()