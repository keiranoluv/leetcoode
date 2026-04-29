class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {

        unordered_map<int, int> count_y;
        const int mod = 1e9+7;
        long long ans = 0, total = 0;
        for(auto& point : points) {
            count_y[point[1]]++;
        }
        for(auto& [_,cnt_y]:count_y) {
            long long cnt = (long long)cnt_y*(cnt_y-1)/2;
            ans = (ans + cnt * total) % mod;
            total = (total + cnt) % mod;
        }
        return ans % mod;
    }
};