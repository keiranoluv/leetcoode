class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        move_nums = len(moves)
        moves_split = [c for c in moves]

        ans=0
        cnt=0
        for c in moves_split:
            if (c=='L'):
                ans-=1 
            elif (c=='R'):
                ans+=1
            else:
                cnt+=1
        
        return abs(ans)+cnt
        