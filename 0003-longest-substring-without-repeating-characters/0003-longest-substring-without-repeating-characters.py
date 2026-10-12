class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        list=[]
        l=0
        r=0
        # list.append(s[l])
        maxcount=0
        while r<len(s):
            if s[r] not in list:
                list.append(s[r])
                r=r+1
                # flag=1
                maxcount = max(maxcount, len(list))
            else:
                # flag=0
                # count=0
                # count=len(list)
                # maxcount=max(maxcount,count)

                list.pop(0)
                l=l+1
       
        return maxcount

        