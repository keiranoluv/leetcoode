class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        visited = [False]*n
        
        def dfs(start):
            visited[start] = True
            if (arr[start]==0):
                return True
            
            for target in [start-arr[start], start+arr[start]]:
                if ((0<=target<n) and (visited[target]==False)):
                    if (dfs(target)):
                        return True

            return False


        return dfs(start)
        