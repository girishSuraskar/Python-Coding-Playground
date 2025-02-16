#4.	Write a program to print factorial of given number without using recursion?

def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    print(result)

fact(5)


