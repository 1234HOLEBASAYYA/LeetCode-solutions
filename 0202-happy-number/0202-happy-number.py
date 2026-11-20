class Solution:
    def isHappy(self, n: int) -> bool:

        visit=set()
        while n!=1:
            
            if n in visit:
                return False
            visit.add(n)
            s=0
            while n!=0:
    
                digit=n%10
                s+=digit*digit
                n=n//10
            n=s
        return True
        