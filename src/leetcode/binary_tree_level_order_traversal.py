"""
Right off the bat, we know we are running a BFS.
This means instead of running a stack, we are running a queue.

         1
       2   3
      3 5 6 8

[[1], [2, 3], [3,5,6,8]]

Assumptions:
Root node will always have its own level.

First thing's first:
Create result array equal to an array of a single array containing the root nodes value.
Create a next level array to append children nodes to.

result = prev_level = [[node]]

while len(prev_level) > 0:
    curr_level_vals = next_level = []
    for node in prev_level:
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
        curr_level_vals.append(node.val)
    result.append(curr_level)
    prev_level = next_level

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
