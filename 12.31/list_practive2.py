# print("문제1")
# fruits = ["apple","banana", "cherry", "grape", "watermelon", "strawberry"]
# del fruits[1:4]
# print(fruits)

# print("문제2")
# letters = ["A","B"]
# letters_new = letters*3
# del letters_new[len(letters_new)//2-1]
# print(letters_new)

print("문제3")
train = []
train.extend(["철수","영희"])
train.extend(["민수","지훈"])
train.remove("영희")
train.insert(0,"수진")
train.remove("민수")
train.reverse()
print(train)

print("문제4")
num_list = [5,3,7]
num_list.extend([4,9])
print(max(num_list))
print(min(num_list))
print(sum(num_list))
sorted(num_list)
num_list.pop(-1)
print(num_list)