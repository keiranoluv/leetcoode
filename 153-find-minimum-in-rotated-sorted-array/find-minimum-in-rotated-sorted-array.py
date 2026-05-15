class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        L=0
        R=n-1

        if (n==2):
            return min(nums[L],nums[R])
        
        if (nums[0]<nums[n-1]):
            return nums[0]


        while(L<R):
            mid = (L+R)//2
            nextIndex = (mid+1)%n
            prevIndex = (mid-1)%n
            if (nums[mid]<nums[nextIndex]) and (nums[mid]<nums[prevIndex]):
                return nums[mid]

            if (nums[0]<=nums[mid-1]):
                L = mid+1
            
            if (nums[mid+1]<=nums[n-1]):
                R = mid
        return nums[L]

"""

5 6 [7] 8 0 1 2 3 4
Nếu nums[0]<nums[mid-1] nghĩa là dãy bên trái mid là dãy tăng
=> min phải nằm bên phải

Nếu nums[mid+1]<nums[n-1] nghĩa là dãy bên phải mid cũng là dãy tăng
=> min phải nằm bên trái

Submit01: [2,1]->TLE
Debug: L=0 , R=1 -> mid=0
nextIndex=1
prevIndex=0

Submit02: [11,13,15,17] -> Wrong answer
Debug: L=0, R=3 -> mid=1
nextIndex=2
prevIndex=1
"""


        