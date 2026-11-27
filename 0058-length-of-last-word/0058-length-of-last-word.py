class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        j=len(s)-1
        m=0
        count=0
        while j>=0:
            if s[j].isalpha():
                count+=1
                
                m=max(count,m)
                j=j-1
            else:
                
                j=j-1
                if count > 0:
                    break

        return max(count,m)
                
                
               
        
        