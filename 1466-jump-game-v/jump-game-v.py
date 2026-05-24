class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1]*n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            best=1

            for j in range(i+1, min(n,i+d+1)):
                if (arr[j]>=arr[i]):
                    break
                best = max(best,1+dfs(j))

            for j in range(i-1, max(-1,i-d-1), -1):
                if (arr[j]>=arr[i]):
                    break
                best = max(best,1+dfs(j))

            dp[i] = best
            return best

        ans=0
        for i in range(n):
            ans = max(ans,dfs(i))
        return ans
        