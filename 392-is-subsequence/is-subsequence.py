class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        dp[i][j]= true nếu chuỗi s[:j] là substring của t[:i]

        dp[i][j] = dp[i-1][j-1] nếu s[j]==t[i]
        dp[i][j] = dp[i-1][j]             nếu s[j]!=t[i]
        """
        s,t = "!"+s, "!"+t
        m,n = len(s), len(t)

        dp = [[0]*m for _ in range(n)]

        for i in range(n): dp[i][0]=1

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j-1] if s[j]==t[i] else dp[i-1][j]

        return bool(dp[-1][-1])