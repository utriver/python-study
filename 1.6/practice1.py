class User:
    total_users = 0
    def __init__(self,username = 0,points = 0):
        self.username = username
        self.points = points
        User.total_users+=1
    def add_points(self,amount):
        self.points+=amount
    def get_level(self):
        if self.points>=500:
            return "Gold"
        elif self.points>=100:
            return "Silver"
        else:
            return "Bronze"
    @classmethod
    def get_total_users(cls):
        print(f"총 유저수: {User.total_users}")
        
        
users = [User("철수",80),User("영희",400),User("민수", 350)]

for user in users:
    point = int(input(f"{user.username}의 추가점수를 입력하시오: "))
    user.add_points(point)
    print(user.get_level())
User.get_total_users()        