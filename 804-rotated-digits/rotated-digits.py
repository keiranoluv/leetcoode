class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {'3', '4', '7'}
        changed = {'2', '5', '6', '9'}

        ans = 0

        for num in range(1, n + 1):
            digits = set(str(num))

            if digits & invalid:
                continue

            if digits & changed:
                ans += 1

        return ans