class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i=0
        j=0
        while i<len(nums):
            if nums[i]%2==0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j+=1
                i+=1
            else:
                i+=1
        return nums

        