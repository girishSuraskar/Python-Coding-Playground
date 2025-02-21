"""
Given an array containing both positive and negative numbers in random order.
The task is to rearrange the array elements so that all negative numbers appear before all positive numbers.

Note:

Given array does not contain any zeroes.
Order of resultant array does not matter.
Example :

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
start = 0
mid = 0
end = len(arr)-1
while mid <= end:
    if arr[mid] < 0:
        arr[start],arr[mid] = arr[mid],arr[start]
        start += 1
        mid += 1
    elif arr[mid] > 0:
        arr[end],arr[mid] = arr[mid] , arr[end]
        end -= 1

print(arr)
