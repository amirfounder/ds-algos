"""
First thing I'm thinking about is that this is sorted.
This means that should we need to traverse the list of intervals, we can use a binary search algorithm.

Once we find the position to insert the newInterval in, we need to check 2 intervals to see if we need to merge:

1.
the end value of the interval less than the new interval.
COMPARE this to the start value of the new interval.

2.
the start value of the interval after our last interval.
COMPARE this to the end value of the new interval.

For example:

inputs:
[
    [1, 2],
    [3, 3.5],
    [5, 8],
    [8, 11.5], <== inserting this one
    [9, 10],
    [11, 12]
]

output:
[
    [1, 2],
    [3, 3.5],
    [5, 8],
    [8, 12]
]

Questions I have:

Is [1,2], and [2,3] overlapping and should they be merged? Assuming yes.

"""
from typing import List


# my solution
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        pass

# other solutions:
# https://leetcode.com/problems/insert-interval/discuss/?currentPage=1&orderBy=most_votes&query=

