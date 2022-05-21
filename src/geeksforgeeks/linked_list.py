from __future__ import annotations


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
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.insert(value)

    def __str__(self):
        s = []
        c = self.head
        while c:
            s.append(f'{c.value}')
            c = c.next
        return 'Linked List Nodes: ' + ' > '.join(s)

    def compare(self, other: LinkedList):
        p1 = self.head
        p2 = other.head

        while p1 and p2 and p1.value == p2.value:
            p1 = p1.next
            p2 = p2.next

        if not p1 and not p2:
            return 0

        if not p2 or p1.value > p2.value:
            return 1

        if not p1 or p2.value > p1.value:
            return -1

        if p1.value == p2.value:
            return 0

    def delete(self, value):
        prev = None
        current = self.head

        while current:
            if value == current.value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = self.head.next
                return True

            if not current.next:
                return False

            prev = current
            current = current.next

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

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return self.head

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(value)


def main():
    llist = LinkedList()
    for i in range(10):
        llist.insert_sorted(i)

    llist.insert_sorted(-7)
    llist.insert_sorted(7)
    llist.insert_sorted(100)
    llist.insert_sorted(8.5)
    llist.insert_sorted(-4)
    llist.delete(7)
    llist.delete(-7)
    llist.delete(100)
    print(llist)

    ll1 = LinkedList('hello')
    ll2 = LinkedList('hello')
    print(ll1.compare(ll2))

    ll1 = LinkedList('')
    ll2 = LinkedList('')
    print(ll1.compare(ll2))

    ll1 = LinkedList('1')
    ll2 = LinkedList('')
    print(ll1.compare(ll2))

    ll1 = LinkedList('1')
    ll2 = LinkedList('2')
    print(ll1.compare(ll2))

    ll1 = LinkedList('112')
    ll2 = LinkedList('2')
    print(ll1.compare(ll2))


if __name__ == '__main__':
    main()
