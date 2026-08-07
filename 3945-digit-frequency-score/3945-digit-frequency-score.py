class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sum=0
        x=n
        while x!=0:
            sum=sum+x%10
            x=x//10
        return sum