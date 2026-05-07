class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        prefixMax = []
        suffixMin = []
        n = len(nums)
        MAX = -int(1e9+10)
        MIN = -MAX
        for (i,val) in enumerate(nums):
            MAX = max(val, MAX)
            prefixMax.append(MAX)
            
            MIN = min(nums[n-1-i], MIN)
            suffixMin.append(MIN)

        suffixMin = suffixMin[::-1]
        
        ans = []
        start = 0
        flag = False
        for i in range(n-1):
            if (prefixMax[i]<=suffixMin[i+1]):
                flag = True
                ans.extend([prefixMax[i]]*(i-start+1))
                start = i+1 
        
        ans.extend([prefixMax[-1]]*(n-start))
        if (flag == False):
            return [prefixMax[-1]]*n
        else:
            return ans

        