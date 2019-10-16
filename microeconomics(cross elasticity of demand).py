def CED (P1,P2,Qd1,Qd2):
    result = ((Qd2 - Qd1)*(P1 + P2)) / ((P2-P1)*(Qd1 + Qd2))
    return round(result,2)

Price_1 = float(input("y 재화의 변동 전 가격을 입력하시오: "))
Price_2 = float(input("y 재화의 변동 후 가격을 입력하시오: "))
Quantity_Demand_1 = float(input("x 재화의 변동 전 수요량을 입력하시오: "))
Quantity_Demand_2 = float(input("x 재화의 변동 후 수요량을 입력하시오: "))

Cross_Elasticity_of_Demand = CED(Price_1, Price_2, Quantity_Demand_1, Quantity_Demand_2)
if Cross_Elasticity_of_Demand < 0:
    Relationship_of_Goods = "보완재"

else:
    Relationship_of_Goods = "대체재"
print("수요의 교차탄력성은", Cross_Elasticity_of_Demand, "이고, x 재화와 y 재화의 관계는", Relationship_of_Goods, "입니다.")