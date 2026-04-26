class Solution {
    static constexpr int dirs[4][2] = {{0,-1},{0,1},{-1,0},{1,0}};
public:
    bool dfs(vector<vector<char>>& grid,
        bitset<500*500+1>& visited,
        int m,
        int n,
        int i,
        int j,
        int parent_i,
        int parent_j){
            visited[i*n+j] = 1;
            for (auto&dir: dirs){
                int x = i+dir[0];
                int y = j+dir[1];
                if (x==parent_i and y==parent_j){
                    continue;
                }
                if (x>=m || x<0 || y>=n || y<0){
                    continue;
                }
                if (grid[x][y]!=grid[i][j]){
                    continue;
                }
                if (visited[x*n+y])
                    return true;
                if (dfs(grid,visited,m,n,x,y,i,j))
                    return true;
            }
        return false;
        }

    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        bitset<500*500+1> visited;

        for(int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                if (!visited[i*n+j])
                    if (dfs(grid,visited,m,n,i,j,-1,-1))
                        return true;
            }
        }
        return false;
    }
};