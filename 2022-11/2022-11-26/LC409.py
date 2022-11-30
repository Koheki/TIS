class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        chars = {}

        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        f = 0
        for c in chars.keys():
            res += (chars[c]//2)*2

            if chars[c] % 2 == 1:
                f = 1

        return res + f