# com = [i**2 for i in range(1,11)]
# print(com)
# three_mul = [k for k in range(1,51) if k%3 == 0]
# print(three_mul)
# fruits = ["apple","fig", "banana", "plum",
#           "cheery","pear", "orange"]
# over5=[w for w in fruits if len(w)>5]
# print(over5)
# print("문제1")
# secret_code = "codingonre3"

# pw=input("비밀 코드를 입력하세요: ")
# while (pw!=secret_code):
#     pw = input("다시 입력하세요: ")
# print("입장이 허용되었습니다.")


import random
print("문제2")
print("1~100사이 무작위 수를 생성중입니다")
random_num = random.randrange(1,101)
hint = print(f"힌트는 {random_num}입니다.")
num=int(input("숫자를 입력하세요"))
count = 0

while(num != random_num):
    if random_num>num:
        print(f"{num}보단 커요.")
        num=int(input("숫자를 입력하세요"))
    else:
        print(f"{num}보단 작아요.")
        num=int(input("숫자를 입력하세요"))
    count+=1
    
print(f"{count}번 만에 정답을 맞췄습니다.")