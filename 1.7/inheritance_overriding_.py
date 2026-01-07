#상속  상속 + init = super()세트


class Parent:
    def __init__(self,x):
        self.x = x
        
class Child(Parent):
    def __init__(self,x,y):
        super().__init__(x)  #부모 클래스의 생성자 실행, 부모 변수 초기화
        self.y = y     #자식클래스 전용변수



# c=Child(10,20)
# print(c.x)
# print(c.y)
#자식 __init__이 부모것을 덮어씀
#부모 초기화가 실행되지 않음
