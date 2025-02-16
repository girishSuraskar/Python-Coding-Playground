# 20.	Write a program to Add Two Numbers Without Using the Addition Operator

def add_without_opt(a,b):
    while b != 0:
        carry = (a & b) << 1
        a = a^b
        b = carry
    return a

print(add_without_opt(4,5))