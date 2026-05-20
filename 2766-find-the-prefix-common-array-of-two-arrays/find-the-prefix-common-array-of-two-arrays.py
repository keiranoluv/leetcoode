class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = {}
        ans = [None]*n

        for i in range(n):
            if (A[i] in freq):
                freq[A[i]]+=1
            else:
                freq[A[i]]=1
            if (B[i] in freq):
                freq[B[i]]+=1
            else:
                freq[B[i]]=1
            cnt=0
            for k,v in freq.items():
                if (v==2):
                    cnt+=1
                ans[i]=cnt
        # print(freq)
        return ans
        