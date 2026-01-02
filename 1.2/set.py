submissions = ["kim","lee","kim","park","choi","lee","lee"]
sub_set = set(submissions)
print(f"""제출한 학생수:{len(sub_set)}
제출자 명단: {sub_set}""")

user1 = {'SF','Action','Drama'}
user2 = {'Drama','Romance','Action'}
all = user1|user2
common =  user1&user2
dif = all-common
print(f"""공통 관심 장르: {common}
서로 다른 장르:{dif}
전체 장르: {all}""")

my_certificates = {'SQL','Python','Linux'}
job_required = {'SQL','Python'}
print(f"지원자격충족여부:{job_required.issubset(my_certificates)}")
