#5.	Write a program of Fibonacci series using generators
def fibb(t):
    i = 0
    j = 1
    while t > 0:
        y = i
        yield y

        i ,j = j , i+j
        t -= 1

for i in fibb(10):
    print(i)