class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        visited = [False]*n
        
        q = []
        cnt = 0
        q.append(start)
        while (q):
            s = q.pop(0)
            print(s, arr[s])
            visited[s] = True
            if (arr[s]==0):
                cnt+=1
            
            for target in [s-arr[s],s+arr[s]]:
                if 0<=target<n and visited[target]==False:
                    q.append(target)

        return True if cnt>= 1 else False

        