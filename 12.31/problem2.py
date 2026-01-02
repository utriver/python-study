"""문제 설명
당신은 한 학생의 소비 로그를 분석하는 프로그램을 작성해야 한다.
입력은 문자열과 숫자가 섞여 들어오며,
잘못된 데이터는 조건문으로 걸러내고,
유효한 데이터만 리스트에 저장해 분석해야 한다.
입력 규칙
사용자 입력은 한 줄에 하나씩 주어진다.
입력 형식은 다음 중 하나이다.
금액 (예: 5000)
금액,메모 (예: 7000,점심)
입력이 "END"이면 입력 종료.
금액은 0 이상 정수만 유효하다.
금액이 음수이거나 숫자가 아니면 무효 데이터이다.
1단계: 입력 처리 (핵심 난이도)
END가 나올 때까지 반복해서 입력을 받는다.
입력이
숫자만 있으면 금액으로 처리
금액,메모 형태면 금액만 추출
무효 데이터는 저장하지 않는다.
유효한 금액만 리스트 logs에 저장한다.
2단계: 기본 분석
전체 유효 소비 내역을 출력하라.
전체 소비 횟수를 출력하라.
전체 소비 금액을 출력하라.
전체 평균 소비 금액을 출력하라.
3단계: 고급 조건 분석
평균보다 큰 소비 금액만 모아 리스트로 출력하라.
연속된 소비 증가 구간을 모두 찾아 출력하라.
(예: 3000 → 5000 → 7000)
4단계: 패턴 분석
소비 금액을 5000원 미만 / 이상으로 분류하여
두 개의 리스트로 나누어 출력하라.
가장 많이 등장한 소비 금액을 출력하라.
(동률이면 먼저 나온 값을 사용)
5단계: 데이터 변형
소비 내역을 오름차순 정렬한 리스트를 출력하라.
소비 내역을 내림차순 정렬한 리스트를 출력하라.
원본 소비 내역 리스트를 출력하라.
(정렬 후에도 원본은 변하지 않아야 한다)
6단계: 출력 형식
출력은 아래 형식을 정확히 따른다.
-입력-
3000
5000,점심
abc
-2000
7000,저녁
5000
3000
END
-출력-
유효 소비: [3000, 5000, 7000, 5000, 3000]
소비 횟수: 5
총 소비: 23000
평균 소비: 4600.0
평균 초과 소비: [5000, 7000, 5000]
연속 증가 구간: [[3000, 5000, 7000]]
5000 미만: [3000, 3000]
5000 이상: [5000, 7000, 5000]
최빈 소비 금액: 3000
오름차순: [3000, 3000, 5000, 5000, 7000]
내림차순: [7000, 5000, 5000, 3000, 3000]
원본: [3000, 5000, 7000, 5000, 3000]"""


#1단계
a=input("""입력 형식은 다음 중 하나이다.
금액 (예: 5000)
금액,메모 (예: 7000,점심)""").split(",")
logs = []
while a[0] != "END":
    if len(a) == 1 and a[0].isdigit():
        if int(a[0])>0:
            logs.append(int(a[0]))
    elif len(a) ==2 and a[0].isdigit():
        if int(a[0])>0:
            logs.append(int(a[0]))
    a=input("""입력 형식은 다음 중 하나이다.
금액 (예: 5000)
금액,메모 (예: 7000,점심)""").split(",")
#2단계
count = len(logs)
money = sum(logs)
average =money/count
#3단계
bigger = []
for i in logs:
    if average<i:
        bigger.append(i)
        
increase = []
increase_=[]
increase_num = 0
counta = 0
counta_ = 0
for i in logs:
    if counta ==0:
        increase_num = i
        counta +=1
    else:
        if increase_num<i and counta_ ==0:
            increase_.extend([increase_num,i])
            increase_num = i
            counta_+=1
        elif increase_num<i and counta_!=0:
            increase_.append(i)
            increase_num = i
            counta_+=1
        elif increase_num>i and len(increase_)>0:
            increase.append(list(increase_))
            increase_=[]
            counta_=0
            counta_ = 0
#4단계
under = []
upper = []
for i in logs:
    if i<5000:
        under.append(i)
    else:
        upper.append(i)
        
        
set1=set(logs)
count_ = 0
count_list = []
for i in set1:
    for j in logs:
        if i==j:
            count_+=1
    count_list.append(count_)
    count_ = 0
max_value = max(count_list)
max_index = count_list.index(max_value)
max_result = list(set1)[max_index]
            
#5단계
up=sorted(logs)     
down = sorted(logs,reverse=1)     
#6단계
print(f"""
유효 소비: {logs}
소비 횟수: {count}
총 소비: {money}
평균 소비: {average}
평균 초과 소비: {bigger}
연속 증가 구간: {increase}
5000 미만: {under}
5000 이상: {upper}
최빈 소비 금액: {max_result}
오름차순: {up}
내림차순: {down}
원본: {logs}
""")       

    