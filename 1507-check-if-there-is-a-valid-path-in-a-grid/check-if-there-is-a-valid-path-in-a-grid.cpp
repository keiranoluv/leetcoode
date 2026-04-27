class Solution {
public:
    vector<vector<pair<int,int>>> dirs={
        {{{0,0},{0,0}}},
        {{{0,-1},{0,1}}},//1
        {{{1,0},{-1,0}}},//2
        {{{0,-1},{1,0}}},//3
        {{{0,1},{1,0}}},//4
        {{{0,-1},{-1,0}}},//5
        {{{0,1},{-1,0}}},//6
    };

    bool dfs(int i, int j, vector<vector<int>>&grid, vector<vector<bool>>& visited){
        int m = grid.size();
        int n = grid[0].size();

        visited[i][j]=true;
        if (i==m-1 && j ==n-1)
            return true;
        int val=grid[i][j];

        for(int k=0; k<dirs[val].size();++k){
            int i_ = i+dirs[val][k].first;
            int j_ = j+dirs[val][k].second;

            bool flag = false;

            if (i_>=0 && i_<m && j_>=0 && j_<n){
                int new_val = grid[i_][j_];
                for(auto&[x,y]:dirs[new_val]){
                    if (i_+x == i && j_+y==j){
                        flag = true;
                        break;
                    }
                }
                if (flag == false){
                    continue;
                }
                if (visited[i_][j_] == false){
                    if (dfs(i_,j_, grid, visited)){
                        return true;
                    }
                }
            }  
        } 
        return false;
    }
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size(), n=grid[0].size();
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        return dfs(0,0,grid,visited);
    }
};