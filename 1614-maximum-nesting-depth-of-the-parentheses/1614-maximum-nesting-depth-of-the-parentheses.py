class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        max=0
        for ch in s:
            if ch=="(":
                depth+=1
                if max<depth:
                    max=depth
            elif ch==")":
                depth-=1
            else:
                continue
        return max
            