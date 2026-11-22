class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m=max(candies)
        list=[]
        for ch in candies:
            if m<=ch+extraCandies:
                list.append(True)
            else:
                list.append(False)
        return list
        