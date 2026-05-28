class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        children = []
        best = []

        def new_node():
            children.append([-1]*26)
            best.append(-1)
            return len(children) - 1

        root = new_node()

        def better(i, j):
            if j==-1:
                return i
            if (len(wordsContainer[i]) != len(wordsContainer[j])):
                return i if len(wordsContainer[i]) < len(wordsContainer[j]) else j
            return i if i<j else j
        
        for i, word in enumerate(wordsContainer):
            node = root
            best[node] = better(i, best[node])

            for ch in reversed(word):
                c = ord(ch) - ord('a')
                if children[node][c] == -1:
                    children[node][c] = new_node()
                node = children[node][c]
                best[node] = better(i, best[node])

        ans = []

        for query in wordsQuery:
            node = root
            for ch in reversed(query):
                c = ord(ch) - ord('a')
                if children[node][c] == -1:
                    break
                node = children[node][c]
            ans.append(best[node])

        return ans