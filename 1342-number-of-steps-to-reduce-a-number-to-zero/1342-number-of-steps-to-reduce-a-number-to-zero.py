class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num !=0:
            # divide=num//2
            if num%2==1:
                num=num-1
            else:
               num=num//2
            count+=1
        return count
        

        