from .single_node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        values = []

        while current:
            values.append(current.value)
            current = current.next

        return 'Nodes: ' + ', '.join(values)

    def insert_before(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


if __name__ == '__main__':
    linked_list = SinglyLinkedList()

    for i in range(10):
        linked_list.insert_before(i)
    for i in range(50, 60):
        linked_list.insert_after(i)

    print(linked_list)

