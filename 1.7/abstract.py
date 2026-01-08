from abc import ABC, abstractclassmethod

# 추상 클래스 VS 일반 클래스
# 일반 클래스 -> 바로 써도 되는 완제품
# 추상 클래스 -> 혼자 쓰면 안 되는 설계도

#일반 클래스
# - 버튼 누르면 바로 음료 나옴
# 바로 사용가능

# 추상클래스
# - 버튼 이름만 적힌판
# - 안에 기계가 없음
# - 직접 사용 불가

#일반 클래스

# class Dog:
#     def sound(self):
#         print("멍멍")

# d=Dog()     #바로 사용 가능
# d.sound()   #바로 사용 가능        
#특징
# - 바로 객체 생성 가능
# - 함수가 다 완성됨


#추상 클래스  (설계도)
        
class Animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("멍멍!")
    pass
class Cat(Animal):
    def sound(self):
        print("야옹!")  
        
        
# a= Animal() #에러!
d=Dog()
c=Cat()

d.sound()
c.sound()
#특징
# 직접 사용 x
# "이 함수 꼭 만들어라" 규칙만 있음
     
# d=Dog()
# d.sound()