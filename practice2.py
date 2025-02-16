# 2.	Write a program to print n prime number?
def isprimenum(num):
    flag = True
    for i in range(2,num):
        if num % i == 0 :
            flag = False
            break
    return flag

def gen(n):
    y = 3
    while n > 0:
        if isprimenum(y):
            yield y

        n -= 1
        y += 1

for i in gen(10):
    print(i)