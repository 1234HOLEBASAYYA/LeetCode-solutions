class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max1=max(nums)
        count=0
        for ch in nums:
            count+=max1-ch
        return count

        