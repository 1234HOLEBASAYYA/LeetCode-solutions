class Solution:
    def findMin(self, nums: List[int]) -> int:
        min=nums[0]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if min>nums[mid]:
                min=nums[mid]
                r=mid-1
            else:
                l=mid+1
        return min
