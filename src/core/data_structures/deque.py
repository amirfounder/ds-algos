from collections import deque, Counter

if __name__ == '__main__':
    d = deque()
    d.appendleft(1)
    d.append(2)
    r = d.pop()
    l = d.popleft()
    print(l, r)
