class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp={}
        for ch in strs:
            s="".join(sorted(ch))
            if s not in mp:
                mp[s]=[]
            mp[s].append(ch)
        return list(mp.values())

        