class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l=0
        r=k-1
        
        windo=0
        # windo=sum(nums[:k])
        for i in range(l,r+1):
            windo+=nums[i]

        maxavg=windo/k
        
        while r<len(nums)-1:
            
            windo=windo-nums[l]+nums[r+1]
            avg=windo/k
            maxavg=max(avg,maxavg)
            l+=1
            r+=1
        return maxavg
        