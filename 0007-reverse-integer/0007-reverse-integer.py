class Solution:
    def reverse(self, x: int) -> int:
        
            # return 0
        reverse=0
        num=x
        x=abs(x)
        while x!=0:
            reverse=(reverse*10)+x%10
            x=x//10
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        if num<0:
            return -reverse
        return reverse
        