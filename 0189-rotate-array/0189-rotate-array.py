class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=[]
        k = k % len(nums)
        n=len(nums)-k
        for i in range(n,len(nums)):
            r.append(nums[i])
        ans=[]
        for i in range(len(r)):
            ans.append(r[i])
        for i in range(0,n):
            ans.append(nums[i])
        nums[:]=ans
        
        