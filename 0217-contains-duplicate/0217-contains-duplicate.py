class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mp=set()
        for ch in nums:
            
            if ch in mp:
                return True
            mp.add(ch)
        return False
        