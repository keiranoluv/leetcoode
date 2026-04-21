class Solution {
private:
    vector<int> fa;
    vector<int> rank;
    
    int find(int x){
        if (fa[x]!=x){
            fa[x]=find(fa[x]);
        }
        return fa[x];
    }

    void Union(int x, int y){
        x = find(x);
        y = find(y);
        if (x==y)
            return;
        if (rank[x]<rank[y])
            swap(x,y);
        fa[y]=x;
        if (rank[x]==rank[y]){
            rank[x]++;
        }
    }
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        fa.resize(n);
        rank.resize(n,0);
        for(int i=0; i<n;++i){
            fa[i]=i;
        }
        for(auto&pair: allowedSwaps){
            Union(pair[0],pair[1]);
        }

        unordered_map<int, unordered_map<int,int>> sets;
        for(int i=0;i<n;++i){
            int f = find(i);
            sets[f][source[i]]++;
        }
        int ans=0;
        for(int i=0;i<n;++i){
            int f = find(i);
            if (sets[f][target[i]]>0){
                sets[f][target[i]]--;
            } 
            else
                ans++;
        }


        return ans;
    }
};

/*

"""
Tóm tắt đề bài:
Dựa vào allowedSwaps, min_Hamming_distance(source,target)

Gợi ý của đề:
- source array -> graph với index là node và allowedSawps[i] là cạnh
- node trong cùng 1 "thành phần" có thể tự do swap với node khác
- với mỗi "thành phần", tìm số phần tử chung, phần tử không chung -> chính là Hamming distance
"""
source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,1],[1,2],[3,4]]

B1: gộp nhóm
fa=[0,1,2,3,4]
rank=[0,0,0,0,0]
Uinon(0,1):
    x=0,y=1
    fa[1]=0
    rank[0]=1

Union(1,2):
    x=0
    y=2
    fa[2]=0

Union(3,4):
    x=3
    y=4
    fa[4]=3
    rank[3]=1

*/