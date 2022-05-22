def bubble_sort(arr):
    n = len(arr)

    if n < 2:
        return arr

    for _ in arr:
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                swap(arr, i, i-1)

    return arr


def swap(arr, idx1, idx2):
    temp = arr[idx2]
    arr[idx2] = arr[idx1]
    arr[idx1] = temp


if __name__ == '__main__':
    nums = [1, 9, 8, 3, 2, 1, 0, 7]
    bubble_sort(nums)
    print(nums)
