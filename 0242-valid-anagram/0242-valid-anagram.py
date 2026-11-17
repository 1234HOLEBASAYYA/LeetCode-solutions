class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        fre=[0]*26
        for i in range(len(s)):
            fre[ord(s[i])-ord('a')]+=1
            fre[ord(t[i])-ord('a')]-=1
        for count in fre:
            if count!=0:
                return False
        return True

        