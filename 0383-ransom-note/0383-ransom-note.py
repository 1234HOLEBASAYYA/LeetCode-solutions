class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fre=[0]*26
        for ch in magazine:
            fre[ord(ch)-ord('a')]+=1

        for ch in ransomNote:
            fre[ord(ch)-ord('a')]-=1
            if fre[ord(ch)-ord('a')]<0:
                return False
        return True