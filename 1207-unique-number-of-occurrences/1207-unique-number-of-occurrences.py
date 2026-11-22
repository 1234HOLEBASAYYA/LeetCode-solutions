class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        mp={}
        for num in arr:
            mp[num]=mp.get(num,0)+1
        list=[]
        for ch in mp:
            list.append(mp[ch])
        set1=set(list)
        if len(set1)==len(list):
            return True
        else:
            return False
        