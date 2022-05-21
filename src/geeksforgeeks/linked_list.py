class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert_sorted(self, value):
        if value == self.value:
            node = Node(value)
            node.next = self.next
            self.next = node
            return node
        if value > self.value:
            if self.next:
                if value > self.next.value:
                    return self.next.insert_sorted(value)
                else:
                    node = Node(value)
                    node.next = self.next
                    self.next = node
                    return node
            else:
                self.next = Node(value)
                return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ['Nodes']
        c = self.head
        while c:
            s.append(f'{c.value}')
            c = c.next
        return ' > '.join(s)

    def insert_sorted(self, value):
        if not self.head:
            self.head = Node(value)
            return self.head
        elif value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return node
        else:
            return self.head.insert_sorted(value)


if __name__ == '__main__':
    llist = LinkedList()
    for i in range(10):
        llist.insert_sorted(i)

    llist.insert_sorted(-7)
    llist.insert_sorted(7)
    llist.insert_sorted(100)
    llist.insert_sorted(8.5)
    llist.insert_sorted(-4)

    print(llist)
