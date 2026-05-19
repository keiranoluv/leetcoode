class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        z = nums1 & nums2

        if (len(z))==0:
            return -1
            
        return min(z)
        