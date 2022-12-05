class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        def isValid(m):
            start = 0
            maxfreq = 0
            freq = collections.defaultdict(int)
            for end in range(n):
                freq[s[end]] += 1

                if end+1-start > m:
                    freq[s[start]] -= 1
                    start += 1

                maxfreq = max(maxfreq,freq[s[end]])
                if m - maxfreq <= k:
                    return True
            return False

        l,r = 1,n+1
    
        while r-l > 1:
            m = l+(r-l)//2
            if isValid(m):
                l = m
            else:
                r = m
        return l
