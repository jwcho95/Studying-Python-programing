# 수요가격탄력성을 구하는 간단한 프로그램
def PED (Price_1,Price_2,Quantitiy_demand_1,Quantitiy_demand_2):
    mid_point_P = (Price_2 + Price_1) / 2
    mid_point_Qd = (Quantitiy_demand_1 + Quantitiy_demand_2) / 2

    percent_change_in_P = (Price_2 - Price_1) / mid_point_P
    percent_change_in_Qd = (Quantitiy_demand_2 - Quantitiy_demand_1) / mid_point_Qd

    Price_Elasticity_of_Demand = percent_change_in_Qd / percent_change_in_P

    print(round((-1)*Price_Elasticity_of_Demand,2)) # round 함수를 이용하면 내가 원하는 자리까지 나오게 가능하다.

while(1):
    answer = input("수요가격탄력성을 구할까요?(Y/N): ")
    if answer in ["y","Y"] :
        P1 = int(input("첫번째 재화의 가격을 입력하세요: "))
        Qd1 = int(input("첫번째 재화의 수요량을 입력해주세요: "))
        P2 = int(input("두번째 재화의 가격을 입력하세요: "))
        Qd2 = int(input("두번째 재화의 수요량을 입력해주세요: "))
        
        PED(P1,P2,Qd1,Qd2)
    
    elif answer in ["n","N"]:
        break

    else:
        continue