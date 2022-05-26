class MinHeap:
    def __init__(self, items=None):
        self._items = items or []

    def peek(self):
        if self._items:
            return self._items[0]

    def pop(self):
        if self._items:
            item = self._items.pop(0)
            self._swap(0, len(self._items) - 1)
            self._sift_down(0)
            return item

    def insert(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _sift_down(self, index):
        if index >= len(self._items):
            return

        while self._has_left_child(index):
            smallest_index = self._left_child_index_of(index)
            if self._has_right_child(index) and \
                    self._items[self._right_child_index_of(index)] < self._items[smallest_index]:
                smallest_index = self._right_child_index_of(index)

            if self._items[index] < self._items[smallest_index]:
                return

            self._swap(index, smallest_index)
            index = smallest_index

    def _sift_up(self, index):
        while self._has_parent(index) and self._items[self._parent_index_of(index)] > self._items[index]:
            self._swap(index, self._parent_index_of(index))
            index = self._parent_index_of(index)

    @staticmethod
    def _has_parent(index):
        return index > 0

    def _has_left_child(self, index):
        return self._left_child_index_of(index) < len(self._items)

    def _has_right_child(self, index):
        return self._right_child_index_of(index) < len(self._items)

    @staticmethod
    def _parent_index_of(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child_index_of(index):
        return (index * 2) + 1

    @staticmethod
    def _right_child_index_of(index):
        return (index * 2) + 2


if __name__ == '__main__':
    heap = MinHeap([int(x) for x in list('23456789065432345678993234567')])
    popped = heap.pop()

