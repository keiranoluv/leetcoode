class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)

        for i,num in enumerate(nums):
            f+=i*num

        res=f
        for i in range(1,n):
            f = f + numSum - n*nums[n-i]
            res = max(res,f)

        return res
    

"""
F(0)=0*nums[0] + 1*nums[1]+...+(n-1)*nums[n-1]
F(1)=1*nums[0] + 2*nums[1]+...+(n-1)*nums[n-2] + 0*nums[n-1]
   = F(0) + numsum - n*nums[n-1]

F(2)=2*nums[0] + 3*nums[1]+...+ 0*nums[n-2] + 1*nums[n-1]
   =F(1) + numSum - n*nums[n-2]


=> F(k)=F(k-1)+num_sum - n*nums[n-k]


"""