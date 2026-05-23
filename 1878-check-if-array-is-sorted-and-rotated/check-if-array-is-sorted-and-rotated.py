class Solution:
    def check(self, nums: List[int]) -> bool:

        idx = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                idx = i+1
                break
        if (idx == 0):
            return True

        for i in range(idx, n-1):
            if nums[i] > nums[i+1]:
                return False

        if (nums[-1] <= nums[0]) and (nums[idx]<=nums[0]):
            return True
        else:
            return False