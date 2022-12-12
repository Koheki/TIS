class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for si,ti in zip(s,t):
            if si not in smap and ti not in tmap:
                smap[si] = ti
                tmap[ti] = si
            elif si in smap and ti in tmap:
                if smap[si] == ti and tmap[ti] == si:
                    continue
                else:
                    return False
            else:
                return False

        return True