def split_into_halves(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    left, right = divide(arr)

    merge_sort(left)
    merge_sort(right)

    merge_halves(left, right, arr)


def merge_halves(a, b, temp):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        temp[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        temp[k] = b[j]
        j += 1
        k += 1


divide_and_conquer = merge_sort
divide = split_into_halves
conquer = merge_halves


if __name__ == '__main__':
    nums = [1, 9, 8, 3, 2, 1, 0, 7, 5]
    merge_sort(nums)
    print(nums)
