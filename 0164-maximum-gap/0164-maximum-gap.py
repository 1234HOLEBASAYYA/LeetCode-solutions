class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        nums=sorted(nums)
        max1=0
        for i in range(1,len(nums)):
            max1=max(max1,(nums[i]-nums[i-1]))
            
            
        return max1
            
        