class Solution:
    def findValidPair(self, s: str) -> str:
        mp={}
        for i in range(len(s)):
            mp[s[i]]=mp.get(s[i],0)+1
        list=[]
        for i in range(len(s)-1):
            if mp[s[i]]==int(s[i]) and mp[s[i+1]]==int(s[i+1]) and int(s[i+1])!=int(s[i]):
                list.append(s[i])
                list.append(s[i+1])
                return "".join(list)
        return ""