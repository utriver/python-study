money = 300000
book = 80000
lunch = 9000
earning_money = 120000
plus_percent = 20
extract_percent = 1/3

result = ((money -book-lunch*5+earning_money)*(1+plus_percent/100))*(1-extract_percent)
print(int(result))
# new methods
money = 300000
money -= book
money -= lunch*5
money += earning_money
money = money+money*0.2
money *= (1-extract_percent)
print(int(money))
print(type(money))