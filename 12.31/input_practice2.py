print("실습4-1\n")
height = int(input())
width = int(input())
dimmension, circumference = (height*width,height*2+width*2)
print(f"넓이:{dimmension}\n둘레: {circumference}")
print("\n실습4-2\n")
num = input()
print(f"""천의 자리: {num[0]}
백의 자리: {num[1]}
십의 자리: {num[2]}
일의 자리: {num[3]}""")

print("실습5\n")
year, month, day=input("년.월.일: ").split(sep=".")
hour, minute, sec=input("시:분:초: ").split(sep=":")
print(f"""Res3의 개강일은 {year}년{month}월{day}일
시작 시간은 {hour}시 {minute}분 {sec}초입니다.""")