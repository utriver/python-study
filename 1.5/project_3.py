numbers = [3,6,1,8,4]
double_list = []
for i in numbers:
    double_list.append(i*2)
print("문제1")
print(double_list)

words = ["apple","banana", "kiwi", "grape"]
new_list =[]
for w in words:
    new_list.append(len(w))
print("문제2")
print(new_list)

coordinates = [(1,2),(3,4),(5,6),(7,8)]
x_values = []
y_values = []
for x,y in coordinates:
    x_values.append(x)
    y_values.append(y)
print("문제3")
print(x_values,y_values)