class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_value = max(nums)
        n = len(nums)

        if (max_value+1 != n):
            return False
        nums.sort()
        for i in range(n-1):
            if (i+1!=nums[i]):
                return False
        return nums[n-2]==nums[n-1]
        