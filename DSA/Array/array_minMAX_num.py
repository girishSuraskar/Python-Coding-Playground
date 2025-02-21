"""Given an array of size N. The task is to find the
maximum and the minimum element of the array using the minimum number of comparisons. """
def min_max(arr):
    n  = len(arr)
    if n == 1:
        return arr[0], arr[0]
    if arr[0] > arr[1]:
        maxi = arr[0]
        mini = arr[1]
    else:
        maxi = arr[1]
        mini = arr[0]

    for i in range(2, n):
        if arr[i] > maxi:
            maxi = arr[i]
        elif arr[i] < mini:
            mini = arr[i]

    print("min:",mini,"max:", maxi)


def main():
    arr1 = [3, 5, 4, 1, 9]
    min_max(arr1)
    return


if __name__ == main():
    main()