#7.	Write a program to print Fibonacci series  using recursion?
def fibb(t1,t2,term):
    if term == 0:
        return
    print(t1,end=" ")
    return fibb(t2,t1+t2,term-1)

fibb(0,1,10)