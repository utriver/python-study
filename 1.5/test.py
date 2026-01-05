# for i in range(2,31):
#     for j in range(1,31):
#         print(f"{i}x{j}={i*j}")

#3차원 리스트
# nums = [[[1,2]],[[3,4]],[[5,6]]]
# for row in nums:
#     for n in row:
#         for i in n:
#             print(i)

# for i in range(10):
#     if i==5:
#         break
#     print(i)
    
# for i in range(5):
#     if i==2:
#         continue
#     print(i)

#for문이 다 돌고 나서 else가 수행 break가 있는지 여부 판단

# for i in range(5):
#     print(i)
# else:
#     print("루프 정상종료")
    
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("루프 정상 종료")

nums = [x**2 for x in range(1,6)]
print(nums)


evens = [x for x in range(1,11) if x%2 == 0]
print(evens)

unique = {len(word) for word in {"apple","sdfsadf","adfadsfadsf"}}
print(unique)