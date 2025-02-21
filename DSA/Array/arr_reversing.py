# Q1 : write a code to reverse the array

arr = [1,2,3,4,5]
n = len(arr)-1
rev_arr = []
# using list comprehension
rev = [arr[i] for i in range(n,-1,-1)]
# using normal for loop
for i in range(n,-1,-1):
    rev_arr.append(arr[i])

print(rev_arr)
print(rev)

# Reverseing original array
right = n
left = 0
for i in range(n):
    if left == right or left > right:
        break
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1

print(arr)
