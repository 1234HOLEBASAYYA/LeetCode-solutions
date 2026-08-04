class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
                i+=1
                
            else:
                i+=1
        return j+1