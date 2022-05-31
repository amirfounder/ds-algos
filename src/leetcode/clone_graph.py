"""
Looks like when we are just cloning thing, it doesn't matter if we do DFS or BFS.
I prefer the DFS approach so that we can use the recursion stack.
We will start at our current node and for every neighbor, we will clone.
Given the values are unique, we can also carry a set of visited nodes.
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()

        for neighbor in node.neighbors:
            pass

    def cloneGraphHelper(self, node, visited):
        if node.val in visited:
            return node

        new = Node(node, [])

        for neighbor in node.neighbors:
            new.neighbors.append(self.cloneGraphHelper(neighbor, visited))

        return new