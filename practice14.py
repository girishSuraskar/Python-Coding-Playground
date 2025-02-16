# 18.	Write a program to check the given number format is in binary or not.
def isbinary(num):
    s1 = set(num)
    if len(s1)==2 and s1.intersection({'1','0'}):
        return  True
    else :
        return False

print(isbinary('23'))
