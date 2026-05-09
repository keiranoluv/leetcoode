class Solution:
    def rotate(self, grid, layerNum,m,n):
        temp = grid[layerNum][layerNum]
        for i in range(layerNum,n-1-layerNum): #U
            grid[layerNum][i]=grid[layerNum][i+1]
        for i in range(layerNum,m-1-layerNum): #R
            grid[i][n-1-layerNum]=grid[i+1][n-1-layerNum]
        for i in range(layerNum,n-1-layerNum): #R
            grid[m-1-layerNum][n-1-i] = grid[m-1-layerNum][n-1-(i+1)]
        for i in range(layerNum,m-1-layerNum): #L
            grid[m-1-i][layerNum] = grid[m-1-(i+1)][layerNum]
        grid[layerNum+1][layerNum]=temp
        return grid

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = (len(grid)), len(grid[0])
        numLayer = min(m,n)//2
        for i in range(numLayer):
            freq = (m-2*i)*(n-2*i) - (m-2*(i+1))*(n-2*(i+1)) #out square minus in square
            rotateTimes = k%freq
            while(rotateTimes > 0):
                grid = self.rotate(grid,i,m,n)
                rotateTimes -=1
        
        return grid