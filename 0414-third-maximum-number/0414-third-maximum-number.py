class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        l = float('-inf')
        s = float('-inf')
        t = float('-inf')
        for num in nums:
            if num>l:
                t=s
                s=l
                l=num
            elif num>s and num !=l:
                t=s
                s=num
            elif num>t and num !=s and num !=l:
                t=num
        if t==float(-inf):
            return l
        else:
            return t
        