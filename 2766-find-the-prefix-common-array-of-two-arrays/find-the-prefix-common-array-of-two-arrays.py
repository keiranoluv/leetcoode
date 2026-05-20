class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0]*(n+1)
        ans = [0]*n

        cnt=0
        
        for i in range(n):
            freq[A[i]]+=1
            freq[B[i]]+=1
            if (freq[A[i]]==2) and (freq[B[i]]==2) and A[i]!=B[i]:
                cnt+=2
            elif (freq[A[i]]==2):
                cnt+=1
            elif (freq[B[i]]==2):
                cnt+=1
            # print(freq, cnt)
            ans[i]=cnt
        # print(freq)
        return ans
        