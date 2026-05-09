class Solution {
public:

    void rotate(vector<vector<int>>&grid, int layerNum){
        
        int m= grid.size(), n = grid[0].size();
        int temp = grid[layerNum][layerNum];

        for (int i=layerNum; i<n-1-layerNum;++i)
            grid[layerNum][i]=grid[layerNum][i+1];

        for(int j=layerNum; j<m-1-layerNum;++j)
            grid[j][n-1-layerNum]=grid[j+1][n-1-layerNum];

        for(int i=layerNum; i<n-1-layerNum;++i)
            grid[m-1-layerNum][n-1-i]=grid[m-1-layerNum][n-1-(i+1)];

        for (int j=layerNum; j<m-layerNum-1;++j)
            grid[m-1-j][layerNum]=grid[m-1-(j+1)][layerNum];
        
        grid[layerNum+1][layerNum] = temp;

        return;
    }
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m =  grid.size(), n = grid[0].size();
        int layerNums = min(m,n)/2;

        for(int i=0; i<layerNums;++i){
            int rotateTimes = k% ((m-2*i)*(n-2*i)-(m-2*(i+1))*(n-2*(i+1)));
            // cout<<rotateTimes<<" ";
            while (rotateTimes--)
                rotate(grid,i); 
        }
        return grid;
    }
};