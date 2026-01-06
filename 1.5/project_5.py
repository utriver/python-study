# def calculate(a,b,operator):
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a - b
#     elif operator == "*":
#         return a * b
#     elif operator == "/":
#         return a / b
#     else:
#         return "지원하지 않는 연산자입니다."
    
# a,b,operator = input("두 숫자와 연산자를 입력하세요 (예: 3 5 +): ").split(',')
# a = int(a)
# b = int(b)
# result = calculate(a,b,operator)
# print(result)

# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 5
#         print(f"inner 함수 내부: a = {a}")
#     inner()
#     print(f"outer 함수 내부: a = {a}")
    
    
# outer()

add = lambda x,y: x + y
result = add(3,5)
print(result)





