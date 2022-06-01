"""
When it comes to serializing and deserializing, we are probably going to want to either do one of the following:
inorder, preorder, postorder.

Question is... which one should we choose?

if we were to serialize in order:

- serialized = []
- serialized.append(node.value) for each value recursively.
    - recursive call
    - serialize
    - recursive call
    we break when the value is null (add None to the result and return)


deserializing would go as follows:

- serialized = '1 2 3 None 4 None None 5' or something like that.
- serialized = serialized.split(' ')
The problem with inorder traversal, it is not apparent what the head node is.

deserializing preorder:

- node = Node(serialized.pop(0))
- if node.value == 'None':
    - return
- pass prev node to the function to assign
- build this back up using DFS
- call deserialize(serialized)
- call deserialize(serialized)
this is a little tough. let's go with postorder

deserializing postorder:

node = Node(serialized.pop(0))
node.left = Node(serialized.pop(0))
node.right = Node(serialized.pop(0))

Deserializing a node will require the parent node, and it's left and right children to be accessible.

Example (In order):

1, 2, None, None, 3, 4, None, None, 5, None, None

Leaf nodes are nodes followed by 2 Nones.


def deserialize(serialized: list[str]):
    value = serialized.pop(0)

    if value == "None":
        return

    node = Node(int(value))
    node.left = deserialize(serialized)
    node.right = deserialize(serialized)

    return node


def serialize(root: Node):



def main():
    serialized = input.split(', ')

    head = Node(int(serialized.pop(0)))
    head.left = deserialize(serialized)
    head.right = deserialize(serialized)

    return head


We also want to factor in some NULL value cases. those can be represented as the string None.

Good answer:
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        serialized = self.serialize_helper(root)
        return ', '.join([str(s) for s in serialized])

    def serialize_helper(self, root):
        serialized = []

        if not root:
            return [None]

        serialized.extend(self.serialize_helper(root.left))
        serialized.append(root.val)
        serialized.extend(self.serialize_helper(root.right))

        return serialized

    def deserialize(self, data):
        serialized = data.split(', ')
        return self.deserialize_helper(serialized)

    def deserialize_helper(self, data):
        value = data.pop(0)

        if value == "None":
            return

        node = TreeNode(int(value))
        node.left = self.deserialize(serialized)
        node.right = self.deserialize(serialized)

        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))