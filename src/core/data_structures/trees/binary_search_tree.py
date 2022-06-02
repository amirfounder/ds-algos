class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    @classmethod
    def from_sorted(cls, arr):
        pass

    def _serialize_helper(self, node, serialized):
        if node:
            serialized.append(node.value)
            self._serialize_helper(node.left, serialized)
            self._serialize_helper(node.right, serialized)
        else:
            serialized.append('#')

    def serialize(self):
        serialized = []
        self._serialize_helper(self.root, serialized)
        return ' '.join(serialized)

    def _deserialize_helper(self, values: iter):
        value = next(values)
        if not value:
            return None

        node = TreeNode(value)
        node.left = self._deserialize_helper(values)
        node.right = self._deserialize_helper(values)

        return node

    def deserialize(self, s: str):
        self.root = self._deserialize_helper(iter(s.split(' ')))


def main():
    pass


if __name__ == '__main__':
    main()
