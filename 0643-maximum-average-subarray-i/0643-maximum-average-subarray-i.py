class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l=0
        r=k-1
        sum=0
        for i in range(l,r+1):
                sum+=nums[i]
        maxavg=sum/k

        while r<len(nums)-1:
            sum=sum-nums[l]+nums[r+1]
            
            avg=0
            
            

            avg=sum/k
            maxavg=max(avg,maxavg)
            l=l+1
            r=r+1
        return maxavg

        