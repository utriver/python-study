print("문제1")
nums = [10,20,30,40,50]
print(f"첫번쩨 요소: {nums[0]}\n두번째 요소: {nums[-1]}")

print("문제2")
nums = [100,200,300,400,500,600,700]
middle = len(nums)//2
print(f"가운데 요소 3개: {nums[middle-1:middle+2]}")

print("문제3")
nums = [1,2,3,4,5]
print(f"원소 두배하기: {[i*2 for i in nums]}")

print("문제 4")
items = ["a","b","c","d","e"]
print(f"리스트 역순으로 슬라이싱:{items[::-1]}")

print("문제5")
data = ["zero", "one", "two", "three", "four", "five"]
print(data[1::2])

print("문제6")
movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print(movies)

print("문제7")
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
new = []
for i in subjects:
    if i=="물리" or i=="생물"or i=="지구과학":
        new.append(i)
print(new)

print("문제8")
data = ["A","B","C","D","E","F","G","H","I"]
print(data[2::-1], data[5:2:-1], data[8:5:-1])