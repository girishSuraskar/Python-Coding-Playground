"""
Given an array arr, rotate the array by one position in clockwise direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
"""

arr = [1, 2, 3, 4, 5]
n = len(arr)

current = arr[0]
nextt = arr[1]
for i in range(n):
    nextt = arr[(i + 1) % n]
    arr[(i + 1) % n] = current
    current = nextt
print(arr)