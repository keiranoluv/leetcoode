class Solution {
public:
    int numberOfSpecialChars(string word) {
        int n = word.size();
        vector<int> lastLower(26, -1);
        vector<int> firstUpper(26, -1);

        for (int i=0; i<n; i++){
            char c = word[i];
            if ('a'<=c && c<='z'){
                lastLower[c-'a'] = i;
            }
            else if ('A'<=c && c<='Z'){
                if (firstUpper[c-'A']==-1){
                    firstUpper[c-'A'] = i;
                }
            }
        }

        int ans=0;
        for (int i=0; i<26; i++){
            if (lastLower[i]!=-1 && firstUpper[i]!=-1 && lastLower[i]<firstUpper[i]){
                ans++;
            }
        }
        return ans;
    }
};