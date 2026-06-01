class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        ans = 0
        cnt = 0
        for num in cost[::-1]:
            cnt += 1
            if cnt % 3 != 0:
                ans += num

        return ans
