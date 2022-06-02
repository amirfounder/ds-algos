from enum import Enum


class Colors(Enum):
    Black = 0
    Red = 1


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.color = Colors.Black


class RedBlackTree:
    def __init__(self):
        pass
