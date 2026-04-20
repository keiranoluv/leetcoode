class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        infor = dict()

        for (i,color) in enumerate(colors):
            if color not in infor:
                infor[color]=[i]
            else:
                if (len(infor[color])==1):
                    infor[color].append(i)
                else:
                    infor[color][1]=i

        ans = max(
            abs(u-v)
            for k1,k2 in product(infor,infor)
            if k1!=k2
            for u in infor[k1]
            for v in infor[k2]
        )

        
        return ans
        
        


"""
Duyệt trâu :D
"""