class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        list=nums.copy()
        for ch in nums:
            reverse=0

            while ch!=0:
                reverse=(reverse*10)+ch%10
                ch=ch//10
            list.append(reverse)
        # fre=[0]
        # count=0

        # for ch in list:
        #     fre[ch]=1
        #     if ch not in  fre:
        #         fre[ch]=1
        

                
            
        return len(set(list))
                


        