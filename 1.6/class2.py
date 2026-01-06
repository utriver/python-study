class Student:
    #클래스 변수
    school = "파이썬 고등학교" #전역변수 느낌
    
    def __init__(self, name, score):
        #인스턴스 변수:self.변수
        #객체 하나하나가 각자 따로 가지는변수
        self.name = name  # 학생마다 이름 다름
        self.score = score #학생마다 점수가 다름
        
#객체 생성
s1 = Student("철수",90)
s2 = Student("영희",70)

print(s1.name)
print(s2.name)

print(s1.score)
print(s2.score)

s1.score = 100 #철수 점수 변경

print(s1.score)
print(s2.score)

print(s1.school)
print(s2.school)

s1.school = "자바 고등학교" # 클래스 변수를 바꾼게 아니라 새 인스턴스 변수가 생긴거임        

print(s1.school)
print(s2.school)

Student.school = "자바고등학교"

print(s1.school)
print(s2.school)

#접근순서
#1. 객체 안에 변수있는지 확인
#2. 없으면 클래스 안에서 찾음

print(s1.school)

#s1 안에 school 있음? X
#Student 안에 school있음? 있으면 -> ㅇㅋ 사용

