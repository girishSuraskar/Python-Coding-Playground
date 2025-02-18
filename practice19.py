# 22.	Write a program to Multiply an Integer Number by other number Without Using Multiplication Operator

def mul_withouth_using_opt(num1,num2):
    result = 0
    for _ in range(num2):
        result += num1
        num2 = num2 >> 1
    return result

print(mul_withouth_using_opt(3,3))