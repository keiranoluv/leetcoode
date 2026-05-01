class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int n = nums.size();
        long long f = 0;
        long long sum_nums = 0;
        for(int i=0; i< n; ++i){
            sum_nums+=nums[i];
            f+=i*nums[i];
        }
        long long ans = f;
        for(int i=1;i<n;++i){
            f=f+sum_nums - n*nums[n-i];
            ans = max(f,ans);
        }
        return ans;


    }
};