class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        allchars = set(s)
        res = 0
        for c in allchars:
            start,end = 0,0
            countC = 0
            for end in range(n):
                if s[end] == c:
                    countC += 1

                if end+1-start-countC > k:
                    # res = max(res,end-start)
                    if s[start] == c:
                        countC -= 1
                    start += 1

            res = max(res,end-start+1)

        return res