class Solution:
    def rotatedDigits(self, n: int) -> int:
        mapping = {
            '0': '0',
            '1': '1',
            '2': '5',
            '3': None,
            '4': None,
            '5': '2',
            '6': '9',
            '7': None,
            '8': '8',
            '9': '6',
        }
        ans = 0

        for i in range(1,n+1):
            num_str = str(i)
            num_str = [mapping[c] for c in num_str]
            if None not in num_str:
                num = int(''.join(num_str))
                if num!=i:
                    ans+=1
            else:
                continue

        return ans