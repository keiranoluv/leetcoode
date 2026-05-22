class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while(L<R):
            mid=(L+R)//2
            if (nums[mid]==target):
                return mid
            
            if nums[mid]<nums[R]:
                if nums[mid]<target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
            
            elif nums[mid]>nums[R]:
                if nums[L]<=target<nums[mid]:
                    R=mid-1
                else:
                    L=mid+1

        return L if nums[L]==target else -1
                