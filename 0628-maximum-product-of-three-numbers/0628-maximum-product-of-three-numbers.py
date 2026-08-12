class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        maxsum= nums[0]*nums[1]*nums[-1]
        sum=nums[-1]*nums[-2]*nums[-3]
        if maxsum<sum:
            return sum
        else:
            return maxsum