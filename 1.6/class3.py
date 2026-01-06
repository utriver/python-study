class Student:
    #클래스 변수
    school = "파이썬 고등학교" 
    
    def __init__(self, name, score):
        self.name = name  # 학생마다 이름 다름
        self.score = score #학생마다 점수가 다름
        
    ###########################################
    #인스턴스 매서드
    ############################################
    def show(self):
        #self -> 이 매서드를 호출한 "객체자신"
        #인스턴스 매서드
        print(self.name,self.score, Student.school)
        
    #=======================================
    #클래스매서드
    #=======================================
    @classmethod
    def change_school(cls,new_school):
        #cls -> 클래스 자신(Student)
        #인스턴스 변수(self.xxxx)는 사용x
        #클래스 변수만 사용 o
        cls.school = new_school
    # =====================================    
    #정적매서드
    # ========================================
    @staticmethod
    # self x
    # cls  x
    # 클래스 안에 있지만
    # 클래스 / 객체 정보 전혀 안씀
    # "관련있는 함수"를 묶어둔것
    
    def is_pass(score):
        if score >= 60:
            return "합격"
        else:
            return "불합격"

        
s1 = Student("철수",90)
s2 = Student("영희",70)

#인스턴스 매서드 사용
# 각 객체의 값 사용 가능
s1.show()
s2.show()        
#클래스 매서드 사용
#모든 객체에 영향을 미침
Student.change_school("자바고등학교")
s1.show()
s2.show()

#스태딕매서드 사용
print(s1.is_pass(60))  #권장하지 않음
print(Student.is_pass(80))


#절대 헷갈리면 안되는 차이!!
#클래스 메서드는 아래의 내용이 안됨
# @classmethod
# def wrong(cls):
#     print(self.name)

# def wron(self):
#     self.school = "C언어 고등학교" -> 새로운 인스턴스 변수가 생성

#접근 기준
#self -> 한명
#cls -> 전체
#구분          |     인스턴스        |    클래스매서드
#첫번째 인자   |      self           |    cls
#호출방법      |      객체.매서드()   |    클래스.매서드()
#접근가능      |      인스턴스+클래스 |    클래스만
#용도          |      개인행동       |    전체 설정
#예시          |      점수 출력      |    학교 변경


#최종요약
#인스턴스 매서드 =  개인용
# 클래스 매서드 = 공용설정

#스태틱 매서드 핵심 주의점
# 의미없는 행동예시
@staticmethod
def wrong(self):
    print(self.name)  #접근불가

# 스태틱매서드 언제 사용?
# 클래스/객체상태를 전혀 모를때만 사용

#언제 어떤 매서드를 쓰냐?
# self 필요 -> 인스턴스 매서드
# cls 필요 -> 클래스 매서드
# 둘다 필요x -> 정적 매서드

#비유예시
# 인스턴스 매서드-> 학생 개인행동
# 클래스 매서드 -> 학교 규칙 위반
# 스태틱 매서드 -> 계산기

#결론
# 스태틱 매서드는 "클래스와 관련은 있지만 상태는 필요없는 함수(도우미)"
