"""실습 1. 중첩 if
영화관 입장 가능 여부
조건
• 회원이어야 함
• 성인(19세 이상) 이면 바로 입장
• 미성년자면
보호자 동반 and
야간 상영 아님 → 입장 가능"""
is_member = input("회원인가요? (y/n)")
age = int(input("나이를 입력하세요: "))
with_parent = input("보호자 동반인가요? (y/n)")
is_night = input("야간 상영인가요? (y/n): ")

if is_member == "y":
    if age >= 19:
        print("입장 가능")
    else:
        if with_parent == "y" and is_night =="n":
            print("입장 가능")
        else:
            print("입장 불가")
else:
    print("입장 불가")