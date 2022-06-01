class MinStack:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append((value, min(value, self.items[-1][1])))

    def peek(self):
        if self.items:
            return self.items[-1][0]

    def pop(self):
        if self.items:
            return self.items.pop()[0]

    def min(self):
        if self.items:
            return self.items[-1][1]
