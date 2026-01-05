"""
도서관 대출 기록 분석 시스템
제한 조건 (절대 중요)
if / for / while 사용 금지
map, filter 사용 금지
입력 포함 전체 코드에서 반복문·조건문 사용 금지
반드시 사용할 자료구조
list, tuple, set, dict
입력 형식
대출 기록은 항상 10개 주어진다.
각 줄은 아래 형식이다.
회원ID,도서명,대출일,반납여부
예시
U001,파이썬입문,2025-03-01,반납
U001,자료구조,2025-03-03,미반납
U002,파이썬입문,2025-03-02,반납
U003,알고리즘,2025-03-01,반납
U003,자료구조,2025-03-04,미반납
U002,알고리즘,2025-03-05,반납
U004,데이터베이스,2025-03-01,미반납
U001,알고리즘,2025-03-06,반납
U004,파이썬입문,2025-03-02,반납
U005,운영체제,2025-03-07,미반납
입력은 input()을 정확히 10번 직접 호출하여 받는다.
데이터 규칙
모든 항목은 문자열
반납여부는 "반납" 또는 "미반납"
입력 형식은 항상 올바르다고 가정한다
(검증 로직 없음)
1단계: 데이터 저장
각 입력을 튜플로 변환
(회원ID, 도서명, 대출일, 반납여부)
모든 기록을 리스트에 저장
전체 회원 ID를 set으로 저장
회원별 대출 기록을 dict로 구성
2단계: 전체 통계
전체 대출 기록 수v
전체 회원 수 v
전체 도서 종류 수 v
반납 기록 수 v
미반납 기록 수 v
3단계: 회원별 분석
회원별로 다음 정보 출력
대출 횟수 
반납 횟수
미반납 횟수
대출 도서 목록 (중복 제거)
4단계: 도서별 분석
도서별 대출 횟수
최다 대출 도서
1회 대출 도서 목록
5단계: 데이터 변형
반납 기록 리스트
미반납 기록 리스트
대출일 기준 정렬된 기록 리스트
원본 기록 리스트 유지
:보낼_편지함_트레이: 출력 요구
출력 구조는 예시와 동일
자료형 유지 필수 (list, set, dict, tuple)
입력
U001,파이썬입문,2025-03-01,반납
U001,자료구조,2025-03-03,미반납
U002,파이썬입문,2025-03-02,반납
U003,알고리즘,2025-03-01,반납
U003,자료구조,2025-03-04,미반납
U002,알고리즘,2025-03-05,반납
U004,데이터베이스,2025-03-01,미반납
U001,알고리즘,2025-03-06,반납
U004,파이썬입문,2025-03-02,반납
U005,운영체제,2025-03-07,미반납
출력
전체 대출 기록 수: 10
전체 회원 수: 5
전체 도서 수: 6
반납 기록 수: 6
미반납 기록 수: 4
[U001]
대출 횟수: 3
반납: 2
미반납: 1
도서 목록: {'파이썬입문', '자료구조', '알고리즘'}
[U002]
대출 횟수: 2
반납: 2
미반납: 0
도서 목록: {'파이썬입문', '알고리즘'}
[U003]
대출 횟수: 2
반납: 1
미반납: 1
도서 목록: {'알고리즘', '자료구조'}
[U004]
대출 횟수: 2
반납: 1
미반납: 1
도서 목록: {'데이터베이스', '파이썬입문'}
[U005]
대출 횟수: 1
반납: 0
미반납: 1
도서 목록: {'운영체제'}
도서별 대출 횟수: {'파이썬입문': 3, '자료구조': 2, '알고리즘': 3, '데이터베이스': 1, '운영체제': 1}
최다 대출 도서: 파이썬입문
1회 대출 도서: ['데이터베이스', '운영체제']
반납 기록: [('U001', '파이썬입문', '2025-03-01', '반납'),
('U002', '파이썬입문', '2025-03-02', '반납'),
('U003', '알고리즘', '2025-03-01', '반납'),
('U002', '알고리즘', '2025-03-05', '반납'),
('U001', '알고리즘', '2025-03-06', '반납'),
('U004', '파이썬입문', '2025-03-02', '반납')]
미반납 기록: [('U001', '자료구조', '2025-03-03', '미반납'),
('U003', '자료구조', '2025-03-04', '미반납'),
('U004', '데이터베이스', '2025-03-01', '미반납'),
('U005', '운영체제', '2025-03-07', '미반납')]
정렬된 기록: [('U001', '파이썬입문', '2025-03-01', '반납'),
('U003', '알고리즘', '2025-03-01', '반납'),
('U004', '데이터베이스', '2025-03-01', '미반납'),
('U002', '파이썬입문', '2025-03-02', '반납'),
('U004', '파이썬입문', '2025-03-02', '반납'),
('U001', '자료구조', '2025-03-03', '미반납'),
('U003', '자료구조', '2025-03-04', '미반납'),
('U002', '알고리즘', '2025-03-05', '반납'),
('U001', '알고리즘', '2025-03-06', '반납')
('U005', '운영체제', '2025-03-07', '미반납')]
원본 기록: [('U001', '파이썬입문', '2025-03-01', '반납'),
('U001', '자료구조', '2025-03-03', '미반납'),
('U002', '파이썬입문', '2025-03-02', '반납'),
('U003', '알고리즘', '2025-03-01', '반납'),
('U003', '자료구조', '2025-03-04', '미반납'),
('U002', '알고리즘', '2025-03-05', '반납'),
('U004', '데이터베이스', '2025-03-01', '미반납'),
('U001', '알고리즘', '2025-03-06', '반납'),
('U004', '파이썬입문', '2025-03-02', '반납'),
('U005', '운영체제', '2025-03-07', '미반납')]
"""
import itertools

