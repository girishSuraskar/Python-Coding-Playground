# 21.	Write a program to Subtract Two Number Without Using Subtraction Operator
def sub_without_opt(num1,num2):

    while num2 != 0:
        num1 = num1^num2
        num2 = (num1 & num2) << 1
    return num1

print(sub_without_opt(9,1))
