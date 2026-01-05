# cost = int(input("금액을 입력해주세요"))
# projuct = input("상품을 입력해주세요(최대3개): ").split(',')
# cost_dict = {"김밥":2500,"삼각김밥":1500,"도시락":4000}
# if len(projuct) ==3:
#     if cost>=cost_dict[projuct[0]]+cost_dict[projuct[1]]+cost_dict[projuct[2]]:
#         print("구매 성공")
#     else:
#         print("금액이 부족합니다.")
# if len(projuct) ==2:
#     if cost>=cost_dict[projuct[0]]+cost_dict[projuct[1]]:
#         print("구매 성공")
#     else:
#         print("금액이 부족합니다.")
# if len(projuct) ==1:
#     if cost>=cost_dict[projuct[0]]:
#         print("구매 성공")
#     else:
#         print("금액이 부족합니다.")
# if len(projuct) ==0:
#     print("금액을 입력하세요.")
lis=1234
num = str(lis)
a=num.find(str(0))
print(a)