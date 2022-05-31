"""
Brute force: Loop over every point in points and calculate the euclidean distance.
Append to a minheap
Have a variable that stores the minimum point so far along with the distance.
Compare distances and reassign the point.
This would equal o(n) time.
"""
import math
from heapq import heapify, heappop, heappush
from typing import List


class Point:
    def __init__(self, x, y):
        self.point = [x, y]
        self.distance = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.distance < other.distance


class MinHeap:
    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def pop(self):
        return heappop(self.heap).point

    def push(self, item: Point):
        heappush(self.heap, item)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = MinHeap()
        [heap.push(Point(*point)) for point in points]
        return [heap.pop() for _ in range(k)]
