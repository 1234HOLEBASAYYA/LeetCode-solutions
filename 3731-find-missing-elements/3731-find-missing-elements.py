class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min1=min(nums)
        max1=max(nums)
        nums.sort()
        ans=[]
        i=min1
        k=0
        while i<max1:
            if i==nums[k]:
                k+=1
                i+=1
            else:
                ans.append(i)
                i+=1
        return ans

        