class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        MOD = int(1e9+7)

        count_y = Counter(y for _, y in points)

        ans=total=0

        for cnt in count_y.values():
            f = cnt*(cnt-1)//2
            ans=(ans+f*total)%MOD
            total+=f

        return ans

"""
Count the number of trapezoids.

Approach:
- For each y-level, count how many ways to choose 2 points → f[y] = C(cnt[y], 2)
- A trapezoid is formed by choosing:
    - 2 points from y1
    - 2 points from y2 (y1 != y2)
→ Total contribution from (y1, y2) is f[y1] * f[y2]

So the answer is:
    sum of f[y1] * f[y2] for all y1 < y2

Instead of using two nested loops, we compute it in one pass:

Let:
    total = 0   # prefix sum of previous f values
    ans = 0

For each f[i]:
    ans += total * f[i]
    total += f[i]

Explanation:
- At step i, total = f[1] + f[2] + ... + f[i-1]
- So we add:
    f[i] * (f[1] + f[2] + ... + f[i-1])

Expanding:
    i = 1: ans = 0
    i = 2: ans = f[1] * f[2]
    i = 3: ans = f[1]*f[2] + f[1]*f[3] + f[2]*f[3]
    ...

Thus, we compute all pairs (i < j) exactly once.
"""