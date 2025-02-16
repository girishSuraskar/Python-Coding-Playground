#3.	Write a program to check Armstrong number?

num = 153
sum = 0
str_num = str(num)

for i in str_num:
    sum += int(i) ** len(str_num)

print("it is armstrong") if sum == num else print("not an amrstrong num")