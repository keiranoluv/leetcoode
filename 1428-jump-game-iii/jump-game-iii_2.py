from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)

        visited = [False] * n
        visited[start] = True

        q = deque([start])

        while q:

            s = q.popleft()

            if arr[s] == 0:
                return True

            for target in [s - arr[s], s + arr[s]]:

                if 0 <= target < n and not visited[target]:

                    visited[target] = True
                    q.append(target)

        return False