"""
Are these ordered? Are there any decimals?
The solution cannot have duplicates, but does the input array have duplicates?

Brute force approach, is loop over each item and loop again and again. O(n**3)
But we can do this smarter. We can first order the array, loop over every item, and for every item, we run 2 pointer.

Order the array.
For every item in the array:
we then add that to a set of possible nums.
subtract the sum from the target and pass that into a function along with the array except for the current item
From there on out, we can run the 2 sum approach for the array to find the target sum. we should also make sure that
there are no duplicates in the input array.

Complexity:

O(n log n)
sort

O(n**2)
3 sum approach:

    O(n)
    First iteration

    O(n):
    2 sum 
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
