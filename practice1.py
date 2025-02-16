# 1.	Write a program for counting the number of every character of a given text file

with open("Coding questions.txt") as file:
    content = file.readlines()

content.remove('\n')
dct = {}
for line in content:
    for ch in line :
        if ch.isalpha():
            if ch not in dct:
                dct[ch] =1
            else:
                dct[ch] += 1

print(dct)

#chagpt approch

from collections import Counter

with open("Coding questions.txt", "r") as file:
    content = file.read()

# Filter only alphabetic characters and count them
char_count = Counter(ch for ch in content if ch.isalpha())

print(char_count)

num_count = Counter(num for num in content if num.isnumeric())
print(num_count)

#for line in content:
#    print(line)