class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        queue<int> q;
        q.push(start);

        vector<bool> visited(n,false);

        while (!q.empty()){
            int s = q.front();
            q.pop();

            visited[s] = true;

            if (arr[s]==0)
                return true;
            
            int u=s+arr[s], v = s-arr[s];
            if (0<=u && u<n && visited[u]==false)
                q.push(u);
            if (0<=v && v<n && visited[v]==false)
                q.push(v);
        }

        return false;
    }
};