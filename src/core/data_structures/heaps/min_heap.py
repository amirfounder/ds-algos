class MinHeap:
    def __init__(self, items=None):
        self._items = items or []

    def peek(self):
        if not self._items:
            return

        return self._items[0]

    def pop(self):
        if not self._items:
            return

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
            pass

        left_idx = (2 * index) + 1
        right_idx = left_idx + 1

        left = self._items[left_idx] if left_idx < len(self._items) else float('inf')
        right = self._items[right_idx] if right_idx < len(self._items) else float('inf')

        smallest_child_idx = left_idx if left < right else right_idx

        if self._items[index] > self._items[smallest_child_idx]:
            self._swap(index, smallest_child_idx)
            self._sift_down(smallest_child_idx)

    def _sift_up(self, index):
        while self._has_parent(index) and self._items[self._parent_index_of(index)] > self._items[index]:
            self._swap(index, self._parent_index_of(index))
            index = self._parent_index_of(index)

    @staticmethod
    def _has_parent(index):
        return index > 0

    @staticmethod
    def _has_left_child(index):
        pass

    @staticmethod
    def _has_right_child(index):
        pass

    @staticmethod
    def _parent_index_of(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child_of(index):
        pass

    @staticmethod
    def _right_child_of(index):
        pass


if __name__ == '__main__':
    heap = MinHeap([int(x) for x in list('23456789065432345678993234567')])
    popped = heap.pop()

