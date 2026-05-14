class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        i,j,k=0, n-2,n-1
        ans = 0
        attemps = n//3
        while (attemps>0):
            attemps-=1 
            ans+=piles[j]
            i+=1
            k-=2
            j-=2
        
        return ans

        