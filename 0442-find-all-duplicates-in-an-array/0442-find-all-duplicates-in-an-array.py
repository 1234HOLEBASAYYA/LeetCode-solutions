class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fre=[0]*(len(nums)+1)
        for x in nums:
            fre[x]+=1
        ans=[]
        for i in range(len(fre)):
            if fre[i]==2:
                ans.append(i)
        return ans

        