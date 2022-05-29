from typing import List

def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1


if __name__ == '__main__':
    arr = [1, 3, -3, 8, 5, 7]
    target = 5
    res = subarray_sum(arr, target)
    print(' '.join(map(str, res)))
