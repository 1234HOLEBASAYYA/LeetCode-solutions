class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        
        fre=[0]*101
        for ch in nums:
            fre[ch]+=1
        s=0
        for ch in range(101):
            if fre[ch]==1:
                s+=ch
        return s


        