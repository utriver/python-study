"""학습 관리 + 투두 + 데이터 분석 시스템
기본 데이터 (수정 :x:)
students = [
    {"name": "김철수", "grade": 1, "scores": [85, 90, 88]},
    {"name": "이영희", "grade": 2, "scores": [70, 75, 72]},
    {"name": "박민수", "grade": 1, "scores": [95, 92, 93]},
    {"name": "최지은", "grade": 3, "scores": [60, 65, 58]},
    {"name": "정다은", "grade": 2, "scores": [88, 84, 90]},
    {"name": "한유진", "grade": 3, "scores": [100, 100, 100]}
]
- 학생 성적 분석 파트 -
(1) 평균 계산
def get_average(scores):
소수점 둘째 자리 반올림
(2) 등급 계산
def get_grade(avg):
(등급표)
평균	등급
90+	A
80+	B
70+	C
60+	D
else	F
(3) 전체 학생 출력
출력 예:
김철수 | 1학년 | 평균: 87.67 | 등급: B
- 데이터 필터링 & 정렬 -
(4) 학년별 학생 조회
def print_by_grade(students, grade):
결과 없으면 메시지 출력
(5) 성적 우수자 출력
def print_top_students(students):
평균 90 이상
- 투두 리스트 시스템 -
todos = []
# ["공부하기", 중요도, 완료여부]
(7) 투두 추가
def add_todo(todos):
할 일:
중요도(1~5):
(8) 완료 처리
def complete_todo(todos):
번호 출력
선택한 항목 완료 처리
(9) 투두 출력
def print_todos(todos):
상태는 삼항 연산자 사용
(10) 중요도 필터
def print_important_todos(todos, level):
- 통계 & 요약 -
(11) 투두 통계
def print_todo_stats(todos):
출력:
총 투두: 5
완료: 2
미완료: 3
완료율: 40.0%
- 메뉴 시스템 -
1. 학생 전체 출력
2. 학년별 학생 조회
3. 성적 우수자 출력
4. 평균 기준 정렬
5. 투두 추가
6. 투두 완료
7. 투두 전체 출력
8. 중요도 높은 투두
9. 투두 통계
0. 종료
"""




def get_average(scores):
    return round(sum(scores) / len(scores), 2)

def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
def print_by_grade(students, grade):
    search = []
    if grade == 1 :
        for student in students:
            if student["grade"] == 1:
                search.append(student["name"])
    elif grade == 2 :
        for student in students:
            if student["grade"] == 2:
                search.append(student["name"])    
    elif grade == 3:
        for student in students:
            if student["grade"] == 3:
                search.append(student["name"]) 
    else:
        print("원하는 학년의 학생 조회가 불가능합니다.")   
    print(f"{grade}학년에는 {search}학생이 있습니다") 

def print_top_students(students):
    top_student = []
    for student in students:
        avg = get_average(student["scores"])
        if avg >= 90:
            top_student.append(student["name"])
    return top_student


def add_todo():
    global todos
    todo_list = input("할일, 중요도를 작성해주세요: ").split(',')
    while (todo_list[0] != ''):
        todos.append({"할일": todo_list[0], "중요도": int(todo_list[1]), "완료여부": False})
        todo_list = input("할일, 중요도를 작성해주세요: ").split(',')

def complete_todo():
    global todos
    print(f"미완료 번호 리스트: {[index+1 for index in range(len(todos))]}")
    complete = input("완료한 항목 번호를 입력해주세요: ")
    while complete != "":
        todos[int(complete)-1]["완료여부"] = True
        complete = input("완료한 항목 번호를 입력해주세요: ")


def print_todos(todos):
    for index, todo in enumerate(todos):
        status = "완료" if todo["완료여부"] else "미완료"
        print(f"{index+1}. {todo['할일']} | 중요도: {todo['중요도']} | 완료여부: {status}")
        
def print_important_todos(todos, level):
    important = []
    for todo in todos:
        if todo["중요도"]>=level:
            important.append(todo["할일"])
    return important

def print_todo_stats(todos):
    all_todo = len(todos)
    complete_todo = 0
    uncomplete_todo = 0
    for todo in todos:
        if todo["완료여부"]:
            complete_todo +=1
        else:
            uncomplete_todo+=1
    percent = complete_todo/(uncomplete_todo+complete_todo)
    print(f"""총 투두: {all_todo}
완료: {complete_todo}
미완료: {uncomplete_todo}
완료율: {percent*100}%""")
    

if __name__ == "__main__":
    students = [
        {"name": "김철수", "grade": 1, "scores": [85, 90, 88]},
        {"name": "이영희", "grade": 2, "scores": [70, 75, 72]},
        {"name": "박민수", "grade": 1, "scores": [95, 92, 93]},
        {"name": "최지은", "grade": 3, "scores": [60, 65, 58]},
        {"name": "정다은", "grade": 2, "scores": [88, 84, 90]},
        {"name": "한유진", "grade": 3, "scores": [100, 100, 100]}
    ]
    todos = []

    #학생별 점수
    cheolsu_scores = students[0]['scores']
    yeonghee_scores = students[1]['scores']
    minsu_scores = students[2]['scores']
    jieun_scores = students[3]['scores']
    daeun_scores = students[4]['scores']
    yujin_scores = students[5]['scores']
    #학생별 평균계산
    cheolsu_avg = get_average(cheolsu_scores)
    yeonghee_avg = get_average(yeonghee_scores)
    minsu_avg = get_average(minsu_scores)
    jieun_avg = get_average(jieun_scores)
    daeun_avg = get_average(daeun_scores)
    yujin_avg = get_average(yujin_scores)
    #학생별 등급계산
    cheoulsu_grade = get_grade(cheolsu_avg)
    yeonghee_grade = get_grade(yeonghee_avg)
    minsu_grade = get_grade(minsu_avg)
    jieun_grade = get_grade(jieun_avg)
    daeun_grade = get_grade(daeun_avg)
    yujin_grade = get_grade(yujin_avg)





    #전체 학생 출력
    all_students = [{"name":students[0]["name"], "grade":students[0]["grade"], "average":cheolsu_avg, "grade_level":cheoulsu_grade},
                    {"name":students[1]["name"], "grade":students[1]["grade"],  "average":yeonghee_avg, "grade_level":yeonghee_grade},
                    {"name":students[2]["name"], "grade":students[2]["grade"], "average":minsu_avg, "grade_level":minsu_grade},
                    {"name":students[3]["name"], "grade":students[3]["grade"], "average":jieun_avg, "grade_level":jieun_grade},
                    {"name":students[4]["name"], "grade":students[4]["grade"], "average":daeun_avg, "grade_level":daeun_grade},
                    {"name":students[5]["name"], "grade":students[5]["grade"], "average":yujin_avg, "grade_level":yujin_grade}]
    print("전체 학생 정보")

    for student in all_students:
        print(f"{student['name']} | {student['grade']}학년 | 평균: {student['average']} | 등급: {student['grade_level']}")


    grade = int(input("조회할 학년을 입력해주세요: "))

    print_by_grade(students,grade)

    top_student = print_top_students(students)
    print(f"성적 우수자: {top_student}")
    add_todo()
    complete_todo()
    print_todos(todos)
    print(f"중요도 높은 투두: {print_important_todos(todos,4)}")
    print_todo_stats(todos)
