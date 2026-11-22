class Solution:
    def countElements(self, nums: list[int]) -> int:
        max1=max(nums)
        min1=min(nums)
        count=0
        for num in nums:
            if num !=max1 and num !=min1:
                count+=1
        return count
        