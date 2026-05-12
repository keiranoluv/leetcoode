class Solution:
    
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        diff = [(i,val[1]-val[0]) for (i, val) in enumerate(tasks)]
        order = sorted(diff, key=lambda x: x[1], reverse=True)

        low = sum(x[0] for x in tasks)
        high = sum(x[1] for x in tasks)

        def check(energy):
            curr = energy
            for item in order:
                index = item[0]
                actual = tasks[index][0]
                minimum = tasks[index][1]
                if (curr<minimum):
                    return False
                curr -= actual
            return True

        while (low<high):
            mid = (low+high)//2
            if (check(mid)==True):
                high = mid
            else:
                low = mid+1
        
        return low