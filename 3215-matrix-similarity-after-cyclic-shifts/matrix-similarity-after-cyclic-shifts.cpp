class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        int m = mat.size(); //số hàng
        int n = mat[0].size(); //số cột

        const vector<vector<int>> ref = mat;

        if (k%m==0 and k%n==0)
            return 1;
        
        for (int iter=0; iter<k; ++iter){
            for(int i=0; i<m; i+=2){
                int tmp=mat[i][0];
                for(int j=0; j<n-1; ++j)
                    mat[i][j] = mat[i][j+1];
                mat[i][n-1] = tmp;
            }

            for(int i=1;i<m; i+=2){
                int tmp=mat[i][n-1];
                for(int j=n-1; j>0; --j){
                    mat[i][j] = mat[i][j-1];
                }
                mat[i][0] = tmp;
            }
        }
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j)
                if (mat[i][j] != ref[i][j])
                    return false;
        }
        return true;
    }
};