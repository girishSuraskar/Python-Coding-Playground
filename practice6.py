# 6.	Program to find n’th Fibonacci number
def sim_fibb(n):
    i,j = 0,1
    while n > 1:
        i,j = j,i+j
        n -=1
    return i

print(sim_fibb(10))