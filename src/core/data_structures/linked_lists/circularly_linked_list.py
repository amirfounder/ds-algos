from typing import Optional, Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self, values: list[Any] = None):
        self.head: Optional[Node] = None
        self.last: Optional[Node] = None

        if not values:
            return

        for value in values:
            self.insert_last(value)

    def __str__(self):
        s = 'Nodes:'
        current = self.head
        s += f' {current.value} >'
        current = current.next
        while current is not self.head:
            s += f' {current.value} >'
            current = current.next

        return s

    def insert_last(self, value):
        temp = Node(value)

        if not self.head:
            self.head = temp
            self.head.next = self.head
            return

        if self.head == self.last:
            self.head.next = temp
            temp.next = self.head
            return

        self.last = temp
        self.last.next = self.head

        return


if __name__ == '__main__':
    llist = LinkedList([1, 23, 4, 5, 6])
    print(llist)

    print('Breakpoint here')
