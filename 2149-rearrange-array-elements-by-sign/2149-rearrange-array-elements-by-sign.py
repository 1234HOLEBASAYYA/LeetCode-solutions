class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for x in nums:
            if x<0:
                n.append(x)
            else:
                p.append(x)
        ans=[]
        for i  in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])
            
        return ans
   
        