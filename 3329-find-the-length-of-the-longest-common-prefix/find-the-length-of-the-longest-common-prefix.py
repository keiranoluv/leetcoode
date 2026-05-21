class TrieNode:
    def __init__(self):
        self.child = [None]*10

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        str_num = str(num)

        for digit in str_num:
            idx = int(digit)
            if node.child[idx] is None:
                node.child[idx] = TrieNode()
            node = node.child[idx]
    def find_longest_prefix(self,num):
        node = self.root
        str_num = str(num)
        length=0
        for digit in str_num:
            idx = int(digit)
            if (node.child[idx] is not None):
                length+=1
                node = node.child[idx]
            else:
                break
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(num)

        ans = 0
        for num in arr2:
            ans = max(trie.find_longest_prefix(num), ans)

        return ans


"""
Brute-force solution:
-> O(mn)

Trie:
O(8m)+O(8n)
"""
        