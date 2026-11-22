class Solution:
    def findLucky(self, arr: list[int]) -> int:
        mp={}
        for num in arr:
            mp[num]=mp.get(num,0)+1
        max1=-1
        for ch in mp:
            if mp[ch]==ch:
                
                max1=max(max1,ch)
        
        return max1
        