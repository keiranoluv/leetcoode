# from typing import List
# from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, pos: int, val: int):
        self._update(1, 0, self.n - 1, pos, val)

    def _update(self, node: int, l: int, r: int, pos: int, val: int):
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2

        if pos <= mid:
            self._update(node * 2, l, mid, pos, val)
        else:
            self._update(node * 2 + 1, mid + 1, r, pos, val)

        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, l: int, r: int, left: int, right: int) -> int:
        if right < l or r < left:
            return 0

        if left <= l and r <= right:
            return self.tree[node]

        mid = (l + r) // 2

        return max(
            self._query(node * 2, l, mid, left, right),
            self._query(node * 2 + 1, mid + 1, r, left, right)
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max(q[1] for q in queries)
        limit = max_x + 1

        obstacles = SortedList([0, limit])

        seg = SegmentTree(limit + 1)
        seg.update(limit, limit)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = obstacles.bisect_right(x)
                r = obstacles[idx]
                l = obstacles[idx - 1]

                obstacles.add(x)

                seg.update(x, x - l)
                seg.update(r, r - x)

            else:
                x, sz = q[1], q[2]

                idx = obstacles.bisect_right(x)
                left_obstacle = obstacles[idx - 1]

                best_inside = seg.query(0, x)
                tail = x - left_obstacle

                ans.append(max(best_inside, tail) >= sz)

        return ans