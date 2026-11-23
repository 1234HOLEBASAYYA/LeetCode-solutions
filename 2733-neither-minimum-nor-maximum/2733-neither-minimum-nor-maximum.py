class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        m=max(nums)
        l=min(nums)
        for ch in nums:
            if ch !=m and ch !=l:
                # e=ch
                return ch
        return -1
        