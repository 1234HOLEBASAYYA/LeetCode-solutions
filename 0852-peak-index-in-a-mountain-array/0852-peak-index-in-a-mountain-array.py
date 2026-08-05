class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
       i=0
       while i <len(arr):
        if arr[i]<arr[i+1]:
            i+=1
        else:
            return i
        
            