import random

class Character:
    member = 0 
    def __init__(self,name,level,health,role):
        self.name = name
        self.level = level
        self.__health = health
        self.role = role
        Character.member+=1
    @property
    def check(self):
        return self.__health
    @check.setter
    def check(self,change):
        self.__health = change
    
    def show_info(self):
        print(f"이름: {self.name}, 레벨: {self.level}, 체력: {self.__health}, 역랄: {self.role}")
    def take_damage(self,damage):
        self.__health-=damage
        if self.__health == 0:
            print("사망")
    # def level_up(self,plus):
    #     self.level+=plus
    # def 
    @classmethod
    def count_all(cls):
        return(cls.member)

    @staticmethod
    def health_calculator(now,damage):
        return now-damage
            
class Warrior(Character):
    def __init__(self):
        self.attack_gage = 10
    def attack(self):
        print("전사가 검으로 공격합니다!")
        return self.attack_gage
class Mage(Character):
    def __init__(self):
        self.attack_gage = 15
    def attack(self):
        print("마법사가 마법을 사용합니다!")
        return self.attack_gage
if __name__ == '__main__':
    member = []
    while(True):
        print("""-메뉴 예시-
    1. 캐릭터 생성
    2. 전체 캐릭터 보기
    3. 공격 실행
    4. 종료""")
        num = int(input("번호 입력: "))
        if num ==1:
            name,level,health,role = input("[이름,레벨,체력,역할]을 입력하세요 : ").split(',')
            character = Character(name,int(level),int(health),role)
            member.append(character)
        elif num == 2:
            print(f"전체 캐릭터 목록(총 {Character.count_all()})")
            for ch in member:
                ch.show_info()
        elif num ==3:
            #공격 -> 필요한것: 공격자,공격 대상(대상 선택 or 데미지 랜덤)
            #공격자, 공격할 대상을 입력
            #공격 메서드 활성화
            #공격 받은 대상 체력 감소
            attacker = input("공격자를 입력하세요: ")
            attacked = input("공격 대상자를 입력하세요: ")

            for ch in member:
                if ch.name == attacker:
                    if ch.role == "전사":
                        warrior = Warrior()
                        attack_gage = warrior.attack()
                    else:
                        mage = Mage()
                        attack_gage = mage.attack()

            for ch in member:
                if ch.name ==attacked:
                    ch.take_damage(attack_gage)
                    if ch.check == 0:
                        member.remove(ch)
                    else:
                        print(f"{attacked}의 현재 체력은 {ch.check}")
                # else:
                #     select_ = random.randint(0,len(member))

        elif num ==4:
            break


