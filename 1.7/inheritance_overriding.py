#상속과 오버라이딩
#상속이란 기존 클래스를 물려받아서 기능을 그대로 쓰거나 확장하는것


class Speaker:   #부모클래스(기본적인 기능)
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
    def play_sound(self):    #모든 스키커가 공통으로 가지는 기능
        print("소리를 재생합니다. ")

# 오버라이딩
# 부모메서드를 자식 클래스에서 다시 만듦
class SmartSpeaker(Speaker):  #상속, 스피커의 기능을 물려받음
    
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
        
    def play_sound(self):    #부모의 play_sound를 덮어씀
        super().play_sound()        #부모 클레스 매서드 호출       
        print("AI가 추천할 음악을 재생합니다.")    #자신만의 동작


# sp = Speaker() 
   
normal = Speaker()
smart = SmartSpeaker()

# normal.play_sound()
smart.play_sound()
#같은 매서드
#객체에 따라 다른동작

