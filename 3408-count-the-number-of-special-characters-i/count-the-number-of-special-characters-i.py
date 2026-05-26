class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercaseCount = [False] * 26
        uppercaseCount = [False] * 26
        for c in word:
            if "a" <= c <= "z":
                lowercaseCount[ord(c) - ord("a")] = True
            elif "A" <= c <= "Z":
                uppercaseCount[ord(c) - ord("A")] = True
        ans = 0
        for i in range(26):
            if lowercaseCount[i] and uppercaseCount[i]:
                ans += 1

        return ans
