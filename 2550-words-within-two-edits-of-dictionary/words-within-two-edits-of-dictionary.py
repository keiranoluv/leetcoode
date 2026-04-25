class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for source in queries:
            for target in dictionary:
                diff = sum(a!=b for a,b in zip(source,target))

                if (diff<=2):
                    ans.append(source)
                    break
        return ans
                    



"""
brute force:
for each word in queries:
    compare with each word in dictionary
-> O(n^2.leng(word))

First submit: wrong answer:
queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"]
dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]
-> Wrong because I didnt remove duplicate words in ans
"""