#1단계
a=input().split(',')
b=input().split(',')
c=input().split(',')
d=input().split(',')
e=input().split(',')
f=input().split(',')
g=input().split(',')
h=input().split(',')
i=input().split(',')
j=input().split(',')

a=tuple(a)
b=tuple(b)
c=tuple(c)
d=tuple(d)
e=tuple(e)
f=tuple(f)
g=tuple(g)
h=tuple(h)
i=tuple(i)
j=tuple(j)
data = []
data.extend([a,b,c,d,e,f,g,h,i,j])
ID= set([a[0],b[0],c[0],d[0],e[0], f[0],g[0],h[0],i[0],j[0]])
return_ = set([a[3],b[3],c[3],d[3],e[3], f[3],g[3],h[3],i[3],j[3]])
ID_list = sorted(list(ID))
return_list = list(return_)
info ={a[0]:[],b[0]:[],c[0]:[],d[0]:[],e[0]:[], f[0]:[],g[0]:[],h[0]:[],i[0]:[],j[0]:[]}
info[a[0]].append(list(a[1:]))
info[b[0]].append(list(b[1:]))
info[c[0]].append(list(c[1:]))
info[d[0]].append(list(d[1:]))
info[e[0]].append(list(e[1:]))
info[f[0]].append(list(f[1:]))
info[g[0]].append(list(g[1:]))
info[h[0]].append(list(h[1:]))
info[i[0]].append(list(i[1:]))
info[j[0]].append(list(j[1:]))
return_info = {return_list[0]:[],return_list[1]:[]}
return_info[a[3]].append(list(a[:3]))
return_info[b[3]].append(list(b[:3]))
return_info[c[3]].append(list(c[:3]))
return_info[d[3]].append(list(d[:3]))
return_info[e[3]].append(list(e[:3]))
return_info[f[3]].append(list(f[:3]))
return_info[g[3]].append(list(g[:3]))
return_info[h[3]].append(list(h[:3]))
return_info[i[3]].append(list(i[:3]))
return_info[j[3]].append(list(j[:3]))


print(info)
print(ID_list)

#2단계
record_num = len(data)
member = len(ID_list)
book = len(set([a[1],b[1],c[1],d[1],e[1], f[1],g[1],h[1],i[1],j[1]]))
return_book = len(return_info.get("반납"))
notreturn_book = len(return_info.get("미반납"))

#3단계 
loan1=len(info[ID_list[0]])
return1_list = info.get(ID_list[0])
all_list1 = list(itertools.chain.from_iterable(return1_list))
return1 = all_list1.count("반납")
notreturn1 = all_list1.count("미반납")
book_list1 = set(list(itertools.chain.from_iterable(return1_list))[::3])

loan2=len(info[ID_list[1]])
return2_list = info.get(ID_list[1])
all_list2 = list(itertools.chain.from_iterable(return2_list))
return2 = all_list2.count("반납")
notreturn2 = all_list2.count("미반납")
book_list2 = set(list(itertools.chain.from_iterable(return2_list))[::3])

loan3=len(info[ID_list[2]])
return3_list = info.get(ID_list[2])
all_list3 = list(itertools.chain.from_iterable(return3_list))
return3 = all_list3.count("반납")
notreturn3 = all_list3.count("미반납")
book_list3 = set(list(itertools.chain.from_iterable(return3_list))[::3])

loan4=len(info[ID_list[3]])
return4_list = info.get(ID_list[3])
all_list4 = list(itertools.chain.from_iterable(return4_list))
return4 = all_list4.count("반납")
notreturn4 = all_list4.count("미반납")
book_list4 = set(list(itertools.chain.from_iterable(return4_list))[::3])

loan5=len(info[ID_list[4]])
return5_list = info.get(ID_list[4])
all_list5 = list(itertools.chain.from_iterable(return5_list))
return5 = all_list5.count("반납")
notreturn5 = all_list5.count("미반납")
book_list5 = set(list(itertools.chain.from_iterable(return5_list))[::3])

# 4단계
book_library = [a[1],b[1],c[1],d[1],e[1], f[1],g[1],h[1],i[1],j[1]]
