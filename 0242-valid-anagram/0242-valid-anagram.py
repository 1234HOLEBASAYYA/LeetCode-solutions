class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        s="".join(sorted(s))
        mp[s]=True
        t="".join(sorted(t))
        if t in mp:
            return True
        else:
            return False