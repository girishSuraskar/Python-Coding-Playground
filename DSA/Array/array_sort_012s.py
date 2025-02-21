"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
"""

def sort012(arr):
    start,mid,end = 0,0,len(arr)-1
    while mid <= end:
        if arr[mid] == 0:
            arr[mid],arr[start] = arr[start],arr[mid]
            mid += 1
            start += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid],arr[end]=arr[end],arr[mid]
            end -= 1

    return arr

arr = [0, 1, 2, 0, 1, 2]
arr = sort012(arr)
print(arr)