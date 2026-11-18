class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fre=[0]*26
        fr=[0]*26
        for i in range(len(ransomNote)):
            fre[ord(ransomNote[i])-ord('a')]+=1
        for i in range(len(magazine)):
            fr[ord(magazine[i])-ord('a')]+=1
        for i in range(26):
            if fre[i]>fr[i]:
                return False
        return True
        
