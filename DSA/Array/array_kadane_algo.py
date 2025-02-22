"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
"""
arr = [2, 3, -8, 7, -1, 2, 3]
max_sum = 0
cs = 0
start = 0
end = 0
for i in range(len(arr)):
    cs += arr[i]
    if cs > max_sum :
        max_sum = cs
        end = i+1
    if cs <0:
        cs = 0
        start = i+1
print(max_sum)
print(arr[start:end])
