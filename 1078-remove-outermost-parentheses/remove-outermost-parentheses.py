class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        for c in s:
            if c == '(':
                stack.append(c)
                if (len(stack)>1):
                    ans+=c
            else:
                if (len(stack)>=2):
                    ans+=c
                stack.pop()

        return ans
        