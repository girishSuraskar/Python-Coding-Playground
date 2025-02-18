# 23.	Write a program to Check whether the number is EVEN or ODD, without using any arithmetic or relational operators
def odd_even_binary(num):
     print(f"{num} is odd") if num & 1 else print(f"{num} is even")

print(odd_even_binary(23))