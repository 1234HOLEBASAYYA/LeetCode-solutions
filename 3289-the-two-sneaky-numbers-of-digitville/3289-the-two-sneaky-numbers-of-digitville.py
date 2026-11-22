class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp={}
        list=[]
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
            # mp.get(num, 0)+1
        for ch in mp:
            if mp[ch]==2:
                list.append(ch)
        return list
        