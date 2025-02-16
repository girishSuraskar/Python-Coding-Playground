# 14.	Given a list and find even numbers in that list using lambda function
lst = [12,1,33,4,55,602,45]
evn_num = list(filter(lambda x : x%2 == 0,lst))
print(evn_num)