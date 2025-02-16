# 11.	Write a program to print factorial of given number without using recursion?

def fact(n):
    result = 1
    for i in range(n, 0,-1):
        result *= i

    return result


print(fact(5))
