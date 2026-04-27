class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])

        dirs = {
            1: [(0,-1),(0,1)], #LR
            2: [(-1,0),(1,0)], #UD
            3: [(0,-1),(1,0)],#LD
            4: [(0,1),(1,0)],  #RD
            5: [(0,-1),(-1,0)], #LU
            6: [(0,1),(-1,0)],  #RU
        }
        visited = [[False]*n for _ in range(m)]

        def dfs(i, j):
            visited[i][j] = True
            if (i==m-1 and j==n-1):
                return True
            
            val = grid[i][j]
            for dir in dirs[val]:
                x = i+dir[0]
                y = j+dir[1]

                flag = False
                if (0<=x<m and 0<=y<n):
                    new_val = grid[x][y]
                    for new_dir in dirs[new_val]:
                        if (x+new_dir[0]==i and y+new_dir[1]==j):
                            flag = True
                            break
                if (not flag): 
                    continue
                if (not visited[x][y]):
                    if (dfs(x,y)):
                        return True
            
            return False

        return dfs(0,0)

"""
Key:
    current cell can go to next cell
    AND
    next cell can go back to current cell

"""