class TrieNode{
public:
    bool isEnd;
    TrieNode* children[26];

    TrieNode(){
        isEnd = false;
        memset(children,0,sizeof(children));
    }
};

class Trie {
public:

    TrieNode *root;

    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for(auto&c: word){
            int idx = c-'a';
            if (node->children[idx] == nullptr){
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }   
        node->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for(auto&c: word){
            int idx = c-'a';
            if (node->children[idx] == nullptr)
                return 0;
            node=node->children[idx];
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for(auto&c: prefix){
            int idx = c-'a';
            if (node->children[idx] == nullptr)
                return 0;
            node=node->children[idx];
        }
        return 1;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */