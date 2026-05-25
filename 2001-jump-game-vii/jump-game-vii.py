class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False]*n
        dp[0]=True

        reachableCount = 0
        for i in range(1,n):
            addIndex = i-minJump
            if (addIndex>=0 and dp[addIndex]==True):
                reachableCount+=1
            
            removeIndex = i-maxJump-1
            if (removeIndex>=0 and dp[removeIndex]==True):
                reachableCount-=1
            
            if (s[i]=='0' and reachableCount>0):
                dp[i]=True

        return dp[-1]