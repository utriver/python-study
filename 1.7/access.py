# #정보 은닉과 캡슐화
# #public / protected / private


# class Box:  #Box라는 클래스 생성
#     school = "파이썬 고등학교"
#     def __init__(self, name, price, secret):  #객체가 만들어질때 자동 실행되는 함수
#          self.name = name  #public  어디서든 접근 가능
#          self._price = price  #protected   외부 접근 가능하지만 건들지 말것
#          self.__secret = secret  #private    클래스 내부에서만 사용
         
#     def show(self):     # 박스 정보 출력용 메서드
#         print(self.name)  #자유롭게 접근 가능
#         print(self._price)  #외부접근 가능하지만 권장하지 않음  내부에서 Ok
#         print(self.__secret)  #클래스 내부에서만 OK
    
#     def get_secret(self):  #private값을 꺼내기 위한 메서드
#         return self.__secret    #외부에서는 이 방법으로만 접근가능
    
    
# box = Box("사과박스", 1000, "비밀번호")
# print(box.name)  #가능 public이라서
# print(box._price)  #가능 단,권장하지 않음
# # print(box.__secret)  #불가능 -> 에러 발생
# print(box.get_secret()) #올바른 접근
   
#캡슐화 -> 데이터를 직접 만지지 못하게 하고 메서드를 통해서만 사용
#캡슐화 안한경우
# class Speaker:
#     def __init__(self):
#         self.volume = 5
        
# sp = Speaker()
# sp.volume = 100  #  X 말도 안되는 값
# sp.volume = -10  #  X 말도 안되는 값

# print(sp.volume,"확인용")   

#캡슐화인경우
class Speaker:
    def __init__(self):
        self.__volume = 5

    @property     #getter역할-> sp.volume으로 읽기가 가능
    def volume(self):    #값 읽기 전용
        return self.__volume   #private값 반환
    
    @volume.setter    #setter역할 -> sp.volume = 값 형태가 가능
    def volume(self,value):  #setter(값 설정 담당)
        if 0 <= value <=10: #값 검증
            self.__volume = value   #검증 통과한 것만 저장
            print(self.get_volume())
        else:
            print("볼륨은 0~10사이에서만 가능")


        
sp = Speaker()    
# sp.get_volume()
# sp.set_volume(7)  
#문범이 어색함-> 변수처럼 쓰고 싶은데 메서드처럼 써야 함  
# sp.volume = 100
#값 검증 불가
#내부 상태 망가짐 -> 직접접근x, 매서드로만 접근
#property 
#매서드인데 변수처럼 쓰게 해주는 문법


print(sp.volume) #getter호출
sp.volume = 8 #setter 호출
sp.volume = 20 #x 제한됨
#겉보기에는 변수이지만 속은 매서드


#비교정리
#방식               사용법
#직접접근           sp.volumex
#getter/setter      get_volume()/set_volume()
#@property          sp.volume o

#캐슐화란?
#데이터는 숨기고 접근 통제 사용은 편하게
#@property는 캡슐화를 유지하면서 변수처럼 사용하게 해준다.

        

        
        