class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        m=nums[0]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=m:
                l=mid+1
            else :
                m=nums[mid]
                r=mid-1
        return m