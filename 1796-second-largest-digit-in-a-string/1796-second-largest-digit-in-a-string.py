class Solution:
    def secondHighest(self, s: str) -> int:
        m=-1
        l=-1
        for ch in s:
            if ch.isdigit():
                num=int(ch)
                if num>m:
                    l=m
                    m=num
                elif num>l and num!=m:
                    l=num
        return l
        