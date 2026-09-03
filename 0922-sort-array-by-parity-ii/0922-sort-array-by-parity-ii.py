class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)

        e=0
        o=1
        for x in nums:
            if x%2==0:
                ans[e]=x
                e+=2
            else:
                ans[o]=x
                o+=2
        return ans        