class TrieNode{
public:
    TrieNode* child[10];
    TrieNode(){
        for (int i=0;i<10;++i){
            child[i]=NULL;
        }
    }
};

class Trie{
public:
    TrieNode* root;

    Trie() {root = new TrieNode();}

    void insert(int num){
        TrieNode* node = root;
        string numStr = to_string(num);

        for (auto c: numStr){
            if (node->child[c-'0']==NULL)
                node->child[c-'0'] = new TrieNode();
            node = node->child[c-'0'];
        }
    }

    int findLongestPrefix(int num){
        TrieNode* node = root;
        string numStr = to_string(num);
        int length=0;
        for(auto c:numStr){
            if (node->child[c-'0']!=NULL){
                length++;
                node = node->child[c-'0'];
            }
            else{
                break;
            }
        }
        return length;
    }
};


class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {

        Trie trie;
        for (int num:arr1){
            trie.insert(num);
        }

        int ans=0;

        for(int num:arr2){
            ans = max(trie.findLongestPrefix(num), ans);
        }

        return ans;
        
    }
};