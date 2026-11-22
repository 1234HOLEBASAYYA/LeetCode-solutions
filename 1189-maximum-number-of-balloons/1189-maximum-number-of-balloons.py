class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp={}
        for ch in text:
            mp[ch]=mp.get(ch,0)+1
        b=mp.get('b',0)
        l=mp.get('l',0)//2
        a=mp.get('a',0)
        o=mp.get('o',0)//2
        n=mp.get('n',0)
        return min(b,l,o,a,n)


