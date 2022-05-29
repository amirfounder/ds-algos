def boundary_search_boundary(arr):
    p1 = 0
    p2 = len(arr) - 1
    boundary_index = -1

    while p1 <= p2:
        mid = (p1 + p2) // 2
        if arr[mid]:
            boundary_index = mid
            p2 = mid - 1
        else:
            p1 = mid + 1

    return boundary_index


if __name__ == '__main__':
    res = boundary_search_boundary([x == '1' for x in list('000000000111111')])
    print(res)
