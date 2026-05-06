class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        m,n = len(boxGrid), len(boxGrid[0])
        rotate = [[None]*m for _ in range(n)]


        for i in range(m):
            for j in range(n):
                if (boxGrid[i][j]=="*"):
                    rotate[j][m-1-i]="*"
                 
        countStone = []
        for row in boxGrid:
            countStoneRow = []
            cnt=0
            for (i,val) in enumerate(row):
                if (val=='#'):
                    cnt+=1
                elif(val=="*"):
                    countStoneRow.append(cnt)
                    cnt=0
                if (i==len(row)-1):
                    countStoneRow.append(cnt)
            countStone.append(countStoneRow)

        countStone = countStone[::-1]
        countStone = [ count[::-1] for count in countStone]

        for j in range(m):
            idx = 0
            for i in range(n-1,-1,-1):
                if (rotate[i][j] is None):
                    if countStone[j][idx]>0:
                        rotate[i][j] = "#"
                        countStone[j][idx]-=1
                    else:
                        rotate[i][j] = "."
                elif (rotate[i][j]=="*" and countStone[j][idx]==0):
                    idx+=1
                    if (idx>=len(countStone[j])):
                        break
        return rotate