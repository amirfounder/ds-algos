"""
Algorithmic approach.
First thing I'm seeing is nearest and distance. I am already thinking of BFS for each cell.
I don't want to think too much about time complexity at this moment before the solution,
but minimum for brute force is O(m*n).
Is there a faster one? Not sure yet.

Inputs:
We can assume that m and n are at least 1 and less than 1000.
The lower bound is good, so we don't need to do `if n == 0` checks.
The upper bound is good too, if we were dealing with limited memory.
Larger matrices would expand that memory usage significantly.
Additionally, if we need to, can we modify the inputs?

Data structure:
We can either keep this as a matrix, or introduce a graph.
This problem doesn't seem like it needs a graph just yet, so we'll keep that in our back pocket for now.

The approach.

First thing's first, let's run the brute force approach without complicating it with any caching.

I'll loop over each row and for each row, i'll loop over each cell.
For each cell:
    If the number is 0: return 0
    Else run a DFS on the number while keeping track of the level depth.
    Once a node with 0 has been reached, return the level depth.
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pass
