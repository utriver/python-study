user = ("minji",25,"Seoul")
user_rename = list(user)
user_rename[0] = "eunji"
user = tuple(user_rename)
print(user)

name,age,city = user

if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상자입니다.")
else:
    print("일반지역 보안 정책 적용대상자입니다.")

users = ("minji", "eunji","soojin","minji","minji")
count = 0
for i in users:
    if i == "minji":
        count +=1
print(count)
for i in users:
    if i =="soojin":
        print(users.index(i))
        break

sorted_users = list(users)
print(sorted(sorted_users))

