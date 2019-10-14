# 수요의 소득탄력성을 구하는 간단한 프로그램
def IED (Income_1,Income_2,Quantity_demand_1,Quantity_demand_2):
    result = ((Quantity_demand_2-Quantity_demand_1)*(Income_2+Income_1)) / ((Income_2-Income_1)*(Quantity_demand_1+Quantity_demand_2))
    return round(result,2)

while(1):
    answer = input("수요의 소득탄력성을 구할까요?(Y/N): ")
    if answer in ["y","Y"] :
        Inc1 = float(input("첫번째 소득 가격을 입력하세요: "))
        Qd1 = float(input("첫번째 재화의 수요량을 입력해주세요: "))
        Inc2 = float(input("두번째 소득 가격을 입력하세요: "))
        Qd2 = float(input("두번째 재화의 수요량을 입력해주세요: "))
        
        Inc_Elasticity = IED(Inc1,Inc2,Qd1,Qd2)
        if Inc_Elasticity < 0:
            Goods = "열등재"
        elif 0 < Inc_Elasticity < 1:
            Goods = "필수재"
        else:
            Goods = "사치재"

        print("이 재화의 수요의 소득탄력성은", Inc_Elasticity,"이고, 이 재화는", Goods, "입니다.")
    
    elif answer in ["n","N"]:
        break

    else:
        continue