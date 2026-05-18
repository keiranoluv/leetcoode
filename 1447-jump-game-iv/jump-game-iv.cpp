class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        if (n==1)
            return 0;
      
        unordered_map<int, vector<int>> graph;
        for(int i=0; i<n;++i){
            graph[arr[i]].push_back(i);
        }

        vector<bool> visited(n+1,false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        int ans = 0;
        while (!q.empty()){
            int queue_size =    q.size();
            for(int i=0; i< queue_size;++i){
                int j = q.front(); q.pop();

                if (j==n-1)
                    return ans;
                
                for (int teleport: graph[arr[j]]){
                    if (visited[teleport]==false){
                        q.push(teleport);
                        visited[teleport]=true;
                    }
                }

                graph[arr[j]].clear();

                vector<int> neighbors = {j-1,j+1};
                for (auto neighbor:neighbors){
                    if (neighbor>=0 && neighbor<n && visited[neighbor]==false){
                        q.push(neighbor);
                        visited[neighbor]=true;
                    }
                }
        
            }
            ans+=1; 
        }
        return ans;
    }
};