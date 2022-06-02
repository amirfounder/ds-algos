"""
First, we want to create 3 variables to store information:
1. the frequency counter map.
2. the stack (as a hashmap. The key is the frequency, the value is the list of vals at that frequency)
3. the max frequency so far.

the freq counter will allow us to keep track of the frequencies of all previous number so we can accurately
recalculate the max_so_far.

the stack is what we will be using to push and remove things.
the stack is a map, where the key is the frequency (stored in the freq counter) and value are the items
that have that frequency.

the max so far is the value that we will use to know where in our stack to get the next item to pop.
"""
class FreqStack:

    def __init__(self):
        self.frequency_map = {}
        self.stack = {}
        self.max_so_far = 0

    def push(self, val: int) -> None:
        if val not in self.frequency_map:
            self.frequency_map[val] = 0
        self.frequency_map[val] += 1

        frequency = self.frequency_map[val]

        if frequency not in self.stack:
            self.stack[frequency] = []
        self.stack[frequency].append(val)

        self.max_so_far = max(self.max_so_far, frequency)

    def pop(self) -> int:
        return_val = self.stack[self.max_so_far].pop()
        if not self.stack[self.max_so_far]:
            self.max_so_far -= 1

        self.frequency_map[return_val] -= 1

        return return_val


def main():
    s = FreqStack()
    s.push(5)
    s.push(7)
    s.push(5)
    s.push(7)
    s.push(4)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    main()