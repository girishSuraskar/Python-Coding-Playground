# 10.	Write a program to check palindrome number?
def check_palindrome(num):
    cnv = str(num)
    h_ln = len(cnv)//2
    if cnv[:h_ln] == cnv[:-h_ln-1:-1]:
        return True
    else:
        return False


print(check_palindrome('nitin'))