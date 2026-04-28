class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [num for row in grid for num in row]
        ans = 0

        arr.sort()
        median = arr[len(arr)//2]

        for num in arr:
            if (num%x!=median%x):
                return -1
            
            ans+=abs(median - num)//x
        return ans
        