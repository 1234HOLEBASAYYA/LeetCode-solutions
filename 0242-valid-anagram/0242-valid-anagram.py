class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        s=sorted(s)
        t=sorted(t)
        l=0
        while l<len(s):
            if s[l] ==t[l]:
                l=l+1
            else:
                return False
        return True
        