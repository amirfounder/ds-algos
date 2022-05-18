from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


if __name__ == '__main__':
    head = Node(0)
    prev = head
    for i in range(1, 11):
        current = Node(i)
        prev.next = current
        current.prev = prev
        prev = current
    # last = Node(12)
    # prev.next = last
    # last.prev = prev
    # prev.next = last

    print_val = 'Nodes:'
    current = head
    while current:
        print_val += f' {current.value} >'
        current = current.next

    print(print_val)

    # print_val = 'Nodes:'
    # current = last
    # while current.prev:
    #     print_val += f' {current.value} >'
    #     current = current.prev
    #
    # print(print_val)
