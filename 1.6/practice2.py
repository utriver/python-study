class MoneyItem:
    def __init__(self, date, name, money, type):
        self.date = date
        self.name = name
        self.money =money
        self.type = type
    def show(self):
        info_= {"날짜":self.date,
                "이름": self.name,
                "금액":self.money,
                "수입/지출 정보":self.type}
        print(info_)   
        
        
items = []


while(True):
    select=int(input("""원하시는 항목 번호를 선택해주세요
1. 내역 추가
2. 전체 내역 보기
3. 총 수입 / 총 지출 / 잔액 보기
4. 특정 금액 이상 지출 보기
5. 특정 날짜 내역 보기
6. 종료
--->"""))
    if select == 1:
        information = input("날짜,항목이름, 금액, 종류(수입/지출) 형식으로 입력하세요: ").split(',')
        money_item = MoneyItem(information[0],information[1],int(information[2]),information[3])
        items.append(money_item)
    elif select == 2:
        for item in items:
            item.show()
    elif select == 3:
        income = 0
        expense = 0
        for item in items:
            if item.type == '지출':
                expense+=item.money
            elif item.type == '수입':
                income+=item.money
        print(f"총 수입:{income}\n총 지출:{expense}\n잔액:{income-expense}")
    elif select == 4:
        
        regular = int(input("특정 금액 이상 지출 보기: "))
        for item in items:
            if item.type == "지출" and item.money>= regular:
                item.show()

    elif select == 5:
        w_date = input("조회할 날짜를 입력하세요: ")
        for item in items:
            if item.date == w_date:
                item.show()
            else:
                print("조회하신 날짜에 내역이 존재하지 않습니다.")
    elif select ==6:
        break
            