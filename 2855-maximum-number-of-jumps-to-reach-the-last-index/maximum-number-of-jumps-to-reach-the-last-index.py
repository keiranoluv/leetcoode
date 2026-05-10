
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if (i==n-1):
                return 0
            res = -inf
            for j in range(i+1,n):
                if (abs(nums[i]-nums[j])<=target):
                    res = max(res,dfs(j)+1)

            return res

        ans = dfs(0)
        return -1 if ans < 0 else ans