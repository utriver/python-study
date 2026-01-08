class UserAccount:
    def __init__(self,username,__password):
        self.username = username
        self.__password = __password
    
    def change_password(self,old_pw, new_pw):
        if self.__password ==old_pw:
            print("변경허용")
            self.__password=new_pw
        else:
            print("비밀번호 불일치")
    
    def check_password(self,password):
        if self.__password==password:
            return True
        else:
            return False
        
usr = UserAccount("김우진",1234)
old,new = input("기존 비번과 신규 비번을 입력하세요: ").split(',')
usr.change_password(int(old),int(new))
password = int(input("비밀번호를 입력하세요: "))
print(usr.check_password(password))


class Student:
    def __init__(self,score):
        self.__score = score
    @property
    def test(self):
        return self.__score
    @test.setter
    def test(self,num):
        if 0<= num <= 100:
            self.__score = num 
        else:
            raise ValueError("범위를 벗어났습니다.")
        
s=Student(30)
s.test=int(input("점수를 입력하시오:"))
print(s.test)
s.test=int(input("점수를 입력하시오:"))
print(s.test)