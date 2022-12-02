class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:        

        lens,lenp = len(s),len(p)

        score = sum([hash(c) for c in p])
        nums = [0]*(lens+1)
        nums[1] = hash(s[0])
        for i in range(2,lens+1):
            nums[i] = hash(s[i-1]) + nums[i-1]

        indices = []
        for i in range(lens-lenp+1):
            if score == nums[i+lenp]-nums[i]:
                indices.append(i)

        return indices
