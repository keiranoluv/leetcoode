MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2,MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
   
        n = len(nums)
        bucket = dict()
        for idx, val in enumerate(nums): 
            for p in factors[val]: #bucket[p] = all indices in nums mode p = 0
                if p not in bucket:
                    bucket[p]=[idx]
                else:
                    bucket[p].append(idx)
        
        dist = [-1]*n
        dist[0]=0

        queue=deque()
        queue.append(0)
        used_prime = set()

        while (queue):
            idx =queue.popleft()

            for i in (idx-1,idx+1): #neighbor
                if (0<=i<n and dist[i]==-1):
                    dist[i]=dist[idx]+1
                    queue.append(i)

            num = nums[idx]
            if (factors[num]==[num]) and num not in used_prime: #teleport
                for i in bucket[num]:
                    if (dist[i]==-1):
                        dist[i]=dist[idx]+1
                        queue.append(i)

                used_prime.add(num)

        return dist[-1]






        