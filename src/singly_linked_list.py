from __future__ import annotations

from abc import ABC
from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList(ABC):
    head: Optional[Node]

    def __str__(self):
        current = self.head
        msg = 'Nodes:'
        while current is not None:
            msg += f' {current.value} >'
            current = current.next
        return msg

    def insert_before(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return True


class TrackingHeadAndLast(LinkedList):
    def __init__(self):
        self.head: Optional[Node] = None
        self.last: Optional[Node] = None

    def insert_after(self, value):
        new_node = Node(value)
        if not self.last:
            self.head = new_node
        else:
            self.last.next = new_node

        self.last = new_node
        return True

class TrackingHeadOnly(LinkedList):
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_after(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


if __name__ == '__main__':
    linked_list = TrackingHeadOnly()

    for i in range(10):
        linked_list.insert_before(i)
    for i in range(50, 60):
        linked_list.insert_after(i)

    print(linked_list)

