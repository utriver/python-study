"""
dict생성방법
1.  {}사용-> 키는 문자열, 튜플, 숫자
2. dict()사용, zip함수와 같이 사용할 수 있음

dict 데이터 접근
1.딕셔너리 이름["key이름"]
2.get("키 이름", 키값이 없을때 출력할 문구)

dict 데이터 추가 및 수정
1. 딕셔너리값[키] = 값-> 이미 있는 값이면 값이 수정되고 없으면 새로운 키-값 쌍이 생김
2. update() -> 키 = "값"혹은 딕셔너리를 괄호 안에 넣어도 됨

dict 데이터 삭제
1. del 딕셔너리 이름[키]-> 키 항목 자체가 사라짐
2. pop(키, 해당 키가 없을때 출력 문구)->
3. 딕셔너리이름.popitem() -> 가장 마지막 키-값 쌍을 지우고 반환
4. clear(딕셔너리) -> 딕셔너리 자체를 없앰

주요메서드
1. 딕셔너리이름.keys()-> 모든 키 반환, 리스트로 보임 하지만 실제 리스트는 아니므로 주의
2.  딕셔너리이름.values()-> 모든 값 반환, 리스트로 보임 하지만 실제 리스트는 아니므로 주의
3. 딕셔너리이름.items()-> 모든 키-값 반환, 리스트로 보임 하지만 실제 리스트는 아니므로 주의
"""


print("실습1-1\n")
user = {}
user.update(
    username="skywalker",
    email = "sky@example.com",
    level = 5
)
# email_value = user.get("email")
email_value = user["email"]
print("email_value:",email_value)
user.update(level = 6)
print(user.get("phone","미입력"))
user.update(nickname = "sky")
del user["email"]
user.setdefault("signup_date","2025-07-10")
print(user)

print("\n실습1-2\n")
students = {}
students.update(Alice = 85, Bob = 90, Charlie = 95)
students.update(David=80)
students.update(Alice = 88)
del students["Bob"]
print(students)
