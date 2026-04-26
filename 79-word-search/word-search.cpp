class Solution {
public:
    const vector<vector<int>> dirs = {{0,-1},{0,1},{1,0},{-1,0}};
    bool dfs(
        vector<vector<char>>& board,
        vector<vector<bool>>& visited,
        string& word,
        int i,
        int j,
        int index,
        int m,
        int n
    ){
        if (index == word.size())
            return true;

        if (i<0 || i>=m || j<0 || j>=n)
            return false;

        if (visited[i][j])
            return false;
        
        if (board[i][j]!=word[index])
            return false;
        
        visited[i][j] = true;

        for(auto& dir:dirs){
            int x = i+dir[0];
            int y = j+dir[1];

            if (dfs(board,visited,word,x,y,index+1,m,n))
                return true;
        }

        visited[i][j]=false;
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, visited, word, i, j, 0, m, n)) {
                    return true;
                }
            }
        }

        return false;

    }
};