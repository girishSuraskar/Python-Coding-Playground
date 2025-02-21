""" Given an array arr[] and an integer k where k is smaller than the size of the array,
the task is to find the kth smallest element in the given array.
Follow up: Don't solve it using the inbuilt sort function."""


def kthSmallest( arr, k):
    temp = arr.copy()
    while k > 1:
        temp.remove(min(temp))
        k -= 1

    return min(temp)


def main():
    arr = [7, 10, 4, 3, 20, 15]
    print("3rd smallest number is : ",kthSmallest(arr,3))


if __name__ == "__main__":
    main()