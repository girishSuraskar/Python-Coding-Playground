# 19.	Write a program to find a sum of digits of a number using recursion.
def sum_of_dig(num,sum):
    if num == 0 :
        return sum

    return sum_of_dig(num//10 , sum + num%10)


print(sum_of_dig(123,0))