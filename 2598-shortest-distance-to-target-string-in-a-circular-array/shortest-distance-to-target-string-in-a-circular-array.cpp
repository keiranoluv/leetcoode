class Solution {
public:
    bool isEqual(string&a, string&b){
        if (a.size()!=b.size())
            return false;
        for(int i=0; i< a.size();++i){
            if (a[i]!=b[i]){
                return false;
            }
        }
        return true;
    }

    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size();
        int realIndex = -1;
        int ans = INT_MAX;
        for (int i=1; i<=n ; ++i){//forward
            int idx = (startIndex+i)%n;
            if (isEqual(target, words[idx])){
                ans=min(ans, abs(idx-startIndex));
                ans=min(ans, abs((idx+n)-startIndex));
                ans=min(ans, abs((idx-n)-startIndex));
            }
        }
        
        if (ans==INT_MAX)
            return -1;
        else
            return ans;
    }
};