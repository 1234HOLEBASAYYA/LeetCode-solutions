class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even=[]
        odd=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even=sorted(even)
        # odd=sorted(odd)
        # n=len(n)
        nums=[0]*len(nums)
        j=0
        for i in range(len(even)):
            nums[j]=even[i]
            j+=2
        j=1
        odd.sort(reverse=True)
        for i in range(len(odd)):
            nums[j]=odd[i]
            j+=2
        return nums



        