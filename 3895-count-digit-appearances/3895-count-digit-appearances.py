class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for ch in nums:
            while ch !=0:
                if ch%10==digit:
                    count+=1
                ch=ch//10
        return count
               

        