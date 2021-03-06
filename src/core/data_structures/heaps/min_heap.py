class MinHeap:

    @property
    def size(self):
        return len(self._items)

    @property
    def is_empty(self):
        return self.size == 0

    def __init__(self, items=None):
        self._items = items or []

        parent_idx = self._parent_index_of(self.size - 1)

        for idx in reversed(range(parent_idx + 1)):
            self._sift_down(idx)

    def peek(self):
        if self._items:
            return self._items[0]

    def pop(self):
        if self.is_empty:
            return

        self._swap(0, self.size - 1)
        item = self._items.pop()

        if not self.is_empty:
            self._sift_down(0)

        return item

    def insert(self, item):
        self._items.append(item)
        self._sift_up(self.size - 1)

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _sift_down(self, index):
        while self._has_left_child(index):
            smaller_index = self._left_child_index_of(index)
            if self._has_right_child(index) and \
                    self._items[self._right_child_index_of(index)] < self._items[smaller_index]:
                smaller_index = self._right_child_index_of(index)

            if self._items[index] < self._items[smaller_index]:
                return

            self._swap(index, smaller_index)
            index = smaller_index

    def _sift_up(self, index):
        while self._has_parent(index) and self._items[self._parent_index_of(index)] > self._items[index]:
            self._swap(index, self._parent_index_of(index))
            index = self._parent_index_of(index)

    @staticmethod
    def _has_parent(index):
        return index > 0

    def _has_left_child(self, index):
        return self._left_child_index_of(index) < self.size

    def _has_right_child(self, index):
        return self._right_child_index_of(index) < self.size

    @staticmethod
    def _parent_index_of(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child_index_of(index):
        return (index * 2) + 1

    @staticmethod
    def _right_child_index_of(index):
        return (index * 2) + 2


def main():
    items = [int(item) for item in list('546123478965134564321465546')]
    heap = MinHeap(items=items)
    ordered = []
    while not heap.is_empty:
        ordered.append(heap.pop())
    print(ordered)


if __name__ == '__main__':
    main()
