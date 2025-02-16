# 15.	Remove duplicates from an array?
arr = [2,2,3,4,5,6,8,8,9]
arr1 = list(filter(lambda x : arr.count(x) == 1 , arr))
print(arr1)