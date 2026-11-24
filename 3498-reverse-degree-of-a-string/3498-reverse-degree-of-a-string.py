class Solution:
    def reverseDegree(self, s: str) -> int:
        # sum=0
        total=0        
        for i in range(1,len(s)+1):
            sum=0
            sum=26-(ord(s[i-1])-ord('a'))
            total=total+(sum*i)
        return total


        