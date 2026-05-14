class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size();
        vector<int> cnt(210,0);

        for(int&a: nums){
            cnt[a]++;
        }

        for(int i=1; i<=n-2;++i){
            if (cnt[i]!=1)
                return false;
        }

        return cnt[n-1]==2 ? true:false;
        
    }
};