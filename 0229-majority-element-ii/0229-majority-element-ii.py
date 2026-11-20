class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        mp={}
        # list=[]


        for ch in nums:
            if ch in mp:
                mp[ch]+=1
            else:
                mp[ch]=1
        list=[]
        for ch in mp:
            if mp[ch]>len(nums)//3:
                list.append(ch)
        
        
        return list

        