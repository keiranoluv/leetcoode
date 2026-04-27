class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)

        def dfs(u):
            visited[u]=True

            for v in rooms[u]:
                if (not visited[v]):
                    dfs(v)
        
        dfs(0)

        for v in visited:
            if (v==False):
                return False
        return True