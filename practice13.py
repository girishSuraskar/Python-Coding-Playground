# 17.	Write a program to check if it is a palindrome number or not using a recursive method.
def ispalindrome(si,ei,num):
    if si >= ei :
        return True
    if num[si] != num[ei]:
        return False
    return ispalindrome(si+1,ei-1,num)

num = str('nitin')
num1 = str(123)
print(ispalindrome(0,len(num)-1,num))
print(ispalindrome(0,len(num1)-1,num1))
