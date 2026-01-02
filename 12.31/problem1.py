"""*문제 설명*
한 학생의 소비 기록을 관리하는 프로그램을 작성하시오.
프로그램은 사용자 입력을 기반으로 리스트를 생성하고,
리스트 조작 메서드를 활용해 데이터를 추가, 삽입, 삭제, 분석해야 한다.
조건문(if), 반복문(for/while) 사용 금지
함수 정의 금지
1단계: 초기 데이터 입력
사용자로부터 10개의 정수를 입력받아 리스트 data에 저장하라.
(1일차 ~ 10일차 소비 금액)
2단계: 리스트 수정
마지막에 5000원을 추가하라.
리스트의 맨 앞에 3000원을 삽입하라.
값이 0인 요소를 삭제하라.
(0은 정확히 한 번만 존재함)
3단계: 부분 분석
처음 5일 소비 내역을 슬라이싱으로 출력하라.
마지막 5일 소비 내역을 슬라이싱으로 출력하라.
4단계: 계산
전체 소비 금액을 출력하라.
전체 평균 소비 금액을 출력하라.
처음 5일 평균 소비 금액을 출력하라.
마지막 5일 평균 소비 금액을 출력하라.
5단계: 리스트 복사 및 추가 수정
data를 슬라이싱으로 복사하여 data_copy를 만들어라.
data_copy에서 첫 번째 요소를 삭제하라.
data_copy에서 마지막 요소를 삭제하라.
수정된 data_copy를 출력하라.
원본 data를 출력하라.
6단계: 출력 형식
아래 출력 형식과 완전히 동일하게 출력하시오.
-입력-
1000
2000
0
3000
4000
5000
6000
7000
8000
9000
-출력-
처음 5일: [3000, 1000, 2000, 3000, 4000]
마지막 5일: [6000, 7000, 8000, 9000, 5000]
총 소비: 48000
전체 평균: 4800.0
처음 5일 평균: 2600.0
마지막 5일 평균: 7000.0
수정된 리스트: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
원본 리스트: [3000, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 5000]
"""

#1단계
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
data = [a,b,c,d,e,f,g,h,i,j]
#2단계
data.append(5000)
data.insert(0,3000)
data.remove(0)
#3단계
first_5day = data[:5]
last_5day = data[-1:-6:-1]
#4단계
all_spend = sum(data)
average = all_spend/len(data)
average_first_5day=sum(first_5day)/len(first_5day)
average_last_5day = sum(last_5day)/len(last_5day)
#5단계
data_copy = data[::]
data_copy.pop(0)
data_copy.pop(-1)
print(f"""-입력-
{a}
{b}
{c}
{d}
{e}
{f}
{g}
{h}
{i}
{j}
-출력-
처음 5일: {first_5day}
마지막 5일: {last_5day}
총 소비: {all_spend}
전체 평균: {average}
처음 5일 평균: {average_first_5day}
마지막 5일 평균: {average_last_5day}
수정된 리스트: {data_copy}
원본 리스트: {data}
""")

