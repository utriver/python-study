# class Box: #Box라는 상자를 만든다.
#     def __init__(self,name):    #상자를 만드는 순간 자동으로 실행
#         self.name = name # 상자 안에 name을 넣어라
    
#     def show(self):  #상자 안에 있는걸 출력
#         print(self.name)2
#     def showPrint(self):
#         print(f"{self.name} 입니다.")
        


# a = Box("사과")
# b = Box("바나나")

# a.show()
# b.show()

# a.showPrint()
# b.showPrint()



# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def pass_status(self):
#         if self.score >=60:
#             print(f"{self.name}합격")
#         else:
#             print(f"{self.name}불합격")
        
        
# if __name__ == "__main__":     
#     students = [
#         Student("철수",70),
#         Student("영희",55),
#         Student("민수",90)
#     ]

#     #출력하기 for문 사용
#     print("-------합격여부------")
#     for student in students:
#         student.pass_status()

print("문제1")
class Book:
    def __init__(self,title,author,total_pages,current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
    
    def read_page(self):
        if self.current_page<=self.total_pages:
            print("현재페이지는",self.current_page,"입니다.")
        else:
            print("잘못된 입력입니다.")
        pass
        

    def progress(self):
        if self.current_page<=self.total_pages:
            print(round(self.current_page/self.total_pages,1)*100,"%")

book1 = [Book("나니아연대기","C.S 루이스",500,302),
         Book("먼저온 미래","장강명",300,500)]
for book in book1:
    book.read_page()
    book.progress()

print("문제2")
class Rectangle:
    def __init__(self,width,height):
        self.width = int(width)
        self.height = int(height)
    
    def area(self):
        return self.width*self.height
    
    
information = input("너비와 높이를 입력하세요: ").split(',')   
rectancle1=Rectangle(information[0],information[1])
print(rectancle1.area())