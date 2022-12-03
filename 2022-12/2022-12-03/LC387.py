class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        notRepeat = set()
        
        for c in count:
            if count[c] == 1:
                notRepeat.add(c)
        
        if len(notRepeat) == 0:
            return -1
        
        for i in range(len(s)):
            if s[i] in notRepeat:
                return i
        
        return -1