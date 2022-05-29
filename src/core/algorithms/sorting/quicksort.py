def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()

    lower = []
    greater = []

    for element in arr:
        if element > pivot:
            greater.append(element)
        else:
            lower.append(element)

    return sort(lower) + [pivot] + sort(greater)


if __name__ == '__main__':
    nums = list('459842658953658652')
    nums = [int(n) for n in nums]
    print(sort(nums))
