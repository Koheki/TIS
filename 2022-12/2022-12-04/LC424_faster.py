class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)

        start,end = 0,0
        freq = collections.defaultdict(int)
        maxfreq = 0

        for end in range(n):
            freq[s[end]]+=1
            maxfreq = max(maxfreq,freq[s[end]])

            if end+1 - start - maxfreq > k:
                freq[s[start]] -= 1
                start += 1

        return end+1-start
