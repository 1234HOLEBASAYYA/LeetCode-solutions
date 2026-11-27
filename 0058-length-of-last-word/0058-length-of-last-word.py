class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=len(s)-1
        count=0
        m=0
        while j>=0:
            if s[j].isalpha():
                count+=1
                m=max(m,count)
                j=j-1
            else:
                if count>0:
                    break
                j=j-1
        return m

        