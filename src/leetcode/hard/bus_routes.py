"""
routes = [
    [1, 2, 7],
    [3, 6, 7]
]

source = 1
target = 6


routes = [
    [7, 12],
    [4, 5, 15],
    [6],
    [15, 19],
    [9, 12, 13]
]

source = 15
target = 12


Looking at this, my brain is thinking BFS.
- Find all the arrays containing the target -> 12.
- For each array, find the "neighbors" of the target.

Are the routes of a bus sorted?
If so, this can help us narrow down from O(n) to O(log n) when looking for initial arrays

- node (none)
- neighbors = 2 arrays
- for each neighbor in neighbors:
    for value in neighbor:
        find the value in the other routes.
        if value found, add it to our queue.
        mark this neighbor as visited {}.

i did come across a thought -> how come not DFS?
well, since there could be infinite cycles when hopping from route to route, we want to keep track of visited routes.
if we go dfs, we may never be able to mark the initial route as visited.

"""

from collections import defaultdict


class Solution:
    @classmethod
    def num_buses_to_destination(cls, routes, source, target):
        if source == target:
            return 0
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        queue = graph[source]
        visited = set()
        steps = 0
        while queue:
            temp = []
            for route_idx in queue:
                if route_idx in visited:
                    continue
                visited.add(route_idx)
                for stop in routes[route_idx]:
                    if stop == target:
                        return steps + 1
                    for route_idx2 in graph[stop]:
                        if route_idx2 not in visited:
                            temp.append(route_idx2)
            queue = temp
            steps += 1
        return -1


if __name__ == '__main__':
    result = Solution.num_buses_to_destination(
        routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]],
        source=15,
        target=12
    )

    print(result)
