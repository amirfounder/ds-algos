def split_into_halves(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]


def merge_sort(arr):
    # divide
    n = len(arr)
    if n <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # conquer
    len_a = len(left)
    len_b = len(right)
    i = j = k = 0

    while i < len_a and j < len_b:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    nums = [1, 9, 8, 3, 2, 1, 0, 7, 5]
    merge_sort(nums)
    print(nums)
