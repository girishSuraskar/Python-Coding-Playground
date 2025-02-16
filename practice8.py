# 9.	Write a program to check prime number?
def isprimenum(num):
    ul = int(pow(num ,0.5))+1
    for i in range(2, ul):
        if num % i == 0:
            return False

    return True

print(isprimenum(8))
