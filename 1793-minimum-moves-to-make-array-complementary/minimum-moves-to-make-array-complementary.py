class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        m = n//2
        diff = [0]*(2*limit+10)
        for i in range(0,m):
            a=nums[i]
            b=nums[n-1-i]
            S = a+b
            low = min(a,b)
            high = max(a,b)
            L = low+1
            R = high+limit
            diff[L]+=1
            diff[R+1]-=1
            diff[S]+=1
            diff[S+1]-=1
        # print(diff[2:limit*2+1])
        ans=int(2*1e5+10)
        saving=0
        for s in range(2,2*limit+1):
            saving+=diff[s] 
            ans=min(ans, n-saving)

        return ans

        