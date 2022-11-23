class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Chars = {}
        Chart = {}
        for cs,ct in zip(s,t):
            if cs not in Chars and ct not in Chart:
                Chars[cs] , Chart[ct] = ct,cs
            else:
                if cs in Chars and ct in Chart and Chars[cs] == ct and Chart[ct] == cs:
                    continue
                else:
                    return False            
        return True